import requests


def help():
    return """
✨ سلام عزیزم ✨
برای استفاده از این ربات اسکل 🤖 فقط باید دستوراتش رو استفاده کنی:

📜 دستورات:

📖 داستان: نمایش یک داستان کوتاه ✍️📚

🌐 پروکسی: آماده‌سازی پروکسی‌های متصل 🔗🚀

🧠 دانستنی: حاجی نمی‌دونم، یه چیزی که احتمالاً نمی‌دونستی 🤯📌

💊 اطلاعات دارو: اسم دارویی که می‌خوای رو بفرست، اطلاعاتشو بهت میدم! 😷💉 (بعضی داروها شاید نباشن! ❌)

🎬 دیالوگ: بهت یه دیالوگ خفن میده 🎭🔥

🔮 فال: بهت فالتو نشون میده! 🃏✨

🕌 اوقات شرعی: اسم شهرتو بده، وضعیتشو بهت میگه! 🕋🕰️

🔥 بزن بریم! 😎🚀
    """
def mini_story():
    response = requests.get("https://api.codebazan.ir/dastan")
    if response.status_code == 200:
        return response.text
    else:
        return f"متاسفانه باید بگم اینجا ایرانه و اینترنت خوب نیست رفیق دوباره تلاش کن {response.status_code} کد ارور هست"

def proxy():
    response = requests.get("https://api.codebazan.ir/proxy/?type=mtproto")
    if response.status_code == 200:
        data = response.json() 
        if not isinstance(data, list): 
            return "خودمم نمیدونم چمه :)"

        proxies = []
        for proxy_data in data[:10]:
            proxy_link = f"https://t.me/proxy?server={proxy_data.get('host')}&port={proxy_data.get('port')}&secret={proxy_data.get('secret')}  -> ping : {proxy_data.get('ping', 'نامعلوم')}"
            proxies.append(proxy_link)
        
        return "\n".join(proxies) 
    else:
        return f"متاسفانه باید بگم اینجا ایرانه و اینترنت خوب نیست رفیق دوباره تلاش کن {response.status_code} کد ارور هست"


def danestani():
    response = requests.get("https://api.codebazan.ir/danestani/")
    if response.status_code == 200:
        return response.text
    else:
        return f"متاسفانه باید بگم اینجا ایرانه و اینترنت خوب نیست رفیق دوباره تلاش کن {response.status_code} کد ارور هست"


def daroo(name):
    response = requests.get(f"https://api.codebazan.ir/daro/?name={name}")
    if response.status_code == 200:
        output_json = response.json()
        return f"نام دارو‌ : {output_json['result']['name']}\n\n{output_json['result']['description']}"
    else:
        return f"متاسفانه باید بگم اینجا ایرانه و اینترنت خوب نیست رفیق دوباره تلاش کن {response.status_code} کد ارور هست"


def dialog():
    response = requests.get("https://api.codebazan.ir/dialog/")
    if response.status_code == 200:
        return response.text
    else:
        return f"متاسفانه باید بگم اینجا ایرانه و اینترنت خوب نیست رفیق دوباره تلاش کن {response.status_code} کد ارور هست"


def fal():
    response = requests.get("https://api.codebazan.ir/fal/")
    if response.status_code == 200:
        with open("fal_image.jpg", "wb") as file:  
            file.write(response.content)
        photo = open("fal_image.jpg", "rb")
        return photo
    else:
        return f"خطا در دریافت تصویر کد وضعیت: {response.status_code}"



def oghat_shari(city):
    response = requests.get(f"https://api.codebazan.ir/owghat/?city={city}")  # نام شهر به‌صورت مستقیم وارد شد
    if response.status_code == 200:
        output = response.json()

        result = output["Result"][0]  
            
        return f"""
        شهر : {result.get('shahr')}
        تاریخ : {result.get('tarikh')}
        اذان صبح : {result.get('azansobh')}
        طلوع آفتاب : {result.get('toloaftab')}
        اذان ظهر : {result.get('azanzohr')}
        غروب آفتاب : {result.get('ghorubaftab')}
        اذان مغرب : {result.get('azanmaghreb')}
        نیمه شب شرعی : {result.get('nimeshab')}
        """


    else:
        return f"متاسفانه باید بگم اینجا ایرانه و اینترنت خوب نیست رفیق دوباره تلاش کن {response.status_code} کد ارور هست"

