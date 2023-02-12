--- ---

<h2>Commands</h2>

```
POST /posts/          ---> Create

GET /posts/1          ---> Read

POST /post/1          ---> Update
PUT /post/1           ---> Update
POST /post/1/edit     ---> Update

DELETE /post/1         ---> Delete
POST /post/1/delete    ---> Delete
```

----

<h2>More information</h2>

RESTful APIs are really easy to spot
* They have a defined structure which relates to CRUD funcitonality

You can easy predict new endpoints simply by knowing an application

* Eg: If YouTube’s API has something like GET /video/1
+ You can assume DELETE /video/1 also exists
* And that if YouTube has videos maybe GET /comment/1 exists for comments

They are widely used, however some of the endpoints may be more custom
+ EgDELETE /posts/1 vs POST /posts/1/delete

They usually return JSON
+ You can get a Burp plugin to automatically visualise JSON (JSONBeautifier)