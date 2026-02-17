import requests
import json

# Define the base URL
url = 'https://api.gbif.org/v1/species/search'

params = {
    'datasetKey': 'd7dddbf4-2cf0-4f39-9b2a-bb099caae36c',
    'q': 'kangaroo'
}

headers = {
    'accept': 'application/json'
}

# Send GET request
response = requests.get(url, headers=headers, params=params)

# Check if request was successful
if response.status_code == 200:
    data = response.json()
    extracted_animals = []

    for animal in data.get("results", []):
        vernaculars = animal.get("vernacularNames", [])

        # Try to get first English name
        best_name = next(
            (
                v.get("vernacularName").strip().title()
                for v in vernaculars
                if v.get("vernacularName")
                and (v.get("language") == "eng" or v.get("c") == "eng")
            ),
            None
        )

        # Fallback to first available name if no English found
        if not best_name:
            best_name = next(
                (
                    v.get("vernacularName").strip().title()
                    for v in vernaculars
                    if v.get("vernacularName")
                ),
                None
            )

        extracted_animals.append({
            "scientificName": animal.get("scientificName"),
            "authorship": animal.get("authorship"),
            "kingdom": animal.get("kingdom"),
            "habitats": animal.get("habitats", []),
            "threatStatuses": animal.get("threatStatuses", []),
            "vernacularName": best_name
        })

    print(json.dumps(extracted_animals, indent=2))

else:
    print(f"Request failed with status code {response.status_code}")
