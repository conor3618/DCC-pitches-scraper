"""
Fingal County Council Pitch Playability Scraper
"""

import requests
from bs4 import BeautifulSoup
import json
from datetime import datetime, timezone
import os

FINGAL_URL = "https://www.fingal.ie/playability-pitches"

def scrape_fingal_pitches():
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36"}
    r = requests.get(FINGAL_URL, headers=headers, timeout=30)
    soup = BeautifulSoup(r.text, "html.parser")

    # Use only the first (main) table
    table = soup.find_all("table")[0]
    rows = table.find_all("tr")

    # Row 1 = report date
    report_date = rows[1].get_text(strip=True) if len(rows) > 1 else "Unknown"

    pitches = []
    # Row 0 = title, Row 1 = date, Row 2 = headers (Park/ON/OFF), Row 3+ = data
    for row in rows[3:]:
        cols = [td.get_text(strip=True) for td in row.find_all("td")]
        if cols and cols[0]:
            name = cols[0]
            status_on = cols[1] if len(cols) > 1 else ""
            status_off = cols[2] if len(cols) > 2 else ""

            # Skip malformed rows where name bleeds into status_on
            if status_on == name:
                status_on = ""

            status = status_on if status_on.strip() else status_off
            playable = status_on.strip() != "" and status_off.strip() == ""

            pitches.append({
                "name": name,
                "status": status,
                "playable": playable,
                "Council": "FCC"
            })

    data = {
        "scrape_time": datetime.now(timezone.utc).isoformat(),
        "council": "FCC",
        "pitches": pitches
    }
    
    os.makedirs("data", exist_ok=True)
    with open("data/fingal_pitches.json", "w", encoding='utf-8') as f:
        json.dump(data, f, indent=2, ensure_ascii=False)

    return pitches

def print_fingal_statuses(pitches):
    playable = sum(1 for p in pitches if p["playable"])
    print("FINGAL COUNTY COUNCIL PITCHES:")
    print(f"PLAYABLE: {playable}/{len(pitches)}\n")
    
    for p in pitches:
        status = "Playable" if p["playable"] else "Unplayable"
        print(f"{p['name']} : {status}")

if __name__ == "__main__":
    pitches = scrape_fingal_pitches()
    print_fingal_statuses(pitches)
    print("\n✓ Data exported to data/fingal_pitches.json")
