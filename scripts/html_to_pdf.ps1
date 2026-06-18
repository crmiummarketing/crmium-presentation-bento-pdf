<#
html_to_pdf.ps1 — рендерить HTML-презентацію CRMiUM (Bento) у PDF через
headless Chrome/Edge. НЕ потребує Python — лише браузер Chrome або Edge.
На Windows PowerShell вбудований, а Edge присутній завжди, тож працює "з коробки".

Використання:
  powershell -ExecutionPolicy Bypass -File html_to_pdf.ps1 <input.html> [output.pdf]

Якщо output не вказано — PDF ляже поряд з input з тим же іменем.
#>
param(
  [Parameter(Mandatory = $true)][string]$HtmlPath,
  [string]$PdfPath
)

$in = (Resolve-Path -LiteralPath $HtmlPath -ErrorAction SilentlyContinue).Path
if (-not $in) { Write-Host "[error] HTML не знайдено: $HtmlPath"; exit 1 }

if (-not $PdfPath) { $PdfPath = [System.IO.Path]::ChangeExtension($in, '.pdf') }
$PdfPath = [System.IO.Path]::GetFullPath($PdfPath)

# Знаходимо Chrome або Edge на стандартних шляхах
$candidates = @(
  (Join-Path $env:ProgramFiles 'Google\Chrome\Application\chrome.exe'),
  (Join-Path ${env:ProgramFiles(x86)} 'Google\Chrome\Application\chrome.exe'),
  (Join-Path $env:ProgramFiles 'Microsoft\Edge\Application\msedge.exe'),
  (Join-Path ${env:ProgramFiles(x86)} 'Microsoft\Edge\Application\msedge.exe'),
  (Join-Path $env:LocalAppData 'Google\Chrome\Application\chrome.exe')
)
$browser = $candidates | Where-Object { Test-Path $_ } | Select-Object -First 1
if (-not $browser) {
  Write-Host "[error] Chrome/Edge не знайдено. Встанови Google Chrome або Microsoft Edge,"
  Write-Host "        або зроби PDF вручну: відкрий HTML -> Ctrl+P -> Save as PDF -> Background graphics ON -> Landscape."
  exit 1
}

$uri = ([System.Uri]$in).AbsoluteUri

# Один рядок аргументів; шляхи зі space — у лапках.
# Start-Process тримає stderr браузера поза error-stream PowerShell (інакше
# нешкідливі warning-и Chrome у PS 5.1 стають термінальною помилкою).
$argString = '--headless=new --disable-gpu --no-pdf-header-footer --no-first-run ' +
             '--disable-background-networking --disable-sync ' +
             ('"--print-to-pdf={0}"' -f $PdfPath) +
             ' --virtual-time-budget=12000 ' +
             ('"{0}"' -f $uri)

Write-Host "[i] browser : $browser"
Write-Host "[i] input   : $in"
Write-Host "[i] output  : $PdfPath"

$errLog = [System.IO.Path]::GetTempFileName()
try {
  Start-Process -FilePath $browser -ArgumentList $argString -NoNewWindow -Wait -RedirectStandardError $errLog | Out-Null
} catch {
  Write-Host "[error] не вдалося запустити браузер: $($_.Exception.Message)"
}
Remove-Item $errLog -ErrorAction SilentlyContinue

if ((Test-Path -LiteralPath $PdfPath) -and ((Get-Item -LiteralPath $PdfPath).Length -gt 0)) {
  $kb = [math]::Round((Get-Item -LiteralPath $PdfPath).Length / 1KB)
  Write-Host "[ok] PDF готовий: $PdfPath ($kb KB)"
  exit 0
} else {
  Write-Host "[error] PDF не створено. Спробуй вручну: відкрий HTML у Chrome -> Ctrl+P -> Save as PDF -> Background graphics ON -> Landscape."
  exit 1
}
