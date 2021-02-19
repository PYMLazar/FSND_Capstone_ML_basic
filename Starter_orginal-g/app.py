import os
import requests
from flask import Flask, request, abort, jsonify, render_template, session, flash, make_response, Response, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS, cross_origin
from models import setup_db, Actor
import simplejson as json
from auth.auth import requires_auth, AuthError

#----------------------------------------------------------------------------#
# Initialize App 
#----------------------------------------------------------------------------#
def create_app(test_config=None):
	# create and configure the app
  	app = Flask(__name__)
  	
  	# app.secret_key = SECRET_KEY
  	# app.config['SECRET_KEY'] = SECRET_KEY
  	setup_db(app)
  	CORS(app)

  	return app

app = create_app()



@app.after_request
def after_request(response):
	response.headers.add('Access-Control-Allow-Headers', 'Content-Type,Authorization,true')
	response.headers.add('Access-Control-Allow-Methods', 'GET,PATCH,POST,DELETE,OPTIONS')
	return response


#  Actors
#  ----------------------------------------------------------------
# route handler to get list of actors
@app.route('/actors', methods = ['GET'])
@cross_origin()
@requires_auth('get:actors')
#def get_actors(payload):
# print(0)
def get_actors():
	actors = Actor.query.all()
	print(1.1)
	actors_data = []
	print(2)
	for actor in actors:
		print(3)
		actors_data.append({
			"id": actor.id,
			"name": actor.name,
			"age": actor.age,
			"gender": actor.gender,
			"image_link": actor.image_link
			})

	return jsonify(actors_data)
	
if __name__ == '__main__':
    app.run()(debug=True)
    #app.run(host='0.0.0.0', port=8080, debug=True)