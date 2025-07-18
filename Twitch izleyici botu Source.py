import tkinter as tk
import customtkinter as ctk
from tkinter import messagebox
import threading, random, time, webbrowser, requests
from PIL import Image, ImageTk, ImageSequence
from io import BytesIO
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")


class ToprakChatBot:
    def __init__(self):
        self.root = ctk.CTk()
        self.root.title("✨ Toprak İzleyici Botu")
        self.root.geometry("900x650")
        self.driver = None

        self.theme_colors = ["#FF6B6B", "#4ECDC4", "#45B7D1", "#FFEAA7", "#DDA0DD", "#F7DC6F", "#98D8C8"]
        self.proxy_list = [
            "https://www.blockaway.net",
            "https://www.croxyproxy.com",
            "https://www.croxyproxy.rocks",
            "https://www.croxy.network",
            "https://www.croxy.org",
            "https://www.youtubeunblocked.live"
        ]

        self.refresh_seconds = 180
        self.gif_frames = []
        self.gif_index = 0
        self.gif_running = True

        self.build_ui()
        self.animate_gif()
        self.root.mainloop()

    def build_ui(self):
        self.frame = ctk.CTkFrame(self.root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        self.gif_label = tk.Label(master=self.root, bd=0, bg="#242424")
        self.gif_label.place(relx=0.5, y=20, anchor="n")

        gif_url = "https://media3.giphy.com/media/v1.Y2lkPTc5MGI3NjExOGZod2NrenNxbTVkbzVwMzFmdHNweGl6MzVraGsxanV0OTJtc2FhdyZlcD12MV9pbnRlcm5hbF9naWZfYnlfaWQmY3Q9cw/nvnCtgFUPvXS9MELci/giphy.gif"
        gif_data = requests.get(gif_url).content
        gif_image = Image.open(BytesIO(gif_data))
        self.gif_frames = [ImageTk.PhotoImage(frame.copy().resize((80, 80))) for frame in ImageSequence.Iterator(gif_image)]

        self.title_label = ctk.CTkLabel(self.frame, text="Toprak İzleyici Botu", font=ctk.CTkFont(size=28, weight="bold"))
        self.title_label.pack(pady=(100, 5))

        self.channel_entry = self.create_entry("Kanal Adı (örnek: ishowspeed)")
        self.viewer_entry = self.create_entry("İzleyici Sayısı", "5")

        self.proxy_var = ctk.StringVar(value="Rastgele Proxy")
        self.proxy_container = ctk.CTkFrame(self.frame, fg_color="transparent")
        self.proxy_container.pack(pady=5)
        self.proxy_menu = ctk.CTkOptionMenu(self.proxy_container, variable=self.proxy_var,
                                            values=["Rastgele Proxy"] + self.proxy_list,
                                            width=400)
        self.proxy_menu.pack()

        self.show_tabs = ctk.BooleanVar(value=False)
        self.tab_checkbox = ctk.CTkCheckBox(self.frame, text="🖥️ Sekmeleri Göster", variable=self.show_tabs)
        self.tab_checkbox.pack(pady=5)

        self.refresh_enabled = ctk.BooleanVar(value=True)
        self.refresh_checkbox = ctk.CTkCheckBox(self.frame, text="🔁 Sekmeleri 3 dakikada bir yenile", variable=self.refresh_enabled)
        self.refresh_checkbox.pack(pady=5)

        self.refresh_label = ctk.CTkLabel(self.frame, text="")
        self.refresh_label.pack(pady=5)

        button_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        button_frame.pack(pady=10)

        self.start_btn = ctk.CTkButton(button_frame, text="🚀 Gönder", command=self.start_bot, width=180)
        self.start_btn.pack(side="left", padx=10)

        self.stop_btn = ctk.CTkButton(button_frame, text="✖ Durdur", command=self.stop_bot, state="disabled", width=120)
        self.stop_btn.pack(side="left", padx=10)

        self.github_btn = ctk.CTkButton(self.frame, text="🌐 GitHub",
                                        command=lambda: webbrowser.open("https://github.com/toprak1224"))
        self.github_btn.pack(pady=5)

        color_frame = ctk.CTkFrame(self.frame, fg_color="transparent")
        color_frame.pack(pady=10)
        for color in self.theme_colors:
            btn = ctk.CTkButton(color_frame, text="", width=25, height=25,
                                fg_color=color, corner_radius=12,
                                command=lambda c=color: self.set_theme(c))
            btn.pack(side="left", padx=4)

        self.status_label = ctk.CTkLabel(self.frame, text="", text_color="lightgreen")
        self.status_label.pack(pady=5)

        self.signature = ctk.CTkLabel(self.root, text="✨ Coded by Toprak", text_color="gray")
        self.signature.place(relx=1.0, rely=1.0, anchor="se", x=-10, y=-10)

    def create_entry(self, label, default=""):
        ctk.CTkLabel(self.frame, text=label, anchor="w").pack(pady=(10, 0), fill="x")
        entry = ctk.CTkEntry(self.frame)
        entry.insert(0, default)
        entry.pack(fill="x", pady=5)
        return entry

    def animate_gif(self):
        if self.gif_frames:
            frame = self.gif_frames[self.gif_index]
            self.gif_label.configure(image=frame)
            self.gif_index = (self.gif_index + 1) % len(self.gif_frames)
        self.root.after(80, self.animate_gif)

    def set_theme(self, color):
        self.title_label.configure(text_color=color)
        self.status_label.configure(text_color=color)
        self.signature.configure(text_color=color)
        self.start_btn.configure(fg_color=color, hover_color=color, text_color="black")
        self.stop_btn.configure(fg_color=color, hover_color=color, text_color="black")
        self.github_btn.configure(fg_color=color, hover_color=color, text_color="black")

        try:
            self.proxy_menu.configure(
                fg_color=color,
                button_color=color,
                text_color="black",
                dropdown_fg_color=color,
                dropdown_hover_color=color
            )
        except:
            old_value = self.proxy_var.get()
            self.proxy_menu.destroy()
            self.proxy_menu = ctk.CTkOptionMenu(self.proxy_container,
                                                variable=self.proxy_var,
                                                values=["Rastgele Proxy"] + self.proxy_list,
                                                fg_color=color,
                                                button_color=color,
                                                text_color="black",
                                                dropdown_fg_color=color,
                                                dropdown_hover_color=color,
                                                width=400)
            self.proxy_menu.set(old_value)
            self.proxy_menu.pack()

    def start_bot(self):
        channel = self.channel_entry.get().strip()
        try:
            count = int(self.viewer_entry.get().strip())
        except:
            messagebox.showerror("Hata", "İzleyici sayısı geçerli değil.")
            return

        if not channel:
            messagebox.showerror("Hata", "Kanal adı boş olamaz.")
            return

        self.status_label.configure(text="Bot başlatılıyor...")
        self.start_btn.configure(state="disabled")
        self.stop_btn.configure(state="normal")

        use_random = self.proxy_var.get() == "Rastgele Proxy"
        base_proxy = None if use_random else self.proxy_var.get()

        threading.Thread(target=self.run_bot, args=(channel, count, base_proxy, use_random), daemon=True).start()

    def run_bot(self, channel, count, base_proxy, use_random):
        try:
            options = webdriver.ChromeOptions()
            if not self.show_tabs.get():
                options.add_argument('--headless')
            options.add_argument('--disable-dev-shm-usage')
            options.add_argument('--mute-audio')
            options.add_experimental_option('excludeSwitches', ['enable-logging'])

            self.driver = webdriver.Chrome(options=options)
            self.driver.get(base_proxy or random.choice(self.proxy_list))

            for _ in range(count):
                proxy = random.choice(self.proxy_list) if use_random else base_proxy
                self.driver.execute_script(f"window.open('{proxy}')")
                self.driver.switch_to.window(self.driver.window_handles[-1])
                time.sleep(0.5)
                try:
                    box = self.driver.find_element(By.ID, 'url')
                    box.send_keys(f"https://www.twitch.tv/{channel}")
                    box.send_keys(Keys.RETURN)
                except:
                    pass

            self.status_label.configure(text=f"{count} izleyici gönderildi.")

            if self.refresh_enabled.get():
                threading.Thread(target=self.refresh_loop, daemon=True).start()

        except Exception as e:
            self.status_label.configure(text="Hata: " + str(e))
        finally:
            self.start_btn.configure(state="normal")
            self.stop_btn.configure(state="disabled")

    def refresh_loop(self):
        while self.driver:
            for i in range(self.refresh_seconds, 0, -1):
                if not self.driver:
                    return
                self.refresh_label.configure(text=f"Yenilemeye kalan süre: {i} saniye")
                time.sleep(1)
            try:
                for handle in self.driver.window_handles:
                    self.driver.switch_to.window(handle)
                    self.driver.refresh()
                self.status_label.configure(text="Sekmeler yenilendi.")
            except Exception as e:
                self.status_label.configure(text=f"Yenileme hatası: {e}")

    def stop_bot(self):
        if self.driver:
            self.driver.quit()
            self.driver = None
            self.status_label.configure(text="Bot durduruldu.")
        self.start_btn.configure(state="normal")
        self.stop_btn.configure(state="disabled")
        self.refresh_label.configure(text="")

if __name__ == "__main__":
    ToprakChatBot()
