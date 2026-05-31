---
layout: page
title: photos
permalink: /photos/
description: A collection of photos.
nav: true
nav_order: 4
---

<style>
.photo-grid {
  display: grid;
  grid-template-columns: repeat(3, 1fr);
  gap: 12px;
  margin-top: 1rem;
}
.photo-grid a img {
  width: 100%;
  height: 220px;
  object-fit: cover;
  border-radius: 6px;
  transition: opacity 0.2s;
}
.photo-grid a img:hover {
  opacity: 0.85;
}
.photo-caption {
  font-size: 0.8rem;
  color: #666;
  text-align: center;
  margin-top: 4px;
}
@media (max-width: 600px) {
  .photo-grid { grid-template-columns: repeat(2, 1fr); }
}
</style>

<div class="photo-grid">
  <div>
    <a href="https://picsum.photos/id/10/800/600" target="_blank">
      <img src="https://picsum.photos/id/10/400/300" alt="Photo 1">
    </a>
    <p class="photo-caption">Nature</p>
  </div>
  <div>
    <a href="https://picsum.photos/id/20/800/600" target="_blank">
      <img src="https://picsum.photos/id/20/400/300" alt="Photo 2">
    </a>
    <p class="photo-caption">City</p>
  </div>
  <div>
    <a href="https://picsum.photos/id/30/800/600" target="_blank">
      <img src="https://picsum.photos/id/30/400/300" alt="Photo 3">
    </a>
    <p class="photo-caption">Architecture</p>
  </div>
  <div>
    <a href="https://picsum.photos/id/40/800/600" target="_blank">
      <img src="https://picsum.photos/id/40/400/300" alt="Photo 4">
    </a>
    <p class="photo-caption">Landscape</p>
  </div>
  <div>
    <a href="https://picsum.photos/id/50/800/600" target="_blank">
      <img src="https://picsum.photos/id/50/400/300" alt="Photo 5">
    </a>
    <p class="photo-caption">Travel</p>
  </div>
  <div>
    <a href="https://picsum.photos/id/60/800/600" target="_blank">
      <img src="https://picsum.photos/id/60/400/300" alt="Photo 6">
    </a>
    <p class="photo-caption">Street</p>
  </div>
</div>
