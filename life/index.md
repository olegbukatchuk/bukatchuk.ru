---
layout: page
title: Жизнь
description: Thoughts about the researcher and developer life
permalink: /life/
---

Публикации моего творчества, путешествий, авто/мото приключений и многое другое, что по моему мнению не подходит под формат блога. Иными словами, здесь будут моменты из моей жизни, которыми хочется поделится.

{% assign posts_by_year = site.categories.life | group_by_exp:"post", "post.date | date: '%Y'" %}

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