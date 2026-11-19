# RetroCast – Local on the 8s

A 1990s cable-weather style local forecast that runs in your browser: Local on the 8s, a red warning crawl, surrounding cities, the week ahead and smooth jazz.

## Install (GitHub Pages)
1. Create a GitHub repo → **Add file → Upload files** → drag in *everything* from this folder (keep the `css`, `js`, `icons`, `fonts` folders).
2. **Settings → Pages** → Source: *Deploy from a branch* → `main` / `(root)` → Save.
3. Open the Pages link. iPhone: Safari → Share → **Add to Home Screen**. Mac/PC: Chrome or Edge → install icon in the address bar.

## Controls
Tap the screen (or move the mouse) to show controls. Keyboard: ←/→ pages, Space pause, M music, S settings, L location, F fullscreen.

## Data sources (free, no API keys)
- **Open-Meteo**: current conditions, forecasts, sunrise/sunset and nearby cities. Worldwide.
- **NOAA / National Weather Service**: US only. Station observations, forecast text and severe weather alerts.

## Refresh
Current conditions and alerts refresh every 30 seconds. The full forecast refreshes every 15 minutes. Refreshing pauses in the background and catches up when you come back.

## Local testing
`python3 serve.py`, then open http://localhost:8008. Add `?demo=1` for a snowy demo with a test warning.

A fan tribute to 1990s cable weather. Not affiliated with The Weather Channel.
