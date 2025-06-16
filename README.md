### discord自動發言廣告
![version](https://img.shields.io/badge/version-1.0.0-blue)
![license](https://img.shields.io/badge/license-MIT-green)
![python](https://img.shields.io/badge/python-3.8+-yellow)
![GitHub issues](https://img.shields.io/github/issues/chase5ws/asc_discord_auto_ad)
![GitHub stars](https://img.shields.io/github/stars/chase5ws/asc_discord_auto_ad)
![GitHub forks](https://img.shields.io/github/forks/chase5ws/asc_discord_auto_ad)
![icon](asset/icon.png)

---
* 這教學文篇是講述我用雲端code託管教學透過Py網頁端驅動discord傳送訊息
[(上)學習教材](https://www.linkedin.com/pulse/part1-py%25E7%25B6%25B2%25E9%25A0%2581%25E7%25AB%25AF%25E9%25A9%2585%25E5%258B%2595discord%25E5%2582%25B3%25E9%2580%2581%25E8%25A8%258A%25E6%2581%25AF%25E5%2590%25AB%25E9%259B%25B2%25E7%25AB%25AFcode%25E8%25A8%2597%25E7%25AE%25A1%25E6%2595%2599%25E5%25AD%25B8-yang-tseng-5eqne/)、[(下)學習教材](https://www.linkedin.com/pulse/%E4%B8%8Bpy%E7%B6%B2%E9%A0%81%E7%AB%AF%E9%A9%85%E5%8B%95discord%E5%82%B3%E9%80%81%E8%A8%8A%E6%81%AF%E5%90%AB%E9%9B%B2%E7%AB%AFcode%E8%A8%97%E7%AE%A1%E6%95%99%E5%AD%B8-yang-tseng-oqgne/?trackingId=GPU1Ug9skOF5nNYya0NkUg%3D%3D)

---
### 專案簡介

在 Discord 上，許多伺服器都會設立「分享頻道」，讓大家可以宣傳自己的群組或各種資源。這樣的「免費廣告」方式不僅受到許多伺服器管理員的歡迎，有時也成為友善群組間互動的一種象徵。

有趣的是，我發現有些 Discord 群組甚至設有「公關」職位，而這些公關的考核標準之一，就是必須透過這種分享群組的方式來吸引新成員，才能順利轉正。雖然聽起來有點不可思議，但這確實是目前不少社群的現實情況。

本專案的主題，就是希望能自動化這一流程。這次我學習並運用了 `openpyxl` 這個 Python 套件，來讀取 Excel 檔案，將檔案中的訊息載入程式，並在指定時間於 Discord 頻道自動發送。這樣不但可以節省大量人工操作時間，也讓分享流程變得更有效率、更有條理。

---

### 技術重點

- 使用 `openpyxl` 讀取 Excel 檔案，彈性管理分享內容
- 支援定時自動發言，方便雲端主機 24 小時運作
- 適合 Discord 公關、管理員、或任何需要自動分享資訊的場合

---