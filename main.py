import requests
import json
#from time import sleep
#from tqdm import tqdm
import webbrowser

print(r"""\

 .--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--.
/ .. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \.. \..  \.. \.. \.. \.. \.. \
\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/ \/\ \/\ \/\ \/\ \/\ \/\ 
 \/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\// / /
 / /\/ /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`' /`'/\/ /
/ /\ \/`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'--'`--'`--'`--'`--'`--/ /\ \
\/ /\ \                                                          -ARBOFF 2021   / /\/ /
 / /\/ /  ██████╗ ██╗   ██╗██████╗  █████╗ ███████╗███████╗███╗   ███╗███████╗  \ \/ /\
/ /\ \/   ██╔══██╗╚██╗ ██╔╝██╔══██╗██╔══██╗██╔════╝██╔════╝████╗ ████║██╔════╝   \ \/\ \
\ \/\ \   ██████╔╝ ╚████╔╝ ██████╔╝███████║███████╗███████╗██╔████╔██║█████╗     /\ \/ /
 \/ /\ \  ██╔══██╗  ╚██╔╝  ██╔═══╝ ██╔══██║╚════██║╚════██║██║╚██╔╝██║██╔══╝     / /\/ /
 / /\/ /  ██████╔╝   ██║   ██║     ██║  ██║███████║███████║██║ ╚═╝ ██║███████    \ \/ /\
/ /\ \/   ╚═════╝    ╚═╝   ╚═╝     ╚═╝  ╚═╝╚══════╝╚══════╝╚═╝     ╚═╝╚══════╝    \ \/\ \
\ \/\ \.--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--..--/\ \/ /
 \/ /\/ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ../ ..//\/ /
 / /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /\/ /
/ /\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \/\ \ \/\ \ \/\ \ \/\ \ \/\ 
\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `'\ `' \ `'\ `'\ `'\ `'\ `'\ /
 `--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'`--'--'--'--'--'--'--'--'--'


            """)


while True:
    missing = input("Paste LINKVERTISE link: ")

    bypassURL = "https://bypass.bot.nu/bypass2?" + missing


    params = {'url': missing}

    r = requests.get(bypassURL, params=params)
    jjson = r.json()

    #for i in tqdm(range(10)):
    #    sleep(0.1)

    print("")
    print("")
    try:
        print("LINK: " + jjson['destination'])
        target = str(jjson['destination'])
        input("Press any key...")
        #webbrowser.get("google-chrome").open(target)
        break
    except KeyError:
        print("Invalid Link // Bad Request")
        input("Press any key...")