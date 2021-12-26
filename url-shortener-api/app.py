from flask import Flask, request, jsonify
from db import connect_mongo
from dotenv import load_dotenv
import json
import hashlib
import os



app = Flask(__name__)

load_dotenv()

URL = os.getenv('URL')
url_collection = connect_mongo().get_collection('shortened-urls')

@app.route('/api/health')
def get_health():
    return 'URL Shortner API is up'

@app.route('/api/urls', methods=["POST"])
def url_shortener():
    if request.method == 'POST':        
        original_url = json.loads(request.get_data().decode()).get('longURL')
        find_original = url_collection.find_one({'original_url': original_url})
        short_url = ''
        if (find_original):
            short_url = URL + find_original.get('slug')
        else:
            num = int(hashlib.sha256(original_url.encode("utf-8")).hexdigest(), 16) % (10 ** 7)
            slug = str(hex(num))[2:]
            url_collection.insert_one({'original_url': original_url, 'slug': slug})
            short_url = URL + slug

        return jsonify(shortUrl=short_url, isError=False, message="Success", statusCode=200)


@app.route('/api/resolve/<slug>', methods=["GET"])
def resolve_shortened_url(slug):
    if request.method == "GET":
        find_short = url_collection.find_one({'slug': slug})
        if not slug or not find_short:
            return jsonify(isError=True, message="Not Found", statusCode=404)

        original_url = find_short.get("original_url")
        return jsonify(originalUrl=original_url, isError=False, message="Success", statusCode=200)


# if __name__ == '__main__':
#     app.run(debug=True, port=5000) #debug=True, port=5000