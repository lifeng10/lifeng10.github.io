---
layout: page
title: projects
permalink: /projects/
description: Research projects and software.
nav: true
nav_order: 3
---

{% assign sorted_projects = site.projects | sort: "importance" %}

<div class="projects">
  {% for project in sorted_projects %}
    <article class="card mt-3 p-3">
      <h3><a href="{{ project.url | relative_url }}">{{ project.title }}</a></h3>
      <p>{{ project.description }}</p>
    </article>
  {% endfor %}
</div>
