# Background Remover & Image Enhancer Bot

A Telegram bot that removes the background of images and enhances their quality using Python. This bot is built using the **Telethon** library for Telegram API, **rembg** for background removal, and **Pillow** for image quality improvement.

## Features
- **Background Removal**: Removes the background of any image with high accuracy.
- **Image Enhancement**: Increases sharpness and brightness of the image.
- **Simple to Use**: Just send an image to the bot, and it will process and return the result.

1. Clone the repository:
   ```bash
git clone https://github.com/aliahoran2/background_remover_bot.git
cd background_remover_bot
---
pip install -r requirements.txt
python background_remover_bot.py

---

### **نکات مهم**
1. **ساخت ربات تلگرام**:
   - با استفاده از [BotFather](https://core.telegram.org/bots#botfather) یک ربات ایجاد کنید و توکن آن را دریافت کنید.
   - مقادیر `YOUR_API_ID`, `YOUR_API_HASH`, و `YOUR_BOT_TOKEN` را جایگزین کنید.

2. **نصب `rembg`**:
   - برای کار با **`rembg`** باید **Docker** یا پکیج کامل `rembg` را نصب کنید:
     ```bash
     pip install rembg
     ```

3. **تست ربات**:
   - پس از اجرا، عکس ارسال کنید و خروجی را بررسی کنید.

---

آیا نیاز به تغییرات یا جزئیات بیشتری در این پروژه داری؟ 😊

