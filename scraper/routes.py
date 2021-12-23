from scraper import app
from flask import render_template, request, jsonify
import requests, json
from os import environ


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search_affil' , methods=['GET'])
def search_affil():
    input = request.args.get("name")
    url = f'https://api.elsevier.com/content/search/affiliation?query=affil(${input})'
    headers = {
                "X-ELS-APIKey": environ.get('ELSERVIER_API_KEY'),
                "Accept": 'application/json'
            }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        resp = json.loads(resp.text)
        return jsonify({
            "result": True,
            "description": "Details gathered",
            "category": "success",
            "details": resp
        })
    else:
        resp = json.loads(resp.text)
        return jsonify({
            "result": False,
            "description": "Error",
            "category": "danger",
            "details": resp
        })


@app.route('/get_affil', methods=['GET'])
def get_affil():
    input = request.args.get("name")
    url = f'https://api.elsevier.com/content/affiliation/affiliation_id/{input}'
    headers = {
                "X-ELS-APIKey": environ.get('ELSERVIER_API_KEY'),
                "Accept": 'application/json'
                }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        resp = json.loads(resp.text)
        return jsonify({
            "result": True,
            "description": "Details gathered",
            "category": "success",
            "details": resp
        })
    else:
        resp = json.loads(resp.text)
        return jsonify({
            "result": False,
            "description": "Error",
            "category": "danger",
            "details": resp
        })


@app.route('/authorlist', methods=['GET'])
def authorlist():
    input = request.args.get("name")
    page = str(request.args.get("page"))
    id = str(request.args.get("id"))
    print(page)
    url = f'https://api.elsevier.com/content/search/author?query={input}+AND+AF-ID({id})&count={page}'
    print(url)
    headers = {
                "X-ELS-APIKey": environ.get('ELSERVIER_API_KEY'),
                "Accept": 'application/json'
                }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        resp = json.loads(resp.text)
        return jsonify({
            "result": True,
            "description": "Details gathered",
            "category": "success",
            "details": resp
        })
    else:
        return jsonify({
            "result": False,
            "description": "Error",
            "category": "danger"
        })

@app.route('/author', methods=['GET'])
def author():
    url = request.args.get("url")
    print(url)
    headers = {
                "X-ELS-APIKey": environ.get('ELSERVIER_API_KEY'),
                "Accept": 'application/json'
                }
    resp = requests.get(url, headers=headers)
    if resp.status_code == 200:
        resp = json.loads(resp.text)
        return jsonify({
            "result": True,
            "description": "Details gathered",
            "category": "success",
            "details": resp
        })
    else:
        return jsonify({
            "result": False,
            "description": "Error",
            "category": "danger"
        })

