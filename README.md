# kwork-router

Единый маршрутизатор карточек Kwork: здесь лежат описания, цены, FAQ и промпты обложек. Репозитории `kwork-*` — только рабочие демо, на которые ссылается каталог.

![Каталог](screenshots/catalog.png)

## Что здесь есть

- `index.html` — витрина, которая рендерится из `data/services.json`;
- `data/services.json` — реестр семейств, статусов, цен и ссылок;
- `cards/` — полные описания карточек, FAQ и промпты обложек;
- `app.js` — рендер карточек и фильтры «Все / Готово / В работе»;
- `KWORK.md` — правила, что можно обещать покупателю;
- `docs/ARCHITECTURE.md` — контракт данных и границы;
- `tests/test_catalog.py` — проверка реестра, карточек и отсутствия секретов.

## Статусы

| Статус | Значение |
|---|---|
| `active` | карточка опубликована на Kwork |
| `ready` | репозиторий и демо готовы, карточка ещё не опубликована |
| `planned` | направление заявлено, репозитория ещё нет |

Сейчас: 1 `active` (Hermes), 4 `ready` (парсер, Telegram-бот, Google Sheets, Python-скрипты), 3 `planned`.

## Быстрый запуск

```powershell
python -m http.server 8080
# открыть http://127.0.0.1:8080/
```

`index.html` загружает `data/services.json` через `fetch`, поэтому открывать его как `file://` не нужно — используйте локальный сервер.

## Проверка

```powershell
python -m unittest discover -s tests -v
```

Тесты проверяют:
- обязательные поля реестра и допустимые статусы;
- наличие файла карточки для каждого готового направления;
- ссылки на GitHub-репозитории;
- отсутствие секретов.

## Где что лежит

```text
kwork-router/
├── index.html
├── app.js
├── data/services.json
├── cards/
│   ├── 01-hermes-vps.md
│   ├── 02-parser.md
│   ├── 03-tg-bot.md
│   ├── 04-sheets.md
│   └── 05-python-scripts.md
├── docs/ARCHITECTURE.md
└── tests/test_catalog.py
```

## Связь с демо-репозиториями

| Карточка | Репозиторий | Статус |
|---|---|---|
| Hermes Agent на VPS | [kwork-hermes-vps](https://github.com/StesNiash/kwork-hermes-vps) | active |
| Парсер сайта → CSV / Excel | [kwork-parser](https://github.com/StesNiash/kwork-parser) | ready |
| Telegram-бот для заявок | [kwork-tg-bot](https://github.com/StesNiash/kwork-tg-bot) | ready |
| Автоматизация Google Sheets | [kwork-sheets](https://github.com/StesNiash/kwork-sheets) | ready |
| Python-скрипты для рутины | [kwork-python-scripts](https://github.com/StesNiash/kwork-python-scripts) | ready |
| Мониторинг цен и наличия | `kwork-monitor` | planned |
| API-интеграция с таблицами | `kwork-api-sync` | planned |
| AI-ассистент по документам | `kwork-ai-rag` | planned |

Демо-репозитории не содержат текстов карточек: только код, тесты, README и доказательство, что услуга выполнима.

## Обложки

В каждом файле `cards/*.md` есть блок **«Обложка»**:

- точный крупный текст для карточки;
- промпт для ChatGPT / Gemini с типографикой;
- негативный промпт;
- для Hermes — правила по исходникам и скриншотам.

## Правила

- Карточка не считается готовой, пока под неё нет рабочего репозитория с демо и тестами.
- Текст карточки хранится только здесь; в демо-репозиториях — ссылка на этот файл.
- В репозитории нет клиентских токенов, ключей и персональных данных.
- Цены и сроки — черновые, не публичная оферта.
