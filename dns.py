import requests
import json
import sys
import argparse

# Global variables
recordType={
1:'A', 2:'NS', 3:'MD', 4:'MF', 5:'CNAME', 6:'SOA', 7:'MB', 8:'MG', 9:'MR', 10:'NULL', 11:'WKS', 12:'PTR',
13:'HINFO', 14:'MINFO', 15:'MX', 16:'TXT', 17:'RP', 18:'AFSDB', 19:'X25', 20:'ISDN', 21:'RT', 22:'NSAP',
23:'NSAP-PTR', 24:'SIG', 25:'KEY', 26:'PX', 27:'GPOS', 28:'AAAA', 29:'LOC', 30:'NXT', 31:'EID', 32:'NIMLOC', 
33:'SRV', 34:'ATMA', 35:'NAPTR', 36:'KX', 37:'CERT', 38:'A6', 39:'DNAME', 40:'SINK', 41:'OPT', 42:'APL', 43:'DS',
44:'SSHFP', 45:'IPSECKEY', 46:'RRSIG', 47:'NSEC', 48:'DNSKEY', 49:'DHCID', 50:'NSEC3', 51:'NSEC3PARAM', 52:'TLSA',
53:'SMIMEA', 55:'HIP', 56:'NINFO', 57:'RKEY', 58:'TALINK', 59:'CDS', 60:'CDNSKEY', 61:'OPENPGPKEY', 62:'CSYNC',
 63:'ZONEMD', 64:'SVCB', 65:'HTTPS', 99:'SPF', 100:'UINFO', 101:'UID', 102:'GID', 103:'UNSPEC', 104:'NID', 105:'L32',
106:'L64', 107:'LP', 108:'EUI48', 109:'EUI64', 249:'TKEY', 250:'TSIG', 251:'IXFR', 252:'AXFR', 253:'MAILB', 254:'MAILA',
255:'*', 256:'URI', 257:'CAA', 258:'AVC', 259:'DOA', 260:'AMTRELAY', 32768:'TA', 32769:'DLV'}

provider="https://dns.google.com/resolve?"

#
# Print 80 -
def pLine():
   print('-' * 80)

#
# Dump a bunch of info
def debug(response):
   pLine()
   print(response.headers)
   print(response.status_code)
   print(str(response._content))
   print(json.dumps(response.json(), indent=3))
   pLine()

#
# Main
def main():
   # Initialize parser
   isDebug=False
   parser = argparse.ArgumentParser()
   # Adding optional argument
   parser.add_argument( "-d","--debug" , required=False, help = "Show additional HTTP info.")
   # Adding required arguments
   parser.add_argument( "-r", "--res", required=True, help = "Record/value to look up (e.g. www.google.com).")
   parser.add_argument( "-t", "--type", required=True, help = "DNS record type (e.g. A, MX, NS).")
   # Read arguments from command line
   args = parser.parse_args() 
   
   if args.res:
      value = args.res

   if args.type:
      type = args.type

   if args.debug:
      print("Debug")
      isDebug=True
   
   if type.upper() == "PTR":
     value += ".in-addr.arpa"

   url = provider + "name=" + value + "&type=" + type
   print(url)

   response=requests.get(url)
   if isDebug:
      debug(response)

   if response.status_code == 200:
      myDict=response.json()
      if myDict['Status'] ==0:
         print(('Status: {}'.format(myDict['Status']) ))
         print('Value:\t' + value)
         print('Type:\t' +  type.upper())
         print('Answer:')
         answer=myDict['Answer']
         for x in answer:
            print("{}\t{}\t{}".format(x['name'],recordType.get(x['type'],x['type']),x['data']))
            #print(*x.items(), sep=" - ")
      else:
         print("Some Error")
   elif response.status_code == 404:
      print('Not Found.')
   else:
      print(response.status_code)

if __name__ == "__main__": 
   main() 

