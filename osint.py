#!/usr/bin/python3
# VERSION 1.2
# CREATED 2023 BY MR,OWLBIRD05
# REFIXED & OPTIMIZED FOR TERMUX

import time
import os
import sys
import requests
import json
import colorama
from time import sleep
from datetime import datetime
import phonenumbers as pnumb
from phonenumbers import parse, geocoder, carrier, timezone
import instaloader

### colors
RED = "\033[91m"
GREEN = "\033[92m"
BLUE = "\033[94m"
YELLOW = "\033[1;93m"
WHITE = "\033[1;97m"
NORMAL = "\033[0;37m"

OKGREEN = '\033[92m'
WARNING = '\033[93m'
YE = '\033[1;33m'
BOLD = '\033[1m'
ENDC = '\033[0m'
CRED2 = "\33[91m"

now = datetime.now()
current_time = now.strftime("%H:%M:%S")

def animation(s):
    for c in s + "\n":
        sys.stdout.write(c)
        sys.stdout.flush()
        time.sleep(0.0025)

def banner():
    animation(f"""
    {BLUE}░█████╗░░██╗░░░░░░░██╗██╗░░░░░░██████╗██╗███╗░░██╗████████╗   
    ██╔══██╗░██║░░██╗░░██║██║░░░░░██╔════╝██║████╗░██║╚══██╔══╝          
    ██║░░██║░╚██╗████╗██╔╝██║░░░░░╚█████╗░██║██╔██╗██║░░░██║░░░             
    ██║░░██║░░████╔═████║░██║░░░░░░╚═══██╗██║██║╚████║░░░██║░░░               
    ╚█████╔╝░░╚██╔╝░╚██╔╝░███████╗██████╔╝██║██║░╚███║░░░██║░░░                  
    ░╚════╝░░░░╚═╝░░░╚═╝░░╚══════╝╚═════╝░╚═╝╚═╝░░╚══╝░░░╚═╝░░░                   
            Version 1.2 - 2023 coded by Mr,OwlBird05

         \033[91m[??] Choose an option:
         \033[91m[\033[93m1\033[91m] \033[1;97mPhone Number Information
         \033[91m[\033[93m2\033[91m] \033[1;97mTrack IP
         \033[91m[\033[93m3\033[91m] \033[1;97mInstagram User Information
         \033[91m[\033[93mA\033[91m] \033[1;97mAbout""")

