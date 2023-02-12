--- ---

<h2>Manipulation</h2>

###### **SELECT**
```
SELECT * (or SOMETHING) FROM table_name;
```

- SELECT            = Indicate the action (Witch is select) --> *`clause`*
- *                       = Everything 
- SOMETHING  = Speficy the name of the columns we want to take the information (Columns Name)
- FROM             = Indicate what table to check --> *`clause`*
- table_name    = EX: Table (Composed of coluns and rows) (Data in form of TEXT, DATE, REAL, ...)
-  ;                      = end of the statment

**AS**
```
SELECT name AS 'Titles'  
FROM movies;
```

- SELECT            = Indicate the action (Witch is select) --> *`clause`*
- name = columns normal name
- AS = Change the name of the Column
- 'Titles' = The name column renamed 
- - FROM             = Indicate what table to check --> *`clause`*
- table_name    = EX: Table (Composed of coluns and rows) (Data in form of TEXT, DATE, REAL, ...)
-  ;                      = end of the statment

**DISTINCT**
```
SELECT DISTINCT tools  
FROM inventory;
```

- SELECT            = Indicate the action (Witch is select) --> *`clause`*
- DISTINCT        = Return unique values in the output
- tools               = Column name
- FROM             = Indicate what table to check --> *`clause`*
- table_name    = EX: Table (Composed of coluns and rows) (Data in form of TEXT, DATE, REAL, ...)
-  ;                      = end of the statment

**Opperation**
```
SELECT *  
FROM movies  
WHERE imdb_rating > 8;
```
- `=` `!=` `>` `<` `>=` `<=`

- SELECT            = Indicate the action (Witch is select) --> *`clause`*
- *                       = Everything 
- FROM             = Indicate what table to check --> *`clause`*
- movies            = Table name
- WHERE            = Looking for value (following statement)
- imdb_rating > 8 = Looking for imdb_rating that is unter 8
-  ;                      = end of the statment

**LIKE**
```
SELECT *   
FROM movies  
WHERE name LIKE 'Se_en';
```

- SELECT            = Indicate the action (Witch is select) --> *`clause`*
- *                       = Everything 
- FROM             = Indicate what table to check --> *`clause`*
- movies            = Table name
- WHERE            = Looking for value (following statement)
- name               = columns
- LIKE 'Se_en'      = `LIKE 'Se_en'` is a condition evaluating the `name` column for a specific pattern.
- ;                        = end of the statment

**LIKE**
```
SELECT *   
FROM movies  
WHERE name LIKE '%man%';
```

- SELECT            = Indicate the action (Witch is select) --> *`clause`*
- *                       = Everything 
- FROM             = Indicate what table to check --> *`clause`*
- movies            = Table name
- WHERE            = Looking for value (following statement)
- name               = Column name
- LIKE                  = `LIKE` is a condition evaluating the `name` column for a specific pattern.
- '%man%'          = Mean anything that has something before 'man' and something after
- ;                        = end of the statment                

**IS / IS NOT**
```
SELECT name  
FROM movies  
WHERE imdb_rating IS (NOT) NULL;
```

- SELECT            = Indicate the action (Witch is select) --> *`clause`*
- *                       = Everything 
- FROM             = Indicate what table to check --> *`clause`*
- movies            = Table name
- WHERE            = Looking for value (following statement)
- imbd_rating     = columns name
- IS (NOT) NULL  = Looking for field that are NULL or NOT
- ;                        = end of the statment                

**BETWEEN**
```
SELECT *
FROM movies
WHERE name BETWEEN 'D 'AND 'G';
```

- SELECT            = Indicate the action (Witch is select) --> *`clause`*
- *                       = Everything 
- FROM             = Indicate what table to check --> *`clause`*
- movies            = Table name
- WHERE            = Looking for value (following statement)
- name               = Column name
- BETWEEN         = Looking for value between 2 elements
- 'D' AND 'G'       = Values we are looking for
- IS (NOT) NULL  = Looking for field that are NULL or NOT
- ;                        = end of the statment                

**AND**
```
SELECT *   
FROM movies  
WHERE year BETWEEN 1990 AND 1999  
   AND genre = 'romance';
```

