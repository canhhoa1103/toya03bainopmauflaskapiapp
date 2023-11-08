"""
00 fork this replit to your replit 

01a do your code
01b your final goal is to hit Run and have all tests PASS IN GREEN

02a git commit push to github repo - view guide https://drive.google.com/file/d/1PZZ2xIlamM0pPtLlbpDodseCKcIVhTzW/view?usp=sharing
02b get url to your git repo in 02a above - we call it :gitrepourl

03 paste :gitrepourl into this google form and submit it
   https://forms.gle/cuxhb8cbYaJLHRYz5
   ma_debai = toya03bainopmauflaskapiapp
"""

from flask import Flask, jsonify
import os
import requests

#
# from src.helper import github_request


app = Flask(__name__)


@app.route('/')
def index():
  return {}


@app.route('/release')
def release():
  url = 'https://api.github.com/repos/pyenv/pyenv/releases'
  GITHUB_API_KEY = os.environ.get('GITHUB_API_KEY')
  header = {
  "Authorization": f"Bearer {GITHUB_API_KEY}"
  }
  res = requests.get(url, header)
  d = res.json()
  kq =[]
  for i in range(len(d)):  
    created_at = d[i]['created_at']
    tag_name = d[i]['tag_name']
    body = d[i]['body']
    kq.append({'created_at': created_at, 'tag_name': tag_name, 'body': body})
  return jsonify(kq)
@app.route('/most_3_recent/release')
def most_3_recent__release():
  url = 'https://api.github.com/repos/pyenv/pyenv/releases'
  GITHUB_API_KEY = os.environ.get('GITHUB_API_KEY')
  header = {
  "Authorization": f"Bearer {GITHUB_API_KEY}"
  }
  res = requests.get(url, header)
  d = res.json()
  kq2 = list()
  for new in (sorted((date['created_at'] for date in d),reverse=True)[:3]):
    for vitri in range(len(d)):
      if d[vitri]['created_at'] == new:
        created_at = new
        tag_name = d[vitri]['tag_name']
        body = d[vitri]['body']
        kq2.append({'created_at': created_at, 'tag_name': tag_name, 'body': body})
  return (kq2)

if __name__ == '__main__':
  app.run(debug=True, port=os.environ.get('PORT', 5000))
