import tkinter as tk
from tkinter import messagebox, scrolledtext, ttk
import requests
import json
import random
import threading
import time
import os

CONFIG_FILE = "discord_sender_config.json"
stop_flag = threading.Event()

def save_config(channels, token, interval, messages):
    config = {
        "channels": channels,
        "token": token,
        "interval": interval,
        "messages": messages
    }
    with open(CONFIG_FILE, "w", encoding="utf-8") as f:
        json.dump(config, f, ensure_ascii=False, indent=2)

def load_config():
    if not os.path.exists(CONFIG_FILE):
        return "", "", "5", ""
    with open(CONFIG_FILE, "r", encoding="utf-8") as f:
        config = json.load(f)
        return (
            config.get("channels", ""),
            config.get("token", ""),
            str(config.get("interval", "5")),
            config.get("messages", "")
        )

def send_message(channel_id, token, content):
    url = f"https://discord.com/api/v9/channels/{channel_id}/messages"
    headers = {
        "Authorization": token,
        "Content-Type": "application/json",
        "User-Agent": "Mozilla/5.0",
    }
    msg = {
        "content": content,
        "nonce": str(random.randint(100000000000000000, 999999999999999999)),
        "tts": False,
    }
    try:
        res = requests.post(url, headers=headers, data=json.dumps(msg))
        print(f"發送到頻道 {channel_id}，回應：{res.status_code}")
        return res.status_code in (200, 204)
    except Exception as e:
        print(f"發送失敗：{e}")
        return False

def start_sending():
    stop_flag.clear()
    channel_ids = entry_channels.get().replace('，', ',').split(',')
    channel_ids = [cid.strip() for cid in channel_ids if cid.strip()]
    token = entry_token.get().strip()
    interval = int(combo_interval.get())
    messages = text_messages.get("1.0", tk.END).strip().split('\n')
    messages = [m.strip() for m in messages if m.strip()]
    if not channel_ids or not token or not messages:
        messagebox.showerror("錯誤", "請確認所有欄位都已正確填寫")
        return
    # 儲存設定
    save_config(entry_channels.get(), token, interval, text_messages.get("1.0", tk.END).strip())
    btn_start.config(state=tk.DISABLED)
    btn_stop.config(state=tk.NORMAL)
    def loop_send():
        while not stop_flag.is_set():
            content = random.choice(messages)
            for cid in channel_ids:
                send_message(cid, token, content)
            for _ in range(interval):
                if stop_flag.is_set():
                    break
                time.sleep(1)
        btn_start.config(state=tk.NORMAL)
        btn_stop.config(state=tk.DISABLED)
    threading.Thread(target=loop_send, daemon=True).start()
    messagebox.showinfo("啟動", "自動發言已啟動！")

def stop_sending():
    stop_flag.set()
    btn_start.config(state=tk.NORMAL)
    btn_stop.config(state=tk.DISABLED)
    messagebox.showinfo("停止", "自動發言已停止！")

def format_program():
    # 清空所有欄位
    entry_channels.delete(0, tk.END)
    entry_token.delete(0, tk.END)
    combo_interval.set("5")
    text_messages.delete("1.0", tk.END)
    # 刪除本地設定檔
    if os.path.exists(CONFIG_FILE):
        try:
            os.remove(CONFIG_FILE)
        except Exception as e:
            messagebox.showerror("錯誤", f"刪除設定檔失敗：{e}")
            return
    messagebox.showinfo("格式化", "所有資料已清除！")

# UI設計
root = tk.Tk()
root.title("Discord自動發言機")

# 載入上次參數
last_channels, last_token, last_interval, last_messages = load_config()

tk.Label(root, text="頻道ID（可多個，用逗號分隔）:").grid(row=0, column=0, sticky='e')
entry_channels = tk.Entry(root, width=50)
entry_channels.grid(row=0, column=1)
entry_channels.insert(0, last_channels)

tk.Label(root, text="TOKEN:").grid(row=1, column=0, sticky='e')
entry_token = tk.Entry(root, width=50, show="*")
entry_token.grid(row=1, column=1)
entry_token.insert(0, last_token)

tk.Label(root, text="發言間隔秒數:").grid(row=2, column=0, sticky='e')
combo_interval = ttk.Combobox(root, values=["1", "5", "10", "30", "60"], width=10, state="readonly")
combo_interval.grid(row=2, column=1, sticky='w')
combo_interval.set(last_interval if last_interval in ["1","5","10","30","60"] else "5")

tk.Label(root, text="發言內容（每行一則）:").grid(row=3, column=0, sticky='ne')
text_messages = scrolledtext.ScrolledText(root, width=50, height=8)
text_messages.grid(row=3, column=1)
text_messages.insert(tk.END, last_messages)

btn_start = tk.Button(root, text="啟動自動發言", command=start_sending)
btn_start.grid(row=4, column=0, pady=10)

btn_stop = tk.Button(root, text="停止自動發言", command=stop_sending, state=tk.DISABLED)
btn_stop.grid(row=4, column=1, pady=10, sticky='w')

btn_format = tk.Button(root, text="格式化程式（清除所有資料）", command=format_program, fg="red")
btn_format.grid(row=5, column=0, columnspan=2, pady=10)

root.mainloop()
