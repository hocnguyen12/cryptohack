# Saying Hello challenge

## Solution 1

by visiting (Qualys SSL Labs)[https://www.ssllabs.com/ssltest/analyze.html] and searching for the `tls1.cryptohack.org` domain name we can get information about protocols used by the server.

![[saying_hello.png]]

The only cipher suite supported with TLS 1.2 is :

`TLS_ECDHE_RSA_WITH_AES_256_GCM_SHA384`

-> by formatting the cipher suite we get the flag :

`ECDHE-RSA-AES256-GCM-SHA384`

## Solution 2

```bash
curl --tls-max 1.2 -v https://tls1.cryptohack.org
```

```bash
[...]
* TLSv1.2 (OUT), TLS handshake, Client key exchange (16):
* TLSv1.2 (OUT), TLS header, Finished (20):
* TLSv1.2 (OUT), TLS change cipher, Change cipher spec (1):
* TLSv1.2 (OUT), TLS header, Certificate Status (22):
* TLSv1.2 (OUT), TLS handshake, Finished (20):
* TLSv1.2 (IN), TLS header, Finished (20):
* TLSv1.2 (IN), TLS header, Certificate Status (22):
* TLSv1.2 (IN), TLS handshake, Finished (20):
* SSL connection using TLSv1.2 / ECDHE-RSA-AES256-GCM-SHA384
[...]
```

-> flag : `ECDHE-RSA-AES256-GCM-SHA384`