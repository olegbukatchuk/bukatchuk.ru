---
layout: page
title: Книги
description: Здесь буду постить книги которые прочитал и могу рекомендовать...
permalink: /books/
---

Здесь буду постить книги которые прочитал и могу рекомендовать...

{% assign posts_by_year = site.categories.books | group_by_exp:"post", "post.date | date: '%Y'" %}

{% for year in posts_by_year %}
<h2>{{ year.name }}</h2>
<ul>
  {% for post in year.items %}
    <!-- <li>
      {{ post.date | date_to_string  | split: " " | slice: 0, 2 | join: " " }} » 
      {% if post.highlight %}&starf; {% endif %}
      <a href="{{ post.url }}" title="{{ post.title }}">
        {{ post.title | truncate: 72 }}
      </a>
    </li> -->
    <li>
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
{% endfor %}