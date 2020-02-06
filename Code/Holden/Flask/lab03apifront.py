from flask import Flask, render_template, request, redirect
import requests
import json
from secrets import cat_key
import codecs
import os
import time
app = Flask(__name__)
headers = {"x-api-key": cat_key}
@app.route('/')
def index():
    response = requests.get('https://api.thecatapi.com/v1/images/search?limit=1&page=0&mime_types=png', headers=headers)
    image_list = json.loads(response.text)
    background = image_list[0]["url"]
    breed_resp = requests.get('https://api.thecatapi.com/v1/breeds/', headers=headers)
    if os.path.getmtime('breeds.json') < (time.time()-3600):
        with codecs.open('breeds.json', 'w', 'utf-8-sig') as file:
            file.write(breed_resp.text)
    with codecs.open('breeds.json', 'r', 'utf-8-sig') as file:
        breedfile = file.read()
    breed_info = json.loads(breedfile)
    breeds = []
    for breed in breed_info:
        breeds.append((breed["id"], breed["name"]))
    category_resp = requests.get('https://api.thecatapi.com/v1/categories/', headers=headers)
    # if os.path.getmtime('categories.json') < (time.time()-3600):
    with codecs.open('categories.json', 'w', 'utf-8-sig') as file:
        file.write(category_resp.text)
    with codecs.open('categories.json', 'r', 'utf-8-sig') as file:
        categoryfile = file.read()
    category_info = json.loads(categoryfile)
    categories = []
    for category in category_info:
        categories.append((category["id"], category["name"]))
    print(background)
    return render_template('catindex.html', background=background, breeds=breeds, categories=categories)

@app.route('/search/', methods=["POST"])
def searchgrab():
    urlstart = 'https://api.thecatapi.com/v1/images/search?page=' + request.form['page']
    listform_url = [urlstart, ('limit=' + request.form['limit'])]
    breed = request.form['breed']
    category = request.form['category']
    # file = request.form['image_type']
    if breed:
        listform_url.append('breed_ids=' + breed)
    urlout = "&".join(listform_url)
    return redirect('/')
    # response = requests.get('https://api.thecatapi.com/v1/images/search?limit=3&page=0', headers=headers)
