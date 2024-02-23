import vk_api
import random
from colorama import Fore
from config import APP_ID

from take_screenshots import take_screenshots

FORCE_QUIT = False  # Quit if unknown error has occurred
MESSAGES = []


# Randomly change cyrillic characters to latin to avoid detection in VK
def Obfuscate(msg):
    if random.getrandbits(1):
        msg = msg.replace('о', 'o')
    if random.getrandbits(1):
        msg = msg.replace('е', 'e')

    return msg


# Get list of messages to post on
def GetAllMessage(file):
    global MESSAGES
    with open(file, 'r', encoding='utf-8') as file:
        for line in file:
            MESSAGES.append(line.strip())


# Get random message
def GetMessage():
    global MESSAGES
    return Obfuscate(random.choice(MESSAGES))


# Get list of target links to post on
def GetLinks(file):
    with open(file) as links:
        return links.read().split()


# Convert link to post to ID
def LinkToID(link):
    return link.split("wall")[-1].split('_')


# Captcha solver
def SolveCaptcha(c):
    print(Fore.RED + "[!] Captcha needed:", c.get_url())
    key = input(Fore.GREEN + "[>] Please enter the code: ")
    return c.try_again(key)


def main():
    SUCCESS = 0
    global MESSAGES
    global FORCE_QUIT
    print(Fore.CYAN + "VK Commenter\n")

    links = GetLinks("links.txt")
    login = input("Login: ")
    password = input("Password: ")
    GetAllMessage("messages.txt")

    vk_session = vk_api.VkApi(login=login, password=password, app_id=APP_ID, captcha_handler=SolveCaptcha)
    vk_session.auth()

    vk = vk_session.get_api()

    print(Fore.GREEN + "[?] Login successful")

    for link in links:
        ids = LinkToID(link)
        try:
            vk.wall.createComment(owner_id=ids[0], post_id=ids[1], message=GetMessage())
        except Exception as e:
            if "parent deleted" in str(e).lower():
                print(Fore.RED + f"[-] {e} ({link})")
            else:
                print(Fore.RED + f"[-] {e} ({link})")
                if FORCE_QUIT:
                    exit()
        else:
            print(Fore.GREEN + "[+] Posted on", link)
            take_screenshots(link)
            print(Fore.MAGENTA + "[+] Screenshot saved", link)
    else:
        print(Fore.YELLOW + f"[!] Posted: {SUCCESS}")


if __name__ == "__main__":
    main()