---- ---

Unicode characters can look the same to the naked eye but actually, have a different web address. Some letters in the Roman alphabet, used by the majority of modern languages, are the same shape as letters in Greek, Cyrillic, and other alphabets, so it’s easy for an attacker to launch a domain name that replaces some ASCII characters with Unicode characters. 

For example, you could swap a normal T for a Greek Tau: τ, the user would see the almost identical T symbol but the punycode behind this, read by the computer, is actually xn--5xa.

- Limitation with modern browser

---> https://www.punycoder.com/ (Encode unicode to domain)