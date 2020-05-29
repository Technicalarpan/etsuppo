import requests, json
from flask import Flask, render_template
from flask_cors import CORS
from bs4 import BeautifulSoup as bs

app=Flask(__name__)
cors=CORS(app)

@app.route('/')
def index():
	lst=""

	j=json.loads(requests.get('https://support.earningtrick.in/api/knowledgebase/entries?apikey=PrkJJOmKaFSLcTb8xifW6gUK9jkFzyKW').text)['response']['entries']


	for aj in j:
		lst+=aj["title"]+'\n'
	
	return lst



@app.route('/s/')
def all():
	
	titles=[]
	contents=[]
	
	j=json.loads(requests.get('https://support.earningtrick.in/api/knowledgebase/entries?apikey=PrkJJOmKaFSLcTb8xifW6gUK9jkFzyKW').text)['response']['entries']
	
	for aj in j:
		titles.append(aj['title'])
		contents.append(aj['metadescription'])
		
	return render_template('all.html',tls=titles,cts=contents,q='All Articles',r=len(titles))



@app.route('/s/<string:q>')
def wut(q):
	j=json.loads(requests.get('https://support.earningtrick.in/api/knowledgebase/search?apikey=PrkJJOmKaFSLcTb8xifW6gUK9jkFzyKW&query='+q).text)['response']['entries']
	
	
	if len(j)==1:
		title=j[0]['title']
		content = j[0]['content_text']
	
		return render_template('article.html',title=title,content=content)
		
	elif len(j)==0:
		return render_template('article.html',title='No Results Found', content='<h4>Try Searching for another term</h4>')
	
	elif len(j)>1:
		tls=[]
		cts=[]
		for aj in j:
			ct=aj['content_text']
			ct=bs(ct,'lxml').text
			if len(ct)>20:
				ct=ct[0:19]
			
			title=aj['title']
			
			tls.append(title)
			cts.append(ct)
		
		
		return render_template('res.html',tls=tls,cts=cts,q=q,r=len(tls))

if __name__ == '__main__':
	app.run()
