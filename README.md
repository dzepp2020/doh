# DNS over HTTP - DoH
Python wrapper for DNS over HTTP


This a simple little wrapper to make DNS over HTTP to Google.

# Args
- RES (-r/--res) which is the resource you're looking up (e.g. www.google.com).
- TYPE (-t/--type) which is the type of DNS record you're looking up (e.g. A, MX, NS).
- DEBUG (-d/--debug) if you want to see additional HTTP information ... debug.

# Usage
```
$ python3 ./dns.py -h
usage: dns.py [-h] [-d] -r RES -t TYPE

optional arguments:
  -h, --help            show this help message and exit
  -d, --debug           Flag to show additional information.
  -r RES, --res RES     Record/value to look up (e.g. www.google.com).
  -t TYPE, --type TYPE  DNS record type (e.g. A, MX, NS).
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

