from flask import Flask, request, jsonify, render_template
import requests
import os
import json

app = Flask(__name__)

GITHUB_API_URL = "https://api.github.com/search/repositories"

@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search', methods=['GET'])
def search_repositories():
    keyword = request.args.get('keyword', '')
    if not keyword:
        return jsonify({"error": "Keyword is required"}), 400

    params = {
        "q": keyword,
        "sort": "stars",
        "order": "desc",
        "per_page": 10
    }
    response = requests.get(GITHUB_API_URL, params=params)

    if response.status_code == 200:
        return jsonify(response.json()["items"])
    else:
        return jsonify({"error": "Failed to fetch data from GitHub"}), response.status_code

@app.route('/save_favorites', methods=['POST'])
def save_favorites():
    data = request.get_json()  
    file_name = "favorites.json"

    # Validating the data
    if not data or not isinstance(data, list):
        return jsonify({"error": "Invalid data format"}), 400

    # Checking if the file exists
    if os.path.exists(file_name):
        with open(file_name, "r") as file:
            try:
                existing_favorites = json.load(file)
            except json.JSONDecodeError:
                existing_favorites = []
    else:
        existing_favorites = []


    existing_favorites.extend(repo for repo in data if repo not in existing_favorites)

    with open(file_name, "w") as file:
        json.dump(existing_favorites, file, indent=4)

    return jsonify({"message": "Favorites saved successfully!"})

if __name__ == '__main__':
    app.run(debug=True)