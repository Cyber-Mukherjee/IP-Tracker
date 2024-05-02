import requests
import json
import time

class Data:
    def __init__(self, city, region, country, loc, org, postal, timezone):
        self.city = city
        self.region = region
        self.country = country
        self.loc = loc
        self.org = org
        self.postal = postal
        self.timezone = timezone

def main():
    print("\nIP Tracker by Cyber-Mukherjee")
    print("Disclaimer: Any unauthorised use of this program is strictly prohibited. \n ")
    
    while True:
        ip = input("Please enter the IP Address: ")
        url = f"https://ipinfo.io/{ip}/json"
        try:
            response = requests.get(url)
            response.raise_for_status()

            print("\n[+] Request successfully made")
            time.sleep(1.5)

            responseData = response.json()

            ipInfo = Data(
                responseData.get('city'),
                responseData.get('region'),
                responseData.get('country'),
                responseData.get('loc'),
                responseData.get('org'),
                responseData.get('postal'),
                responseData.get('timezone')
            )

            print("\n")
            print(" Country:", ipInfo.country)
            print(" Region:", ipInfo.region)
            print(" City:", ipInfo.city)
            print(" PIN:", ipInfo.postal)
            print(" Coordinates:", ipInfo.loc)
            print(" Timezone:", ipInfo.timezone)
            print(" Organization:", ipInfo.org)

            coords = ipInfo.loc.split(',')
            print(f" Maps: https://www.google.com/maps/?q={coords[0]},{coords[1]}")
            print("\n[*] Note: Use the information responsibly! \n")
            
            # Menu-driven approach
            while True:
                choice = input("Track another IP Address? (0 - No, 1 - Yes): ")
                if choice == '0':
                    print("Thank you!")
                    return
                elif choice == '1':
                    break
                else:
                    print("Invalid choice. Please enter 0 or 1.")
                    
        except requests.exceptions.RequestException as ex:
            print(f" [x] Error: Unable to track \"{ip}\" \n Please re-enter a valid IP Address")

if __name__ == "__main__":
    main()