# Slide Recipes — 11 типів слайдів

Готові HTML+CSS патерни. Копіюй блок, заміни контент, не змінюй структуру CSS-класів (`.slide`, `.slide--<type>`).

---

## 1. Cover (титульний)

Заголовний слайд презентації. Дата події + велика типографіка + спікер унизу.

```html
<section class="slide slide--cover" data-slide="1">
  <div class="slide-content">
    <div class="eyebrow reveal">27 ТРАВНЯ 2026 · ZOHO SUMMIT</div>
    <h1 class="slide-h1 reveal">
      Як <em>Zoho</em> трансформував<br>
      виробничу компанію
    </h1>
    <p class="slide-sub reveal">Кейс впровадження CRM+ERP за 6 місяців</p>
    <div class="cover-speaker reveal">
      <div class="cover-speaker-name">Олександр Мельник</div>
      <div class="cover-speaker-role">Solutions Architect · CRMiUM</div>
    </div>
  </div>
</section>
```

**CSS особливості:**
```css
.slide--cover { background: radial-gradient(120% 80% at 80% 0%, rgba(239,101,47,0.18) 0%, transparent 55%), var(--c-bg); }
.slide--cover .slide-h1 em { color: var(--c-acc); font-style: normal; }
.cover-speaker { margin-top: auto; padding-top: 64px; border-top: 1px solid var(--c-line); }
```

---

## 2. Section divider — gradient + watermark

Розділ між темами. **НЕ плоский помаранчевий** — використовуємо gradient orange→dark + CRMiUM-outline watermark. Білий текст, дуже великий h1.

```html
<section class="slide slide--section" data-slide="5">
  <!-- watermark: default (центр) АБО --top / --bottom -->
  <img class="slide-watermark" src="assets/crmium-outline.png" alt="">
  <div class="slide-content">
    <div class="section-num reveal">02</div>
    <h1 class="slide-h1 reveal">Рішення</h1>
    <p class="section-sub reveal">Один стек. <em>Всі процеси.</em></p>
  </div>
</section>
```

### Варіант watermark зверху

```html
<section class="slide slide--section" data-slide="7">
  <img class="slide-watermark slide-watermark--top" src="assets/crmium-outline.png" alt="">
  <div class="slide-content">…</div>
</section>
```

**CSS:**
```css
.slide--section {
  background:
    radial-gradient(140% 100% at 100% 100%, rgba(239,101,47,0.55) 0%, transparent 50%),
    radial-gradient(100% 80% at 0% 0%, rgba(239,101,47,0.20) 0%, transparent 55%),
    linear-gradient(135deg, var(--c-acc-dark) 0%, var(--c-bg) 100%);
}
.slide--section .slide-h1 {
  color: #FFFFFF;
  font-size: clamp(80px, 10vw, 176px);
  letter-spacing: -0.045em;
  line-height: 0.92;
}
.section-num {
  font-family: var(--font-mono);
  font-size: 22px;
  letter-spacing: 0.22em;
  color: rgba(255,255,255,0.75);
  font-weight: 600;
  margin-bottom: 28px;
}
.section-sub {
  font-size: 34px;
  color: rgba(255,255,255,0.85);
  margin-top: 28px;
  max-width: 1000px;
  font-weight: 500;
  line-height: 1.3;
}
.section-sub em { font-style: normal; color: var(--c-acc); font-weight: 600; }
```

⚠️ Хедер `.pres-bar` автоматично ховається на section слайдах через JS (`body.no-bar`).

---

## 3. Bullets (3-5 пунктів)

Заголовок + список з помаранчевими маркерами `—`. Найпопулярніший слайд.

```html
<section class="slide slide--bullets" data-slide="3">
  <div class="slide-content">
    <h2 class="slide-h2 reveal">Чому Zoho виграв тендер</h2>
    <ul class="bullets-list reveal">
      <li>Найкращий ROI з 5 розглянутих систем</li>
      <li>Українська локалізація і підтримка</li>
      <li>Готова інтеграція з 1С та Bitrix24</li>
      <li>Гнучкі мобільні застосунки для польових продавців</li>
    </ul>
  </div>
</section>
```

