# Bento Presentation · Design Reference

Дизайн-система презентацій CRMiUM у Bento-стилі. Це **скорочена версія** довідки лендінгу `bento-style-page` — без mobile-specifics, без CMS-нюансів, з фокусом на слайди 16:9.

---

## 1. Палітра — 3 кольори, без винятків

| Назва | HEX | Призначення |
|---|---|---|
| **Темний** | `#15171C` | Основний фон. **НЕ `#000`**. |
| **Помаранч** | `#EF652F` | Єдиний акцент. Hover: `#D45520`. Lighter: `#F58456`. |
| **Білий** | `#FFFFFF` | Текст, у тому числі ТЕКСТ НА ПОМАРАНЧЕВОМУ. |

### Допоміжні (rgba)
```css
--c-card:      #1B1E25;                     /* +6% lightness — для карток */
--c-dark:      #0E1015;                     /* footer / deeper shadows */
--c-ink-2:     rgba(255,255,255,0.62);      /* secondary text */
--c-ink-3:     rgba(255,255,255,0.38);      /* tertiary */
--c-line:      rgba(255,255,255,0.10);      /* borders */
--c-tint-soft: rgba(255,255,255,0.05);      /* subtle hover bg */
--c-acc-soft:  rgba(239,101,47,0.10);
--c-acc-mid:   rgba(239,101,47,0.25);
--c-acc-ink:   #FFFFFF;                     /* text on orange */
--c-acc-ink-2: rgba(255,255,255,0.82);
```

⚠️ **Правило:** на помаранчевому фоні (section divider, accent card, Q&A слайд) текст завжди білий `#FFFFFF`. Не помаранчевий, не темний.

---

## 2. Шрифти

**Onest** — display + body (Google Fonts, weights 300-800, supports Cyrillic).
**JetBrains Mono** — для UPPERCASE-міток (eyebrow, дати, slide-counter).

```html
<link href="https://fonts.googleapis.com/css2?family=Onest:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@300;400;500;600;700&display=swap" rel="stylesheet">
```

### Типографія для презентацій (більша за лендінг — для проєктора)

| Рівень | Розмір | Вага | Letter-spacing | Line-height |
|---|---|---|---|---|
| **H1 cover** | `clamp(88px, 11vw, 200px)` | 800 | -0.045em | 0.92 |
| **H1 section** | `clamp(80px, 10vw, 176px)` | 800 | -0.045em | 0.92 |
| **H1 slide** | `clamp(56px, 6.5vw, 104px)` | 800 | -0.035em | 1.0 |
| **H2 slide** | `clamp(42px, 4.8vw, 80px)` | 800 | -0.03em | 1.05 |
| **H3 cards (pain-h, bento-h)** | 28-42px | 700-800 | -0.02em | 1.1-1.15 |
| **Feature-h** | 28-32px | 700 | -0.02em | 1.15 |
| **Lead/subtitle** | 22-34px | 400-500 | -0.005em | 1.3-1.5 |
| **Body** | 19-22px | 400 | normal | 1.5 |
| **Bullet item** | `clamp(24px, 1.9vw, 34px)` | 500 | normal | 1.45 |
| **Big number** | 80-160px | 800 | -0.04em | 1 |
| **Bento number** | 104px (big card) / 80px | 800 | -0.04em | 1 |
| **QA-text "Питання?"** | `clamp(120px, 16vw, 280px)` | 800 | -0.045em | 0.9 |
| **Eyebrow (mono)** | 14-16px | 600 | 0.18-0.2em | 1 |
| **Caption** | 19-24px | 400-500 | normal | 1.4-1.55 |

> Чому шрифти більші за лендінг: презентації дивляться з відстані 3-15 метрів. Body 14-16px не читається з останнього ряду. **Мінімум для body — 19px**, **для card-headers — 28px**.

---

## 3. Layout — 16:9 фіксований

### Розміри слайдів

```css
.slide {
  width: 100vw;
  height: 100vh;
  padding: 8vh 10vw;
  display: flex;
  flex-direction: column;
  justify-content: center;
}
```

