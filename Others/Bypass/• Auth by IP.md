--- ---

<h2>Auth by IP</h2>

What is FireProx
	FireProx leverages the AWS API Gateway to create pass-through proxies that rotate the source IP address with every request! Use FireProx to create a proxy URL that points to a destination server and then make web requests to the proxy URL which returns the destination server response

---

<h2>Commands</h2>

- First setup the API key for AWS
- Use the tool

```
usage: fire.py [-h] [--profile_name PROFILE_NAME] [--access_key ACCESS_KEY] [--secret_access_key SECRET_ACCESS_KEY] [--session_token SESSION_TOKEN] [--region REGION] [--command COMMAND] [--api_id API_ID] [--url URL]

FireProx API Gateway Manager

optional arguments:
  -h, --help            show this help message and exit
  --profile_name PROFILE_NAME
                        AWS Profile Name to store/retrieve credentials
  --access_key ACCESS_KEY
                        AWS Access Key
  --secret_access_key SECRET_ACCESS_KEY
                        AWS Secret Access Key
  --session_token SESSION_TOKEN
                        AWS Session Token
  --region REGION       AWS Region
  --command COMMAND     Commands: list, create, delete, update
  --api_id API_ID       API ID
  --url URL             URL end-point
```

---

<h2>More Information</h2>

More information ---> https://github.com/ustayready/fireprox

<iframe src="https://github.com/ustayready/fireprox" width="100%" height="1300"></iframe>