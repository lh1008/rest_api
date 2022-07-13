# Recipes

This file contains the `cURL` format to create (POST), list (GET), update (UPDATE), and delete (DELETE) calls/requests to the API.

## CRUD (Create, Read, Update, Delete) Requests 

curl -X POST http://127.0.0.1:5000/api/v0.1/recipes -d '@data.json' -H 'Content-Type: application/json'