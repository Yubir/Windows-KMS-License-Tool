import tkinter as tk
import tkinter.messagebox as mbox
import ctypes
import webbrowser

import os

root = tk.Tk()
root.title("Windows KMS license Tool")
root.geometry("400x870")

# 배경색
root.configure(bg="#333333")

# 버튼 스타일 설정
button_style = {"font": ("Arial", 14),
                "bg": "#0066FF",
                "fg": "white",
                "activebackground": "#0047B3",
                "activeforeground": "white",
                "bd": 0,
                "highlightthickness": 0}

# 그 뒤 쓸 명령
def defualtset():
    os.system("slmgr /skms kms8.msguides.com")
    os.system("slmgr /ato")
    os.system("slmgr /xpr")

# Home
def home():
    os.system("slmgr /ipk TX9XD-98N7V-6WMQ6-BX7FG-H8Q99")
    defualtset()

# Home N
def homen():
    os.system("slmgr /ipk 3KHY7-WNT83-DGQKR-F7HPR-844BM")
    defualtset()

# Pro
def pro():
    os.system("slmgr /ipk W269N-WFGWX-YVC9B-4J6C9-T83GX")
    defualtset()

# Pro N
def pron():
    os.system("slmgr /ipk MH37W-N47XK-V7XM9-C7227-GCQG9")
    defualtset()

# Workstation Pro
def workpro():
    os.system("slmgr /ipk NRG8B-VKK3Q-CXVCJ-9G2XF-6Q84j")
    defualtset()

# Workstation Pro N
def workpron():
    os.system("slmgr /ipk 9FNH-K3HBT-3W4TD-6383H-6XYWF")
    defualtset()

# Education Pro
def proedu():
    os.system("slmgr /ipk 6TP4R-GNPTD-KYYHQ-7B7DP-J447y")
    defualtset()

# Education
def edu():
    os.system("slmgr /ipk NW6C2-QMPVW-D7KKK-3GKT6-VCFB2")
    defualtset()

# Education Pro N
def proedun():
    os.system("slmgr /ipk YVWGF-BXNMC-HTQYQ-CPQ99-66QFC")
    defualtset()

# Education N
def edun():
    os.system("slmgr /ipk 2WH4N-8QGBV-H22JP-CT43Q-MDWJ")
    defualtset()

# Enterprise
def enter():
    os.system("slmgr /ipk NPPR9-FWDCX-D2C8J-H872K-2YT43")
    defualtset()

# Enterprise N
def entern():
    os.system("slmgr /ipk DPH2V-TTNVB-4X9Q3-TJR4H-KHJW4")
    defualtset()

# Enterprise G
def enterg():
    os.system("slmgr /ipk YYVX9-NTFWV-6MDM3-9PT4T-4M68B")
    defualtset()

# Enterprise GN
def entergn():
    os.system("slmgr /ipk 44RPN-FTY23-9VTTB-MP9BX-T84FV")
    defualtset()

# 버튼 위젯 생성
button1 = tk.Button(root, text="Windows Home", command=home, **button_style)
button1.pack(pady=10)

button1 = tk.Button(root, text="Windows Home N", command=homen, **button_style)
button1.pack(pady=10)

button1 = tk.Button(root, text="Windows Pro", command=pro, **button_style)
button1.pack(pady=10)

button1 = tk.Button(root, text="Windows Pro N", command=pron, **button_style)
button1.pack(pady=10)

button1 = tk.Button(root, text="Windows Workstation Pro", command=workpro, **button_style)
button1.pack(pady=10)

button1 = tk.Button(root, text="Windows Workstation Pro N", command=workpron, **button_style)
button1.pack(pady=10)

button1 = tk.Button(root, text="Windows Education", command=edu, **button_style)
button1.pack(pady=10)

button1 = tk.Button(root, text="Windows Education N", command=edun, **button_style)
button1.pack(pady=10)

button1 = tk.Button(root, text="Windows Education Pro", command=proedu, **button_style)
button1.pack(pady=10)

button1 = tk.Button(root, text="Windows Education Pro N", command=proedun, **button_style)
button1.pack(pady=10)

button1 = tk.Button(root, text="Windows Enterprise", command=enter, **button_style)
button1.pack(pady=10)

button1 = tk.Button(root, text="Windows Enterprise G", command=enterg, **button_style)
button1.pack(pady=10)

button1 = tk.Button(root, text="Windows Enterprise GN", command=entergn, **button_style)
button1.pack(pady=10)

button1 = tk.Button(root, text="Windows Enterprise N", command=entern, **button_style)
button1.pack(pady=10)

# 프로그램 정보 표시 라벨
label1 = tk.Label(root, text="Windows KMS License Tool", font=("Arial", 18), fg="white", bg="#333333")
label1.pack(side=tk.TOP, pady=(20,0))

label2 = tk.Label(root, text="Version 1.0", font=("Arial", 12), fg="white", bg="#333333")
label2.pack(side=tk.TOP, pady=(5,0))

def open_link():
    webbrowser.open_new("https://github.com/yubir")
label3 = tk.Label(root, text="Make / By. Yubir", font=("Arial", 18), fg="blue", cursor="hand2")
label3.pack(pady=10)
label3.bind("<Button-1>", lambda e: open_link())



# 현재 프로세스가 관리자 권한을 가지고 있는지 확인하기
def is_admin():
    try:
        return ctypes.windll.shell32.IsUserAnAdmin()
    except:
        return False

if not is_admin():
    ctypes.windll.user32.MessageBoxW(None, "Run as Administrator.", "Error", 0x10)
    sys.exit()

# 윈도우 루프
root.mainloop()
