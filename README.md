========================================================================
FORTNITE UPDATE TRACKER BOT DOCUMENTATION (ENGLISH)
========================================================================

A smart, free, open-source Python script automated via GitHub Actions 
to track Fortnite updates and server maintenance, sending real-time 
notifications straight to your Telegram channel/chat.

------------------------------------------------------------------------
1. FEATURES
------------------------------------------------------------------------
- Automated Tracking: Runs every 15 minutes completely free using GitHub 
  Actions Cron jobs. No local machine or paid server required.
- Zero Power Consumption: Runs in temporary GitHub cloud containers and 
  terminates immediately after checking.
- Persistent Memory: Saves the last known game version into a local file 
  (last_status.txt) within the repository to prevent duplicate spam alerts.
- Rich Formatting: Sends beautifully formatted Markdown messages directly 
  to your Telegram device.

------------------------------------------------------------------------
2. PROJECT STRUCTURE
------------------------------------------------------------------------
├── .github/workflows/
│   └── main.yml        # GitHub Actions workflow & permissions configuration
├── tracker.py          # Core Python script querying the Fortnite API
├── last_status.txt     # Persistent storage file updating the last version
└── README.txt          # Documentation guide

------------------------------------------------------------------------
3. SETUP & CONFIGURATION GUIDE
------------------------------------------------------------------------
STEP 1: Setup the Telegram Bot
1. Open Telegram, search for the official @BotFather account, and start a chat.
2. Send the command /newbot and follow the prompts to name your bot.
3. Copy the HTTP API Token provided (This will be your TELEGRAM_BOT_TOKEN).
4. Search for @userinfobot or @idbot on Telegram, send any message to find 
   your unique personal account ID (This will be your TELEGRAM_CHAT_ID).
5. CRITICAL: Open your newly created bot and click the "Start" button. 
   Otherwise, the bot cannot message you.

STEP 2: Configure GitHub Secrets
To safely store your private API keys and IDs without exposing them:
1. Navigate to your GitHub Repository -> Settings -> Secrets and variables -> Actions.
2. Click the green "New repository secret" button.
3. Add the first secret:
   - Name: TELEGRAM_BOT_TOKEN
   - Value: [Your copied Bot Token]
4. Add the second secret:
   - Name: TELEGRAM_CHAT_ID
   - Value: [Your unique Telegram ID]

STEP 3: Enable Workflow Read & Write Permissions
To allow the script to save the game version status and stop repeat messages:
1. Go to your GitHub Repository -> Settings -> Actions -> General.
2. Scroll down to the "Workflow permissions" section.
3. Change the setting to: "Read and write permissions".
4. Click the "Save" button.

------------------------------------------------------------------------
4. TECH STACK
------------------------------------------------------------------------
- Python 3.x
- Requests Library (For HTTP API interactions with Fortnite and Telegram)
- GitHub Actions Workflows (For completely free scheduling and automation)
- Fortnite-API.com (The primary source endpoint for AES/Build validation)


========================================================================
دليل توثيق وتشغيل بوت تتبع تحديثات فورتنايت (باللغة العربية)
========================================================================

بوت برميجي ذكي ومجاني بالكامل لتتبع تحديثات وصيانة لعبة Fortnite فور صدورها، 
مبني باستخدام لغة Python ومؤتمت بالكامل عبر GitHub Actions لإرسال إشعارات 
فورية ومباشرة إلى تطبيق Telegram.

------------------------------------------------------------------------
1. المميزات (Features)
------------------------------------------------------------------------
- فحص تلقائي ومستمر: يعمل السكربت تلقائياً كل 15 دقيقة (عبر خاصية Cron Job) 
  دون الحاجة لامتلاك سيرفر مدفوع أو تشغيل جهازك الشخصي.
- استهلاك منعدم للطاقة: يتم تشغيل الكود على خوادم GitHub المؤقتة بأمان ثم 
  إغلاقها فوراً بعد الفحص.
