--- ---

<h2>What is Collaborator Module?</h2>

Burp Collaborator is a network service that Burp Suite uses to help discover many kinds of vulnerabilities. For example:

-   Some injection-based vulnerabilities can be detected using payloads that trigger an interaction with an external system when successful injection occurs. For example, some [blind SQL injection](https://portswigger.net/web-security/sql-injection/blind) vulnerabilities cannot be made to cause any difference in the content or timing of the application's responses, but they can be detected using payloads that cause an external interaction when injected into a SQL query.
-   Some service-specific vulnerabilities can be detected by submitting payloads targeting those services to the target application, and analyzing the details of the resulting interactions with a collaborating instance of that service. For example, mail header injection can be detected in this way.
-   Some vulnerabilities arise when an application can be induced to retrieve content from an external system and process it in some way. For example, the application might retrieve the contents of a supplied URL and include it in its own response.

When Burp Collaborator is being used, Burp sends payloads to the application being audited that are designed to cause interactions with the Collaborator server when certain vulnerabilities or behaviors occur. Burp periodically polls the Collaborator server to determine whether any of its payloads have triggered interactions:

![Burp Collaborator](https://portswigger.net/burp/documentation/images/collaborator/collaborator-1.svg)

Burp Collaborator is used by [Burp Scanner](https://portswigger.net/burp/documentation/scanner) and the [manual Burp Collaborator client](https://portswigger.net/burp/documentation/desktop/tools/collaborator-client), and can also be used by [Burp extensions](https://portswigger.net/burp/documentation/desktop/extensions).

---

<h2>How to use it</h2>

- Click the Brup menu ---> Burp Collaborator Client
- Select the button "Copy to clipboard"
- Use this URL has the receiver to verify if the connection is done

---

<h2>More Information</h2>

**All Information** --->  https://portswigger.net/burp/documentation/collaborator

<iframe src="https://portswigger.net/burp/documentation/collaborator" width="100%" height="1300"></iframe>