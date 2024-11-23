from telethon import TelegramClient, events
from PIL import Image, ImageEnhance
from rembg import remove
import io

# اطلاعات API و Bot Token
api_id = "YOUR_API_ID"
api_hash = "YOUR_API_HASH"
bot_token = "YOUR_BOT_TOKEN"

# ایجاد کلاینت تلگرام
client = TelegramClient('BackgroundRemoverBot', api_id, api_hash).start(bot_token=bot_token)

# تابع برای حذف پس‌زمینه تصویر
def remove_background(image_bytes):
    """حذف پس‌زمینه از تصویر با استفاده از rembg."""
    return remove(image_bytes)

# تابع برای بهبود کیفیت تصویر
def enhance_image(image):
    """افزایش کیفیت تصویر (روشنایی و شفافیت)."""
    enhancer = ImageEnhance.Sharpness(image)
    image = enhancer.enhance(2.0)  # افزایش شفافیت
    enhancer = ImageEnhance.Brightness(image)
    image = enhancer.enhance(1.2)  # افزایش روشنایی
    return image

# مدیریت پیام‌های دریافتی
@client.on(events.NewMessage)
async def handle_message(event):
    sender = await event.get_sender()

    # بررسی اینکه پیام شامل تصویر است
    if event.photo:
        await event.reply("در حال پردازش تصویر شما... لطفاً منتظر بمانید.")
        
        # دریافت تصویر از پیام
        photo = await event.download_media(file=io.BytesIO())
        input_image = Image.open(photo)

        # حذف پس‌زمینه
        output_bytes = remove_background(photo)
        output_image = Image.open(io.BytesIO(output_bytes)).convert("RGBA")

        # بهبود کیفیت تصویر
        enhanced_image = enhance_image(output_image)

        # ذخیره تصویر پردازش شده
        processed_image = io.BytesIO()
        enhanced_image.save(processed_image, format="PNG")
        processed_image.seek(0)

        # ارسال تصویر پردازش شده
        await event.reply("تصویر شما آماده است!", file=processed_image)
    else:
        await event.reply("لطفاً یک تصویر ارسال کنید.")

# اجرای ربات
print("ربات فعال است...")
client.run_until_disconnected()
