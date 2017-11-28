import os, sys
from PIL import Image

def resize(name_root, new_width):
    # bierze ścieżkę do bierzącego folderu
    folder = os.getcwd()

    for nr, foto in enumerate(os.listdir(folder)):
        # rozdziela plik na nazwę i rozszerzenie i bierze rozszerzenie
        ext = os.path.splitext(foto)[1]

        if ext.lower() not in ['png', 'jpg', 'jpeg', 'bmp']:
            continue

        zdjecie = Image.open(os.path.join(folder, foto))

        ratio = zdjecie.width / zdjecie.height
        new_height = round(new_width / ratio)

        male_foto = zdjecie.resize((new_width, new_height))
        # bo enumerate liczy od 0
        nowa_nazwa = f'{name_root}{nr+1}.{ext}'

        male_foto.save(os.path.join(folder, nowa_nazwa))

        zdjecie.close()