**CSS:**
```css
.bullets-list { list-style: none; padding: 0; margin: 56px 0 0; }
.bullets-list li {
  font-size: clamp(24px, 1.9vw, 34px);
  line-height: 1.45;
  color: var(--c-ink);
  padding: 22px 0 22px 42px;
  position: relative;
  border-bottom: 1px solid var(--c-line);
  font-weight: 500;
}
.bullets-list li::before {
  content: '—';
  position: absolute; left: 0; top: 22px;
  color: var(--c-acc);
  font-weight: 700;
}
.bullets-list li:last-child { border-bottom: none; }
```

---

## 4. Stats (1-3 великі цифри)

Метрики, кількісні докази. Counter-анімація при появі.

```html
<section class="slide slide--stats" data-slide="4">
  <div class="slide-content">
    <h2 class="slide-h2 reveal">Результати за рік</h2>
    <div class="stats-grid reveal">
      <div class="stat-card">
        <div class="stat-num" data-counter="42">0</div>
        <div class="stat-suffix">%</div>
        <div class="stat-label">Зростання продажів</div>
      </div>
      <div class="stat-card">
        <div class="stat-num" data-counter="3">0</div>
        <div class="stat-suffix">x</div>
        <div class="stat-label">Швидкість обробки заявок</div>
      </div>
      <div class="stat-card">
        <div class="stat-num" data-counter="180">0</div>
        <div class="stat-suffix">k</div>
        <div class="stat-label">Зекономлено грн/місяць</div>
      </div>
    </div>
  </div>
</section>
```

**CSS:**
```css
.stats-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 48px; margin-top: 64px; }
.stat-card { text-align: left; }
.stat-num {
  font-size: clamp(80px, 9vw, 160px);
  font-weight: 800;
  line-height: 1;
  letter-spacing: -0.04em;
  color: var(--c-ink);
  font-variant-numeric: tabular-nums;
  display: inline-block;
}
.stat-suffix {
  display: inline-block;
  font-size: clamp(40px, 5vw, 80px);
  font-weight: 800;
  color: var(--c-acc);
  margin-left: 4px;
}
.stat-label { margin-top: 16px; font-size: 20px; color: var(--c-ink-2); line-height: 1.4; }
```

**JS counter:** при `.slide.is-active` знайти `[data-counter]`, анімувати 0→target за 1500ms (ease-out quartic).

---

## 5. Bento grid (4-6 mini-карток)

Кілька рівноцінних пунктів. Як bento на лендінгу, але крупніше.

```html
<section class="slide slide--bento" data-slide="6">
  <div class="slide-content">
    <h2 class="slide-h2 reveal">Що в скоупі проєкту</h2>
    <div class="bento-grid reveal">
      <div class="bento-card">
        <div class="bento-tag">CRM</div>
        <div class="bento-h">Zoho CRM</div>
        <p>Управління лідами, угодами, контактами</p>
      </div>
      <div class="bento-card">
        <div class="bento-tag">ERP</div>
        <div class="bento-h">Zoho Inventory</div>
        <p>Склад, замовлення, відвантаження</p>
      </div>
      <div class="bento-card">
        <div class="bento-tag">DESK</div>
        <div class="bento-h">Zoho Desk</div>
        <p>Тікет-система для саппорту</p>
      </div>
      <div class="bento-card bento-card--accent">
        <div class="bento-tag">+ Інтеграції</div>
        <div class="bento-h">1С, Telegram, Sender</div>
        <p>Автоматичний обмін даними</p>
      </div>
    </div>
  </div>
</section>
```

**CSS:**
```css
.bento-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; margin-top: 48px; }
.bento-card {
  background: var(--c-card);
  border: 1px solid var(--c-line);
  border-radius: 20px;
  padding: 32px;
  transition: border-color .3s, transform .3s, box-shadow .3s;
  transition-timing-function: cubic-bezier(.22,1,.36,1);
}
.bento-card:hover {
  border-color: var(--c-acc-mid);
  transform: translateY(-4px);
  box-shadow: 0 12px 28px rgba(239,101,47,0.14);
}
.bento-tag { font-family: var(--font-mono); font-size: 13px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--c-acc); font-weight: 600; }
.bento-h { font-size: 32px; font-weight: 700; margin: 12px 0 8px; letter-spacing: -0.02em; }
.bento-card p { font-size: 18px; color: var(--c-ink-2); line-height: 1.5; }
.bento-card--accent { background: var(--c-acc); color: var(--c-acc-ink); border-color: transparent; }
.bento-card--accent .bento-tag, .bento-card--accent p { color: var(--c-acc-ink-2); }
```

