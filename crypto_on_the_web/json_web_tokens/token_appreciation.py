"""
    Token Appreciation challenge

HEADER:ALGORITHM & TOKEN TYPE
{

  "typ": "JWT",

  "alg": "HS256"

}

PAYLOAD:DATA
{

  "flag": "crypto{jwt_contents_can_be_easily_viewed}",

  "user": "Crypto McHack",

  "exp": 2005033493

}

VERIFY SIGNATURE

HMACSHA256(
  base64UrlEncode(header) + "." +
  base64UrlEncode(payload),
  
) secret base64 encoded
"""

token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJmbGFnIjoiY3J5cHRve2p3dF9jb250ZW50c19jYW5fYmVfZWFzaWx5X3ZpZXdlZH0iLCJ1c2VyIjoiQ3J5cHRvIE1jSGFjayIsImV4cCI6MjAwNTAzMzQ5M30.shKSmZfgGVvd2OSB2CGezzJ3N6WAULo3w9zCl_T47KQ"

import jwt

decoded = jwt.decode(token, "secret", algorithms=["HS256"])

print(f"flag : {decoded}")