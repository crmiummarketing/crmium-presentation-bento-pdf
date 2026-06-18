# Установка скіла

Скіл живе у воркспейсі: `projects/crmium-presentation-bento-pdf/`. Він уже доступний у цій сесії Claude Code. Щоб користуватися ним глобально (у будь-якому проєкті) — скопіюй у `~/.claude/skills/`.

## Швидкий старт — глобальна установка

```powershell
# Windows (PowerShell)
Copy-Item -Recurse "projects\crmium-presentation-bento-pdf" "$env:USERPROFILE\.claude\skills\crmium-presentation-bento-pdf"
```

```bash
# macOS / Linux
cp -r projects/crmium-presentation-bento-pdf ~/.claude/skills/crmium-presentation-bento-pdf
```

Перезапусти Claude Code (закрий повністю і відкрий заново).

---

## Перевірка що скіл працює

Напиши Claude:

```
/crmium-presentation-bento-pdf

Зроби тестову презентацію на 3 слайди про впровадження Zoho для тестового клієнта
```

Claude має:
- Запитати мову, контакти спікера (onboarding — буде один раз)
- Згенерувати папку `projects/<slug>/index.html`
- Сказати як відкрити і запропонувати зробити PDF після перегляду

---

## Залежності для PDF

Генерація PDF потребує лише браузера **Google Chrome** або **Microsoft Edge** (на Windows Edge є завжди). **Python НЕ обовʼязковий:**
- **Windows:** `scripts/html_to_pdf.ps1` — PowerShell вбудований у систему, нічого ставити не треба.
- **macOS / Linux (або Windows з Python):** `scripts/html_to_pdf.py`.

Жодних npm/pip-пакетів не треба — скрипт сам знаходить браузер.

---

## Якщо щось пішло не так

### Скіл не активується
- Оскільки і цей скіл, і `crmium-presentation-bento` реагують на «презентація»/«слайди» — викликай явно через `/crmium-presentation-bento-pdf`.
- Перезапусти Claude Code повністю.
- Перевір що папка існує і містить `SKILL.md`, `reference/`, `scripts/`.

### PDF не генерується
- Перевір що встановлено Chrome або Edge.
- Якщо ні — використай ручний фолбек: відкрий `index.html` у Chrome → Ctrl+P → Save as PDF → Background graphics ON → Landscape.

### Шрифти не вантажаться (Onest)
- За корпоративним firewall Google Fonts може бути заблоковано — fallback на system-ui спрацьовує автоматично.
