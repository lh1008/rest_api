#!/usr/bin/env python3
from datetime import datetime
from flask import Flask, jsonify, request, session, render_template, redirect, url_for, flash
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine, select
from sqlalchemy import Column, insert, Table, String, Text, DateTime
from sqlalchemy.orm import declarative_base, Session
from sqlalchemy.dialects.postgresql import UUID
import uuid
import json


app = Flask(__name__)
engine =  create_engine('postgresql://postgres:newPassword@localhost:5434/sqlalchemy_db')

Base = declarative_base()

class Recipe(Base):
	__tablename__ = 'recipes'

	recipe_id =  Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4)
	title = Column(String(50), nullable=False)
	ingredients = Column(String(), nullable=False)
	description = Column(String(), nullable=False)
	difficulty = Column(String(), nullable=False)
	created_at = Column(DateTime(), nullable=False, default=datetime.now().isoformat())
	updated_at = Column(DateTime(), nullable=False, default=datetime.now().isoformat())

	def __init__(self, title, ingredients, description, difficulty):
		self.title = title
		self.ingredients = ingredients
		self.description = description
		self.difficulty = difficulty

	def __repr__(self):
		return f'User(recipe_id={self.recipe_id!r}, title={self.title!r}, ingredients={self.ingredients!r}, description={self.description!r}), difficulty={self.difficulty!r}))'

@app.route('/')
def index():
	return jsonify({"message":"Delicious Recipes"})

@app.route('/api/v0.1/recipes', methods=['POST'])
def create_recipe():
	# Route that will create a recipes given a set of data
	with Session(engine) as session:
		
		data = request.json # body en la request lo transforma a diccionario 
		title = json.dumps(data['title'])
		print(title)
		ingredients = json.dumps(data['ingredients'])
		print(ingredients)
		description = json.dumps(data['description'])
		print(description)
		difficulty = json.dumps(data['difficulty'])
		print(difficulty)

		sql = Recipe(title=title, ingredients=ingredients, description=description, difficulty=difficulty)
		session.add(sql)
		session.commit()

		return jsonify({"success": True, "response":"Recipe created"})


@app.route('/api/v0.1/recipes', methods=['GET'])
def get_recipes():
	with Session(engine) as session:
		query = select([Recipe.recipe_id, Recipe.title, Recipe.ingredients, Recipe.description, Recipe.difficulty, Recipe.created_at, Recipe.updated_at])
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