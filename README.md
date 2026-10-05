# bukatchuk.ru

Личный блог Олега Букатчука. Jekyll, публикуется на GitHub Pages.
Оформление — дизайн-система Axis Industrial, та же, что на страницах продуктов
[devops.bukatchuk.ru](https://devops.bukatchuk.ru) и [oncall.bukatchuk.ru](https://oncall.bukatchuk.ru).

## Как добавить статью

Файл в `blog/_posts/` с именем `ГГГГ-ММ-ДД-адрес.md`:

```yaml
---
layout: post
title: "Заголовок статьи"
date: 2026-09-17
category: blog          # blog | books | life | projects — подпись берётся из _data/categories.yml
author: "Олег Букатчук"
description: |
  Одно-два предложения. Показываются в ленте, в описании страницы и при пересылке ссылки.
tags: [devops, инциденты]
---
```

Дальше обычный markdown. Что поддержано в оформлении:

| Что | Как писать |
|---|---|
| Буквица в первом абзаце | `<span class="firstcharacter">Д</span>ля работников…` |
| Врезка с оранжевой линией | `<div class="callout"><span class="callout__l">Важно</span><p>…</p></div>` |
| Цитата | обычный `>` |
| Код с подсветкой | ` ```bash ` |
| Формулы | `math: true` в front matter |
| Скрыть статью из ленты | `hidden: true` |
| Выключить комментарии | `comments: false` |

Врезки из старых постов (инлайновый `style="border…"`) приводятся к общему виду автоматически —
переписывать сто десять статей не нужно.

## Коллекция винила

Раздел `/vinyl/`. Каждый релиз — файл в `_vinyl/` с именем `исполнитель-название.md`,
страница получает адрес `/vinyl/имя-файла/`. Обложка лежит в `assets/img/vinyl/` под тем же именем.

```yaml
---
layout: release
artist: "Schiller"
title: "Sehnsucht"
year: 2024              # год этого издания
original_year: 2008     # год выхода альбома
label: "Universal Music Group"
catno: "06024 5505657 3"
country: "Германия"
format: "2×LP"
discs: 2                # сколько пластинок, идёт в счётчик раздела
color: "Red"            # необязательно
weight: "180 г"         # необязательно
limited: 1500           # тираж, необязательно
features: ["лимитированное издание", "ремастер"]
genres: ["Electronic"]
styles: ["Downtempo", "Ambient"]
discogs: "https://www.discogs.com/release/29819818"
cover: /assets/img/vinyl/schiller-sehnsucht.jpg
image: /assets/img/vinyl/schiller-sehnsucht.jpg
tracklist:
  - {pos: "A1", title: "Willkommen", duration: "1:08"}
  - {pos: "A3", title: "Denn Wer Liebt", duration: "3:47", feat: ["Anna Maria Mühe"]}
---
```

Текст под шапкой — заметка о пластинке, показывается на странице релиза. Пустые поля не выводятся.
Сторона берётся из первой буквы `pos`. Счётчики, фильтры и список лейблов на общей странице считаются сами.

Для сетки на общей странице нужна уменьшенная обложка в `assets/img/vinyl/thumbs/` под тем же именем, 400 пикселей по стороне:
`sips -Z 400 -s format jpeg -s formatOptions 78 assets/img/vinyl/имя.jpg --out assets/img/vinyl/thumbs/имя.jpg`.

На общей странице показывается по 24 релиза в «Витрине» и по 48 в «Каталоге», остальные — по номерам страниц.
В разметке лежат все релизы сразу, поэтому поиск и фильтры ищут по всей коллекции, а обложки грузятся только у видимых карточек.

## Типы страниц

| Layout | Где используется |
|---|---|
| `home` | главная: первый экран, показатели, лента последних статей |
| `post` | статья |
| `archive` | `/blog/`, `/books/`, `/life/`, `/projects/` — список по годам |
| `tags` | `/tags/` — все теги на одной странице |
| `page` | текстовая страница: `/about/`, `/services/` |
| `vinyl` | `/vinyl/` — коллекция винила: витрина и каталог |
| `release` | страница релиза в коллекции |
| `default` | каркас плюс 404 |

Макеты, с которых всё собрано, лежат в `tmp/` — это статичный HTML, его можно открыть
двойным кликом и посмотреть, как задумано.

## Что настраивается в `_config.yml`

- **`career.ops_since`** — год начала работы в эксплуатации. **Стаж нигде не записан текстом:**
  число лет считается от этой даты, склонение слова «год» — тоже. В 2028 году заголовок сам
  станет «Двадцать один год», править ничего не нужно. Число берётся так:
  `{% include years.html %}`, прописью — `{% include years-word.html cap='yes' %}`.
- `home` — заголовок первого экрана, лид, цифры в ленте показателей, длина ленты статей.
- `nav`, `footer_columns` — меню и подвал.
- `comments.enabled` + `comments.repo` — комментарии через utteranc.es. **Сейчас выключены:**
  в старом шаблоне они были привязаны к чужому репозиторию, и комментарии читателей уезжали
  в чужие issues. Включать — только со своим репозиторием.
- `plausible` — счётчик. Выключен; в старом конфиге он считал домен `bukatchuk.com`.

## Всё своё

Шрифты (JetBrains Mono, IBM Plex Sans, Space Grotesk) лежат в `assets/fonts/axis/` вместе
с лицензиями и отдаются с этого же домена: сторонних запросов у шаблона нет ни одного.
Отдельные статьи подгружают свои библиотеки (plotly, vega) — это их содержимое, не шаблон.

## Локально

```bash
bundle install
bundle exec jekyll serve
# http://127.0.0.1:4000
```

## Публикация

Пуш в `main` запускает `.github/workflows/jekyll-gh-pages.yml`: сборка через
`actions/jekyll-build-pages` и публикация через `actions/deploy-pages`.
Плагины ограничены списком GitHub Pages — поэтому страницы тем собраны без плагинов,
одной страницей `/tags/` с якорями.
