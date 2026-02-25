update readme "# Dublin & Fingal Pitches Scraper

A Python project that scrapes **Dublin City Council (DCC)** and **Fingal County Council (FCC)** pitch playability pages to retrieve the latest status for all playing pitches. Includes a scheduled GitHub Action that automatically updates data daily.

## Features
- Extracts pitches from DCC and Fingal County Council sources
- Captures "Latest updated" dates directly from webpages
- Determines playability status from "Status On" / "Status Off" table columns
- Exports structured data to `data/dcc_pitches.json` and `data/fingal_pitches.json`
- GitHub Action runs automatically daily at 8AM UTC
- Data files always up to date via automated commits

## Scripts

| Script | Description | Output |
|--------|-------------|---------|
| `pitch_scraper_dcc.py` | DCC pitches scraper | `data/dcc_pitches.json` |
| `pitch_scraper_fingal.py` | Fingal pitches scraper | `data/fingal_pitches.json` |

## Usage

### Local run

```bash

python pitch_scraper_dcc.py    # DCC only
python pitch_scraper_fingal.py # Fingal only


...
Data exported to data/dcc_pitches.json

```

## JSON Structure
Both files follow identical structure:

```json
{
  "scrape_time": "2026-02-24T23:12:00",
  "last_updated": "Latest updated 20th February 2026",
  "pitches": [
    {
      "name": "SUNDRIVE",
      "status_on": "ON", 
      "status_off": "",
      "status": "ON",
      "playable": true
    }
  ]
}
```

## Data Folder
```
data/
├── dcc_pitches.json      # Dublin City Council pitches
└── fingal_pitches.json   # Fingal County Council pitches
```

## How It Works
1. Scrapes DCC pitch playability page for Dublin pitches
2. Scrapes Fingal County Council pitch playability page
3. Extracts "Latest updated" dates from each source
4. Parses status tables to determine playability
5. Exports structured JSON to `data/` folder
6. GitHub Action commits changes daily

## GitHub Action
Scheduled workflow runs both scrapers daily and commits updated JSON files to `data/` folder. Success confirmed by commit message in repository history.

## Data Sources
- [Dublin City Council Pitch Playability](https://www.dublincity.ie/residential/parks/dublin-city-parks/pitch-playability)
- [Fingal County Council Pitches](https://www.fingal.ie/Pitches)

Official council data. Neither council endorses this project nor guarantees data accuracy.

### License
[Licensed under Unlicense](https://unlicense.org/)
"

```markdown
# Dublin Pitches Tracker (DCC + Fingal + DLR)

A Python project that scrapes **Dublin City Council (DCC)**, **Fingal County Council (FCC)**, and **Dún Laoghaire-Rathdown (DLR)** pitch playability pages. Includes scheduled GitHub Action for daily automated updates.

## Features
- DCC: HTML table parsing (63 pitches)
- Fingal: HTML scraping
- **DLR: Map popup extraction (25 pitches + Lat/Lng coordinates)**
- Gaelic UTF-8 names (Páirc Uí Bhríain ✓)
- Daily GitHub Action at 8AM UTC
- Unified JSON structure across councils

## Scripts

| Script | Council | Output |
|--------|---------|--------|
| `pitch_scraper_dcc.py` | DCC | `data/dcc_pitches.json` |
| `pitch_scraper_fingal.py` | Fingal | `data/fingal_pitches.json` |
| `pitch_scraper_dlr.py` | **DLR** | **`data/dlr_pitches.json`** |

## Usage

### Local run

python pitch_scraper_dcc.py    # DCC only
```

## JSON Structure

**DLR**:
```json
{
  "scrape_time": "2026-02-25T08:00:00Z",
  "council": "DLR",
  "source": "map-popups",
  "pitches": [{
    "name": "Páirc Uí Bhríain",
    "status": "playable",
    "playable": true,
    "coordinates": {"lat": 53.279, "lng": -6.222}
  }]
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
1. DCC: Parses HTML status tables
2. Fingal: Extracts pitch playability from HTML  
3. **DLR: Scrapes Google Maps popups** (`map-popup-rhs-name` + coords)
4. Exports unified JSON to `data/` folder
5. GitHub Action commits daily changes

## GitHub Action
Daily 8AM UTC workflow runs all scrapers → commits to `data/`

## Data Sources
- [DCC Pitch Playability](https://www.dublincity.ie/residential/parks/dublin-city-parks/pitch-playability)
- [Fingal Pitches](https://www.fingal.ie/Pitches)  
- [DLR Pitches Map](https://www.dlrcoco.ie/pitches)

Official council data. Councils neither endorse nor guarantee accuracy.

### License
[Unlicense](https://unlicense.org/)