На `1920×1080`: padding = 86×192px → content-area 1536×908.

### Content cap

```css
.slide-content {
  max-width: 1320px;
  width: 100%;
  margin: 0 auto;
}
```

На ultrawide (>1920px) контент не розтягується. Цифровий проектор найчастіше 1920×1080 native — тоді весь viewport вже capped.

### Чому не absolute-coordinates

Якщо проектор має non-standard resolution (1280×720, 1366×768, 1440×900) — `vh/vw` адаптуються без обрізань. `px`-абсолют ламається.

### Aspect-ratio mismatch (рідкий випадок)

На дисплеях з aspect-ratio < 16/9 (4:3 проектор, MacBook 16:10) контент центрується, по краях темні смуги — як у Keynote. Опційно можна додати `@media (max-aspect-ratio: 16/9)` з меншими paddings.

---

## 4. Структура `index.html`

```html
<!DOCTYPE html>
<html lang="uk">
<head>
  <meta charset="utf-8">
  <meta name="viewport" content="width=1920, initial-scale=1">
  <title>{Тема презентації} · {Спікер}</title>
  <link rel="preconnect" href="https://fonts.googleapis.com">
  <link href="https://fonts.googleapis.com/css2?family=Onest:wght@300;400;500;600;700;800&family=JetBrains+Mono:wght@300;400;500;600;700&display=swap" rel="stylesheet">
  <style>/* ... inline slides.css ... */</style>
</head>
<body class="pres" data-palette="brand-dark">
  <div class="pres-progress"><div class="pres-progress-bar"></div></div>

  <header class="pres-bar">
    <div class="pres-logo">
      <img src="assets/crmium-logo-white.png" alt="CRMiUM">
    </div>
    <div class="pres-counter"><span class="counter-curr">1</span> / <span class="counter-total">11</span></div>
  </header>

  <main class="pres-deck">
    <section class="slide slide--cover" data-slide="1">
      <img class="slide-watermark" src="assets/crmium-outline.png" alt="">
      <div class="slide-content">…</div>
    </section>
    <section class="slide slide--bullets" data-slide="2">
      <div class="slide-content">…</div>
    </section>
    <!-- … -->
  </main>

  <nav class="pres-nav">
    <button class="pres-prev" aria-label="Previous slide">←</button>
    <button class="pres-next" aria-label="Next slide">→</button>
  </nav>

  <script>/* ... inline slides.js ... */</script>
</body>
</html>
```

### Локальні асети

Скіл вкладає у згенеровану папку `assets/` дві картинки:
- `crmium-logo-white.png` — лого для топбару (44px height)
- `crmium-outline.png` — outline-CRMiUM як watermark для section dividers, cover, Q&A

Не використовуємо CDN-лого `crmium.com/wp-content/...` — щоб презентація працювала офлайн.

### Чому single-file?

- Простіше передати спікеру (один файл, без папки `assets/`)
- Працює офлайн (тільки Google Fonts онлайн — fallback на system-ui якщо нема інтернету)
- Розмір ~30 KB — нічого
- Спікер не плутається з `git clone` чи `npm install`

---

## 5. Slide transitions

### CSS

```css
.pres-deck {
  display: flex;
  transition: transform 600ms cubic-bezier(.22, 1, .36, 1);
  will-change: transform;
}
.slide {
  flex-shrink: 0;
  width: 100vw;
}
```

JS оновлює `transform: translateX(-N * 100vw)` де N — індекс активного слайда.

### Easing

`cubic-bezier(.22, 1, .36, 1)` — той самий що у Bento лендінгу. Premium ease-out, природній.

### Per-slide reveal

Активний слайд (`.slide.is-active`) — діти отримують stagger reveal:
```css
.slide.is-active .reveal {
  opacity: 0;
  animation: slideReveal 600ms cubic-bezier(.22, 1, .36, 1) forwards;
}
.slide.is-active .reveal:nth-child(1) { animation-delay: 200ms; }
.slide.is-active .reveal:nth-child(2) { animation-delay: 350ms; }
.slide.is-active .reveal:nth-child(3) { animation-delay: 500ms; }
/* ... */
@keyframes slideReveal {
  from { opacity: 0; transform: translateY(20px); }
  to   { opacity: 1; transform: translateY(0); }
}
```

