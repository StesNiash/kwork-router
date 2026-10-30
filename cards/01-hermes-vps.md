# Карточка 1 — AI-агент Hermes на VPS

**Статус:** active  
**Репозиторий:** https://github.com/StesNiash/kwork-hermes-vps  
**Цена:** 2 500 ₽  
**Срок:** 1 день

## Название для Kwork

Установлю и настрою AI-агента Hermes на вашем сервере

## Что входит

- установка Hermes Agent на Ubuntu 22.04/24.04;
- Docker Compose и `.env` с правами `600`;
- первичная настройка выбранной AI-модели;
- Telegram-бот: подключение, pairing, проверка сообщения;
- dashboard, доступный через SSH-туннель;
- автозапуск и healthcheck;
- backup, restore, update и uninstall;
- короткая инструкция владельцу.

## Что нужно от покупателя

- SSH-доступ к VPS (root или sudo);
- Telegram bot token от @BotFather;
- API-ключ модели (OpenRouter / Anthropic / OpenAI / другой провайдер);
- VPS с исходящим доступом к `api.telegram.org:443`; иначе нужен зарубежный сервер или разрешённый прокси;
- домен — только если нужен HTTPS-dashboard.

## Допы

- дополнительная настройка под процесс — 6 000 ₽;
- поддержка на неделю — 12 000 ₽;
- несколько профилей/ботов — оценивается отдельно.

## Что не входит

- стоимость VPS, API-запросов, домена и прокси;
- обход лимитов провайдера или оплата чужих подписок;
- бессрочная поддержка;
- публикация dashboard в интернет без TLS и пароля;
- обещание, что агент «сам всё сделает»: качество зависит от модели, ключей и задач.

## FAQ

**Нужен ли мой API-ключ?** Да, ключ модели и токен бота — ваши; я не храню их после передачи.

**Можно без Telegram?** Да, но базовая карточка рассчитана на Telegram как основной канал.

**Данные защищены?** `.env` закрывается правами `600`, dashboard — через SSH-туннель; при необходимости настраивается HTTPS.

## Обложка

**Текст на обложке (крупно, без изменений):**

- `AI-АГЕНТ HERMES` — главный заголовок, 2 строки;
- `НА ВАШЕМ VPS` — второй крупный заголовок;
- `УСТАНОВКА ЗА 1 ДЕНЬ` — небольшой бейдж.

**Промпт для ChatGPT / Gemini:**

> 4:3 Kwork cover, bold editorial tech poster. Huge Russian headline "AI-АГЕНТ HERMES" in massive white sans-serif uppercase, split into two lines, occupying the top 40% with strong hierarchy. Directly below it a second large Russian line "НА ВАШЕМ VPS" in bright amber, then a compact rounded badge "УСТАНОВКА ЗА 1 ДЕНЬ". Main visual in the lower half: a clean compact server box with a subtle SSH terminal on the left, a minimal browser dashboard and a Telegram-style chat bubble on the right, connected by a secure glowing line; an abstract friendly AI assistant orb in the center, not a human face. Deep navy background, teal and warm amber accents, soft rim light, subtle grid, professional editorial tech style, high contrast, centered composition, generous margins, all text large and perfectly readable. Text must be exactly as specified, no other letters, no extra words, no logos, no watermarks, no real person, crisp 3D-isometric mixed with clean vector.

**Если нужен исходник:** не берите чужие скриншоты и логотип Hermes. Для реального кадра снимите свой dashboard после установки, без токенов, чатов и персональных данных; либо используйте нейтральную схему «VPS → Hermes → Telegram». Логотип и товарные знаки — только с разрешения правообладателя.

**Если модель искажает кириллицу:** сгенерируйте фон без текста по тому же промпту и наложите три строки в Canva/Figma крупным шрифтом.
