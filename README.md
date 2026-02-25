# Dublin Pitches Tracker (DCC, Fingal, DLR)

A Python project that scrapes **Dublin City Council (DCC)**, **Fingal County Council (FCC)**, and **Dún Laoghaire-Rathdown (DLR)** pitch playability pages.  
Includes a scheduled **GitHub Action** that automatically updates data every day at **8 AM UTC**.

## Features
- **DCC:** Parses HTML tables (63 pitches)
- **Fingal:** Extracts pitch data from webpage tables
- **DLR:** Scrapes map popups (25 pitches with latitude/longitude)
- Handles **UTF‑8 Gaelic names** correctly (e.g., *Páirc Uí Bhríain*)
- Unified JSON structure across all councils
- Automated updates committed daily via GitHub Action

## Scripts

| Script | Council | Output |
|--------|----------|--------|
| `pitch_scraper_dcc.py` | Dublin City Council | `data/dcc_pitches.json` |
| `pitch_scraper_fingal.py` | Fingal County Council | `data/fingal_pitches.json` |
| `pitch_scraper_dlr.py` | Dún Laoghaire‑Rathdown County Council | `data/dlr_pitches.json` |

## Usage

### Run Locally
```bash
python pitch_scraper_dcc.py     # DCC only
python pitch_scraper_fingal.py  # Fingal only
python pitch_scraper_dlr.py     # DLR only

# Example output:
# Data exported to data/dcc_pitches.json
```

## JSON Structure

All JSON outputs follow a shared schema.

**Example (DLR):**
```json
{
  "scrape_time": "2026-02-25T08:00:00Z",
  "council": "DLR",
  "source": "map-popups",
  "pitches": [
    {
      "name": "Páirc Uí Bhríain",
      "status": "playable",
      "playable": true,
      "coordinates": {"lat": 53.279, "lng": -6.222}
    }
  ]
}
```

## Data Folder
```
data/
├── dcc_pitches.json      # Dublin City Council
├── fingal_pitches.json   # Fingal County Council
└── dlr_pitches.json      # DLR County Council
```

## How It Works
1. **DCC:** Parses HTML pitch status tables  
2. **Fingal:** Extracts playability data from webpage  
3. **DLR:** Scrapes Google Maps popup content (`map-popup-rhs-name` + coordinates)  
4. Collects "last updated" metadata where available  
5. Exports structured JSON files to `data/`  
6. GitHub Action runs daily and commits updated data to the repository

## GitHub Action
The daily scheduled workflow:
- Runs all scrapers at 8 AM UTC  
- Updates JSON files in the `data/` folder  
- Creates a new commit with the latest data snapshot

## Data Sources
- [Dublin City Council Pitch Playability](https://www.dublincity.ie/residential/parks/dublin-city-parks/pitch-playability)  
- [Fingal County Council Pitches](https://www.fingal.ie/Pitches)  
- [DLR Pitches Map](https://www.dlrcoco.ie/pitches)

These datasets originate from official council sources.  
No council endorses this project, and data accuracy cannot be guaranteed.

### License
[Licensed under the Unlicense](https://unlicense.org/)