---

## 6. Quote (цитата)

Велика italic + author + role. Для customer stories.

```html
<section class="slide slide--quote" data-slide="7">
  <div class="slide-content">
    <div class="quote-mark reveal">"</div>
    <blockquote class="quote-text reveal">
      Після Zoho ми вперше за 10 років побачили реальну картину
      по продажах. До того — кожен керівник мав свою версію правди.
    </blockquote>
    <div class="quote-author reveal">
      <div class="quote-name">Сергій Іваненко</div>
      <div class="quote-role">CEO · ТОВ "Промтехніка"</div>
    </div>
  </div>
</section>
```

**CSS:**
```css
.quote-mark { font-size: 200px; line-height: 0.5; color: var(--c-acc); font-family: serif; font-weight: 800; }
.quote-text { font-size: clamp(28px, 3vw, 44px); font-weight: 400; font-style: italic; line-height: 1.4; max-width: 1100px; margin: 32px 0; color: var(--c-ink); }
.quote-author { display: flex; gap: 16px; align-items: baseline; padding-top: 32px; border-top: 1px solid var(--c-line); }
.quote-name { font-size: 22px; font-weight: 600; }
.quote-role { font-size: 16px; color: var(--c-acc); font-weight: 500; }
```

---

## 7. Image (full-bleed)

Велике зображення на весь слайд. Підпис унизу.

```html
<section class="slide slide--image" data-slide="8" style="background-image: url('https://crmium.com/wp-content/uploads/2026/05/zoho-dashboard.jpg')">
  <div class="image-caption reveal">
    Dashboard Zoho CRM після впровадження — usual day view
  </div>
</section>
```

**CSS:**
```css
.slide--image { background-size: cover; background-position: center; padding: 0; position: relative; }
.slide--image::after {
  content: '';
  position: absolute; inset: 0;
  background: linear-gradient(180deg, transparent 60%, rgba(0,0,0,0.7) 100%);
  pointer-events: none;
}
.image-caption {
  position: absolute; bottom: 64px; left: 64px; right: 64px;
  z-index: 1;
  font-size: 20px;
  color: #FFF;
  text-shadow: 0 2px 8px rgba(0,0,0,0.5);
}
```

---

## 8. Compare (2 колонки)

До/Після, A/B, переваги/недоліки.

```html
<section class="slide slide--compare" data-slide="9">
  <div class="slide-content">
    <h2 class="slide-h2 reveal">До і Після</h2>
    <div class="compare-grid reveal">
      <div class="compare-col">
        <div class="compare-tag compare-tag--neg">До</div>
        <ul>
          <li>Excel-таблиці з продажами</li>
          <li>Інформація розкидана по людях</li>
          <li>3 дні на формування звіту</li>
        </ul>
      </div>
      <div class="compare-col">
        <div class="compare-tag compare-tag--pos">Після</div>
        <ul>
          <li>Єдина база лідів у Zoho CRM</li>
          <li>Прозорі pipelines для усіх ролей</li>
          <li>Real-time dashboard за 5 хв</li>
        </ul>
      </div>
    </div>
  </div>
</section>
```

**CSS:**
```css
.compare-grid { display: grid; grid-template-columns: 1fr 1fr; gap: 32px; margin-top: 48px; }
.compare-col { padding: 32px; background: var(--c-card); border-radius: 16px; border: 1px solid var(--c-line); }
.compare-tag {
  display: inline-block;
  font-family: var(--font-mono); font-size: 13px; letter-spacing: 0.18em;
  text-transform: uppercase; font-weight: 600;
  padding: 6px 14px; border-radius: 999px;
  margin-bottom: 24px;
}
.compare-tag--neg { background: rgba(255,255,255,0.05); color: var(--c-ink-2); }
.compare-tag--pos { background: var(--c-acc); color: var(--c-acc-ink); }
.compare-col ul { list-style: none; padding: 0; }
.compare-col li { font-size: 20px; line-height: 1.5; padding: 12px 0 12px 24px; position: relative; }
.compare-col li::before { content: '—'; position: absolute; left: 0; color: var(--c-acc); }
```

