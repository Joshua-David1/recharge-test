from flask import Flask,redirect,jsonify
from process import process_data

app=Flask(__name__)


username="anonymous"
password="youknowwho"


@app.route("/")
def home():
	return "<h1>Welcome! <p>Cick here to get redirected<a href='/vulnerable-endpoint'>yes</a></p></h1>"

@app.route("/vulnerable-endpoint",defaults={'uname':None})
@app.route("/vulnerable-endpoint/<uname>")
def haha(uname):
	global password
	global username
	username,password=process_data(uname,password)
	if username == "rec" and password == "helloworld":
		return jsonify({"secret":""})
	return jsonify({"Try-harder":"This ain't the flag (Check whether the endpoint is correct)","username":username,"password":password})



if __name__=="__main__":
	app.run(debug=True,host="0.0.0.0",port=80)
