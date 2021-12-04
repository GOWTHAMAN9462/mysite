from scraper import app
from flask import render_template, request, jsonify
from bs4 import BeautifulSoup
import requests


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search')
def search():
    input = request.args.get("name")
    filter = request.args.get("filter")
    print("start")
    page = request.args.get("page")
    if filter == "AllField":
        url = f'https://www.science.org/action/doSearch?AllField={input}&pageSize=15&startPage={page}'
    else:
        url = f'https://www.science.org/action/doSearch?field1={filter}&text1={input}&pageSize=15&startPage={page}'
    content = requests.get(url).text
    soup = BeautifulSoup(content, 'lxml')
    card = soup.find_all('div', class_='card')

    list1 = []

    for i in card:
        title = i.find('h2', class_='article-title').text
        link = i.find('h2', class_='article-title').a['href']
        date_time = i.find('time').text
        author_data = i.find_all('span', class_='hlFld-ContribAuthor')
        author_list = []
        for j in author_data:
            author = j.text
            author_list.append(author)
        abstract = i.find('span', class_='hlFld-Abstract')
        if abstract != None:
            abstract = abstract.text
        else:
            abstract = ""

        data = {
            'title': title,
            'link': 'https://www.science.org'+link,
            'author': author_list,
            'abstract': abstract,
            'time': date_time
        }

        list1.append(data)
    print("stop")

    return jsonify({
        "result": True,
        "description": "Details gathered",
        "category": "success",
        "data": list1
    })