---

## 9. Timeline (process steps)

Вертикальна лінія, 3-7 кроків. Кожен з номером, заголовком, описом.

```html
<section class="slide slide--timeline" data-slide="10">
  <div class="slide-content">
    <h2 class="slide-h2 reveal">Етапи впровадження</h2>
    <div class="timeline reveal">
      <div class="tl-step">
        <div class="tl-dot"></div>
        <div class="tl-content">
          <div class="tl-num">01</div>
          <div class="tl-h">Discovery</div>
          <p>Інтервʼю зі стейкхолдерами, маппінг процесів</p>
        </div>
      </div>
      <div class="tl-step">
        <div class="tl-dot"></div>
        <div class="tl-content">
          <div class="tl-num">02</div>
          <div class="tl-h">Pilot</div>
          <p>2-тижневий pilot з відділом продажів</p>
        </div>
      </div>
      <div class="tl-step">
        <div class="tl-dot"></div>
        <div class="tl-content">
          <div class="tl-num">03</div>
          <div class="tl-h">Rollout</div>
          <p>Поетапне підключення усіх відділів</p>
        </div>
      </div>
      <div class="tl-step">
        <div class="tl-dot"></div>
        <div class="tl-content">
          <div class="tl-num">04</div>
          <div class="tl-h">Optimize</div>
          <p>Доналаштування за фідбеком, тренінги</p>
        </div>
      </div>
    </div>
  </div>
</section>
```

**CSS:**
```css
.timeline { position: relative; padding-left: 48px; margin-top: 48px; }
.timeline::before {
  content: '';
  position: absolute; left: 8px; top: 12px; bottom: 12px;
  width: 2px;
  background: linear-gradient(180deg, transparent, var(--c-acc-mid) 10%, var(--c-acc-mid) 90%, transparent);
}
.tl-step { position: relative; padding-bottom: 32px; }
.tl-step:last-child { padding-bottom: 0; }
.tl-dot {
  position: absolute; left: -47px; top: 18px;
  width: 18px; height: 18px;
  background: var(--c-acc);
  border-radius: 50%;
  box-shadow: 0 0 0 4px var(--c-bg), 0 0 0 5px var(--c-acc-mid);
}
.tl-num { font-family: var(--font-mono); font-size: 13px; letter-spacing: 0.18em; color: var(--c-acc); font-weight: 600; }
.tl-h { font-size: 28px; font-weight: 700; margin: 4px 0 8px; letter-spacing: -0.02em; }
.tl-step p { font-size: 18px; color: var(--c-ink-2); line-height: 1.5; max-width: 800px; }
```

---

## 10. Speaker intro

Фото спікера + імʼя + посада + 2-3 рядки біо.

```html
<section class="slide slide--speaker" data-slide="2">
  <div class="slide-content speaker-content">
    <div class="speaker-photo reveal">
      <img src="https://crmium.com/wp-content/uploads/2026/05/oleksandr-melnyk.jpg" alt="Олександр Мельник">
    </div>
    <div class="speaker-info">
      <div class="speaker-eyebrow reveal">СПІКЕР</div>
      <h1 class="speaker-name reveal">Олександр Мельник</h1>
      <div class="speaker-role reveal">Solutions Architect · CRMiUM</div>
      <p class="speaker-bio reveal">
        12 років у CRM/ERP. Веду команду з 6 архітекторів.
        За плечима 40+ впроваджень Zoho для виробничих і дистрибʼюторських компаній.
      </p>
    </div>
  </div>
</section>
```

