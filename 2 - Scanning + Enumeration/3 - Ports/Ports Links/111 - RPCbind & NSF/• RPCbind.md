--- ---

<h2>Find RPCbind Port</h2>

Nmap
```
nmap -sV -SC IP -p111
```

- Possible to find RPCbind on an other port

---

<h2>Connection</h2>

- RPCbind (Display Directory)
```Terminal
showmount -e IP
```

---

<h2>What is RPCbind</h2>

The **rpcbind** utility is a server that converts RPC program numbers into universal addresses.  It must be running on the host to be able to make RPC calls on a server on that machine.

When an RPC service is started, it tells **rpcbind** the address at which it is listening, and the RPC program numbers it is prepared to serve.  When a client wishes to make an RPC call to a given program number, it first contacts **rpcbind** on the server machine to determine the address where RPC requests should be sent.

The **rpcbind** utility should be started before any other RPC service. Normally, standard RPC servers are started by port monitors, so **rpcbind** must be started before port monitors are invoked.

When **rpcbind** is started, it checks that certain name-to-address translation-calls function correctly.  If they fail, the network configuration databases may be corrupt.  Since RPC services cannot function correctly in this situation, **rpcbind** reports the condition and terminates.

The **rpcbind** utility can only be started by the super-user.