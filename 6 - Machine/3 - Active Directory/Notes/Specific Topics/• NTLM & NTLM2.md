--- ---

<h2>General</h2>

NTLM (short for "NT Lan Manager") is a proprietary Microsoft authentication protocol that was originally developed for use on Windows NT systems. It is used to authenticate users and computers on a network and to provide secure communication between them.

NTLMv2 (short for "NT Lan Manager version 2") is an updated version of the NTLM protocol that was introduced with Windows 2000. It includes several improvements over the original NTLM protocol, including better security and support for longer passwords and multilingual characters.

One of the main differences between NTLM and NTLMv2 is that NTLMv2 is more secure than NTLM. NTLM uses a simple challenge-response mechanism to authenticate users, which can be vulnerable to certain types of attacks. NTLMv2, on the other hand, uses a more secure mechanism that is resistant to these attacks.

Another difference is that NTLMv2 supports longer passwords and multilingual characters, while NTLM does not. This makes NTLMv2 more flexible and easier to use in international environments.

Overall, NTLMv2 is the preferred authentication protocol for Windows networks, as it provides better security and flexibility than the original NTLM protocol.

![[Pasted image 20230103210003.png]]

---

<h2>NTLM</h2>

NTLM (NT Lan Manager) is an authentication protocol that is primarily used to verify the identity of a user or computer trying to access a network resource, such as a shared folder on a file server or a website.

- How does it work (More Detailed)
	When the user's computer sends the request to the server, it includes a "challenge" that the server sends back _(the server know the hash of the user, this is why it can compute the result, and our computer also use the hash to calculate the value of the challenge, this is why pass the hash attack are possible, since you dont need to know the password but simply the hash to confirm the challenge)_. This challenge is a random string of characters that the user's computer must then use to "prove" that it knows the correct password.
	
	To do this, the user's computer combines the challenge with the user's password and applies a special mathematical function to the resulting string of characters. The result of this function is called the "response".
	
	The user's computer then sends the response back to the server. The server applies the same mathematical function to the challenge and the password that it has on file for the user. If the result of this function is the same as the response that the user's computer sent, then the server knows that the user's computer knows the correct password, and the user is allowed to access the resource.
	
	This process helps to ensure that the password is not transmitted across the network in plain text, which would make it vulnerable to being intercepted and used by unauthorized users. Instead, only a "proof" of knowledge of the password is transmitted, which makes it much more secure.

---

<h2>NTLM2</h2>

NTLMv2 (NT Lan Manager version 2) is an updated version of the NTLM (NT Lan Manager) authentication protocol that was introduced with Windows 2000. It is used to authenticate users and computers on a network and to provide secure communication between them.

NTLMv2 is a challenge-response protocol, which means that it uses a series of messages exchanged between the user's computer and the server to verify the user's identity. Here is an overview of how NTLMv2 authentication works:


How does it work (Less Detailed)
1.  The user's computer sends a request to access a network resource, along with the user's credentials (such as the username and password).
    
2.  The server sends back a challenge, which is a random string of characters that the user's computer must use to "prove" that it knows the correct password.
    
3.  The user's computer combines the challenge with the user's password and applies a special mathematical function to the resulting string of characters. The result of this function is called the "response".
    
4.  The user's computer sends the response back to the server.
    
5.  The server applies the same mathematical function to the challenge and the hashed version of the user's password that it has on file. If the result of this function is the same as the response that the user's computer sent, then the server knows that the user's computer knows the correct password, and the user is allowed to access the resource.