**CSS:**
```css
.speaker-content { display: grid; grid-template-columns: 400px 1fr; gap: 64px; align-items: center; }
.speaker-photo {
  aspect-ratio: 1/1;
  border-radius: 24px;
  overflow: hidden;
  background: var(--c-card);
}
.speaker-photo img { width: 100%; height: 100%; object-fit: cover; object-position: top center; }
.speaker-eyebrow { font-family: var(--font-mono); font-size: 14px; letter-spacing: 0.2em; color: var(--c-acc); font-weight: 600; }
.speaker-name { font-size: clamp(48px, 5vw, 80px); font-weight: 800; line-height: 1; letter-spacing: -0.03em; margin: 12px 0; }
.speaker-role { font-size: 24px; color: var(--c-acc); font-weight: 500; margin-bottom: 32px; }
.speaker-bio { font-size: 22px; line-height: 1.55; color: var(--c-ink-2); max-width: 700px; }
```

---

## 11. Contact (фінальний)

Контакти спікера. Великий email + соцмережі. Логотип CRMiUM унизу.

```html
<section class="slide slide--contact" data-slide="12">
  <div class="slide-content">
    <div class="contact-eyebrow reveal">КОНТАКТИ</div>
    <h1 class="contact-name reveal">Олександр Мельник</h1>
    <div class="contact-role reveal">Solutions Architect · CRMiUM</div>
    <div class="contact-grid reveal">
      <a class="contact-link" href="mailto:o.melnyk@crmium.com">
        <div class="contact-label">Email</div>
        <div class="contact-value">o.melnyk@crmium.com</div>
      </a>
      <a class="contact-link" href="tel:+380501234567">
        <div class="contact-label">Phone</div>
        <div class="contact-value">+380 50 123 45 67</div>
      </a>
      <a class="contact-link" href="https://linkedin.com/in/melnyk-o" target="_blank">
        <div class="contact-label">LinkedIn</div>
        <div class="contact-value">linkedin.com/in/melnyk-o</div>
      </a>
      <a class="contact-link" href="https://crmium.com" target="_blank">
        <div class="contact-label">Web</div>
        <div class="contact-value">crmium.com</div>
      </a>
    </div>
    <div class="contact-logo reveal">
      <img src="https://crmium.com/wp-content/uploads/2026/05/logo-white-for-dark-background.png" alt="CRMiUM" height="32">
    </div>
  </div>
</section>
```

**CSS:**
```css
.contact-eyebrow { font-family: var(--font-mono); font-size: 16px; letter-spacing: 0.2em; color: var(--c-acc); font-weight: 600; }
.contact-name { font-size: clamp(48px, 6vw, 96px); font-weight: 800; letter-spacing: -0.035em; margin: 12px 0; line-height: 1; }
.contact-role { font-size: 24px; color: var(--c-ink-2); margin-bottom: 64px; }
.contact-grid { display: grid; grid-template-columns: repeat(2, 1fr); gap: 24px; max-width: 1100px; }
.contact-link {
  display: block;
  padding: 24px 28px;
  background: var(--c-card);
  border: 1px solid var(--c-line);
  border-radius: 16px;
  text-decoration: none;
  color: inherit;
  transition: border-color .3s cubic-bezier(.22,1,.36,1), transform .3s;
}
.contact-link:hover { border-color: var(--c-acc-mid); transform: translateY(-2px); }
.contact-label { font-family: var(--font-mono); font-size: 13px; letter-spacing: 0.18em; color: var(--c-ink-2); font-weight: 600; text-transform: uppercase; margin-bottom: 8px; }
.contact-value { font-size: 22px; color: var(--c-ink); font-weight: 500; }
.contact-logo { margin-top: 64px; opacity: 0.6; }
```

---

## 12. Pains-grid (3 картки болів — як на лендінгу `.br-pains-grid`)

3 проблеми бізнесу, кожна — окрема картка з тегом + заголовком + 3-4 пунктами.

```html
<section class="slide slide--pains" data-slide="6">
  <div class="slide-content">
    <div class="eyebrow reveal">БОЛІ БІЗНЕСУ</div>
    <h2 class="slide-h2 reveal">3 симптоми <em>застарілої</em> системи</h2>
    <div class="pains-grid reveal">
      <div class="pain-card">
        <div class="pain-tag">ДАНІ</div>
        <h3 class="pain-h">Кожен має <em>свою правду</em></h3>
        <ul class="pain-list">
          <li>15 файлів Excel із продажами</li>
          <li>Інформація розкидана по людях</li>
          <li>Звіт для CEO формується 3 дні</li>
        </ul>
      </div>
      <!-- ще 2 pain-cards -->
    </div>
  </div>
</section>
```

