# Карточка 3 — Telegram-бот для заявок

**Статус:** ready  
**Репозиторий:** https://github.com/StesNiash/kwork-tg-bot

## Название

Telegram-бот для заявок → Google Sheets

## Рубрика

Разработка и IT

## Подрубрика

Скрипты, боты и mini apps

## Тип

Чат-боты

## Вид

Написание и доработка

## Языки

Python

## Обложка (660×440, 3:2)

**Текст на обложке:**

- `TELEGRAM-БОТ` — главный заголовок;
- `ЗАЯВКИ В ТАБЛИЦУ` — подзаголовок;
- `ЗА 1–2 ДНЯ` — небольшой бейдж.

**Промпт для ChatGPT / Gemini:**

> 3:2 Kwork cover, 660×440. Bold editorial tech poster. Huge Russian headline "TELEGRAM-БОТ" in massive white sans-serif uppercase across the top 40%, one strong line. Below it a bright mint subheadline "ЗАЯВКИ В ТАБЛИЦУ" and a compact amber badge "ЗА 1–2 ДНЯ". Lower half: a smartphone with a minimal chat form on the left, a clean lead card and small database cylinder in the middle, a tidy spreadsheet row on the right; a subtle paper-plane trail connects them. Deep midnight-blue background, electric blue and mint accents, soft neon rim light, minimal geometric style, high contrast, centered composition, generous margins, all text large and perfectly readable. Text must be exactly as specified, no other letters, no extra words, no Telegram logo, no brand marks, no watermarks, no real person, crisp vector details.

**Формат:** 660×440, 3:2. Если модель искажает кириллицу — сгенерируйте фон без текста и наложите три строки в Canva/Figma.

## Описание

Сделаю Telegram-бота, который принимает заявки по шагам: имя, телефон, комментарий. Заявки сохраняются в SQLite и выгружаются в CSV; при наличии webhook — уходят в Google Sheets. Ошибка внешней таблицы не теряет заявку.

Подойдёт для сбора заявок с рекламы, сайта или визитки без ручного переноса. Токен бота и доступ к таблице — ваши; бот не публикует сообщения от вашего имени. Срок — 1–2 дня, базовая цена — от 2 500 ₽.

## От покупателя нужно

- токен Telegram-бота от @BotFather;
- текст приветствия и вопросы, если отличаются от стандартных;
- нужен ли Google Sheets и доступ к тестовой таблице;
- куда уведомлять о новых заявках.

## Стоимость и опции

### Объем услуг в 1 кворке

- бот принимает заявку по шагам: имя, телефон, комментарий;
- проверка телефона и команда отмены;
- сохранение в SQLite;
- выгрузка заявок в CSV;
- опциональная отправка в Google Sheets через Apps Script webhook;
- инструкция запуска и ограничения.

### Стоимость одного кворка

от 2 500 ₽

### Срок выполнения

1–2 дня

## Дополнительные опции

### Меню и FAQ

- **Цена и срок:** 1 500 ₽ · 1 день
- **Подсказка для покупателя:** Добавлю меню, кнопки и ответы на частые вопросы.

### Google Sheets / CRM

- **Цена и срок:** 2 000 ₽ · 1 день
- **Подсказка для покупателя:** Настрою передачу заявок в таблицу или CRM.

### Оплата в боте

- **Цена и срок:** 3 000 ₽ · 2 дня
- **Подсказка для покупателя:** Подключу оплату и статусы платежей.

## Что не входит

- админ-панель и роли операторов;
- оплата, рассылки и CRM;
- вложения, фото и голосовые;
- сложная антиспам-защита;
- хостинг и сопровождение после сдачи;
- автоматическая повторная отправка при недоступности Sheets.

## FAQ

**Вопрос:** Где хранятся заявки?  
**Ответ:** В SQLite на вашем сервере; можно экспортировать в CSV.

**Вопрос:** Обязателен ли Google Sheets?  
**Ответ:** Нет, это опциональный webhook.

**Вопрос:** Что будет, если webhook недоступен?  
**Ответ:** Заявка останется в SQLite; ошибка не теряет данные, но автоматического повтора нет.