def start():
    os.system("clear")
    banner()
    chose = input("           \033[94mChoose\033[0m: ")
    
    if chose == "1":
        sleep(1)
        print(f"""
        \033[91m[\033[93m1\033[91m] \033[1;97mTrack Number V1
        \033[91m[\033[93m2\033[91m] \033[1;97mTrack Number V2
        \033[91m[\033[93m3\033[91m] \033[1;97mTrack Number V3""")
        V = input(f"      {BLUE}Choose\033[0m: ")
        
        if V == "1":
            number = input(f"{WHITE}Enter Number {NORMAL}({GREEN}Without +){WHITE} :{CRED2}➤ ")
            try:
                parsing = parse("+" + number if not number.startswith("+") else number)
                loc = geocoder.description_for_number(parsing, "id")
                isp = carrier.name_for_number(parsing, "id")
                tz = timezone.time_zones_for_number(parsing)
                
                print()
                sleep(0.1)
                print(f"{YELLOW}International Format          {NORMAL}:", pnumb.normalize_digits_only(parsing))
                print(f"{YELLOW}National Format               {NORMAL}:", pnumb.national_significant_number(parsing))
                print(f"{YELLOW}Valid Number                  {NORMAL}:", pnumb.is_valid_number(parsing))
                print(f"{YELLOW}Can Be Internationally Dialled{NORMAL}:", pnumb.can_be_internationally_dialled(parsing))
                print(f"{YELLOW}Location                      {NORMAL}:", loc)
                print(f"{YELLOW}Region Code For Number        {NORMAL}:", pnumb.region_code_for_number(parsing))
                print(f"{YELLOW}Number Type                   {NORMAL}:", pnumb.number_type(parsing))
                print(f"{YELLOW}Is Carrier Specific           {NORMAL}:", pnumb.is_carrier_specific(parsing))
                print(f"{YELLOW}ISP                           {NORMAL}:", isp)
                print(f"{YELLOW}Time Zone                     {NORMAL}:", tz)
                print('\n\033[1;93mWhatsApp Number               \033[0m: wa.me/' + number + '\n')
                print(f"{YELLOW}Is Number Geographical        {NORMAL}:", pnumb.is_number_geographical(parsing))
                print("")
                
                open_wa = input(f"{WHITE}TYPE 1 To Open Chat Target on WhatsApp or press ENTER to next: ")
                if open_wa == "1":
                    os.system('xdg-open http://wa.me/' + number)
            except Exception as e:
                print(f"{RED}Error: {e}")

        elif V == "2":
            number = input(f"{WHITE}Enter Number {NORMAL}({GREEN}Without +){WHITE} :{CRED2}➤ ")
            try:
                phe = requests.get("http://apilayer.net/api/validate?access_key=I2A2HXBuGbEJbufG8AxD2IGeFpqFyWFU=" + number).json()
                print()
                print(f"{YELLOW}Valid                 {NORMAL}:{GREEN} " + str(phe.get('valid', 'N/A')))
                print(f"{YELLOW}Number                {NORMAL}: " + str(phe.get('number', 'N/A')))
                print(f"{YELLOW}Local Format          {NORMAL}: " + str(phe.get('local_format', 'N/A')))
                print(f"{YELLOW}International Format  {NORMAL}: " + str(phe.get('international_format', 'N/A')))
                print(f"{YELLOW}Country Prefix        {NORMAL}: " + str(phe.get('country_prefix', 'N/A')))
                print(f"{YELLOW}Country Code          {NORMAL}: " + str(phe.get('country_code', 'N/A')))
                print(f"{YELLOW}Country Name          {NORMAL}: " + str(phe.get('country_name', 'N/A')))
                print(f"{YELLOW}Location              {NORMAL}: " + str(phe.get('location', 'N/A')))
                print(f"{YELLOW}Carrier               {NORMAL}: " + str(phe.get('carrier', 'N/A')))
                print(f"{YELLOW}Line Type             {NORMAL}: " + str(phe.get('line_type', 'N/A')))
            except Exception as e:
                print(f"{RED}Error fetching data: {e}")

        elif V == "3":
            User_phone = input(f"{WHITE}Enter Number {NORMAL}({GREEN}EX +62xxx){WHITE} :{CRED2}➤ ")
            try:
                parsed_number = pnumb.parse(User_phone, "ID")
                region_code = pnumb.region_code_for_number(parsed_number)
                jenis_provider = carrier.name_for_number(parsed_number, "en")
                location = geocoder.description_for_number(parsed_number, "id")
                is_valid_number = pnumb.is_valid_number(parsed_number)
                is_possible_number = pnumb.is_possible_number(parsed_number)
                formatted_number = pnumb.format_number(parsed_number, pnumb.PhoneNumberFormat.INTERNATIONAL)
                formatted_number_for_mobile = pnumb.format_number_for_mobile_dialing(parsed_number, "ID", with_formatting=True)
                number_type = pnumb.number_type(parsed_number)
                timezone1 = timezone.time_zones_for_number(parsed_number)

                print(f"\n {NORMAL}========== {YELLOW}SHOW INFORMATION PHONE NUMBERS {WHITE}==========")
                print(f"\n {NORMAL}Location             :{YELLOW} {location}")
                print(f" {NORMAL}Region Code          :{YELLOW} {region_code}")
                print(f" {NORMAL}Timezone             :{YELLOW} {', '.join(timezone1)}")
                print(f" {NORMAL}Operator             :{YELLOW} {jenis_provider}")
                print(f" {NORMAL}Valid number         :{YELLOW} {is_valid_number}")
                print(f" {NORMAL}Possible number      :{YELLOW} {is_possible_number}")
                print(f" {NORMAL}International format :{YELLOW} {formatted_number}")
                print(f" {NORMAL}Mobile format        :{YELLOW} {formatted_number_for_mobile}")
                print(f" {NORMAL}Original number      :{YELLOW} {parsed_number.national_number}")
                print(f" {NORMAL}Country code         :{YELLOW} {parsed_number.country_code}")
            except Exception as e:
                print(f"{RED}Error: {e}")

    elif chose == "2":
        try:
            ip = input(f"{WHITE}\n Enter IP target :{CRED2}➤ ")
            print()
            print(f' {NORMAL}============= {YELLOW}SHOW INFORMATION IP ADDRESS {NORMAL}=============')
            req_api = requests.get(f"http://ipwho.is/{ip}")
            ip_data = req_api.json()

            # API Response Validation Check
            if not ip_data.get("success", True):
                print(f"{RED} Failed to retrieve IP information: {ip_data.get('message', 'Invalid IP or Private IP')}")
                return

            time.sleep(1)
            print(f"{NORMAL}\n IP target       :{YELLOW}", ip)
            print(f"{NORMAL} Type IP         :{YELLOW}", ip_data.get("type", "N/A"))
            print(f"{NORMAL} Country         :{YELLOW}", ip_data.get("country", "N/A"))
            print(f"{NORMAL} Country Code    :{YELLOW}", ip_data.get("country_code", "N/A"))
            print(f"{NORMAL} City            :{YELLOW}", ip_data.get("city", "N/A"))
            print(f"{NORMAL} Continent       :{YELLOW}", ip_data.get("continent", "N/A"))
            print(f"{NORMAL} Region          :{YELLOW}", ip_data.get("region", "N/A"))
            print(f"{NORMAL} Latitude        :{YELLOW}", ip_data.get("latitude", "N/A"))
            print(f"{NORMAL} Longitude       :{YELLOW}", ip_data.get("longitude", "N/A"))
            
            lat = ip_data.get('latitude', 0)
            lon = ip_data.get('longitude', 0)
            print(f"{NORMAL} Maps            :{YELLOW}", f"https://www.google.com/maps/@{lat},{lon},8z")
            
            print(f"{NORMAL} EU              :{YELLOW}", ip_data.get("is_eu", "N/A"))
            print(f"{NORMAL} Postal          :{YELLOW}", ip_data.get("postal", "N/A"))
            print(f"{NORMAL} Calling Code    :{YELLOW}", ip_data.get("calling_code", "N/A"))
            print(f"{NORMAL} Capital         :{YELLOW}", ip_data.get("capital", "N/A"))
            print(f"{NORMAL} ASN             :{YELLOW}", ip_data.get("connection", {}).get("asn", "N/A"))
            print(f"{NORMAL} ORG             :{YELLOW}", ip_data.get("connection", {}).get("org", "N/A"))
            print(f"{NORMAL} ISP             :{YELLOW}", ip_data.get("connection", {}).get("isp", "N/A"))
            print(f"{NORMAL} Current Time    :{YELLOW}", ip_data.get("timezone", {}).get("current_time", "N/A"))
            print()
        except Exception as e:
            print(f"{RED} Error: {e}")

    elif chose == "3":
        x = instaloader.Instaloader()
        try:
            print()
            uname = input(f"\033[36mEnter a username \033[0m:{CRED2}➤ \033[36m")
            if uname != "":
                f = instaloader.Profile.from_username(x.context, uname)
                print("\033[32mUsername\033[0m :", f.username)
                print("\033[32mID\033[0m :", f.userid)
                print("\033[32mNama lengkap\033[0m :", f.full_name)
                print("\033[32mBiografi\033[0m :", f.biography)
                print("\033[32mPengikut\033[0m :", f.followers)
                print("\033[32mMengikuti\033[0m :", f.followees)
                print("\033[32mPostingan\033[0m :", f.mediacount)
                print("\033[32mURL foto profil\033[0m :", f.profile_pic_url)
        except Exception as e:
            print(f"{RED}Error: {e}")

    elif chose.upper() == "A":
        print(f"""{NORMAL}
The OwlSint tool is for searching phone numbers and tracking IP.
Created by Mr,OwlBird05.
""")

if __name__ == "__main__":
    start()
