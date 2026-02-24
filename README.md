# Dublin City Council Pitch Scraper

A Python project that scrapes the [DCC Pitch Playability page](https://www.dublincity.ie/residential/parks/dublin-city-parks/pitch-playability) to retrieve the latest playability status for all Dublin City Council pitches. Includes a scheduled GitHub Action that automatically updates data daily.

## Features
- Extracts all 63+ Dublin City Council pitches and playing fields
- Captures "Latest updated" date directly from the webpage
- Determines playability status from "Status On" / "Status Off" table columns
- Exports complete structured data to `dcc_pitches.json`
- GitHub Action runs automatically daily
- `dcc_pitches.json` always up to date via GitHub Actions artifacts

## Scripts

| Script | Description |
|--------|-------------|
| `pitch_scraper.py` | Main scraper - fetches all pitches and generates JSON |

## Usage

### Local run

    python pitch_scraper.py

### Example output

```
DUBLIN CITY COUNCIL PITCHES:
Last updated: Latest updated 20th February 2026

PLAYABLE: 1/63

SUNDRIVE : Playable
ALBERT COLLEGE : Unplayable
ALFIE BYRNE ROAD : Unplayable
...
Data exported to dcc_pitches.json
```

## JSON Structure
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
    },
    {
      "name": "ALBERT COLLEGE",
      "status_on": "",
      "status_off": "OFF",
      "status": "OFF",
      "playable": false
    }
  ]
}
```

## How It Works
1. Fetches HTML from DCC pitch playability page
2. Extracts "Latest updated" date from page `<p><strong>` element
3. Parses pitches table, checking "Status On" column for "ON" keyword
4. Builds structured JSON with timestamps and exports to file
5. Prints clean summary to console

## GitHub Action
A scheduled action runs `pitch_scraper.py` daily and updates `dcc_pitches.json` as an accordingly.

## Data Source
[Dublin City Council](https://www.dublincity.ie)  
Official pitch playability data. DCC neither endorses this project nor guarantees data accuracy.
```
