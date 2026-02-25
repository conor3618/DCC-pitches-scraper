# Dublin & Fingal Pitches Scraper

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
```
