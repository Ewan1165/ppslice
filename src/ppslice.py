import json,tarfile,easygui,sys,os,shutil,subprocess,time,requests
print("Select your portal 2 install directory, if an error message appears, press ok and ignore it")
time.sleep(1.8)
p2dir = easygui.diropenbox()
packages = json.loads(requests.get("https://p2r3.com/spplice/packages",allow_redirects=True).content)
iCount = 1
print("0: Uninstall a mod")
for package in packages["packages"]:
    print(str(iCount) + ": " + package["title"])
    iCount += 1
modSelection = int(input("Select a mod: "))
if modSelection == 0:
    print("Uninstalled the mod!")
    exit()
else:
    modURL = "https://p2r3.com/spplice/packages/" + packages["packages"][modSelection-1]["name"] + "/" + packages["packages"][modSelection-1]["file"]
    serverFile = requests.get(modURL,allow_redirects=True)
    modArchive = open("ppslice_temp.tar","wb")
    modArchive.write(serverFile.content)
    extractedTar = tarfile.open("ppslice_temp.tar")
    extractedTar.extractall(path=p2dir + "\portal2_dlc3")