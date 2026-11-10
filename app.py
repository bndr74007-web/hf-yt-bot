import os, requests, random, time, threading
from flask import Flask

app = Flask(__name__)
bot_views = 0

@app.route('/')
def home():
    global bot_views
    return str(bot_views)

def watch_simulator():
    global bot_views
    video_url = os.environ.get("VIDEO_URL", "https://youtu.be/9Uz04LYQe5k?si=m5KdjuWAC8_DMGs_")
    
    while True:
        try:
            # محاكاة زيارة حقيقية وسريعة للفيديو القصير بدون الحاجة لمتصفح ثقيل ينخنق
            headers = {
                "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36"
            }
            response = requests.get(video_url, headers=headers, timeout=15)
            if response.status_code == 200:
                bot_views += 1
                print(f"✅ تم تسجيل مشاهدة ناجحة! الإجمالي: {bot_views}")
        except Exception as e:
            pass
        
        # استراحة قصيرة جداً لتكرار الضربات بسرعة وسلاسة
        time.sleep(20)

threading.Thread(target=watch_simulator, daemon=True).start()

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=7860)
