# CRMiUM Presentation Skill — Bento Style → PDF (no QR)

Скіл для Claude Code, який генерує фірмові презентації CRMiUM у Bento-дизайні **без QR-кодів** і віддає їх як HTML + готовий **PDF**. Темна тема `#15171C` + помаранч `#EF652F` + Onest шрифт. Універсальний — кожен спікер створює власні презентації для будь-якої теми.

Це PDF / no-QR варіант скіла `crmium-presentation-bento`. Відмінності рівно дві:
1. **Жодних QR-кодів** — Q&A лишається як просте «Питання?», слайд Resources стає текстовим.
2. **PDF як результат** — після підтвердження скіл сам рендерить PDF через headless Chrome.

> Якщо потрібен живий виступ з QR (scan-to-ask, Telegram-бот) — це сусідній скіл `crmium-presentation-bento`.

## Що це дає

- HTML-презентація у фірмовому стилі — 1 файл, ~30 KB
- Презентувати з браузера (F11 fullscreen), стрілки ←→ для навігації
- **Готовий PDF** — генерується автоматично через `scripts/html_to_pdf.ps1` (Windows, без Python) або `.py` (Chrome/Edge headless), з коректним темним фоном і 16:9, без ручного Ctrl+P
- Базові слайди: cover, speaker intro, CRMiUM intro, agenda, Q&A («Питання?»), Resources (текстовий), contacts
- 11+ типів контентних слайдів: bullets, stats, bento, quote, image, compare, timeline, pains-grid, features-grid
- 4 мови: UA / EN / PL / RU
- Контакти спікера запитуються один раз і зберігаються (multi-speaker підтримка)

---

## Установка

Скіл лежить у воркспейсі: `projects/crmium-presentation-bento-pdf/`.

Щоб зробити його глобально доступним у Claude Code — скопіюй папку у `~/.claude/skills/crmium-presentation-bento-pdf/`:

```bash
# Windows (PowerShell)
Copy-Item -Recurse "projects\crmium-presentation-bento-pdf" "$env:USERPROFILE\.claude\skills\crmium-presentation-bento-pdf"

# macOS / Linux
cp -r projects/crmium-presentation-bento-pdf ~/.claude/skills/crmium-presentation-bento-pdf
```

Перезапусти Claude Code. Перевір: напиши `/crmium-presentation-bento-pdf`.

---

## Як використовувати

У Claude Code напиши, наприклад:

- "Зроби презентацію в PDF про впровадження Zoho для виробничої компанії"
- "Потрібні слайди без QR для звіту — тема: міграція з Bitrix24 на Zoho"
- "Презентація на розсилку: кейс клієнта, експорт у PDF"

### ⚠️ Якщо скіл не активувався

Оскільки і цей скіл, і `crmium-presentation-bento` реагують на «презентація»/«слайди», найнадійніше викликати явно:

```
/crmium-presentation-bento-pdf

Зроби презентацію про впровадження Zoho для виробничої компанії
```

(без аргументів — скіл сам запитає чого ти хочеш)

### Перший запуск

Скіл задасть онбоардинг-питання:
1. **Мова** презентації (UA / EN / PL / RU)
2. **Контакти спікера** — імʼя, посада, email, телефон, LinkedIn, фото-URL, біо
3. **Тема цієї презентації** + аудиторія + контекст + кількість слайдів + чи додавати CRMiUM intro
4. **Драфт/тези** — якщо є готовий текст, передай його. Якщо ні — Claude згенерує каркас

Відповіді про мову й спікера збережуться у `~/.claude/skills/crmium-presentation-bento-pdf/user-config.md`.

> Питання про QR немає — це no-QR скіл.

### Multi-speaker — підтримка кількох спікерів

При наступних запусках скіл показує список збережених спікерів і підставляє контакти обраного. Один файл `user-config.md` = десятки спікерів.

---

## Як презентувати