- SELECT                      = Indicate the action (Witch is select) --> *`clause`*
- *                                = Everything 
- FROM                        = Indicate what table to check --> *`clause`*
- movies                      = Table name
- WHERE                      = Looking for value (following statement)
- year                            = Column name
- BETWEEN                    = Looking for value between 2 elements
- '1990' AND '1999'       = Values we are looking for
- AND                             = Add a condition
- genre = 'romance';       = Looking for column genre = romance
- ;                                    = end of the statment                

**Or**
```
SELECT *FROM movies
WHERE year > 2014   
OR genre = 'action';
```

- SELECT                      = Indicate the action (Witch is select) --> *`clause`*
- *                                = Everything 
- FROM                        = Indicate what table to check --> *`clause`*
- movies                      = Table name
- WHERE                      = Looking for value (following statement)
- year                            = Column name
- > 2014                       = Biger the 2014
- OR                              = Add a OR condition
- genre = 'action';        = Looking for column genre = romance
- ;                                    = end of the statment    

**Order By**
```
SELECT *  
FROM movies  
ORDER BY name ASD,DSC;
```

- SELECT                      = Indicate the action (Witch is select) --> *`clause`*
- *                                = Everything 
- FROM                        = Indicate what table to check --> *`clause`*
- movies                      = Table name
- ORDER BY                 = Order by
- name                         = columns name
- ASD, DSC                  = Assendent, Dessendent
- ;                                 = end of the statment    

**Limit**
```
SELECT *  
FROM movies  
LIMIT 10;
```

- SELECT                      = Indicate the action (Witch is select) --> *`clause`*
- *                                = Everything 
- FROM                        = Indicate what table to check --> *`clause`*
- movies                      = Table name
- LIMIT 10                    = Limit the number of responses to 10 (In this case)
-  ;                              = end of the statment    

**Case**
```
SELECT name,  
CASE  
  WHEN imdb_rating > 8 THEN 'Fantastic'  
  WHEN imdb_rating > 6 THEN 'Poorly Received'  
  ELSE 'Avoid at All Costs'  
END  
FROM movies;
```

- SELECT                      = Indicate the action (Witch is select) --> *`clause`*
- name                         = Column name
- CASE                          = Only show element that correspond to specific CASE
	WHEN                       = Condition
	ELSE                          = Everything that does not fit in those condition
- END                            = End the case statement
- FROM                        = Indicate what table to check --> *`clause`*
- movies                      = Table name
-  ;                              = end of the statment    

###### **Join**
```
SELECT *  
FROM orders  
JOIN customers  
  ON orders.customer_id = customers.customer_id;
```

- SELECT                      = Indicate the action (Witch is select) --> *`clause`*
- *                                = Everything
- orders                        = Table
- JOIN                           = Join to the other table
- customer                    = Second table (the one we merge in)
- ON                              = Explain what field are the same (to add the right info the right customer)


###### **CREATE**
```
CREATE TABLE table_name (  
   id INTEGER,  
   name TEXT,  
   age INTEGER  
);
```

- CREATE          = Indicate the action --> *`clause
- TABLE             = Specify the table
- table_name    = EX: Table (Composed of coluns and rows) (Data in form of TEXT, DATE, REAL, ...)
- id, name, age = Indicate the name of the columns
- INTEGER, TEXT, ... = Indicate the type of value that will be incerted
-  ;                       = end of the statment


###### **INSERT**
```
INSERT INTO celebs (id, name, age)  
VALUES (1, 'Justin Bieber', 22);
```

- INSERT INTO                = Indicate the action (Add info to a table) --> *`clause
- (id, name, age)             = Identifying the columns that data will be inserted into.
- VALUES                        = Specify the value that will be inclouded in the table --> *`clause
- (1, 'Justin Bieber', 22)    = Value included
- ;                                    = end of the statment


###### **ALTER**
```
ALTER TABLE celebs  
ADD COLUMN twitter_handle TEXT;
```

- ALTER TABLE       = Indicate the action (change the structure of the database) --> *`clause
- celebs                 = Table selected
- ADD COLUMN    = Specify to add a columns --> *`clause
- twitter_handle     = Name of the column added
- TEXT                    = Type of element in this column
- ;                          = End of the statment


###### **Update**
```
UPDATE celebs  
SET twitter_handle = '@taylorswift13'  
WHERE id = 4;
```

- UPDATE = Indicate the action --> *`clause
- celebs    = table selected
- SET         = Action  --> *`clause
- twitter_handle = Column name
- = '@...'    = Input to be added
- WHERE  id equal 4 = Searching for id equal 4
- ;                =  End of the statment


###### **Delete**
```
DELETE FROM celebs  
WHERE twitter_handle IS NULL;
```

- DELETE               = Indicate the action
- FROM                 = Indicate what table to check --> *`clause
- celebs                 =
- WHERE               = Searching for --> *`clause
- twitter_handle     = Column Name
- IS NULL               = Equal Nothing (Empty) --> *`clause
- ;                          = End of the statment


