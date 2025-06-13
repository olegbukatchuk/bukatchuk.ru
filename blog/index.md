---
layout: page
title: Блог
description: Коллекция статей, заметок и проектов. 
permalink: /blog/
---

Здесь я документирую свои мысли по различным темам, а также обзоры по прочитанным книгам или пройденным курсам. Надеюсь, мой блог поможет вам узнать, что-то новое и полезное...
<ul>
  {% for post in site.categories.blog %}
    <li>
        <span>{{ post.date | date_to_string }}</span> » {% if post.highlight %}&starf; {% endif %}<a href="{{ post.url }}" title="{{ post.title }}">{{ post.title | truncate:72 }}</a>
    </li>
  {% endfor %}
</ul>

{% assign posts_by_year = site.categories.blog | group_by_exp:"post", "post.date | date: '%Y'" %}

{% for year in posts_by_year %}
<h2>{{ year.name }}</h2>
<ul>
  {% for post in year.items %}
    <li>
      {{ post.date | date_to_string  | split: " " | slice: 0, 2 | join: " " }} » 
      {% if post.highlight %}&starf; {% endif %}
      <a href="{{ post.url }}" title="{{ post.title }}">
        {{ post.title | truncate: 72 }}
      </a>
    </li>
  {% endfor %}
</ul>
{% endfor %}
