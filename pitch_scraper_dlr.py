#!/usr/bin/env python3
"""
DLR Pitches Scraper - FINAL (Clean Output)
"""

import requests
from bs4 import BeautifulSoup
import json
import re
import os
from datetime import datetime, timezone
from urllib.parse import parse_qs, urlparse

def scrape_dlr_pitches():
    url = "https://www.dlrcoco.ie/pitches"
    headers = {'User-Agent': 'Mozilla/5.0 (compatible; DLR-PitchScraper/2.0)'}
    
    response = requests.get(url, headers=headers, timeout=15)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'html.parser')
    
    pitches = []
    
    popup_elements = soup.find_all('div', class_='map-popup')
    
    for popup in popup_elements:
        name_elem = popup.find('div', class_='map-popup-rhs-name')
        name = name_elem.get_text().strip() if name_elem else "Unknown Pitch"
        
        status_elem = popup.find('div', class_='map-popup-rhs-type')
        status_text = status_elem.get_text().strip().lower() if status_elem else "unknown"
        is_playable = status_text == "playable"
        
        link_elem = popup.find('a', href=True)
        coords = None
        if link_elem and 'google.com/maps' in link_elem['href']:
            query = parse_qs(urlparse(link_elem['href']).query)
            if 'query' in query:
                coord_match = re.search(r'(-?d+.?d*),(-?d+.?d*)', query['query'][0])
                if coord_match:
                    coords = {
                        "lat": float(coord_match.group(1)),
                        "lng": float(coord_match.group(2))
                    }
        
        pitches.append({
            "name": name,
            "status": status_text,
            "playable": is_playable,
            "coordinates": coords
        })
    
    data = {
        "scrape_time": datetime.now(timezone.utc).isoformat(),
        "council": "DLR",
        "source": "map-popups",
        "pitches": pitches,
        "summary": {
            "total": len(pitches),
            "playable": len([p for p in pitches if p["playable"]])
        }
    }
    
    print(f"Exported to data/dlr_pitches.json: {data['summary']['playable']}/{data['summary']['total']} playable")
    return data

def main():
    result = scrape_dlr_pitches()
    
    os.makedirs('data', exist_ok=True)
    
    with open('data/dlr_pitches.json', 'w', encoding='utf-8') as f:
        json.dump(result, f, indent=2, ensure_ascii=False)
    
    print("Exported to data/dlr_pitches.json")

if __name__ == "__main__":
    main()