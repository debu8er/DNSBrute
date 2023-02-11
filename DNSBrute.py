import os
import argparse
import time

class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


parser = argparse.ArgumentParser(description="""This is tool for DNS BruteForce , This tool needs to install { subfinder - shuffledns - massdns - dnsgen }""")

parser.add_argument("-d", "--domain",
                    required=True,
                    help='file input.\n')

parser.add_argument("-w", "--wordlist",
                    required=True,
                    help='wordlist path.\n')

parser.add_argument("-r", "--resolver",
                    required=True,
                    help='reslover path.')

options = parser.parse_args()

print (bcolors.FAIL + " ____  _   _ ____  ____             _     ")
print (bcolors.FAIL + "|  _ \| \ | / ___|| __ ) _ __ _   _| |_ ____")
print (bcolors.OKGREEN + "| | | |  \| \___ \|  _ \| '__| | | | __/ _ \ ")
print (bcolors.ENDC + "| |_| | |\  |___) | |_) | |  | |_| | ||  __/")
print (bcolors.OKBLUE + "|____/|_| \_|____/|____/|_|   \__,_|\__\___|")
time.sleep(1)
print(bcolors.BOLD+"********** Made by debug **********\n")


domain = options.domain
wordlist = options.wordlist
resolver = options.wordlist

os.system("dig A +short somethingdoesntexist."+domain+">dig-output")

dig = open("dig-output","r")
if len(dig.read()) < 1:
    print("continue")

    os.system(f"subfinder -d {domain} -silent > suboutput.txt && cat suboutput.txt {wordlist} > merge1.txt")

    os.system(f"shuffledns -w merge1.txt -d {domain} -r {resolver} -silent -o output.txt")

    os.system("cat suboutput.txt output.txt | sort -u > merge2.txt && dnsgen -w merge2.txt -f - > dnsgen-output.txt")

    os.system(f"shuffledns -w dnsgen-output.txt -d {domain} -r {resolver} -silent -o output2.txt")

    os.system(f"cat output1.txt output2.txt | sort -u > output3.txt && shuffledns -w output3.txt -d {domain} -r {resolver} -silent -o lastoutput.txt")

    os.system("rm -rf suboutput.txt merge1.txt output.txt merge2.txt dnsgen-output.txt output3.txt")
else:
    print("It has A record ):")