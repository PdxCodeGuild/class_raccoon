#lab03.py

from flask import Flask, render_template
import requests
import json

query = '''query ($title: String, $page: Int, $perPage: Int) {
    Page (page: $page, perPage: $perPage) {
        media (search: $title, type: ANIME) {
            title {
                romaji
                english
                native
            }
            streamingEpisodes {
                title
                thumbnail
                url
                site
            }
        }
    }
}'''

variables = {}

userinput = input("Give the title of an anime: ")

variables = {
    'title': userinput,
    'page': 1,
    'perPage': 10
    }

url = 'https://graphql.anilist.co'
response = requests.post(url, json={'query': query, 'variables': variables})
response = json.loads(response.text)['data']['Page']['media']
# [data][page][media]
for i in response:
    print(i)