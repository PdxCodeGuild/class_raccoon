#lab03.py

from flask import Flask, render_template
import requests
import json

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

variables = {
    'id': 15125
}

url = 'https://graphql.anilist.co'
response = requests.post(url, json={'query': query, 'variables': variables})

print(response.text)