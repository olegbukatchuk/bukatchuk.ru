---
layout: default
title: Проекты
description: Проекты
permalink: /projects/
---

Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book.

<!-- <ul>
  {% for post in site.categories.projects %}
    <li>
        <span>{{ post.date | date_to_string }}</span> » <a href="{{ post.url }}" title="{{ post.title }}">{{ post.title }}</a>
        <meta name="description" content="{{ post.summary | escape }}">
        <meta name="keywords" content="{{ post.tags | join: ', ' | escape }}"/>
    </li>
  {% endfor %}
</ul> -->

<style>
  @media screen and (min-width: 769px) {
    .column {
      width: 50%;
      float: left;
      max-width: 50%;
      padding: 5px;
    }

    .row {
      display: flex;
      flex-direction: row;
      width: 100%;
    }
  }
</style>


<div class="home">

  <div class="divider">
    <div class="left">
      <a href="https://bukatchuk.com/gallery/"><img id="profilepic" width="200" height="200" src="assets/olegbukatchuk.png" alt="Profile"></a>
    </div>
    <div class="right">
      <p>Привет! Меня зовут Олег Букатчук. Мне, 41. Занимаюсь ИТ. Интересуюсь музыкой на виниле. Читаю по настроению. Пишу статьи. Преподаю. </p>
      <p>
        На текущий момент погружен в работу над социальной сетью <a href="https://followers.vc">followers.vc</a> и сервисом мониторига <a href="https://uptime.bz">uptime.bz</a>, а также в планах запуск сервиса e-mail рассылок <a href="https://mailer.bz/">mailer.bz</a>.
      </p>
    </div>
  </div>

  <!-- <div style="display:flex;justify-content:center;">
    <iframe src="https://olegbukatchuk.substack.com/embed" width="480" height="100"
      style="border:0px solid #EEE; background:fffff8;" frameborder="0" scrolling="no"></iframe>
  </div> -->
 
  &nbsp;

  <hr>

  &nbsp;
  <div class="row">
    <div class="column" style="width:100%; float:left;">
      <h2 style="font-size: 1.5em;">Статьи</h2>

      <ul class="post-list">
        {% assign mainPosts = site.posts | where: 'type', 'post' %}
        {% for post in mainPosts limit:3 %}
        <li>
          {% assign date_format = site.minima.date_format | default: "%d-%m-%Y" %}
          <span class="post-meta" style="font-size: 0.9em;">{{ post.date | date: date_format }}</span>
          <!-- &verbar; {{ post.category | capitalize }} -->
          <h3 style="font-size: 1.2em;"><a href="{{ post.url | relative_url }}">{{ post.title | escape }}</a></h3>
          <p style="font-size: 0.9em;">{{ post.description }}</p>
        </li>
        {% endfor %}
      </ul>
    </div>

    <div class="column" style="width:100%; float:right;">
      <h2 style="font-size: 1.5em;">Поток</h2>
      <ul class="post-list">
        {% assign news_content = site.pages | where: "path", "news.md" | first %}
        {{ news_content.content | markdownify }}
      </ul>
    </div>
  </div>

</div>