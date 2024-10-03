import os
import time
import phonenumbers
from phonenumbers import carrier, geocoder, timezone, PhoneNumberType, PhoneMetadata
import pyfiglet
from datetime import datetime
from colorama import Fore, Style, init

init(autoreset=True)

def clear_screen():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')

clear_screen()

t = time.localtime(time.time())
localtime = time.asctime(t)
print("Local Time:", localtime)

ascii_art = pyfiglet.figlet_format("Skyhima")
print(Fore.CYAN + ascii_art)

import requests

response = requests.get("https://api.ipify.org?format=json")
ip_data = response.json()

print("Your Public IP:", ip_data['ip'])

import socket

def get_local_ip():                                                                                  # Mengambil hostname dari perangkat
    hostname = socket.gethostname()
    # Mendapatkan alamat IP lokal dari hostname
    local_ip = socket.gethostbyname(hostname)
    return local_ip

if __name__ == "__main__":
    local_ip = get_local_ip()
    print("Your Local IP:", local_ip)

def get_number_type(number):
    number_type = phonenumbers.number_type(number)
    if number_type == PhoneNumberType.MOBILE:
        return "Ponsel"
    elif number_type == PhoneNumberType.FIXED_LINE:
        return "Telepon Tetap"
    elif number_type == PhoneNumberType.FIXED_LINE_OR_MOBILE:
        return "Telepon Tetap atau Ponsel"
    elif number_type == PhoneNumberType.TOLL_FREE:
        return "Bebas Pulsa"
    elif number_type == PhoneNumberType.PREMIUM_RATE:
        return "Nomor Premium"
    elif number_type == PhoneNumberType.VOIP:
        return "VoIP"
    elif number_type == PhoneNumberType.SHARED_COST:
        return "Biaya Bersama"
    elif number_type == PhoneNumberType.PAGER:
        return "Pager"
    elif number_type == PhoneNumberType.UAN:
        return "UAN"
    elif number_type == PhoneNumberType.VOICEMAIL:
        return "Voicemail"
    else:
        return "Tipe Tidak Diketahui"

try:
    current_time = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    print("Current Time:", current_time)
    mobileNo = input("Enter the victim numbers (ex: +62822...): ")
    mobileNo = phonenumbers.parse(mobileNo, "ID")

    print(Fore.BLUE + "== Number Information ==")

    timezones = timezone.time_zones_for_number(mobileNo)
    print(Fore.BLUE + "Time Zone:", timezones)

    provider = carrier.name_for_number(mobileNo, "id")
    print(Fore.BLUE + "Operator:", provider)

    region = geocoder.description_for_number(mobileNo, "id")
    print(Fore.BLUE + "Region:", region)

is_valid = phonenumbers.is_valid_number(mobileNo)
    print(Fore.BLUE + "Valid Number:", is_valid)

    is_possible = phonenumbers.is_possible_number(mobileNo)
    print(Fore.BLUE + "Number Maybe Valid:", is_possible)

    international_format = phonenumbers.format_number(mobileNo, phonenumbers.PhoneNumberFormat.INTER>
    print(Fore.BLUE + "International Format:", international_format)

    mobile_format = phonenumbers.format_number(mobileNo, phonenumbers.PhoneNumberFormat.NATIONAL)
    print(Fore.BLUE + "National Format:", mobile_format)

    e164_format = phonenumbers.format_number(mobileNo, phonenumbers.PhoneNumberFormat.E164)
    print(Fore.BLUE + "Format E.164:", e164_format)

    country_code = mobileNo.country_code
    print(Fore.BLUE + "Country Code:", country_code)

    local_number = mobileNo.national_number
    print(Fore.BLUE + "Local Number:", local_number)

    number_length = len(str(local_number))
    print(Fore.BLUE + "Number Length:", number_length)
    number_type = get_number_type(mobileNo)

    print(Fore.BLUE + "Number Type:", number_type)
    print(Fore.BLUE + "== More Information ==")

    if number_type == "Premium Number":
        print(Fore.BLUE + "Caution: This a premium number, may incur additional charges.")
    else:
        print(Fore.BLUE + "This not premium number.")

    if timezones:
        print(Fore.BLUE + "This number is related to time zone", ", ".join(timezones))
    else:
        print(Fore.BLUE + "There is no time zone associated with this number.")

    is_possible_as_mobile = phonenumbers.is_possible_number_for_type(mobileNo, PhoneNumberType.MOBIL>
    print(Fore.BLUE + "Probably as a phone number:", is_possible_as_mobile)

    has_extension = mobileNo.extension is not None
    print(Fore.BLUE + "Has Extension:", has_extension)

    optimal_format = phonenumbers.format_by_pattern(mobileNo, phonenumbers.PhoneNumberFormat.INTERNA>
    print(Fore.BLUE + "Optimal Format:", optimal_format)

    is_valid_for_region = phonenumbers.is_valid_number_for_region(mobileNo, "ID")
    print(Fore.BLUE + "Valid for Region Indonesia:", is_valid_for_region)

    metadata = PhoneMetadata.load_all()
    print(Fore.BLUE + "Phone Number Metadata Is Loaded")

    print(Fore.BLUE + "Number Status: ")

    print(Fore.BLUE + "This A Phone Number")

except phonenumbers.NumberParseException as e:
    print(f"Errors in processing numbers: {e}")