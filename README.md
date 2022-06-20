# rest_api
Rest API Project


# CRUD REST API description

Root URL

`http://localhost/recipes/api/v0.1/`

|HTTP Method		|URI									              |Action		           |
|-------------------|-----------------------------------------------------|------------------------|
|GET				|http://localhost/recipes/api/v0.1/recipes            |Retrieve lis of recipes |
|GET				|http://localhost/recipes/api/v0.1/recipes/[recipe_id]|Retrieve a recipe       |
|POST               |http://localhost/recipes/api/v0.1/recipes            |Create a new recipe     |
|PUT                |http://localhost/recipes/api/v0.1/recipes/[recipe_id]|Update an existin recipe|
|DELETE				|http://localhost/recipes/api/v0.1/recipes/[recipe_id]|Delete a recipe         |

Recipe fields:

- id: unique UUID. UUID type
- title: short description. String type.
- ingredients: list of ingredients. String type.
- description: long recipe descripion. Text type.
- dificulty: low, medium, high
- created_at: date creation
- update_at: update date. 