# DNSBrute
This is tool for DNS BruteForce
Uses (subfinder - crtsh - abusedb) for subdomain enumeration

# Requirments
This tool needs to install => ```subfinder - dnsx - dnsgen```

# Help

```
usage: DNSBrute.py [-h] -d DOMAIN -w WORDLIST -r RESOLVER

This is tool for DNS BruteForce
This tool needs to install { subfinder - shuffledns - massdns - dnsgen }

optional arguments:
  -h, --help            show this help message and exit
  -d DOMAIN, --domain DOMAIN
                        file input.
  -w WORDLIST, --wordlist WORDLIST
                        wordlist path.
  -r RESOLVER, --resolver RESOLVER
                        reslover path.
```

# Example command

```
python3 -d domain.tld -w wordlist.txt -r resolver.txt
```
