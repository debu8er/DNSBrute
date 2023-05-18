import os
import argparse


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


os.system("dig A +short somethingdoesntexist."+domain+" > dig-output")

dig = open("dig-output","r")
if len(dig.read()) < 1:
    print("continue")

    os.system(f"dnsx -d {domain} -w {wordlist} -r {resolver} -silent -o output")

    os.system(f"subfinder -d {domain} -silent -o subdomains")

    os.system("cat output subdomains | sort -u > output2")

    os.system(f"cat output2 | dnsgen - > output3")

    os.system(f"dnsx -d {domain} -w output3 -r {resolver} -silent -o final_output")

else:
    print("It has A record ):")
