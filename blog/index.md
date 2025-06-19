---
layout: page
title: Статьи
description: Коллекция статей, заметок и проектов. 
permalink: /blog/
---

Здесь я документирую свои мысли по различным темам, а также обзоры по прочитанным книгам или пройденным курсам. Надеюсь, мой блог поможет вам узнать, что-то новое и полезное...

{% assign posts_by_year = site.categories.blog | group_by_exp:"post", "post.date | date: '%Y'" %}

{% for year in posts_by_year %}
<h2>{{ year.name }}</h2>
<ul>
  {% for post in year.items %}
     <li>
        {% assign date_format = site.minima.date_format | default: "%d-%m-%Y" %}
        {{ post.date | date: date_format }} »
        <!-- &verbar; {{ post.category | capitalize }} -->
        <h3 style="font-size: 1.2em;"><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
        <p style="font-size: 0.9em;">{{ post.description }}</p>
      </li>
    <!-- <li>
      {{ post.date | date_to_string  | split: " " | slice: 0, 2 | join: " " }} » 
      {% if post.highlight %}&starf; {% endif %}
      <a href="{{ post.url }}" title="{{ post.title }}">
        {{ post.title | truncate: 72 }}
      </a>
    </li> -->
  {% endfor %}
</ul>
{% endfor %}
