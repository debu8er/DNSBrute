import os
import argparse
from urllib.parse import urlparse

parser = argparse.ArgumentParser(description="DnsBrute is a tool for Dns BruteForce")

parser.add_argument("-d", "--domain",
                    required=True,
                    help='domain input.')

parser.add_argument("-r", "--resolver",
                    required=True,
                    help='resolver file.')

parser.add_argument("-w", "--wordlist",
                    required=True,
                    help='wordlist file.')

options = parser.parse_args()

domain = options.domain
resolver = options.resolver
wordlist = options.wordlist


domain_parts = domain.split('.')

sdomain = domain_parts[-2] if len(domain_parts) >= 2 else domain_parts[0]




os.system("dig A +short somethingdoesntexist."+domain+" > dig-output")

dig = open("dig-output","r")
if len(dig.read()) < 1:

    os.system(f"dnsx -d {domain} -w {wordlist} -r {resolver} -silent -o output")

    os.system(f'curl -s "https://crt.sh/?q={domain}&output=json" | jq -r ".[].common_name" | sort -u > {sdomain}-crtsh')
    os.system(f'subfinder -all -d {domain} -silent > {sdomain}-subfinder')
    os.system(f'curl -s "https://www.abuseipdb.com/whois/{domain}" -H "user-agent: firefox" -b "abuseipdb_session=YOUR-session" | grep -E "<li>\w.*</li>" | sed -E "s/<\/?li>//g" | sed -e "s/$/.{domain}/" > {sdomain}-abuse')
    os.system(f'cat {sdomain}-crtsh {sdomain}-subfinder {sdomain}-subfinder | sort -u > {sdomain}-allsub')


    os.system(f"cat output {sdomain}-allsub | sort -u > output2")

    with open("output2", "r") as file:
        if len(file.readlines()) >= 500:
            os.system("cat output2 | httpx > output2-")
        else:
            os.system("cat output2 > output2-")


    os.system(f"cat output2- | dnsgen - > output3")

    os.system(f"dnsx -d {domain} -w output3 -r {resolver} -silent -o final_output")

else:
    print("It has A record ):")
