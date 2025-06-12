---
layout: page
title: Блог
description: Notes of Lester James V. Miranda
permalink: /blog/
---

Здесь я документирую свои эксперименты, мысли по различным темам. 
На этой странице также размещены мои учебные заметки по прочитанным книгам или курсам, которые я посещаю. 
Надеюсь, мой блокнот поможет вам так же, как он помог мне.

<ul>
  {% for post in site.categories.blog %}
    <li>
        <span>{{ post.date | date_to_string }}</span> » {% if post.highlight %}&starf; {% endif %}<a href="{{ post.url }}" title="{{ post.title }}">{{ post.title | truncate:72 }}</a>
    </li>
  {% endfor %}
</ul>

<!-- {% assign posts_by_year = site.categories.notebook | group_by_exp:"post", "post.date | date: '%Y'" %}

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
{% endfor %} -->
