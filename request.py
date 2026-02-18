import requests
from concurrent.futures import ThreadPoolExecutor

def get_species_images(species_key, image_limit=3):
    url = 'https://api.gbif.org/v1/occurrence/search'
    params = {
        "taxonKey": species_key,
        "mediaType": "StillImage",
        "limit": image_limit
    }

    try:
        response = requests.get(url, params=params, timeout=5)
        response.raise_for_status()
    except:
        return []

    images = []
    for occurrence in response.json().get('results', []):
        for media in occurrence.get("media", []):
            if media.get("identifier"):
                images.append(media["identifier"])
    return images


def search_species(query: str):
    species_url = "https://api.gbif.org/v1/species/search"
    species_params = {"q": query, "limit": 50}  # 🔥 Reduced limit

    try:
        species_response = requests.get(species_url, params=species_params, timeout=5)
        species_response.raise_for_status()
    except:
        return []

    species_results = species_response.json().get('results', [])
    extracted = []

    def process_item(item):
        vernacular_names = item.get('vernacularNames', [])
        vernacular_name = None

        for vn in vernacular_names:
            if vn.get("lang") == 'eng':
                vernacular_name = vn.get("vernacularName")
                break

        if not vernacular_name and vernacular_names:
            vernacular_name = vernacular_names[0].get('vernacularName')

        key = item.get('key')

        return {
            "scientificName": item.get("scientificName"),
            "authorship": item.get("authorship"),
            "kingdom": item.get("kingdom"),
            "extinct": item.get("extinct", False),
            "vernacularName": vernacular_name,
            "habitats": item.get("habitats", []),
            "images": get_species_images(key) if key else []
        }

    # 🔥 PARALLEL EXECUTION
    with ThreadPoolExecutor(max_workers=5) as executor:
        extracted = list(executor.map(process_item, species_results))

    return extracted
