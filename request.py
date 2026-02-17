import requests

# Function to get images for a species using taxonKey
def get_species_images(species_key, image_limit=3):
    url = 'https://api.gbif.org/v1/occurrence/search'
    params = {
        "taxonKey": species_key,
        "mediaType": "StillImage",
        "limit": image_limit
    }

    response = requests.get(url, params=params)
    if response.status_code != 200:
        return []

    images = []
    for occurrence in response.json().get('results', []):
        for media in occurrence.get("media", []):
            if media.get("identifier"):
                images.append(media["identifier"])
    return images


# 🔥 NEW MAIN FUNCTION
def search_species(query: str):
    species_url = "https://api.gbif.org/v1/species/search"
    species_params = {"q": query, "limit": 50}

    species_response = requests.get(species_url, params=species_params)

    if species_response.status_code != 200:
        return []

    species_results = species_response.json().get('results', [])
    extracted = []

    for item in species_results:
        vernacular_names = item.get('vernacularNames', [])
        vernacular_name = None

        # Get English name if available
        for vn in vernacular_names:
            if vn.get("lang") == 'eng':
                vernacular_name = vn.get("vernacularName")
                break

        if not vernacular_name and vernacular_names:
            vernacular_name = vernacular_names[0].get('vernacularName')

        key = item.get('key')

        animal_data = {
            "scientificName": item.get("scientificName"),
            "authorship": item.get("authorship"),
            "kingdom": item.get("kingdom"),
            "rank": item.get("rank"),
            "status": item.get("taxonomicStatus"),
            "extinct": item.get("extinct", False),
            "vernacularName": vernacular_name,
            "images": get_species_images(key) if key else []
        }

        extracted.append(animal_data)

    return extracted
