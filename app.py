import io
import os

import requests
from flask import Flask, render_template, request, send_file

app = Flask(__name__)

TOKEN = os.getenv("TOKEN")

def get_files(public_key: str) -> list:
    url = f"https://cloud-api.yandex.net/v1/disk/public/resources?public_key={public_key}"
    headers = {'Authorization': f'OAuth {TOKEN}',
               'Content-Type': 'application/json'}
    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        return res.json().get('_embedded', {}).get('items', [])

    return []


def download_file(public_key: str, file_path: str):
    url = f"https://cloud-api.yandex.net/v1/disk/public/resources/download?public_key={public_key}&path={file_path}"
    headers = {'Authorization': f'OAuth {TOKEN}',
               'Content-Type': 'application/json'}
    res = requests.get(url=url, headers=headers)
    if res.status_code == 200:
        download_link = res.json().get('href')
        file_res = requests.get(download_link)
        return file_res.content

    return None


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/files', methods=['POST'])
def files():
    public_key = request.form.get('public_key')
    file_list = get_files(public_key)
    return render_template('files.html', files=file_list, public_key=public_key)


@app.route('/download/<path:file_name>', methods=['GET'])
def download(file_name: str):
    file_path = request.args.get('file_path')
    public_key = request.args.get('public_key')

    if not file_path or not public_key:
        return "Файл не найден или публичный ключ не передан.", 404

    file_content = download_file(public_key, file_path)
    if file_content:
        return send_file(
            io.BytesIO(file_content),
            as_attachment=True,
            download_name=file_name
        )

    return 'Ошибка при загрузке'


if __name__ == '__main__':
    app.run(debug=True)