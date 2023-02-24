import requests
from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=['GET'])
def index():
    return render_template('index.html')

@app.route('/', methods=['POST'])
def index_post():
    url = "https://google-translate1.p.rapidapi.com/language/translate/v2"

    
    # Read the values from the form
    original_text = request.form['text']    
    target_language = request.form['language']
    #print(target_language)

    # Define the headers
    headers = {
	"content-type": "application/x-www-form-urlencoded",
	"Accept-Encoding": "application/gzip",
	"X-RapidAPI-Key": "",
	"X-RapidAPI-Host": "google-translate1.p.rapidapi.com"
    }

    # Payload
    payload = "target=en&format=text&q="+original_text
    
    # Post the request
    response = requests.request("POST", url, data=payload, headers=headers)

    # Extract the response
    translated_text = response.json()['data']['translations'][0]["translatedText"]

    # Call the render template, passing the translated text,
    # original text, and target languate to the template
    return render_template(
        'results.html',
        translated_text = translated_text,
        original_text = original_text,
        target_language = target_language
    )


if __name__ == "__main__":
    app.run(debug=True)