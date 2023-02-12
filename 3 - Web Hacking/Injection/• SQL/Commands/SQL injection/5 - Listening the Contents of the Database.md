--- ---

<h2>Listening the Contents of the Database</h2>

```
SELECT * FROM information_schema.tables
```

Returns a table such as this:
![[Pasted image 20221210161850.png]]
	- Indicates the following:
		§ There are three tables (Products, Users, and Feedback)
Query information_schema.columns to list the columns in invidual tables
```
SELECT * FROM information_schema.columns WHERE table_name = 'Users'
```

- Returns the following:
![[Pasted image 20221210161825.png]]
- Shows the columns in the specified table and data type of each column

Information Schema in Oracle

1. List all tables
```
SELECT * FROM all_tables
```

2. List columns by querying all_tab_columns
```
SELECT * FROM all_tab_columns WHERE table_name = 'USERS'
```