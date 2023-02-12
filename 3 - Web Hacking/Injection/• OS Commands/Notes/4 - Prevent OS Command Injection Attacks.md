--- ---

<h2>Prevent OS Command Injection Attacks</h2>

- Never call out OS commands from application-layer code
- If unavoidable, do the following:
	- Validate against a whitelist of permitted values
	- Validate that the input is a number
	- Validate that th`