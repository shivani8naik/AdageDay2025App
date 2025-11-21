self.addEventListener('install', (event) => {
  event.waitUntil(
    caches.open('adageday-cache').then((cache) => {
      return cache.addAll([
        '/',
        '/index.html',
        '/schedule.html',
        '/message.html',
        '/contacts.html',
        '/guest.html',
        '/rules.html',
        '/announcements.html',
        '/static/uploads/images/md_photo.png',
        '/static/css/style.css'
      ]);
    })
  );
});

self.addEventListener('fetch', (event) => {
  event.respondWith(
    caches.match(event.request).then((response) => response || fetch(event.request))
  );
});
