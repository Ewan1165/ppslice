import requests as r
import json,tarfile,easygui,sys,os,shutil,subprocess,time

logo = """
██████╗ ██████╗     ███████╗██╗     ██╗ ██████╗███████╗
██╔══██╗██╔══██╗    ██╔════╝██║     ██║██╔════╝██╔════╝
██████╔╝██████╔╝    ███████╗██║     ██║██║     █████╗  
██╔═══╝ ██╔═══╝     ╚════██║██║     ██║██║     ██╔══╝  
██║     ██║         ███████║███████╗██║╚██████╗███████╗
╚═╝     ╚═╝         ╚══════╝╚══════╝╚═╝ ╚═════╝╚══════╝
"""

print(logo)
print("Select your portal 2 install directory, if an error message appears, press ok and ignore it")
print("If you have anything in dlc3, it will be moved to dlc3_backup")
time.sleep(3)
pathinput = easygui.diropenbox()
if pathinput == "None":
    sys.exit()
path = pathinput+r"\portal2_dlc3"
try:
    shutil.rmtree(path)
except:
    pass
rJson = json.loads(r.get("https://p2r3.com/spplice/packages",allow_redirects=True).content)
for i in range(len(rJson["packages"])):
    print(str(i+1) + ": " + rJson["packages"][i]["title"])
selection = int(input("Choose one (enter 0 to uninstall a mod): "))
if selection == 0:
    print("Uninstalled the mod!")
else:
    url = "https://p2r3.com/spplice/packages/" + rJson["packages"][selection-1]["name"] + "/" + rJson["packages"][selection-1]["file"]
    r = r.get(url,allow_redirects=True)
    open("slice_temp.tar","wb").write(r.content)
    file = tarfile.open("slice_temp.tar")
    file.extractall(path=path)
    file.close()
    os.remove("slice_temp.tar")
    print("Restart your game")
