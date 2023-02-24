import requests
from flask import Flask, request, render_template

app = Flask(__name__)


url = "https://engine.prod.bria-api.com/v1/search"
headers = {"api_token": "my_token"}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        query_text = request.form['query']
        query = {
                "query": query_text,
                "synchronous": "false",
                "gallery_search": "false",
                "num_results_per_page": "1",
                "synthetic_search": "true",
                "num_synthetic_results_per_page": "1",
                "page": "1",
                "style": "oil painting",
                "atmosphere": "vivid",
                #"camera": "portrait",
                "medium": "art"
                }
        # Get the generated new image from Bria API
        response = requests.get(url, headers=headers, params=query, timeout=30)
        # Returns a JSON response
        imgs_url = response.json()
        # Extracting image URL from JSON response
        img_url = imgs_url['results'][0]['url']

        # Render template and image
        return render_template('index.html', img_url=img_url, timeout=30)

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)