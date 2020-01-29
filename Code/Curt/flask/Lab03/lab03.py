#lab03.py

from flask import Flask, render_template
import requests
import json

app = Flask(__name__)

@app.route('/')
def index():
    query = '''query ($id: Int) {
        Media (id: $id, type: ANIME) {
            id
            title {
                romaji
                english
                native
            }
            type
            format
            status
            description
            startDate {
                year
                month
                day
            }
            endDate {
                year
                month
                day
            }
            season
            seasonYear
            seasonInt
            episodes
            duration
            chapters
            volumes
            countryOfOrigin
            genres
            isAdult
            recommendations {
                nodes {
                    media{
                        title{
                            english
                        }
                    }
                }
            }

        }
        }'''

    variables = {}

    url = 'https://graphql.anilist.co'
    response = requests.post(url, json={'query': query, 'variables': variables})

    return render_template('lab03.html', quote_author=quote_author, quote_text=quote_text)