import os

import requests
from flask import Flask, render_template

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")

def get_files(public_key: str) -> list:
    url = f"https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}"
    headers = {'Authorization': f'OAuth {TOKEN}'}
    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        return res.json().get('_embedded', {}).get('items', [])

    return []


def download(file_path: str):
    url = f"https://cloud-api.yandex.net/v1/disk/resources/download?path={file_path}"
    headers = {'Authorization': f'OAuth {TOKEN}'}
    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        download_link = res.json().get('href')
        file_res = requests.get(download_link)
        return file_res.content

    return None

@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)