import requests
import json
from flask import Flask, render_template, request, redirect, escape

app=Flask(__name__)

@app.route('/')
def index():
	return '<h1>403 Access Forbidden</h1>You aren\'t supposed to be here'

@app.route('/<string:email>/<string:name>/<string:p>')
def showdat(email,name,p):
	url='https://support.earningtrick.in/api/conversations?apikey=PrkJJOmKaFSLcTb8xifW6gUK9jkFzyKW&owneridentifier='+email
	
	try:
		j=json.loads(requests.get(url).text)['response']['conversations']
		j=j[::-1]
	except:
		return'<h1>No tickets found</h1>'
	
	
	return render_template('index.html',name=name,email=email,tickets=j,p=p)
	
	
@app.route('/ticket/<string:id>')
def viewT(id):
	
	url='https://support.earningtrick.in/api/conversations/'+id+'?apikey=PrkJJOmKaFSLcTb8xifW6gUK9jkFzyKW'
	
	try:
		j=json.loads(requests.get(url).text)['response']
	except:
		return '<h1>No such ticket found</h1>'
	durl='https://support.earningtrick.in/api/conversations/'+id+'/messages?apikey=PrkJJOmKaFSLcTb8xifW6gUK9jkFzyKW'
	
	k=json.loads(requests.get(durl).text)['response']['groups']
	k=k[:-1]
	k=k[::-1]
	return render_template('ticket.html',data=j, details=k)
	
@app.route('/reply/<string:id>/')
def postit(id):
	msg=escape(request.args.get('message'))
	
	data={'message':msg,'apikey':'PrkJJOmKaFSLcTb8xifW6gUK9jkFzyKW'}
	
	done=requests.post('https://support.earningtrick.in/api/conversations/'+id+'/messages', data=data)
	
	return redirect('/ticket/'+id)


if __name__ == '__main__':
	app.run()