**CSS:**
```css
.pains-grid { display: grid; grid-template-columns: repeat(3, 1fr); gap: 24px; margin-top: 56px; }
.pain-card {
  background: var(--c-card); border: 1px solid var(--c-line); border-radius: 24px;
  padding: 44px 40px; display: flex; flex-direction: column; gap: 22px;
  transition: border-color .3s var(--ease), transform .3s var(--ease), box-shadow .3s var(--ease);
}
.pain-card:hover { border-color: var(--c-acc-mid); transform: translateY(-4px); box-shadow: 0 12px 28px rgba(239,101,47,0.14); }
.pain-tag { font-family: var(--font-mono); font-size: 14px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--c-acc); font-weight: 600; }
.pain-h { font-size: 38px; font-weight: 800; line-height: 1.1; letter-spacing: -0.02em; }
.pain-h em { font-style: italic; color: var(--c-acc); font-weight: 800; }
.pain-list { list-style: none; padding: 0; display: flex; flex-direction: column; gap: 14px; font-size: 20px; line-height: 1.5; color: var(--c-ink-2); }
.pain-list li { padding-left: 22px; position: relative; }
.pain-list li::before { content: '—'; position: absolute; left: 0; color: var(--c-acc); font-weight: 700; }
```

⚠️ **Чому 38px заголовок і 20px список:** з відстані 5-15 метрів дрібніший шрифт нечитабельний. Не зменшуй ці значення.

---

## 13. Bento — mixed grid (як `.br-what-grid` на лендінгу)

5 карток у grid `2fr/1fr/1fr` з 1 великою (span 2 rows) + 4 малими (одна accent помаранчева).

```html
<section class="slide slide--bento" data-slide="8">
  <div class="slide-content">
    <div class="eyebrow reveal">ЩО МИ ВПРОВАДЖУЄМО</div>
    <h2 class="slide-h2 reveal">Zoho One — <em>єдина</em> екосистема</h2>
    <div class="bento-grid reveal">
      <div class="bento-card bento-card--big">
        <div class="bento-tag">ОСНОВА</div>
        <div>
          <div class="bento-num" data-counter="55">0</div>
          <div class="bento-num"><span>+ модулів</span></div>
        </div>
        <p>Все що потрібно для бізнесу — від продажу і маркетингу до фінансів і HR.</p>
      </div>
      <div class="bento-card">
        <div class="bento-tag">CRM</div>
        <div class="bento-h">Zoho CRM</div>
        <p>Pipelines, ліди, угоди</p>
      </div>
      <!-- ще 3 bento-cards (1 accent) -->
    </div>
  </div>
</section>
```

**CSS:**
```css
.bento-grid { display: grid; grid-template-columns: 2fr 1fr 1fr; grid-auto-rows: minmax(220px, auto); gap: 20px; margin-top: 56px; }
.bento-card { background: var(--c-card); border: 1px solid var(--c-line); border-radius: 24px; padding: 36px 34px; display: flex; flex-direction: column; gap: 14px; transition: border-color .3s var(--ease), transform .3s var(--ease), box-shadow .3s var(--ease); }
.bento-card:hover { border-color: var(--c-acc-mid); transform: translateY(-4px); box-shadow: 0 12px 28px rgba(239,101,47,0.14); }
.bento-card--big { grid-row: span 2; justify-content: space-between; padding: 44px 40px; }
.bento-tag { font-family: var(--font-mono); font-size: 14px; letter-spacing: 0.18em; text-transform: uppercase; color: var(--c-acc); font-weight: 600; }
.bento-h { font-size: 34px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.15; }
.bento-card--big .bento-h { font-size: 42px; }
.bento-card p { font-size: 19px; color: var(--c-ink-2); line-height: 1.5; margin-top: auto; }
.bento-num { font-size: 104px; font-weight: 800; line-height: 1; letter-spacing: -0.04em; }
.bento-num span { font-size: 56px; color: var(--c-acc); }
.bento-card--accent { background: var(--c-acc); color: var(--c-acc-ink); border-color: transparent; }
.bento-card--accent .bento-tag, .bento-card--accent p { color: var(--c-acc-ink-2); }
.bento-card--accent .bento-h, .bento-card--accent .bento-num { color: var(--c-acc-ink); }
```

