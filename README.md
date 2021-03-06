# rest_api
Rest API Project


# CRUD REST API description

Root URL

`http://localhost/recipes/api/v0.1/`

|HTTP Method		|URI									              |Action		            |
|-------------------|-----------------------------------------------------|-------------------------|
|GET				|http://localhost/recipes/api/v0.1/recipes            |Retrieve list of recipes |
|GET				|http://localhost/recipes/api/v0.1/recipes/[recipe_id]|Retrieve a recipe        |
|POST               |http://localhost/recipes/api/v0.1/recipes            |Create a new recipe      |
|PUT                |http://localhost/recipes/api/v0.1/recipes/[recipe_id]|Update an existing recipe|
|DELETE				|http://localhost/recipes/api/v0.1/recipes/[recipe_id]|Delete a recipe          |

### Database Model

#### **Recipe**

- id: unique UUID. UUID type
- title: short description. String type.
- ingredients: list of ingredients. String type.
- description: long recipe descripion. Text type.
- difficulty: low, medium, high
- created_at: date creation
- updated_at: update date. 
