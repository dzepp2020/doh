# doh
Python wrapper for DNS over HTTP


This a simple little wrapper to make DNS over HTTP to Google.

# Args
- RES (-r/--res) which is the resource you're looking up (e.g. www.google.com).
- TYPE (-t/--type) which is the type of DNS record you're looking up (e.g. A, MX, NS).
- DEBUG (-d/--debug) if you want to see additional HTTP information ... debug.

# Usage
```
$ python3 ./dns.py
usage: dns.py [-h] [-d DEBUG] -r REC -t TYPE
dns.py: error: the following arguments are required: -r/--rec, -t/--type
```

# Example - google.com NS lookup
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
```

