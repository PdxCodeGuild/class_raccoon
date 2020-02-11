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
            coverImage {
                large
            }
            streamingEpisodes {
                title
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

resultlist = []
for i in response:
    if i['streamingEpisodes']:
        sitelist = []
        site_results = []
        if i['coverImage']['large']:
            cover_img = i['coverImage']['large']
        else:
            cover_img = noimage
        for j in i['streamingEpisodes']:
            if j['site'] not in sitelist:
                sitelist.append(j['site'])
                site_results.append((j['site'],j['url']))

        if i['title']['english']:
            title = i['title']['english']
        if i['title']['romaji']:
            if title:
                title = title + " | " + i['title']['romaji']
            else:
                title = i['title']['romaji']
        if i['title']['native']:
            if title:
                title = title + " | " + i['title']['native']
            else:
                title = i['title']['native']
        resultlist.append({'Title':title,'Image':cover_img,'Sites':site_results})
print(resultlist)