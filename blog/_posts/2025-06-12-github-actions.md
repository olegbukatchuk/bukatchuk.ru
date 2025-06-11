---
layout: post
type: post
title: "Github Actions. Термины"
date: 2025-06-12
category: blog
comments: true
author: "Олег Букатчук"
published: true
header-img: /assets/png/talk-dlsu/header.png
tags:
  [
    github,
    actions,
    ci,
    cd,
  ]
description: |
  Workflow – это высокоуровневый набор правил для того, чтобы делать какие-то действия при определенных условиях.
excerpt: |
---
<ul>
<li>**Workflow** – это высокоуровневый набор правил для того, чтобы делать какие-то действия при определенных условиях.</li>

<li>**Job** – это сущность, которая запускает какую-то задачу в рамках вашего workflow.</li>

<li>**Step** – это шаг. Т. е. один job может состоять из нескольких шагов.</li>

<li>**Action** – это тот переиспользуемый unit, который попал в название GitHub Actions, т. е. это самая минимальная часть, которую можно переиспользовать в нашем CI.</li>

<li><span class="firstcharacter">E</span>vent – это термин, который обозначает, что случилось какое-то действие. А если действие случилось, то мы запускаем какой-то конкретный workflow.</li>
</ul>