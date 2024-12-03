from instabot import Bot
from PIL import Image
import os
import time

# Akun Instagram
USERNAME = "username"
PASSWORD = "password"

# Direktori tempat foto-foto disimpan
PHOTO_DIRECTORY = "photos/"

# Fungsi untuk memproses gambar agar sesuai format Instagram
def preprocess_image(photo_path):
    try:
        img = Image.open(photo_path)

        # Jika gambar memiliki mode RGBA (transparansi), tambahkan latar belakang putih
        if img.mode == "RGBA":
            background = Image.new("RGB", img.size, (255, 255, 255))  # Latar belakang putih
            background.paste(img, mask=img.split()[3])  # Gabungkan transparansi dengan latar belakang
            img = background

        # Resize ke dimensi Instagram (1080x1080)
        img = img.resize((1080, 1080))

        # Simpan gambar yang telah diproses dalam format JPEG
        processed_path = photo_path + "_processed.jpg"
        img.save(processed_path, "JPEG")
        return processed_path
    except Exception as e:
        print(f"Error saat memproses gambar {photo_path}: {e}")
        return None

# Login ke Instagram
def login():
    bot = Bot()
    bot.login(username=USERNAME, password=PASSWORD)
    return bot

# Fungsi untuk mengunggah satu foto
def upload_photo(bot, photo_path, caption=""):
    try:
        processed_photo = preprocess_image(photo_path)  # Proses gambar sebelum unggah
        if not processed_photo:
            print(f"Foto gagal diproses: {photo_path}")
            return
        bot.upload_photo(processed_photo, caption=caption)
        print(f"Foto berhasil diunggah: {photo_path}")
    except Exception as e:
        print(f"Gagal mengunggah foto {photo_path}: {e}")

# Fungsi untuk memproses semua foto di folder
def process_photos(bot):
    for file_name in os.listdir(PHOTO_DIRECTORY):
        if file_name.endswith((".jpg", ".jpeg", ".png")):
            photo_path = os.path.join(PHOTO_DIRECTORY, file_name)
            caption = f"Auto-posted photo: {file_name}"
            upload_photo(bot, photo_path, caption)
            time.sleep(60)  # Tunggu 60 detik sebelum unggahan berikutnya untuk menghindari deteksi spam

# Script utama
def main():
    bot = login()
    try:
        process_photos(bot)
    finally:
        bot.logout()  # Logout setelah selesai

if __name__ == "__main__":
    main()
