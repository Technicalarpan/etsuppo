import requests
import json
from flask import Flask, render_template

app=Flask(__name__)

@app.route('/')
def index():
	return '<h1>403 Access Forbidden</h1>You aren\'t supposed to be here'

@app.route('/<string:email>/<string:name>/<string:p>')
def showdat(email,name,p):
	url='https://support.earningtrick.in/api/conversations?apikey=PrkJJOmKaFSLcTb8xifW6gUK9jkFzyKW&owneridentifier='+email
	
	j=json.loads(requests.get(url).text)['response']['conversations']
	
	return render_template('index.html',name=name,email=email,tickets=j,p=p)
	
	
@app.route('/ticket/<string:id>')
def viewT(id):
	
	url='https://support.earningtrick.in/api/conversations/'+id+'?apikey=PrkJJOmKaFSLcTb8xifW6gUK9jkFzyKW'
	
	j=json.loads(requests.get(url).text)['response']
	
	
	return render_template('ticket.html',data=j)
	
	
if __name__ == '__main__':
	app.run()