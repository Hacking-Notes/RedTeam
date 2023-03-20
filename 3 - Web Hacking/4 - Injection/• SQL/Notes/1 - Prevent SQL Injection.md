--- ---

<h4>Login Input</h4>
use mysql.escape in the query

![[Pasted image 20221204214739.png]]

More information ---> https://www.youtube.com/watch?v=wSOlJ_duQU4


<h4>Number Input</h4>
`Intval()` function will take a string and try to convert it into an integer. If no valid integer is found on the string, it will return 0, which is also an integer. To clarify this, let's look at some values and how they would be converted:

```php
intval("123") = 123
intval("tryhackme") = 0
intval("123tryhackme") = 123
```

```php
$query="select * from users where id=".intval($_GET['id']);
```



<h4>SQL Statment (Step by Step)</h4>
Instead of providing a single SQL query string, we will send any dynamic parameters separately from the query itself, allowing the database to stick the pieces together securely without depending on PHP or the programmer. Let's see how this looks in the code.

First, we will modify our initial query by replacing any parameter with a placeholder indicated with a question mark (`?`). This will tell the database we want to run a query that takes two parameters as inputs. The query will then be passed to the `mysqli_prepare()` function instead of our usual `mysqli_query()`. `mysqli_prepare()` will not run the query yet but will indicate to the database to prepare the query with the given syntax. This function will return a prepared statement.

```php
$query="select * from toys where name like ? or description like ?";
$stmt = mysqli_prepare($db, $query);
```

To execute our query, MySQL needs to know the value to put on each placeholder we defined before. We can use the `mysqli_stmt_bind_param()` function to attach variables to each placeholder. This function requires you to send the following function parameters:

The first parameter should be a reference to the prepared statement to which to bind the variables. 

The second parameter is a string composed of one letter per placeholder to be bound, where letters indicate each variable's data type. Since we want to pass two strings, we put `"ss"` in the second parameter, where each "s" represents a string-typed variable. You can also use the letters "i" for integers or "d" for floats. You can check the full list in [PHP's documentation](https://www.php.net/manual/en/mysqli-stmt.bind-param.php).

After that, you will need to pass the variables themselves. You must add as many variables as placeholders defined with `?` in your query, which in our case, are two. Notice that, in our example, both parameters have the same content, but in other cases, it may not be so.

The resulting code for this would be as follows:

```php
$q = "%".$_GET['q']."%";
mysqli_stmt_bind_param($stmt, 'ss', $q, $q);
```

Once we have created a statement and bound the required parameters, we will execute the prepared statement using `mysqli_stmt_execute()`, which receives the statement `$stmt` as its only parameter.

```php
mysqli_stmt_execute($stmt);
```

Finally, when a statement has been executed, we can retrieve the corresponding result set using the `mysqli_stmt_get_result()`, passing the statement as the only parameter. We'll assign the result set to the `$toys_rs` variable as in the original code.

```php
$toys_rs=mysqli_stmt_get_result($stmt);
```

Our final resulting code should look like this:

```php
$q = "%".$_GET['q']."%";
$query="select * from toys where name like ? or description like ?";
$stmt = mysqli_prepare($db, $query);
mysqli_stmt_bind_param($stmt, 'ss', $q, $q);
mysqli_stmt_execute($stmt);
$toys_rs=mysqli_stmt_get_result($stmt);
```