# Карточка 3 — Telegram-бот для заявок

**Статус:** ready  
**Репозиторий:** https://github.com/StesNiash/kwork-tg-bot  
**Цена:** от 2 500 ₽  
**Срок:** 1–2 дня

## Название для Kwork

Telegram-бот для заявок → Google Sheets

## Что входит

- бот принимает заявку по шагам: имя, телефон, комментарий;
- проверка телефона и команда отмены;
- сохранение в SQLite;
- выгрузка заявок в CSV;
- опциональная отправка в Google Sheets через Apps Script webhook;
- инструкция запуска и ограничения.

## Что нужно от покупателя

- токен Telegram-бота от @BotFather;
- текст приветствия и вопросы, если отличаются от стандартных;
- нужен ли Google Sheets и доступ к тестовой таблице;
- куда уведомлять о новых заявках.

## Что не входит

- админ-панель и роли операторов;
- оплата, рассылки и CRM;
- вложения, фото и голосовые;
- сложная антиспам-защита;
- хостинг и сопровождение после сдачи;
- автоматическая повторная отправка при недоступности Sheets.

## Допы

- меню и FAQ — карточка 8;
- CRM/Sheets-сценарий — карточка 10;
- оплата в боте — карточка 16 и отдельная оценка.

## FAQ

**Где хранятся заявки?** В SQLite на вашем сервере; можно экспортировать в CSV.

**Обязателен ли Google Sheets?** Нет, это опциональный webhook.

**Что будет, если webhook недоступен?** Заявка останется в SQLite; ошибка не теряет данные, но автоматического повтора нет.

## Обложка

**Текст на обложке (крупно, без изменений):**

- `TELEGRAM-БОТ` — главный заголовок;
- `ЗАЯВКИ В ТАБЛИЦУ` — подзаголовок;
- `ЗА 1–2 ДНЯ` — небольшой бейдж.

**Промпт для ChatGPT / Gemini:**

> 4:3 Kwork cover, bold editorial tech poster. Huge Russian headline "TELEGRAM-БОТ" in massive white sans-serif uppercase across the top 40%, one strong line. Below it a bright mint subheadline "ЗАЯВКИ В ТАБЛИЦУ" and a compact amber badge "ЗА 1–2 ДНЯ". Lower half: a smartphone with a minimal chat form on the left, a clean lead card and small database cylinder in the middle, a tidy spreadsheet row on the right; a subtle paper-plane trail connects them. Deep midnight-blue background, electric blue and mint accents, soft neon rim light, minimal geometric style, high contrast, centered composition, generous margins, all text large and perfectly readable. Text must be exactly as specified, no other letters, no extra words, no Telegram logo, no brand marks, no watermarks, no real person, crisp vector details.

**Если модель искажает кириллицу:** сгенерируйте фон без текста по тому же промпту и наложите три строки в Canva/Figma.
