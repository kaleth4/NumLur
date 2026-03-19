import re
import platform
import os
import sys
import requests
import webbrowser
from colorama import Fore, Style, init

init(autoreset=True)

# =========================
# CONFIGURACIÓN
# =========================
API_URL = "https://api.apilayer.com/number_verification/validate?number="
API_KEY = "TU_API_KEY_AQUI"  # <-- reemplazar

# =========================
# BANNER
# =========================
BANNER = r"""
************************************
*        ___   _                   *
*       / / \ | |_   _ _ __ __     *
*      | ||  \| | | | | '_ ` _     *
*     < < | |\  | |_| | | | | | \  *
*      | ||_| \_|\__,_|_| |_| |_|  *
*       \_\                        *
*                                  *                                
*                                  *
************************************
"""

# =========================
# FUNCIONES
# =========================
def clear_screen():
    os.system("cls" if platform.system() == "Windows" else "clear")

def is_valid_mobile_number(number):
    number = number.replace(" ", "").replace("-", "")
    return re.fullmatch(r"\d{10,15}", number) is not None

def consultar_numero():
    number = input(Fore.GREEN + "\n[+] Enter Mobile Number: ").strip()

    if not is_valid_mobile_number(number):
        print(Fore.RED + "[!] Invalid Mobile Number")
        return

    url = f"{API_URL}{number}"
    headers = {"apikey": API_KEY}

    try:
        response = requests.get(url, headers=headers, timeout=10)

        if response.status_code != 200:
            print(Fore.RED + f"[!] Error HTTP: {response.status_code}")
            return

        data = response.json()

        print(Fore.CYAN + "\n[+] Result:\n")
        print(f"Country code        : {data.get('country_code')}")
        print(f"Number              : {data.get('number')}")
        print(f"Country name        : {data.get('country_name')}")
        print(f"Country prefix      : {data.get('country_prefix')}")
        print(f"International format: {data.get('international_format')}")
        print(f"Line type           : {data.get('line_type')}")
        print(f"Local format        : {data.get('local_format')}")
        print(f"Location            : {data.get('location')}")
        print(f"Valid               : {data.get('valid')}")

    except requests.exceptions.RequestException as e:
        print(Fore.RED + f"[!] Network error: {e}")

def abrir_whatsapp():
    number = input(Fore.GREEN + "\n[+] Enter Mobile Number: ").strip()

    if not is_valid_mobile_number(number):
        print(Fore.RED + "[!] Invalid Mobile Number")
        return

    url = f"https://api.whatsapp.com/send?phone={number}"
    print(Fore.YELLOW + f"[+] Opening: {url}")
    webbrowser.open(url)

def mostrar_menu():
    print(Fore.YELLOW + BANNER)
    print(Fore.GREEN + "1) Consultar número")
    print("2) Abrir chat en WhatsApp")
    print("3) Salir")

# =========================
# MAIN
# =========================
def main():
    while True:
        try:
            clear_screen()
            mostrar_menu()

            opcion = input(Fore.CYAN + "\n[+] Select option: ").strip()

            if opcion == "1":
                consultar_numero()
            elif opcion == "2":
                abrir_whatsapp()
            elif opcion == "3":
                print(Fore.YELLOW + "\n[+] Bye!")
                sys.exit()
            else:
                print(Fore.RED + "[!] Invalid option")

            input(Fore.MAGENTA + "\nPress ENTER to continue...")

        except KeyboardInterrupt:
            print(Fore.RED + "\n[!] Interrupted by user")
            sys.exit()

if __name__ == "__main__":
    main()