import os, time, threading
from flask import Flask
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

app = Flask(__name__)
bot_views = 0

@app.route('/')
def home():
    global bot_views
    return f"🔥 إجمالي المشاهدات الحقيقية المسجلة: {bot_views}"

def real_browser_bot():
    global bot_views
    video_url = os.environ.get("VIDEO_URL", "https://youtu.be/9Uz04LYQe5k")
    
    while True:
        driver = None
        try:
            options = Options()
            options.headless = True
            options.add_argument("--disable-gpu")
            
            driver = webdriver.Firefox(options=options)
            driver.set_page_load_timeout(45)
            
            print("🚀 جاري فتح الفيديو بمتصفح حقيقي...")
            driver.get(video_url)
            
            # ⏳ الانتظار مدة الفيديو القصير (35 ثانية) لكي يراها يوتيوب مشاهدة كاملة
            time.sleep(35)
            
            bot_views += 1
            print(f"✅ تم احتساب مشاهدة يوتيوب حقيقية! الإجمالي: {bot_views}")
            
        except Exception as e:
            print(f"⚠️ خطأ مؤقت، جاري إعادة المحاولة...")
        finally:
            if driver:
                try:
                    driver.quit()
                except:
                    pass
        
        # استراحة قصيرة قبل فتح الزيارة التالية
        time.sleep(5)

# تشغيل البوت في الخلفية
threading.Thread(target=real_browser_bot, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