- ذاكرة ذكية مستمرة (Persistent Memory): يحفظ البوت رقم آخر إصدار مكتشف داخل 
  ملف نصي في المستودع (last_status.txt) لتجنب تكرار الإشعارات المزعجة.
- إشعارات غنية ومنسقة: تصلك الرسالة فوراً على تليجرام بصيغة Markdown تحتوي 
  على رقم الـ Build وحالة السيرفرات.

------------------------------------------------------------------------
2. هيكلية المشروع (Project Structure)
------------------------------------------------------------------------
├── .github/workflows/
│   └── main.yml        # ملف أتمتة التشغيل وإعدادات الصلاحيات على جيت هاب
├── tracker.py          # السكربت الأساسي المكتوب بلغة بايثون لفحص الـ API
├── last_status.txt     # ملف الذاكرة التلقائي لحفظ آخر نسخة تم اكتشافها
└── README.txt          # دليل التشغيل والاستخدام (هذا الملف)

------------------------------------------------------------------------
3. متطلبات التشغيل والإعداد (Setup Guide)
------------------------------------------------------------------------
الخطوة 1: إعداد بوت التليجرام (Telegram Bot)
1. اذهب إلى البوت الرسمي BotFather على تليجرام وأنشئ بوتاً جديداً باستخدام الأمر /newbot.
2. قم بنسخ الـ Token الخاص بالبوت (ستحتاجه لاحقاً باسم TELEGRAM_BOT_TOKEN).
3. ابحث عن بوت جلب المعرفات (مثل User Info Bot) وأرسل له أمر /start لكي تحصل 
   على رقم الـ ID الخاص بحسابك (ستحتاجه باسم TELEGRAM_CHAT_ID).
4. خطوة هامة: أرسل رسالة /start للبوت الخاص بك لتفعيل المحادثة والسماح له بمراسلتك.

الخطوة 2: إعداد المتغيرات السرية على GitHub (GitHub Secrets)
لحماية بياناتك وتوكن البوت الخاص بك من التسريب، أضفها كـ Secrets داخل مستودعك:
1. ادخل إلى مستودع المشروع الخاص بك على GitHub، ثم اذهب إلى تبويب Settings في الأعلى.
2. من القائمة الجانبية اليسرى، اختر Secrets and variables ثم اضغط على Actions.
3. اضغط على الزر الأخضر New repository secret وأضف المتغيرين التاليين بدقة:
   - الاسم: TELEGRAM_BOT_TOKEN  <- القيمة: الـ Token الخاص ببوتك.
   - الاسم: TELEGRAM_CHAT_ID    <- القيمة: رقم الـ ID الخاص بمحادثتك.

الخطوة 3: تفعيل صلاحيات الكتابة والأتمتة (خطوة حاسمة ⚠️)
لكي يتمكن البوت من حفظ التحديثات وتعديل ملف last_status.txt بنجاح حتى لا تتكرر 
الرسائل كل 15 دقيقة، يجب منح السيرفر صلاحية الكتابة:
1. من صفحة Settings في مستودعك، اذهب إلى قسم Actions ثم اختر General.
2. انزل إلى أسفل الصفحة حتى تصل إلى قسم Workflow permissions.
3. قم بتغيير الخيار الافتراضي واجعله: "Read and write permissions".
4. اضغط على زر Save الأزرق لحفظ الإعدادات أمنياً.

------------------------------------------------------------------------
4. تقنيات مستخدمة (Tech Stack)
------------------------------------------------------------------------
- Python 3.x
- Requests Library (للاتصال بالـ API وإرسال الـ HTTP requests لبوت تليجرام)
- GitHub Actions workflows (لأتمتة وتوقيت الفحص الدوري مجاناً)
- Fortnite-API.com (المصدر والمستودع الأساسي لجلب بيانات الـ AES والـ Build)
