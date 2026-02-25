# Dublin Pitches Tracker (DCC, FCC, DLR)

A Python project that scrapes **Dublin City Council (DCC)**, **Fingal County Council (FCC)**, and **Dún Laoghaire-Rathdown (DLR)** pitch playability pages.  
Includes a scheduled **GitHub Action** that automatically updates data every day at **8 AM UTC**.

## Features
- **DCC:** Parses HTML tables
- **FCC:** Extracts pitch data from webpage tables  
- **DLR:** Scrapes map popups
- **Unified JSON structure** across all councils
- Automated daily updates via GitHub Action

## Scripts

| Script | Council | Output |
|--------|---------|--------|
| `pitch_scraper_dcc.py` | DCC | `data/dcc_pitches.json` |
| `pitch_scraper_fingal.py` | FCC | `data/fingal_pitches.json` |
| `pitch_scraper_dlr.py` | DLR | `data/dlr_pitches.json` |

## Usage

### Run Locally
```bash
python pitch_scraper_dcc.py     # DCC only
python pitch_scraper_fingal.py  # FCC only  
python pitch_scraper_dlr.py     # DLR only

# Example output:
# Exported 42/63 playable DCC pitches
# ✓ Data exported to data/dcc_pitches.json
```

## JSON Structure

**Unified format across all councils:**

```json
{
  "scrape_time": "2026-02-25T08:00:00Z",
  "council": "DCC",
  "pitches": [
    {
      "name": "SUNDRIVE",
      "status": "ON",
      "playable": true,
      "Council": "DCC"
    }
  ]
}
```

## Data Folder
```
data/
├── dcc_pitches.json      # Dublin City Council (DCC)
├── fingal_pitches.json   # Fingal County Council (FCC)
└── dlr_pitches.json      # Dún Laoghaire-Rathdown (DLR)
```

## How It Works
1. **DCC:** Parses HTML status tables (`Status On`/`Status Off`)
2. **FCC:** Extracts from main table (Park/ON/OFF columns)  
3. **DLR:** Scrapes map popups (`map-popup-rhs-name` + status)
4. Exports **identical JSON structure** to `data/` folder
5. GitHub Action runs daily → commits updated files

## GitHub Action
Daily workflow at **8 AM UTC**:
- Runs all three scrapers
- Updates JSON files in `data/`
- Commits fresh data snapshot

## Data Sources
- [DCC Pitch Playability](https://www.dublincity.ie/residential/parks/dublin-city-parks/pitch-playability)
- [FCC Playability Pitches](https://www.fingal.ie/playability-pitches)
- [DLR Pitches Map](https://www.dlrcoco.ie/pitches)

Official council data. No endorsement or accuracy guarantees.

### License
[Unlicense](https://unlicense.org/)