---

## 14. Features-grid (4 картки з accent — як `.br-flex-grid`)

4 переваги/фічі. Одна (зазвичай ключова) — accent помаранчева і span 2 cols. Кожна з icon-tag.

```html
<section class="slide slide--features" data-slide="9">
  <div class="slide-content">
    <div class="eyebrow reveal">ПЕРЕВАГИ</div>
    <h2 class="slide-h2 reveal">Чому Zoho One обирають <em>українські</em> компанії</h2>
    <div class="features-grid reveal">
      <div class="feature-card">
        <div class="feature-icon">$</div>
        <h3 class="feature-h">ROI 8-12 місяців</h3>
        <p>Найкращий показник серед розглянутих CRM</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">UA</div>
        <h3 class="feature-h">Українська локалізація</h3>
        <p>UI, документація, підтримка українською</p>
      </div>
      <div class="feature-card feature-card--accent">
        <div class="feature-icon">★</div>
        <h3 class="feature-h">CRMiUM — Premium Partner</h3>
        <p>Найвищий рівень партнерства Zoho в Україні. Прямий доступ до Zoho engineering.</p>
      </div>
      <div class="feature-card">
        <div class="feature-icon">⚡</div>
        <h3 class="feature-h">Швидкий запуск</h3>
        <p>Pilot — 2 тижні, повний rollout — 2-3 місяці</p>
      </div>
    </div>
  </div>
</section>
```

**CSS:**
```css
.features-grid { display: grid; grid-template-columns: repeat(4, 1fr); gap: 20px; margin-top: 56px; }
.feature-card { background: var(--c-card); border: 1px solid var(--c-line); border-radius: 22px; padding: 36px 32px; display: flex; flex-direction: column; gap: 20px; transition: border-color .3s var(--ease), transform .3s var(--ease), box-shadow .3s var(--ease); }
.feature-card:hover { border-color: var(--c-acc-mid); transform: translateY(-4px); box-shadow: 0 12px 28px rgba(239,101,47,0.14); }
.feature-card--accent { grid-column: span 2; background: var(--c-acc); color: var(--c-acc-ink); border-color: transparent; }
.feature-icon { width: 64px; height: 64px; border-radius: 16px; background: var(--c-acc-soft); color: var(--c-acc); display: grid; place-items: center; font-size: 28px; font-weight: 700; }
.feature-card--accent .feature-icon { background: rgba(255,255,255,0.18); color: var(--c-acc-ink); }
.feature-h { font-size: 28px; font-weight: 700; letter-spacing: -0.02em; line-height: 1.15; }
.feature-card--accent .feature-h { color: var(--c-acc-ink); font-size: 32px; }
.feature-card p { font-size: 19px; color: var(--c-ink-2); line-height: 1.5; margin-top: auto; }
.feature-card--accent p { color: var(--c-acc-ink-2); font-size: 20px; }
```

---

## 15. Q&A — закриваючий слайд (без QR)

Q&A слайд — фінальний акцент перед контактами: великий помаранчевий «Питання?» + короткий підпис. Тон формальний (Ви) — аудиторія часто власники та C-level. Без QR — цей скіл не збирає питання через форму.

```html
<section class="slide slide--qa" data-slide="10">
  <img class="slide-watermark slide-watermark--top" src="assets/crmium-outline.png" alt="">
  <div class="slide-content qa-grid">
    <div class="qa-text-side">
      <h1 class="qa-text reveal"><em>Питання?</em></h1>
      <p class="qa-sub reveal">
        Дякую за увагу. Звертайтеся будь-коли —
        контакти на наступному слайді.
      </p>
    </div>
  </div>
</section>
```