###### **Constraints**
Reject & accept specific data

```
CREATE TABLE celebs (  
   id INTEGER PRIMARY KEY,  
   name TEXT UNIQUE,  
   date_of_birth TEXT NOT NULL,  
   date_of_death TEXT DEFAULT 'Not Applicable'  
);
```

1. `PRIMARY KEY` columns can be used to uniquely identify the row. Attempts to insert a row with an identical value to a row already in the table will result in a _constraint violation_ which will not allow you to insert the new row.

2. `UNIQUE` columns have a different value for every row. This is similar to `PRIMARY KEY` except a table can have many different `UNIQUE` columns.

3. `NOT NULL` columns must have a value. Attempts to insert a row without a value for a `NOT NULL` column will result in a constraint violation and the new row will not be inserted.

4. `DEFAULT` columns take an additional argument that will be the assumed value for an inserted row if the new row does not specify a value for that column.

---

<h2>Function</h2>

###### **Count**
```
SELECT COUNT(*)  
FROM table_name;
```

- SELECT          = Indicate the action (Witch is select) --> *`clause`*
- COUNT()        = Count the number of row in the column (star) = ALL --> *`clause
- FROM            = Indicate what table to check --> *`clause`*
- table_name    = table name
- ;                     = End of the statement

###### **Sum**

```
SELECT SUM(downloads)  
FROM table_name;
```

- SELECT                       = Indicate the action (Witch is select) --> *`clause`*
- SUM(downloads)        = Check the summury of the download column --> *`clause
- FROM                         = Indicate what table to check --> *`clause`*
- table_name                 = table name
- ;                                  = End of the statement

###### **Max / Min**
```
SELECT MAX(downloads)  
FROM Table_name;
```

- SELECT                       = Indicate the action (Witch is select) --> *`clause`*
- MAX(downloads)        = Check the maximum download (Highest value) --> *`clause
- FROM                         = Indicate what table to check --> *`clause`*
- table_name                 = table name
- ;                                  = End of the statement

###### **Average**
```
SELECT AVG(downloads)  
FROM fake_apps;
```

- SELECT                       = Indicate the action (Witch is select) --> *`clause`*
- AVG(downloads)        = Check the average download --> *`clause
- FROM                         = Indicate what table to check --> *`clause`*
- table_name                 = table name
- ;                                  = End of the statement

###### **Round**
```
SELECT ROUND(price, 0)  
FROM fake_apps;
```

- SELECT                       = Indicate the action (Witch is select) --> *`clause`*
- ROUND(price, 0)        = round the price value with 0 precision value after the decimal
-  FROM                         = Indicate what table to check --> *`clause`*
- table_name                 = table name
- ;                                  = End of the statement

###### **Group By I**
```
SELECT year,  
   AVG(imdb_rating)  
FROM movies  
GROUP BY year  
ORDER BY year;
```

- SELECT                          = Indicate the action (Witch is select) --> *`clause`*
- year, AVG(imdb_rating) = columns
-  FROM                          = Indicate what table to check --> *`clause`*
- movies                          = Table
- GROUP BY year             = Group elements by years
- ;                                     = End of the statement

###### **Group By II**
```
SELECT category,  
   price,  
   AVG(downloads)  
FROM fake_apps  
GROUP BY category, price;
```

- SELECT                                    = Indicate the action (Witch is select) --> *`clause`*
- year, AVG(imdb_rating), ...       = columns
- FROM                                      = Indicate what table to check --> *`clause`*
- movies                                    = Table
- GROUP BY category, price       = Group elements by category and price
- ;                                               = End of the statement



