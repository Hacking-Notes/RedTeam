--- ---

<h2>Vertical Privilege Escalation</h2>

- Non-administrative user gaining access to an admin page where they can delete accounts
- Attacker might be able to access administrative functions via the URL
https://insecure-website.com/admin
- Admin URL might be more obscure but still leaked in JavaScript that constructs the user interface:
```
<script>
var isAdmin = false;
if (isAdmin) {
...
var adminPanelTag = document.createElement('a');
adminPanelTag.setAttribute('https://insecure-
website.com/administrator-panel-yb556');
adminPanelTag.innerText = 'Admin panel';
...
}
</script>
```

Parameter-based Access Control Methods- Storing access information in a user-controlled location (hidden field, cookie, query string, etc.)
https://insecure-website.com/login/home.jsp?admin=true
https://insecure-website.com/login/home.jsp?role=1

- Platform Misconfiguration
	- Restricting access at the platform layer by specific URLs and HTP methods:
```
DENY: POST, /admin/deleteUser,
managers
```

	- Can override by editing the request header
```
POST / HTTP/1.1
X-Original-URL:
/admin/deleteUser
```
