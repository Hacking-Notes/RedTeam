--- ---

<h2>General</h2>

Kerberos and NTLM (NetNTLM) are both authentication protocols used to verify the identity of a user or computer attempting to log in to a network.

Kerberos is a network authentication protocol that uses tickets and encryption to securely authenticate a user to a service. It is designed to prevent eavesdropping and replay attacks, and to allow users to access network resources without transmitting their password over the network.

In general, Kerberos is the preferred authentication protocol for secure networks, as it provides stronger security than NTLM. However, NTLM may still be used in some older systems or in certain scenarios where compatibility with legacy systems is important.

---

<h2>Kerberos Authentication</h2>

![[Pasted image 20230118193419.png]]

In the Kerberos authentication protocol, the Ticket Granting Ticket (TGT) is used to verify the identity of a user, while the Ticket Granting Service (TGS) is used to verify access to a specific service.

<h3>More Information</h3>
Kerberos authentication is the default authentication protocol for any recent version of Windows. Users who log into a service using Kerberos will be assigned tickets. Think of tickets as proof of a previous authentication. Users with tickets can present them to a service to demonstrate they have already authenticated into the network before and are therefore enabled to use it.

When Kerberos is used for authentication, the following process happens:

1.ㅤThe user sends their username and a timestamp encrypted using a key derived from their password to the **Key Distribution Center (KDC)**, a service usually installed on the Domain Controller in charge of creating Kerberos tickets on the network.ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤThe KDC will create and send back a **Ticket Granting Ticket (TGT)**, which will allow the user to request additional tickets to access specific services. The need for a ticket to get more tickets may sound a bit weird, but it allows users to request service tickets without passing their credentials every time they want to connect to a service. ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤAlong with the TGT, a **Session Key** is given to the user, which they will need to generate the following requests.Notice the TGT is encrypted using the **krbtgt** account's password hash, and therefore the user can't access its contents. It is essential to know that the encrypted TGT includes a copy of the Session Key as part of its contents, and the KDC has no need to store the Session Key as it can recover a copy by decrypting the TGT if needed.
	![Kerberos step 1](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/d36f5a024c20fb480cdae8cd09ddc09f.png)


2.ㅤWhen a user wants to connect to a service on the network like a share, website or database, they will use their TGT to ask the KDC for a **Ticket Granting Service (TGS)**. TGS are tickets that allow connection only to the specific service they were created for. To request a TGS, the user will send their username and a timestamp encrypted using the Session Key, along with the TGT and a **Service Principal Name (SPN),** which indicates the service and server name we intend to access.ㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤㅤAs a result, the KDC will send us a TGS along with a **Service Session Key**, which we will need to authenticate to the service we want to access. The TGS is encrypted using a key derived from the **Service Owner Hash**. The Service Owner is the user or machine account that the service runs under. The TGS contains a copy of the Service Session Key on its encrypted contents so that the Service Owner can access it by decrypting the TGS.
	![Kerberos step 2](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/84504666e78373c613d3e05d176282dc.png)


3.ㅤThe TGS can then be sent to the desired service to authenticate and establish a connection. The service will use its configured account's password hash to decrypt the TGS and validate the Service Session Key.
	![Kerberos step 3](https://tryhackme-images.s3.amazonaws.com/user-uploads/5ed5961c6276df568891c3ea/room-content/8fbf08d03459c1b792f3b6efa4d7f285.png)


Video explanation ---> https://www.youtube.com/watch?v=2WqZSZ5t0qk

Kerberos Exploitation via (PtT)  ---> [[3 - Alternate Authentication (PtH, PtT, PtK)]]
Kerberos Exploitation via (PtK) ---> [[3 - Alternate Authentication (PtH, PtT, PtK)]]

Persistence ---> [[2 - Persistence through Tickets]]