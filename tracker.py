import requests
import os

#سحب المتغيرات السرية بأمان من خوادم جيت هاب أثناء التشغيل 
BOT_TOKEN = os.environ.get("TELEGRAM_BOT_TOKEN")
CHAT_ID = os.environ.get("TELEGRAM_CHAT_ID")

STATUS_FILE = "last_status.txt"

def send_telegram_message(message):
    if not BOT_TOKEN or not CHAT_ID:
        print("❌ خطأ: المتغيرات السرية غير معرفة في إعدادات GitHub Secrets!")
        return
    
    url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, json=payload)
        if response.status_code == 200:
            print("📦 تم إرسال الإشعار لتليجرام بنجاح!")
        else:
            print(f"❌ خطأ في إرسال التليجرام: {response.text}")
    except Exception as e:
        print(f"❌ حدث خطأ أثناء الاتصال بتليجرام: {e}")

def check_fortnite_status():
    api_url = "https://fortnite-api.com/v2/aes"
    try:
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            
            # استخراج رقم البناء/التحديث الحالي (مثل: Release-41.10-CL-55227503)
            current_version = data["data"]["build"]
            
            # قراءة النسخة القديمة المحفوظة في الملف إن وجدت
            if os.path.exists(STATUS_FILE):
                with open(STATUS_FILE, "r") as f:
                    last_version = f.read().strip()
            else:
                last_version = ""

            # المقارنة البرمجية: إذا اختلف رقم البناء الحالي عن المسجل سابقاً
            if current_version != last_version:
                msg = (
                    f"🚨 *تحديث جديد لفورتنايت!* 🚨\n\n"
                    f"📦 *الإصدار المكتشف:* `{current_version}`\n"
                    f"⚙️ *الحالة:* السيرفرات بدأت الصيانة أو نزل أبديت جديد الآن للتحميل!"
                )
                print(f"🔥 تم اكتشاف تحديث جديد: {current_version}")
                send_telegram_message(msg)
                
                # حفظ الإصدار الجديد لتجنب إرسال نفس الرسالة في الفحص القادم
                with open(STATUS_FILE, "w") as f:
                    f.write(current_version)
            else:
                print(f"😴 لا توجد تحديثات جديدة. الإصدار الحالي ما زال: {current_version}")
                
        else:
            print(f"⚠️ فشل سحب البيانات من الـ API. كود الحالة: {response.status_code}")
            
    except Exception as e:
        print(f"❌ خطأ غير متوقع أثناء الفحص: {e}")

if __name__ == "__main__":
    check_fortnite_status()