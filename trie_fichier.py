import os
from glob import glob
import shutil
folders = ["Musique","Images","Video","Document"]
folder_source =r"D:\PERSO\python\cours_tp\tri_fichiers_sources"
source =r"D:\PERSO\python\cours_tp\tri_fichiers_sources\**"
files = glob(source,recursive=True)
for file in files:
    if file.endswith(".jpg") or file.endswith(".jpeg") or file.endswith(".png"):
        images = os.path.join(folder_source,"Images")
        if os.path.exists(images):
            file_source = os.path.join(folder_source,file)
            shutil.move(file_source,images)
        else:
           os.makedirs(images,exist_ok=True)
           file_source = os.path.join(folder_source, file)
           shutil.move(file_source, images)
    elif file.endswith(".pdf"):
        docs = os.path.join(folder_source, "Documents")
        if os.path.exists(docs):
            file_source = os.path.join(folder_source, file)
            shutil.move(file_source, docs)
        else:
            os.makedirs(docs, exist_ok=True)
            file_source = os.path.join(folder_source, file)
            shutil.move(file_source, docs)
    elif file.endswith('.mp3') or file.endswith(".wav"):
        musique = os.path.join(folder_source, "Musiques")
        if os.path.exists(musique):
            file_source = os.path.join(folder_source, file)
            shutil.move(file_source, musique)
        else:
            os.makedirs(musique, exist_ok=True)
            file_source = os.path.join(folder_source, file)
            shutil.move(file_source, musique)
    elif file.endswith(".mp4"):
        video = os.path.join(folder_source, "Videos")
        if os.path.exists(video):
            file_source = os.path.join(folder_source, file)
            shutil.move(file_source, video)
        else:
            os.makedirs(video, exist_ok=True)
            file_source = os.path.join(folder_source, file)
            shutil.move(file_source, video)