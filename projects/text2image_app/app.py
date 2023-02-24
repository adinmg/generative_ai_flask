'''
Search for images matching the given text query
Description
By using the Search Route, you can utilize Bria's generative search capabilities, which don't require labels or keywords.
The user can send any text query and receive relevant images that match the query.
The Search Route returns the images, sorted by the match score, from highest match to lowest match. The images are returned in batches, and you can specify how many images to receive in one batch, and which batch to receive in each call.
'''

import requests

url = "https://engine.prod.bria-api.com/v1/search"

query = {
  "query": "woman traveling in the world",
  "synchronous": "true",
  "gallery_search": "true",
  "num_results_per_page": "1",
  "synthetic_search": "false",
  "num_synthetic_results_per_page": "1",
  "page": "1",
  "gallery_id": "123abc",
  "style": "photo realistic",
  "atmosphere": "dramatic",
  "camera": "portrait",
  "medium": "photography"
}

response = requests.get(url, params=query)

data = response.json()
print(data)