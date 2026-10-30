# Карточка 2 — Парсер сайта → CSV / Excel

**Статус:** ready  
**Репозиторий:** https://github.com/StesNiash/kwork-parser  
**Цена:** от 1 500 ₽  
**Срок:** 1–2 дня

## Название для Kwork

Парсер сайта → CSV / Excel

## Раздел

Скрипты и программирование

## Описание

Соберу данные с одного сайта или раздела в CSV/XLSX: настрою нужные поля, пагинацию, удаление дублей и отчёт о пропусках. Подойдёт для каталога товаров, прайса или таблицы объявлений, если источник разрешает сбор данных.

Работаю по ссылкам или сохранённым HTML-страницам. На выходе — таблица, которую можно открыть в Excel, и короткая инструкция запуска. Не обхожу капчу, авторизацию и защиты; сайты с запретом на парсинг не беру. Срок — 1–2 дня, базовая цена — от 1 500 ₽.

## Что входит

- разбор одного сайта или раздела по согласованным полям;
- до 5–7 полей: название, цена, ссылка, артикул и т.п.;
- пагинация по переданным URL;
- удаление дублей;
- выгрузка в CSV и XLSX;
- отчёт: сколько страниц обработано, сколько карточек найдено, сколько пропущено;
- инструкция запуска и ограничения.

## Что нужно от покупателя

- ссылки на страницы или сохранённые HTML-файлы;
- список нужных полей;
- подтверждение, что парсинг источника разрешён;
- пример желаемого CSV/XLSX.

## Что не входит

- обход CAPTCHA, авторизации, платных подписок и антибот-защит;
- парсинг сайтов, где это запрещено правилами;
- рендер JavaScript-приложений;
- круглосуточный мониторинг и расписание;
- Google Sheets, CRM и Telegram-уведомления;
- поддержка произвольного числа сайтов в одной цене.

## Допы

- несколько сайтов или сложная структура — отдельная оценка;
- регулярный запуск — отдельная задача;
- выгрузка в Google Sheets — карточка 6 и отдельный репозиторий.

## FAQ

**Вы можете спарсить любой сайт?** Нет. Сначала проверяем правила сайта и доступность данных.

**Сайт на JavaScript?** Базовый парсер не исполняет JS; нужен отдельный браузерный сценарий.

**Данные придут в Excel?** Да, CSV и XLSX; для XLSX нужен `openpyxl` из `requirements.txt`.

## Обложка

**Текст на обложке (крупно, без изменений):**

- `ПАРСЕР САЙТА` — главный заголовок;
- `В CSV И EXCEL` — подзаголовок;
- `ЗА 1–2 ДНЯ` — небольшой бейдж.

**Промпт для ChatGPT / Gemini:**

> 4:3 Kwork cover, bold editorial tech poster. Huge Russian headline "ПАРСЕР САЙТА" in massive white sans-serif uppercase across the top 40%, split into two balanced lines if needed. Under it a bright cyan subheadline "В CSV И EXCEL" and a compact amber badge "ЗА 1–2 ДНЯ". Lower half: a stack of clean website product cards with selector brackets and a magnifier on the left, a subtle funnel in the middle, and a polished spreadsheet with rows plus small CSV/XLSX file icons on the right. Deep blue background, cyan and warm orange accents, soft glow, thin grid lines, professional vector-3D hybrid, high contrast, centered composition, generous margins, all text large and perfectly readable. Text must be exactly as specified, no other letters, no extra words, no logos, no watermarks, no real person, crisp details.

**Если модель искажает кириллицу:** сгенерируйте фон без текста по тому же промпту и наложите три строки в Canva/Figma.
