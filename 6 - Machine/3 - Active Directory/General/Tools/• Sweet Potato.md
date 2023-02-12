--- ---

<h2>General</h2>

A "hot potato" attack is a type of privilege escalation attack that involves using token impersonation to execute code with higher privileges. Here is a general outline of the steps involved in a hot potato attack:

1.  The attacker identifies a process running on the target system that has high privileges, such as a system service or a process running under the context of a user with administrative privileges.
    
2.  The attacker exploits a vulnerability in the process to execute code with the privileges of the process. This can be done through a variety of methods, such as sending specially crafted input to the process or exploiting a vulnerability in the process's code.
    
3.  The attacker uses token impersonation to assume the security context of the high-privilege process. This allows the attacker to execute code with the privileges of the process.
    
4.  The attacker uses the elevated privileges to gain access to sensitive resources or perform actions that would normally be restricted to them. This can include accessing sensitive files, modifying system settings, or installing malicious software.
    

Overall, a hot potato attack involves exploiting a vulnerability in a process with high privileges and using token impersonation to execute code with those privileges in order to gain unauthorized access to resources or perform actions that would normally be restricted.


- More About Token Impersonation
	Token impersonation can be useful in certain situations where a process needs to temporarily execute with the privileges of another process in order to perform a specific task. In such cases, the process may not need to authenticate as the other process in order to access resources or perform actions, because it is already executing with the appropriate privileges.
	
	For example, consider a service that runs under a user account with limited privileges, but needs to perform a task that requires administrative privileges. Instead of running the entire service under an administrative account, which could present a security risk, the service could use token impersonation to temporarily execute with the privileges of an administrative account when it needs to perform the task. This would allow the service to perform the task without requiring the user to authenticate as an administrator.
	
	Overall, the benefits of using token impersonation are that it allows a process to temporarily or permanently execute with the privileges of another process without requiring the user to authenticate as that process. This can be useful in certain situations where a process needs to perform a specific task that requires higher privileges, but it is not necessary or desirable to run the entire process with those privileges.

---

<h2>Command</h2>

Check is you have the right to impersonate tokens (meterpreter)
```
getprivs     ---> Looking for SetImpersonatePrivilege
```

Execut the exploit
```
SweetPotato.exe -a whoami
```

![[Pasted image 20230105204650.png]]

---

<h2>More Information</h2>

More Information ---> https://github.com/uknowsec/SweetPotato

<iframe src="https://github.com/uknowsec/SweetPotato" width="100%" height="1300"></iframe>