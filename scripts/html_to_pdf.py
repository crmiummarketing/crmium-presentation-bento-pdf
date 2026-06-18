#!/usr/bin/env python3
"""
html_to_pdf.py — рендерить single-file HTML-презентацію CRMiUM (Bento)
у PDF через headless Chrome/Edge.

Чому headless Chrome, а не ручний Ctrl+P:
  - сам форсує темний фон (background graphics увімкнено за замовчуванням
    у headless print-to-pdf — спікер не може випадково забути цю галочку);
  - бере @page size 1920×1080 з @media print самої презентації → коректне 16:9;
  - не вимагає жодних npm/pip-залежностей, тільки Chrome або Edge (які майже
    завжди вже є на машині).

Використання:
    python html_to_pdf.py <input.html> [output.pdf]

Якщо output не вказано — кладемо поряд з input з тим же іменем, розширення .pdf.
"""
import os
import sys
import shutil
import subprocess
from pathlib import Path

# Кандидати на стандартних шляхах (коли браузера нема в PATH).
BROWSER_CANDIDATES = [
    # Windows
    r"C:\Program Files\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Google\Chrome\Application\chrome.exe",
    r"C:\Program Files (x86)\Microsoft\Edge\Application\msedge.exe",
    r"C:\Program Files\Microsoft\Edge\Application\msedge.exe",
    # macOS
    "/Applications/Google Chrome.app/Contents/MacOS/Google Chrome",
    "/Applications/Microsoft Edge.app/Contents/MacOS/Microsoft Edge",
    # Linux
    "/usr/bin/google-chrome",
    "/usr/bin/google-chrome-stable",
    "/usr/bin/chromium",
    "/usr/bin/chromium-browser",
    "/usr/bin/microsoft-edge",
]


def find_browser():
    """Спершу шукаємо у PATH, потім на стандартних шляхах."""
    for name in (
        "chrome", "google-chrome", "google-chrome-stable",
        "chromium", "chromium-browser", "msedge", "microsoft-edge",
    ):
        found = shutil.which(name)
        if found:
            return found
    for candidate in BROWSER_CANDIDATES:
        if os.path.exists(candidate):
            return candidate
    return None


def main():
    if len(sys.argv) < 2:
        print("Usage: python html_to_pdf.py <input.html> [output.pdf]")
        sys.exit(2)

    in_path = Path(sys.argv[1]).resolve()
    if not in_path.exists():
        print(f"[error] HTML не знайдено: {in_path}")
        sys.exit(1)

    out_path = (
        Path(sys.argv[2]).resolve()
        if len(sys.argv) > 2
        else in_path.with_suffix(".pdf")
    )

    browser = find_browser()
    if not browser:
        print("[error] Chrome/Edge не знайдено.")
        print("        Встанови Google Chrome або Microsoft Edge, або згенеруй PDF вручну:")
        print("        відкрий HTML → Ctrl+P → Save as PDF → Background graphics ON → Landscape.")
        sys.exit(1)

    file_url = in_path.as_uri()
    cmd = [
        browser,
        "--headless=new",
        "--disable-gpu",
        "--no-sandbox",
        "--no-pdf-header-footer",          # без колонтитулів Chrome
        f"--print-to-pdf={out_path}",
        "--virtual-time-budget=12000",     # дати час Google Fonts (Onest) + JS осісти
        file_url,
    ]
    print(f"[i] browser : {browser}")
    print(f"[i] input   : {in_path}")
    print(f"[i] output  : {out_path}")

    try:
        result = subprocess.run(cmd, capture_output=True, text=True, timeout=120)
    except subprocess.TimeoutExpired:
        print("[error] Рендер перевищив 120с. Перевір, що HTML відкривається у браузері.")
        sys.exit(1)

    if out_path.exists() and out_path.stat().st_size > 0:
        kb = out_path.stat().st_size / 1024
        print(f"[ok] PDF готовий: {out_path}  ({kb:.0f} KB)")
        return

    print("[error] PDF не створено.")
    if result.stderr:
        print(result.stderr[-1500:])
    print("Fallback: відкрий HTML у Chrome → Ctrl+P → Save as PDF →")
    print("          Background graphics ON → Layout Landscape → Margins None.")
    sys.exit(1)


if __name__ == "__main__":
    main()