1. Відкрий згенерований `index.html` у Chrome / Edge / Firefox.
2. Натисни `F11` — fullscreen без браузерних панелей.
3. Навігація:
   - `→` `Space` `PageDown` — наступний слайд
   - `←` `PageUp` `Backspace` — попередній слайд
   - `Home` / `End` — перший / останній
   - `0-9` — стрибнути на слайд N
   - `F` — toggle fullscreen
   - `P` — print preview (ручний PDF)
   - `Esc` — вийти з fullscreen

---

## Експорт у PDF

PDF робиться **двокроково**: спершу HTML і перегляд, потім PDF — на підтвердження. Так PDF не перегенеровується на кожній правці.

1. Скіл генерує `index.html` і просить переглянути.
2. Коли все ок — напиши **«все добре»** або **«pdf»**.
3. Скіл запускає генератор PDF (потрібен лише Chrome/Edge — **Python не обовʼязковий**):
   ```powershell
   # Windows (без Python)
   powershell -ExecutionPolicy Bypass -File "<skill-dir>\scripts\html_to_pdf.ps1" "projects\<slug>\index.html" "projects\<slug>\<slug>.pdf"
   ```
   ```bash
   # macOS / Linux або Windows з Python
   python "<skill-dir>/scripts/html_to_pdf.py" "projects/<slug>/index.html" "projects/<slug>/<slug>.pdf"
   ```
   Скрипт сам знаходить Chrome або Edge, форсує темний фон і 16:9. На виході — `<slug>.pdf`.

**Ручний фолбек** (якщо Chrome/Edge не знайдено): відкрий `index.html` у Chrome → `Ctrl+P` → Save as PDF → Layout **Landscape** → Margins **None** → **Background graphics: ON** (інакше зникне темний фон).

### Запустити генерацію PDF самому

```powershell
# Windows, без Python:
powershell -ExecutionPolicy Bypass -File projects\crmium-presentation-bento-pdf\scripts\html_to_pdf.ps1 projects\<slug>\index.html
```
```bash
# або з Python:
python projects/crmium-presentation-bento-pdf/scripts/html_to_pdf.py projects/<slug>/index.html
```

(якщо output не вказано — PDF ляже поряд з HTML з тим же іменем)

---

## FAQ

**Як змінити збережені контакти спікера?**
Відкрий `~/.claude/skills/crmium-presentation-bento-pdf/user-config.md` → знайди блок з `id:` → зміни поля → збережи.

**Як змінити мову для наступної презентації?**
Або відредагуй `user-config.md` (`default_language:`), або скажи Claude "Згенеруй презентацію англійською".

**Як замінити фото спікера?**
Слайд `slide--speaker` має `<img src="...">`. Завантаж фото на CRMiUM CDN, отримай URL, заміни.

**Як додати ще слайди до згенерованої презентації?**
Відкрий `index.html`, скопіюй один із `<section class="slide ...">` блоків, заміни контент. Не змінюй структуру класів — JS-навігація рахує total з кількості `.slide`. Або попроси Claude "Додай ще 3 слайди типу stats про X". Після правок перегенеруй PDF.

**Працює офлайн?**
Майже. Google Fonts (Onest) підгружаються онлайн. Без інтернету — system-ui fallback (виглядає трохи інакше, але працює).

**PDF вийшов світлий / без фону?**
Скрипт `html_to_pdf.py` форсує фон автоматично. Якщо робив вручну через Ctrl+P — увімкни **Background graphics**.

**А якщо я не CRMiUM-спікер? Чи можу використати скіл?**
Так (MIT). Заміни лого у `assets/`, заміни `company-info.md` своїм elevator-pitch.

---

## Технічні характеристики

- Single-file HTML (~30 KB) + PDF на виході
- PDF: headless Chrome/Edge (`--print-to-pdf`) через PowerShell (без Python) **або** Python; без npm/pip-залежностей
- Шрифти: Google Fonts (Onest + JetBrains Mono)
- Сумісність: Chrome 90+, Edge 90+, Firefox 90+, Safari 14+

---

## Ліцензія

MIT — використовуй вільно у CRMiUM і поза нею.
