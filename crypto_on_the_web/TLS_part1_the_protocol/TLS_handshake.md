# TLS Handshake challenge

## Instructions / Explaination
This challenge uses the same packet capture as the previous challenge. Let's describe the communication we see at a high level.

The TLS communication only begins at packet 10, but what happens before provides important context:

- Packets 1-2: First, when we typed cryptohack.org into the address bar and hit enter, a Domain Name System (DNS) request was made to translate the domain name (cryptohack.org) to an IP address (178.62.74.206).
- Packets 3-4: The "Safe Browsing" feature in Firefox reached out to a Google server to check that cryptohack.org was not a phishing or malicious domain.
- Packets 5-6: DNS responses to our DNS requests came back, saying that cryptohack.org can be reached at IP address 178.62.74.206.
- Packets 7-9: A TCP three-way handshake (SYN, SYN-ACK, ACK) was initiated between our laptop and port 443 (the TLS port) of the server at 178.62.74.206. This negotiated a stable connection between the two computers over the Internet before the real data transfer could start.
- Packet 10-11: A TLS ClientHello message was sent from our laptop to the server. The next challenge will expand on this, but for now note this was our laptop sending a bunch of important parameters such as the ciphers it supports. Packet 11 is an ACK TCP packet sent from the server ACKnowledging it received the packet from our laptop.
- Packet 12-17: The server sent TLS ServerHello, Change Cipher Spec, and Application Data messages. TLS 1.3 is designed to be really fast - the server sends back its own parameters, then signals Change Cipher Spec which means it is switching over to sending encrypted communications from now on. Then the server sends its TLS certificate encrypted.
- Packets 18-21: An Online Certificate Status Protocol (OCSP) connection was made from our laptop to an OCSP server, to check that the TLS certificate presented by CryptoHack hadn't been revoked... yet another thing we'll explore later!
- Packets 22-27: Our laptop sent a Change Cipher Spec message to note that it is switching over to sending encrypted data, and it finally made a HTTP request requesting the CryptoHack home page. The actual HTTP content of the connection can't be seen in the packet capture, as it's now encrypted!
- Packets 28-39: The server started sending the contents of the CryptoHack homepage to our client over HTTP wrapped in TLS.
- Packets 40-50: Firefox's HTML parser saw that it needed external resources from Content Delivery Networks such as cdnjs.cloudflare.com to load JavaScript resources on the page and sent DNS requests to resolve those domains. This isn't relevant to TLS apart from the notable fact that DNS requests on most systems by default are not encrypted (but DNS-over-HTTPS, which fixes this obvious leak, is starting to get more common).

## Solution

We are looking at packet 12, `Server Hello` message.

In the `Transport Layer Security`, we look at the handshake protocol.

There is a `Random` field with random data sent from the sever.

Flag : **67c6bf8ffda56fcb359fba7f0149f85422223cf021ab1a0af701de5dd2091498**