При зміні слайда reveal перезапускається (через CSS animation rerun trick або direct DOM update).

---

## 6. Navigation

### Keyboard

| Клавіша | Дія |
|---|---|
| `→` `Space` `PageDown` | Next slide |
| `←` `PageUp` `Backspace` | Previous slide |
| `Home` | First slide |
| `End` | Last slide |
| `0-9` | Jump to slide N (1=cover, 2=second...) |
| `F` | Toggle fullscreen |
| `P` | Print preview (для PDF export) |
| `Esc` | Exit fullscreen / hide overlay |

### Mouse

- Click на `.pres-next` / `.pres-prev` — навігація
- Click на `.pres-counter` — слайд-N input (опційно у v2)

### Touch (мобільне)

- `swipeleft` — next, `swiperight` — prev
- Дистанція > 50px — спрацьовує

### Progress bar

`.pres-progress-bar` — `width: (currentIndex / totalSlides) * 100%`. Помаранчева, угорі екрана `2px` висота.

---

## 7. Хедер `.pres-bar` — мінімалістичний

- Position: `fixed; top: 0; left: 0; right: 0`
- Background: `rgba(21, 23, 28, 0.85); backdrop-filter: blur(10px)`
- Height: **76px** (більше за лендінг бо логотип великий)
- Padding: `14px 40px`
- Зліва: лого CRMiUM (44px height — як на лендінгу)
- Справа: `pres-counter` — "5 / 12" монотонним шрифтом

⚠️ На section / qa слайдах (з gradient + watermark) — хедер автоматично ховається через JS, додаючи `body.no-bar`:
```js
const isFullBleed = activeSlide.classList.contains('slide--section') ||
                    activeSlide.classList.contains('slide--qa') ||
                    activeSlide.classList.contains('slide--image');
document.body.classList.toggle('no-bar', isFullBleed);
```
Хедер плавно зникає (opacity + translateY).

---

## 7.5 CRMiUM-outline watermark

На section dividers / cover / Q&A слайдах розміщуємо великий CRMiUM-outline як декоративний фон. Виглядає як на лендінгу але всередині слайду.

### CSS варіанти

```css
.slide-watermark {
  position: absolute;
  left: -3%;
  top: 50%;
  transform: translateY(-50%);
  width: 106%;
  height: auto;
  opacity: 0.08;
  pointer-events: none;
  z-index: 1;
  filter: brightness(0) invert(1);  /* білий outline */
}
.slide-watermark--top    { top: 4%;  transform: none; width: 90%; left: 5%; }
.slide-watermark--bottom { top: auto; bottom: -2%; transform: none; width: 90%; left: 5%; }
.slide--section .slide-watermark,
.slide--qa .slide-watermark { opacity: 0.12; }
```

### Коли який варіант використати

| Варіант | Куди | Як виглядає |
|---|---|---|
| Default (центр) | Cover, перший section divider | Великий "CRMiUM" посередині слайду, контент накладається |
| `--top` | Другий section divider | Watermark зверху над h1 — як шапка |
| `--bottom` | Закриваючий слайд, Q&A | Watermark зливається з низом — як футер-логотип |

### Правило різноманітності

На одній презентації використовуй **2-3 варіанти** watermark для різноманітності. Не на кожному слайді — лише на cover + section dividers + Q&A. Картки / bullet / stats слайди — БЕЗ watermark (зайва візуальна перевантаженість).

### Z-index

- `.slide-watermark { z-index: 1 }` — позаду контенту
- `.slide-content { z-index: 2 }` — попереду
- Контент і watermark **навмисно перетинаються** — це частина дизайну (як на скріншотах CRMiUM digest).

---

## 8. Анімації

