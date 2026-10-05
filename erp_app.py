import webview

SERVER_URL = "https://endolax.online/index.html"
APP_UA = "EndolaxERP-Desktop/1.0 key=YOUR_SECRET"

webview.create_window("Endolax Biomedical ERP", SERVER_URL, width=1400, height=850)
webview.start(user_agent=APP_UA)