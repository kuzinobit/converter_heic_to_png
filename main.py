from pillow_heif import register_heif_opener
from PIL import Image
import os
import configparser

register_heif_opener()

# Читаем конфиг
config = configparser.ConfigParser()
config.read("config.conf")

del_before_convert = config.getboolean("Settings", "del_before_convert", fallback=False)

def convert_heic_to_png(input_folder, output_folder, delete_after=False):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for file in os.listdir(input_folder):
        if file.lower().endswith(".heic"):
            input_path = os.path.join(input_folder, file)
            output_path = os.path.join(output_folder, os.path.splitext(file)[0] + ".png")

            try:
                with Image.open(input_path) as img:
                    img.save(output_path, "PNG", quality=100)
                print(f"Конвертировано: {file} -> {os.path.basename(output_path)}")

                if delete_after:
                    os.remove(input_path)
                    print(f"Удалено: {file}")
            except Exception as e:
                print(f"Ошибка при конвертации {file}: {e}")

if __name__ == "__main__":
    input_folder = "data/heic"
    output_folder = "data/png"

    convert_heic_to_png(input_folder, output_folder, del_before_convert)