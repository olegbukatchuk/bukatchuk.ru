---
layout: page
title: Проекты
description: Проекты
permalink: /projects/
---

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.

<ul>
  {% for post in site.categories.projects %}
    <li>
      <!-- <span>{{ post.date | date_to_string }}</span> » <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
      <meta name="description" content="{{ post.summary | escape }}">
      <meta name="keywords" content="{{ post.tags | join: ', ' | escape }}"/> -->
      {% assign date_format = site.minima.date_format | default: "%d-%m-%Y" %}
      {{ post.date | date: date_format }} »
      <!-- &verbar; {{ post.category | capitalize }} -->
      {% if post.highlight %}&starf; {% endif %}
      <a href="{{ post.url }}" title="{{ post.title }}">
        {{ post.title | truncate: 72 }}
      </a>
    </li>
  {% endfor %}
</ul>