**CSS:**
```css
.slide--qa {
  background:
    radial-gradient(120% 90% at 80% 110%, rgba(239,101,47,0.40) 0%, transparent 55%),
    radial-gradient(80% 70% at 0% 0%, rgba(239,101,47,0.10) 0%, transparent 50%),
    var(--c-bg);
}
.qa-grid { display: flex; flex-direction: column; justify-content: center; max-width: 1200px; }
.qa-text { font-size: clamp(96px, 12vw, 220px); font-weight: 800; line-height: 0.9; letter-spacing: -0.045em; color: #FFFFFF; }
.qa-text em { font-style: normal; color: var(--c-acc); font-weight: 800; }
.qa-sub { font-size: 26px; color: var(--c-ink-2); margin-top: 32px; line-height: 1.4; max-width: 560px; }
```

⚠️ На Q&A слайді хедер ховається автоматично (через `body.no-bar`).

---

## 16. Resources — текстовий слайд "корисні матеріали" (без QR)

Окремий слайд перед Contact: що аудиторія отримає після виступу — як ТЕКСТ, без QR і без Telegram-підписки. Матеріали зазвичай надсилають на пошту або дають у контактах.

```html
<section class="slide slide--resources" data-slide="11">
  <div class="slide-content resources-grid">
    <div class="resources-info">
      <div class="eyebrow reveal">КОРИСНІ МАТЕРІАЛИ</div>
      <h2 class="resources-h reveal">Що <em>далі</em>?</h2>
      <p class="resources-text reveal">
        Усі матеріали по темі цього виступу надішлемо на пошту:
      </p>
      <ul class="resources-features reveal">
        <li>Посилання та джерела з цієї презентації</li>
        <li>Повні кейси клієнтів CRMiUM</li>
        <li>Чек-листи з впровадження Zoho</li>
        <li>Запис виступу та слайди у PDF</li>
      </ul>
      <p class="resources-text reveal" style="margin-top:28px;">
        Напишіть нам — контакти на наступному слайді.
      </p>
    </div>
  </div>
</section>
```

**CSS:**
```css
.slide--resources {
  background:
    radial-gradient(100% 80% at 100% 0%, rgba(239,101,47,0.15) 0%, transparent 55%),
    var(--c-bg);
}
.resources-grid { display: flex; flex-direction: column; justify-content: center; max-width: 1100px; }
.resources-h { font-size: clamp(48px, 5.5vw, 92px); font-weight: 800; line-height: 1.0; letter-spacing: -0.035em; color: var(--c-ink); margin-bottom: 28px; }
.resources-h em { font-style: normal; color: var(--c-acc); font-weight: 800; }
.resources-text { font-size: 22px; color: var(--c-ink-2); line-height: 1.55; max-width: 620px; }
.resources-features { list-style: none; padding: 0; margin-top: 32px; display: flex; flex-direction: column; gap: 14px; }
.resources-features li { font-size: 19px; color: var(--c-ink); padding-left: 28px; position: relative; line-height: 1.4; }
.resources-features li::before { content: '→'; position: absolute; left: 0; top: 0; color: var(--c-acc); font-weight: 700; }
```

> Цей скіл — без QR. Шаблон не містить `.qr-card`, QR-картинок чи Telegram-слайда. Якщо потрібні QR для живого виступу — це сусідній скіл `crmium-presentation-bento`.

---

## Правила вибору слайдів

1. **Не використовувати один тип >3 разів підряд** — варіюй між bullets, stats, bento, quote.
2. **Section divider — на кожну "розділову" точку**: між Discovery і Solution, між Customer Story і Outcome.
3. **Stats — раз на 4-5 слайдів максимум**. Якщо метрик нема — пропусти, не вигадуй.
4. **Quote — раз за презентацію** (макс. 2). Особливо потужно для customer stories.
5. **Image full-bleed — для емоційних моментів** (фото команди, dashboard real-life screenshot).
6. **Compare — для product talks** (до/після, ми/конкурент).
7. **Timeline — для process talks** (як впроваджували, roadmap).

---

## Reveal класи

Будь-який елемент з класом `.reveal` всередині `.slide.is-active` отримує stagger reveal (200/350/500/650/800ms). Перший дочірній `.reveal` — затримка 200ms, кожен наступний +150ms.

Якщо потрібен один великий хіт без stagger — додай `.reveal-instant` (один delay 200ms).
