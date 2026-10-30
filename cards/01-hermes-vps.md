# Карточка 1 — AI-агент Hermes на VPS

**Статус:** active  
**Репозиторий:** https://github.com/StesNiash/kwork-hermes-vps

## Название

Установлю и настрою AI-агента Hermes на вашем сервере

## Рубрика

Разработка и IT

## Подрубрика

Скрипты, боты и mini apps

## Тип

ИИ-агенты

## Вид

—

## Обложка (660×440, 3:2)

**Текст на обложке:**

- `AI-АГЕНТ HERMES` — главный заголовок, 2 строки;
- `НА ВАШЕМ VPS` — второй крупный заголовок;
- `УСТАНОВКА ЗА 1 ДЕНЬ` — небольшой бейдж.

**Промпт для ChatGPT / Gemini:**

> 3:2 Kwork cover, 660×440. Bold editorial tech poster. Huge Russian headline "AI-АГЕНТ HERMES" in massive white sans-serif uppercase, split into two lines, occupying the top 40% with strong hierarchy. Directly below it a second large Russian line "НА ВАШЕМ VPS" in bright amber, then a compact rounded badge "УСТАНОВКА ЗА 1 ДЕНЬ". Main visual in the lower half: a clean compact server box with a subtle SSH terminal on the left, a minimal browser dashboard and a Telegram-style chat bubble on the right, connected by a secure glowing line; an abstract friendly AI assistant orb in the center, not a human face. Deep navy background, teal and warm amber accents, soft rim light, subtle grid, professional editorial tech style, high contrast, centered composition, generous margins, all text large and perfectly readable. Text must be exactly as specified, no other letters, no extra words, no logos, no watermarks, no real person, crisp 3D-isometric mixed with clean vector.

**Формат:** 660×440, 3:2. Если модель искажает кириллицу — сгенерируйте фон без текста и наложите три строки в Canva/Figma.

**Если нужен исходник:** не берите чужие скриншоты и логотип Hermes. Для реального кадра снимите свой dashboard после установки, без токенов, чатов и персональных данных; либо используйте нейтральную схему «VPS → Hermes → Telegram». Логотип и товарные знаки — только с разрешения правообладателя.

## Описание

Разверну Hermes Agent на вашем VPS: установлю, подключу выбранную AI-модель и Telegram, настрою автозапуск и healthcheck. В результате вы получаете личного AI-агента в Telegram и dashboard, доступный через SSH-туннель, а не публичный чат с чужими ключами.

Работаю на Ubuntu 22.04/24.04. VPS, токен бота и API-ключ модели — ваши; после установки передаю короткую инструкцию и чек-лист проверки. Если нужен HTTPS-dashboard, понадобится домен — это обсуждается отдельно. Срок — 1 день, базовая цена — 2 500 ₽.

## От покупателя нужно

- SSH-доступ к VPS (root или sudo);
- Telegram bot token от @BotFather;
- API-ключ модели (OpenRouter / Anthropic / OpenAI / другой провайдер);
- VPS с исходящим доступом к `api.telegram.org:443`; иначе нужен зарубежный сервер или разрешённый прокси;
- домен — только если нужен HTTPS-dashboard.

## Стоимость и опции

### Объем услуг в 1 кворке

- установка Hermes Agent на Ubuntu 22.04/24.04;
- Docker Compose и `.env` с правами `600`;
- первичная настройка выбранной AI-модели;
- Telegram-бот: подключение, pairing, проверка сообщения;
- dashboard через SSH-туннель;
- автозапуск и healthcheck;
- backup, restore, update и uninstall;
- короткая инструкция владельцу.

### Стоимость одного кворка

2 500 ₽

### Срок выполнения

1 день

## Дополнительные опции

### Настройка под процесс

- **Цена и срок:** 6 000 ₽ · 1 день
- **Подсказка для покупателя:** Дополнительные сценарии, роли и интеграции под задачу.

### Поддержка на неделю

- **Цена и срок:** 12 000 ₽ · 7 дней
- **Подсказка для покупателя:** Помощь с обновлениями и настройками после сдачи.

### Дополнительный профиль

- **Цена и срок:** по оценке · 1 день
- **Подсказка для покупателя:** Второй бот или профиль с отдельной конфигурацией.

## Что не входит

- стоимость VPS, API-запросов, домена и прокси;
- обход лимитов провайдера или оплата чужих подписок;
- бессрочная поддержка;
- публикация dashboard в интернет без TLS и пароля;
- обещание, что агент «сам всё сделает»: качество зависит от модели, ключей и задач.

## FAQ

**Вопрос:** Нужен ли мой API-ключ?  
**Ответ:** Да, ключ модели и токен бота — ваши; я не храню их после передачи.

**Вопрос:** Можно без Telegram?  
**Ответ:** Да, но базовая карточка рассчитана на Telegram как основной канал.

**Вопрос:** Данные защищены?  
**Ответ:** `.env` закрывается правами `600`, dashboard — через SSH-туннель; при необходимости настраивается HTTPS.
