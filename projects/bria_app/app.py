import time
import requests
from flask import Flask, request, render_template

app = Flask(__name__)


url = "https://engine.prod.bria-api.com/v1/search"
headers = {"api_token": "xyz"}


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'GET':
        return render_template('index.html')
    
    if request.method == 'POST':
        # retrieve the selected options from the form
        query_text = request.form['query']
        style = request.form['style']
        atmosphere = request.form['atmosphere']
        camera = request.form['camera']
        medium = request.form['medium']

        query = {
                "query": query_text,
                "synchronous": "false",
                "gallery_search": "false",
                "num_results_per_page": "1",
                "synthetic_search": "true",
                "num_synthetic_results_per_page": "1",
                "page": "1",
                "style": style,
                "atmosphere": atmosphere,
                "camera": camera,
                "medium": medium
                }
        
        # Get the generated new image from Bria API
        response = requests.get(url, headers=headers, params=query)
        # Returns a JSON response
        imgs_url = response.json()
        # Extracting image URL from JSON response
        img_url = imgs_url['results'][0]['url']

        # Check if status code is 200
        respuesta = requests.get(img_url)
        while respuesta.status_code != 200:
            time.sleep(1)
            respuesta = requests.get(img_url)

        # Render template and image
        return render_template('index.html', img_url=img_url)

    else:
        return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True)