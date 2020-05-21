import requests, json
from flask import Flask
from flask_cors import CORS

app=Flask(__name__)
cors=CORS(app)

@app.route('/')
def index():
	lst=""

	j=json.loads(requests.get('https://support.earningtrick.in/api/knowledgebase/entries?apikey=PrkJJOmKaFSLcTb8xifW6gUK9jkFzyKW').text)['response']['entries']


	for aj in j:
		if aj["deleted"]=='N':
			lst+=aj["title"]+'\n'
	
	return lst
	

if __name__=='__main__':
	app.run()
