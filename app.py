#!/usr/bin/env python3
from datetime import datetime
from flask import Flask, jsonify, request, session, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, select
from sqlalchemy import Column, insert, Table, String, Text, DateTime
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.dialects.postgresql import UUID, JSON
import uuid
import json


app = Flask(__name__)
engine =  create_engine('postgresql://postgres:newPassword@localhost:5434/sqlalchemy_db')

Base = declarative_base()

class Recipe(Base):
	__tablename__ = 'recipes'

	recipe_id =  Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	info = Column(JSON, nullable=False)
	created_at = Column(DateTime(), nullable=False, default=datetime.now().isoformat())
	updated_at = Column(DateTime(), nullable=False, default=datetime.now().isoformat())

	def __init__(self, info):
		self.info = info
		
	def __repr__(self):
		return f'User(recipe_id={self.recipe_id!r}, info={self.info!r})'

@app.route('/')
def index():
	return jsonify({"message":"Delicious Recipes"})

@app.route('/api/v0.1/recipes', methods=['POST'])
def create_recipe():
	# Route that will create a recipes given a set of data
	with Session(engine) as session:
		
		data = request.json # body en la request lo transforma a diccionario 
		info = json.dumps(data)
		
		sql = Recipe(info=info)
		session.add(sql)
		session.commit()

		return jsonify({"success": True, "response":"Recipe created"})


@app.route('/api/v0.1/recipes', methods=['GET'])
def get_recipes():
	with Session(engine) as session:
		query = select([Recipe.recipe_id, Recipe.info])
		res = session.execute(query)
		output = list()

		for row in res:
			output.append(dict(row))
		return jsonify(output)

if __name__ == '__main__':
	#app.run(debug=True)
	Base.metadata.drop_all(engine)
	Base.metadata.create_all(engine)


# cURL requests

# curl -X POST http://127.0.0.1:5000/api/v0.1/recipes -d '@data.json' -H 'Content-Type: application/json'