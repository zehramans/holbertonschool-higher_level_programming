#!/usr/bin/python3
import requests
import csv


def fetch_and_print_posts():
    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    print(f"Status Code: {resp.status_code}")
    if resp.status_code == 200:
        js = resp.json()
        for i in js:
            print(i['title'])


def fetch_and_save_posts():
    resp = requests.get("https://jsonplaceholder.typicode.com/posts")
    if resp.status_code == 200:
        a = []
        for i in resp.json():
            dic = {}
            dic['id'] = i['id']
            dic['title'] = i['title']
            dic['body'] = i['body']
            a.append(dic)
        with open('posts.csv', "w") as final_post:
            writer = csv.DictWriter(
                final_post, fieldnames=[
                    'id', 'title', 'body'])
            writer.writeheader()
            writer.writerows(a)
