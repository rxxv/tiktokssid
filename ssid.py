from requests import Session
import datetime
from os import system
from colorama import init, Fore, Style

init(autoreset=True)
requests = Session()

app_ids = {
    '1233': 'TikTok App (Global)',
    '1459': 'TikTok QR Web Login',
    '1180': 'Tiktok App (Asia)',
    '1125': 'Douyin (Chinese)',
    '1340': 'Tiktok Lite'
}

def banner():
    print(Fore.CYAN + Style.BRIGHT + "\nSession ID Validity Check\n" + Style.RESET_ALL)

def info(sessionid: str):
    try:
        url = "https://api2.musical.ly/passport/account/info/v2/"

        headers = {
            "Host": "api2.musical.ly",
            "Content-Type": "application/json; charset=utf-8",
            "Connection": "Keep-Alive",
            "User-Agent": "TikTok 16.0.16 rv:103005 (iPhone; iOS 11.1.4; en_EN) Cronet",
            "Cookie": "sessionid={}".format(sessionid)
        }

        response = requests.get(url, headers=headers)
        data = response.json()

        if "message" in data and data['message'] == "success":
            account_data = data['data']
            app_id = account_data.get('app_id', 'Unknown')
            app_name = app_ids.get(str(app_id), "Unknown App")

            print(Fore.GREEN + "Session Valid | @{}".format(account_data.get('username', 'N/A')))
            print(Fore.GREEN + "Login from App ID - {} ({})".format(app_id, app_name))
            
            print(Fore.YELLOW + "\nAccount Info:")
            print("Name   - {}".format(account_data.get('name', 'N/A')))
            print("Email  - {}".format(account_data.get('email', 'N/A')))
            print("Mobile - {}".format(account_data.get('mobile', 'N/A')))
            print("UserID - {}".format(account_data.get('user_id', 'N/A')))
            print("AccountCreated - {}".format(datetime.datetime.fromtimestamp(account_data.get('user_create_time', 0)).strftime('%Y-%m-%d')))
        else:
            print(Fore.RED + "\nSession ID not valid/expired, please try again..")
            
    except Exception as e:
        print(Fore.RED + "\nAn error occurred: " + str(e))

banner()
session_id = input(Fore.CYAN + "[?] Session ID >>> " + Style.RESET_ALL)
info(session_id)
