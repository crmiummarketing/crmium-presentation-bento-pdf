# Language Templates · стандартні фрази

4 мови × 18 стандартних рядків. Використовуй при генерації слайдів на основі `user-config.md → language`.

---

## Базові labels для слайдів

| Ключ | UA | EN | PL | RU |
|---|---|---|---|---|
| `speaker_label` | СПІКЕР | SPEAKER | PRELEGENT | СПИКЕР |
| `agenda_title` | План презентації | Agenda | Agenda | План презентации |
| `agenda_label` | ПЛАН | AGENDA | AGENDA | ПЛАН |
| `section_label` | РОЗДІЛ | SECTION | ROZDZIAŁ | РАЗДЕЛ |
| `qa_text` | Питання? | Questions? | Pytania? | Вопросы? |
| `qa_subtext` | Час для діалогу | Time for discussion | Czas na dyskusję | Время для диалога |
| `thanks_text` | Дякую за увагу | Thank you for your attention | Dziękuję za uwagę | Спасибо за внимание |
| `contacts_label` | КОНТАКТИ | CONTACT | KONTAKT | КОНТАКТЫ |
| `email_label` | Email | Email | E-mail | Email |
| `phone_label` | Телефон | Phone | Telefon | Телефон |
| `linkedin_label` | LinkedIn | LinkedIn | LinkedIn | LinkedIn |
| `telegram_label` | Telegram | Telegram | Telegram | Telegram |
| `web_label` | Сайт | Web | Strona | Сайт |
| `about_us_title` | Про CRMiUM | About CRMiUM | O CRMiUM | О CRMiUM |
| `results_title` | Результати | Results | Wyniki | Результаты |
| `before_label` | До | Before | Przed | До |
| `after_label` | Після | After | Po | После |
| `next_slide` | Далі | Next | Dalej | Дальше |

---

## Стандартні заголовки секцій

### UA
- "Чому це важливо"
- "Як ми працюємо"
- "Що ви отримуєте"
- "Кейси клієнтів"
- "Цифри / Результати"
- "Питання та відповіді"

### EN
- "Why it matters"
- "How we work"
- "What you get"
- "Customer stories"
- "Numbers / Results"
- "Q&A"

### PL
- "Dlaczego to ważne"
- "Jak pracujemy"
- "Co otrzymujesz"
- "Historie klientów"
- "Liczby / Wyniki"
- "Pytania i odpowiedzi"

### RU
- "Почему это важно"
- "Как мы работаем"
- "Что вы получаете"
- "Кейсы клиентов"
- "Цифры / Результаты"
- "Вопросы и ответы"

---

## HTML lang attribute

| Мова | `<html lang="...">` |
|---|---|
| UA | `uk` |
| EN | `en` |
| PL | `pl` |
| RU | `ru` |

---

## Cover-слайд eyebrow

Дата + контекст. Формат:

| Мова | Приклад |
|---|---|
| UA | `27 ТРАВНЯ 2026 · ZOHO SUMMIT` |
| EN | `MAY 27, 2026 · ZOHO SUMMIT` |
| PL | `27 MAJA 2026 · ZOHO SUMMIT` |
| RU | `27 МАЯ 2026 · ZOHO SUMMIT` |

Місяці:

| # | UA | EN | PL | RU |
|---|---|---|---|---|
| 1 | СІЧНЯ | JANUARY | STYCZNIA | ЯНВАРЯ |
| 2 | ЛЮТОГО | FEBRUARY | LUTEGO | ФЕВРАЛЯ |
| 3 | БЕРЕЗНЯ | MARCH | MARCA | МАРТА |
| 4 | КВІТНЯ | APRIL | KWIETNIA | АПРЕЛЯ |
| 5 | ТРАВНЯ | MAY | MAJA | МАЯ |
| 6 | ЧЕРВНЯ | JUNE | CZERWCA | ИЮНЯ |
| 7 | ЛИПНЯ | JULY | LIPCA | ИЮЛЯ |
| 8 | СЕРПНЯ | AUGUST | SIERPNIA | АВГУСТА |
| 9 | ВЕРЕСНЯ | SEPTEMBER | WRZEŚNIA | СЕНТЯБРЯ |
| 10 | ЖОВТНЯ | OCTOBER | PAŹDZIERNIKA | ОКТЯБРЯ |
| 11 | ЛИСТОПАДА | NOVEMBER | LISTOPADA | НОЯБРЯ |
| 12 | ГРУДНЯ | DECEMBER | GRUDNIA | ДЕКАБРЯ |

---

## Як використовувати

Коли генеруєш слайд — підставляй ключ з відповідної мови з `user-config.md`. Якщо мова не задана — дефолт `ua`.

Приклад: на Q&A слайді не пиши українською `"Питання?"` коли `language=en` — пиши `"Questions?"`.

---

## Що НЕ перекладаємо

- "CRMiUM" — назва бренду, завжди оригінал
- "Zoho", "Odoo", "Creatio", "Salesforce" — назви продуктів
- "Premium partner", "Solutions Architect" — англомовні маркери, лишаються (хоча можна перекласти на UA "Архітектор рішень")
- URL-и сайту і email — завжди ASCII
