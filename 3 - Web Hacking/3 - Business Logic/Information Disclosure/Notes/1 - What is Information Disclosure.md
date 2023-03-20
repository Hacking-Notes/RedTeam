--- ---

<h2>What is Information Disclosure</h2>

**Information** **disclosure**, also known as **information** leakage, is when a website unintentionally reveals sensitive **information** to its users. Depending on the context, websites may leak all kinds of **information** to a potential attacker, including: Data about other users, such as usernames or financial **information** Sensitive commercial or business data

![[Screenshot from 2022-12-02 13-22-14.png]]

Type of Data that can be leaked:
- Data about other users (usernames or financial data)
- Sensitive commercial or business data
- Technical details about the website or infrastructure

Example of information disclosure:
- Revealing names of hidden directories
- Providing access to source code files via temporary backups
- Explicitly mentioning database table or column names in error messages
- Exposing sensitive info such as credit card details
- Hard-coding API keys, IPs, creds, etc in source code

These are often less severe but can become severe depending on the data. Even "less severe" information
disclosure such as technical details can be used to further enumerate the web server or system and identify more
flaws for exploitation. In other words, this can be chained together for more compromise.