import json,tarfile,os,subprocess,time,requests,shutil
if "portal2.exe" in os.listdir():
    shutil.rmtree("/portal2_tempcontent/")
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
        open("ppslice_temp.tar","wb").write(serverFile.content)
        file = tarfile.open("ppslice_temp.tar")
        file.extractall(path="/portal2_tempcontent/")
        file.close()
        os.remove("ppslice_temp.tar")
        subprocess.call("portal2.exe -novid -tempcontent")
else:
    print("Make sure this exe is in the same dir as your portal2.exe")
    time.sleep(3)