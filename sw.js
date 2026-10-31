// PrepMaster Pro - Offline-First Service Worker
const CACHE_NAME = 'prepmaster-cache-v2';

const OFFLINE_CORE_ASSETS = [
  './',
  './index.html',
  './manifest.json',
  './data/catalog_and_meta.js',
  './data/coding_part1.js',
  './data/coding_part2.js',
  './data/quant_questions.js',
  './data/verbal_logical_questions.js',
  './data/coding_practice_problems.js',
  'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.css',
  'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/katex.min.js',
  'https://cdnjs.cloudflare.com/ajax/libs/KaTeX/0.16.9/contrib/auto-render.min.js'
];

self.addEventListener('install', event => {
  self.skipWaiting();
  event.waitUntil(
    caches.open(CACHE_NAME).then(async cache => {
      console.log('[SW] Pre-caching offline platform assets & question banks...');
      for (const asset of OFFLINE_CORE_ASSETS) {
        try {
          await cache.add(asset);
        } catch (err) {
          console.warn('[SW] Could not pre-cache asset on install:', asset, err);
        }
      }
      console.log('[SW] Pre-caching complete. Offline Mode is Ready.');
    })
  );
});

self.addEventListener('activate', event => {
  event.waitUntil(
    caches.keys().then(keys => {
      return Promise.all(
        keys.filter(key => key !== CACHE_NAME).map(key => {
          console.log('[SW] Cleaning up old cache version:', key);
          return caches.delete(key);
        })
      );
    }).then(() => self.clients.claim())
  );
});

self.addEventListener('fetch', event => {
  const req = event.request;
  if (req.method !== 'GET') return;

  event.respondWith(
    caches.match(req).then(cachedResponse => {
      if (cachedResponse) {
        // Return from cache, but update in background if online
        if (navigator.onLine) {
          fetch(req).then(freshResponse => {
            if (freshResponse && freshResponse.status === 200) {
              caches.open(CACHE_NAME).then(cache => cache.put(req, freshResponse.clone()));
            }
          }).catch(() => {/* Offline */});
        }
        return cachedResponse;
      }

      // If not in cache, fetch from network and cache
      return fetch(req).then(response => {
        if (!response || response.status !== 200 || response.type === 'opaque') {
          return response;
        }
        const responseToCache = response.clone();
        caches.open(CACHE_NAME).then(cache => {
          cache.put(req, responseToCache);
        });
        return response;
      }).catch(err => {
        // Network failed and not in cache, try index.html fallback for navigation
        if (req.mode === 'navigate') {
          return caches.match('./index.html');
        }
        throw err;
      });
    })
  );
});

// Support manual offline pack download trigger
self.addEventListener('message', event => {
  if (event.data && event.data.action === 'CACHE_ALL_ASSETS') {
    caches.open(CACHE_NAME).then(async cache => {
      let cachedCount = 0;
      for (const asset of OFFLINE_CORE_ASSETS) {
        try {
          await cache.add(asset);
          cachedCount++;
          if (event.source) {
            event.source.postMessage({
              type: 'CACHE_PROGRESS',
              loaded: cachedCount,
              total: OFFLINE_CORE_ASSETS.length
            });
          }
        } catch (e) {
          console.warn('[SW] Manual caching error:', asset, e);
        }
      }
      if (event.source) {
        event.source.postMessage({ type: 'CACHE_COMPLETE' });
      }
    });
  }
});
