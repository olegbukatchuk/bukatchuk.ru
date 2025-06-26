---
layout: page
title: Жизнь
description: Здесь будут моменты из моей жизни, которыми хочется поделится.
permalink: /life/
---

Здесь будут моменты из моей жизни, которыми хочется поделится...

{% assign posts_by_year = site.categories.life | group_by_exp:"post", "post.date | date: '%Y'" %}

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