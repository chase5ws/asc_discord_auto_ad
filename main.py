import requests
import json
import random
import time


#載入文本套件
import openpyxl
#載入上線
import keep_alive
keep_alive.keep_alive()

#這個主要是選擇在哪個頻道上說話
def chat(chanel_list, authorization_list, get_context):
  for authorization in authorization_list:
    header = {
        "Authorization":
        authorization,
        "Content-Type":
        "application/json",
        "User-Agent":
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/94.0.4606.61 Safari/537.36",
    }
    for chanel_id in chanel_list:
      msg = {
          "content": get_context,
          "nonce": "82329451214{}33232234".format(random.randrange(0, 1000)),
          "tts": False,
      }
      url = "https://discord.com/api/v9/channels/{}/messages".format(chanel_id)
      try:
        res = requests.post(url=url, headers=header, data=json.dumps(msg))
        print(res.content)
      except:
        pass
      continue
    time.sleep(random.randrange(1, 3))

#主程式
if __name__ == "__main__":
  #這個可以在Discord頻道上，電腦右鍵或手機長按頻道，複製ID後貼上
  chanel_list = [
      1119322738348273674,977539033188159498,997878783900131431,955745340638785566,943101492032835604,1011967814736818217,
      986193039485718548,1090798128304758885,932309061679087617,947188908645572729,932516183326998598,947189146718445580,
      922900609231888454,939138289460445224,1103250255761387600,1158538174675570698
  ]  #頻道右鍵-複製連結-複製最後一段數字
  #首次取得Code建議先在電腦上找
  authorization_list = [
      "OTI2ODY1MDU2NzMyNDIyMTU0.GDMwsK.TaqSneGU7v_tIE8n5SvvLgPpSN5i9r9eC0SH-Q"
  ]  #F12-搜尋science-複製Authorization
    #文檔名稱-dc_context.xlsx
  wb = openpyxl.load_workbook('dc_context.xlsx', data_only=True)
  #Excel的sheet名稱
  sheet = wb['工作表1'] 
  # 取出1x1000格內容(一欄1000列，直欄橫列)
  while  True:
    for i in sheet.iter_cols(min_row=1, min_col=1, max_col=1, max_row=1000):
        for j in i:
            ex_data = j.value
            chat(chanel_list, authorization_list, ex_data)
            #這邊是間隔時間，以秒作單位，1小時即3600秒
            #這句意思是從3600秒到3660秒之間隨機選一個秒數作間隔，一般看頻道設定去作改變
            #sleeptime = random.randrange(3600, 3660)
            #固定1秒就寫1
            time.sleep(60)  
            #這句是執行上一句選到的時間
    time.sleep(3600)