### Принципи
- **Easing**: `cubic-bezier(.22, 1, .36, 1)` (всі transitions)
- **Hardware-accelerated**: `transform`, `opacity`, `filter` only
- **Тривалості**: 600ms slide transition / 200-500ms reveal stagger / 200ms hover

### Спеціальні
- **Cover hero**: при first-load великий h1 → slide in from left (translateX -40px → 0) + opacity (0 → 1), 800ms
- **Stats slide**: при появі — number counter (0 → target за 1500ms ease-out quartic)
- **Bento cards**: hover → `translateY(-4px)`, border helykey → `var(--c-acc-mid)`, shadow помаранчевий 14%

### Що **НЕ** робити
- ❌ Slide-fly-in із сторони (типу Apple Keynote magic-move) — overkill
- ❌ Flip / 3D rotation — занадто кричуще
- ❌ Auto-advance / autoplay — нехай спікер керує
- ❌ Background-image анімації — flicker на проекторі

---

## 9. PDF export

Цей скіл віддає PDF як повноцінний результат. Двокроково: спершу HTML і перегляд, потім PDF — на підтвердження спікера ("все добре"/"pdf").

### Метод A (дефолт): headless Chrome через скрипт

Потрібен лише Chrome або Edge — **Python НЕ обовʼязковий**.

```powershell
# Windows (без Python)
powershell -ExecutionPolicy Bypass -File "<skill-dir>\scripts\html_to_pdf.ps1" "projects\<slug>\index.html" "projects\<slug>\out.pdf"
```
```bash
# macOS / Linux або Windows з Python
python "<skill-dir>/scripts/html_to_pdf.py" "projects/<slug>/index.html" "projects/<slug>/out.pdf"
```

Скрипт сам знаходить Chrome або Edge, рендерить усі слайди стопкою (за рахунок `@media print` нижче), зберігає темний фон і пропорцію 16:9. Жодних ручних галочок: background graphics у headless print-to-pdf увімкнено за замовчуванням.

### Метод B (фолбек): Browser Print

Якщо Chrome/Edge не знайдено — `index.html` → Ctrl+P → Save as PDF:
- Layout: Landscape
- Margins: None
- Background graphics: ✅ ON (інакше темний фон зникне)

### `@media print` у самій презентації форсує:
```css
@media print {
  @page { size: 1920px 1080px; margin: 0; }
  html, body { background: #15171C !important; }
  .pres-bar, .pres-nav, .pres-progress { display: none !important; }
  .pres-deck { transform: none !important; display: block; }
  .slide {
    width: 1920px !important;
    height: 1080px !important;
    page-break-after: always;
    break-inside: avoid;
  }
  .reveal { opacity: 1 !important; transform: none !important; animation: none !important; }
}
```

---

## 10. Speaker notes (опційно)

Якщо спікер хоче нотатки до слайдів — додати `data-notes="..."` атрибут до `<section>`. Натиск `N` показує overlay з нотатками. Реалізація — в `slides.js`.

**За замовчуванням** — не вмикаємо. Якщо спікер просить — додаємо в опційний v2.

---

## 11. Логотипи (CRMiUM CDN)

- Темна палітра (default): `https://crmium.com/wp-content/uploads/2026/05/logo-white-for-dark-background.png`
- Світла (резерв): `https://crmium.com/wp-content/uploads/2026/05/logo-black-for-light-background.png`

У хедері `.pres-bar` і footer/contact слайді — біла версія.

---

## 12. Що НЕ використовуємо з Bento landings

- ❌ Topbar з burger-меню (не потрібна на проекторі)
- ❌ Sticky-секції / scroll-snap (у нас inline slide flexbox)
- ❌ IntersectionObserver reveal (немає скролу між слайдами)
- ❌ Form-секції (немає де ввести CF7)
- ❌ Countdown (специфіка лендінгу)
- ❌ Bento-grid timeline (у нас власний `.slide--timeline` патерн)
- ❌ Mobile breakpoints і `<br class="br-h1-desk-only">` (фіксований aspect)

Усе інше — переюзаємо: палітра, шрифти, hover-lift, easing.
