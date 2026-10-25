import tkinter as tk
import random
import time
import os
import sys
import platform
import datetime

FAKE_LINK = "https://WeWillHackYouNowIfYouDontWantToBeHackedGiveUsBitcoin.corm"
HACK_TEXT = "HACKLENDİNİZ!"

def get_system_info():
    info = []
    info.append("=== SİSTEM BİLGİLERİ ===")
    info.append(f"Tarih: {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    info.append(f"İşletim Sistemi: {platform.system()} {platform.release()}")
    info.append(f"Sürüm: {platform.version()}")
    info.append(f"Mimari: {platform.machine()}")
    info.append(f"İşlemci: {platform.processor()}")
    info.append(f"Python Sürümü: {sys.version}")
    info.append(f"Bilgisayar Adı: {os.getenv('COMPUTERNAME', 'Bilinmiyor')}")
    info.append(f"Kullanıcı: {os.getenv('USERNAME', 'Bilinmiyor')}")
    info.append("")
    info.append("Not: Bu dosya sadece bir şaka/simülasyondur.")
    info.append("Gerçek bir hack işlemi yapılmamıştır.")
    return "\n".join(info)

def start_matrix():
    root = tk.Tk()
    root.title("SİSTEM ÇÖKTÜ")
    root.configure(bg="black")
    root.attributes("-fullscreen", True)
    
    canvas = tk.Canvas(root, bg="black", highlightthickness=0)
    canvas.pack(fill="both", expand=True)
    
    width = root.winfo_screenwidth()
    height = root.winfo_screenheight()
    
    font_size = 16
    columns = width // font_size
    drops = [random.randint(-height, 0) for _ in range(columns)]
    
    start_time = time.time()
    
    def draw():
        canvas.delete("all")
        for i in range(columns):
            x = i * font_size
            y = drops[i]
            char = random.choice("01")
            canvas.create_text(x, y, text=char, fill="#00ff00", font=("Consolas", font_size, "bold"))
            drops[i] += random.randint(10, 20)
            if drops[i] > height:
                drops[i] = random.randint(-200, 0)
        
        if time.time() - start_time > 5:
            root.destroy()
            create_txt_file()
        else:
            root.after(50, draw)
    
    draw()
    root.mainloop()

def create_txt_file():
    masaustu = os.path.join(os.path.expanduser("~"), "Desktop")
    dosya_yolu = os.path.join(masaustu, "HACKLENDINIZ.txt")
    
    with open(dosya_yolu, "w", encoding="utf-8") as f:
        f.write(HACK_TEXT + "\n\n")
        f.write(get_system_info())
    
    print(f"Dosya oluşturuldu: {dosya_yolu}")

def open_fake_link():
    print(f"Sahte link açılıyor: {FAKE_LINK}")
    start_matrix()

def main():
    root = tk.Tk()
    root.title("Sistem Uyarısı...")
    root.geometry("600x350")
    root.config(bg="#220000")
    
    label = tk.Label(
        root,
        text="⚠️ SİSTEM UYARISI ⚠️\n\nBilgisayarınız 24 saat sonra hacklenecektir.\nLütfen zamanınızı iyi kullanın.",
        bg="#220000", fg="red", font=("Consolas", 12, "bold"), justify="center"
    )
    label.pack(pady=30)
    
    link_btn = tk.Button(
        root,
        text="Detaylar için buraya tıklayın",
        command=open_fake_link,
        bg="#220000", fg="#00ff00", font=("Consolas", 10, "underline"),
        relief="flat", cursor="hand2", activebackground="#220000", activeforeground="#00ff00"
    )
    link_btn.pack(pady=10)
    
    def kapat():
        root.destroy()
    
    buton = tk.Button(
        root, text="TAMAM", command=kapat,
        bg="#550000", fg="white", font=("Consolas", 12, "bold")
    )
    buton.pack(pady=20)
    
    root.mainloop()

if __name__ == "__main__":
    main()