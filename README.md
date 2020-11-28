# doh
Python wrapper for DNS over HTTP

============================

This a simple little wrapper to make DNS over HTTP to Google.

============================

```
$ python3 ./dns.py
usage: dns.py [-h] [-d DEBUG] -r REC -t TYPE
dns.py: error: the following arguments are required: -r/--rec, -t/--type

# Example
```
$ python3 ./dns.py -r google.com -t NS
https://dns.google.com/resolve?name=google.com&type=NS
Status: 0
Value:	google.com
Type:	NS
Answer:
google.com.	NS	ns4.google.com.
google.com.	NS	ns1.google.com.
google.com.	NS	ns3.google.com.
google.com.	NS	ns2.google.com.


