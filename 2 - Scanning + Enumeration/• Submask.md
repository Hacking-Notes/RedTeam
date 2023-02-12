--- ---

<h2>Submask</h2>

Subnet masks are used in IP addresses to specify the range of addresses that are part of a network. The subnet mask is denoted by a slash followed by a number, such as /24 or /23, which specifies the number of bits that are used to identify the network portion of the address. A larger subnet mask includes a larger range of IP addresses in the network, while a smaller subnet mask includes a smaller range of IP addresses.

Most Commun
	- A subnet mask of /24 (e.g. 192.168.0.1/24) specifies that the network includes all IP addresses from 192.168.0.1 to 192.168.0.254.
	ㅤ
	-   A subnet mask of /23 (e.g. 192.168.0.1/23) specifies that the network includes all IP addresses from 192.168.0.1 to 192.168.1.254.
	ㅤ
	-   A subnet mask of /16 (e.g. 192.168.0.1/16) specifies that the network includes all IP addresses from 192.168.0.1 to 192.168.255.254.

Others
	-   /25: This subnet mask includes all IP addresses from x.x.x.1 to x.x.x.126, where x.x.x is the network portion of the address. This is often used to split a network into smaller subnetworks.
	ㅤ
	-   /26: This subnet mask includes all IP addresses from x.x.x.1 to x.x.x.62, where x.x.x is the network portion of the address. This is often used to split a network into smaller subnetworks.
	ㅤ
	-   /27: This subnet mask includes all IP addresses from x.x.x.1 to x.x.x.30, where x.x.x is the network portion of the address. This is often used to split a network into smaller subnetworks.
	ㅤ
	-   /28: This subnet mask includes all IP addresses from x.x.x.1 to x.x.x.14, where x.x.x is the network portion of the address. This is often used to split a network into smaller subnetworks.