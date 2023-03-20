--- ---
<h2>Subnet Mask</h2>
A subnet mask is used in IP addresses to specify the range of addresses that are part of a network. The subnet mask is denoted by a slash followed by a number, such as /24 or /23, which specifies the number of bits that are used to identify the network portion of the address. The network portion of an IP address is the part that identifies the network, while the remaining part identifies the host.

The most commonly used subnet masks are:
-   <font color="blue">/24</font>: This subnet mask includes all IP addresses from x.x.x.1 to x.x.x.254, where x.x.x is the network portion of the address. This is often used for small to medium-sized networks.
-   <font color="blue">/23</font>: This subnet mask includes all IP addresses from x.x.x.1 to x.x.x.254, where x.x.x is the network portion of the address. This is often used for larger networks.
-   <font color="blue">/16</font>: This subnet mask includes all IP addresses from x.x.0.1 to x.x.255.254, where x.x is the network portion of the address. This is often used for very large networks.

Other subnet masks that may be used to split a network into smaller subnetworks include:
-   <font color="blue">/25</font>: This subnet mask includes all IP addresses from x.x.x.1 to x.x.x.126, where x.x.x is the network portion of the address.
-   <font color="blue">/26</font>: This subnet mask includes all IP addresses from x.x.x.1 to x.x.x.62, where x.x.x is the network portion of the address.
-   <font color="blue">/27</font>: This subnet mask includes all IP addresses from x.x.x.1 to x.x.x.30, where x.x.x is the network portion of the address.
-   <font color="blue">/28</font>: This subnet mask includes all IP addresses from x.x.x.1 to x.x.x.14, where x.x.x is the network portion of the address.