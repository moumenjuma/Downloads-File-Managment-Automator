from os import scandir, rename
from os.path import splitext, exists, join
from shutil import move
from time import sleep
import logging
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

#FILL IN BELOW!!!!!!!!!!! <- PROGRAM WILL NOT FUN AT ALL WITH THIS INFO 
# folder to track Example for Source Director -> Windows: "C:\\Users\\UserName\\Downloads"
source_dir = ""
dest_dir_sfx = ""
dest_dir_music = ""
dest_dir_video = ""
dest_dir_image = ""
dest_dir_documents = ""

# image types supported
image_fi = [".jpg", ".jpeg", ".jpe", ".jif", ".jfif", ".jfi", ".png", ".gif", ".webp", ".tiff", ".tif", ".psd", ".raw", ".arw", ".cr2", ".nrw",".k25", ".bmp", ".dib", ".heif", ".heic", ".ind", ".indd", ".indt", ".jp2", ".j2k", ".jpf", ".jpf", ".jpx", ".jpm", ".mj2", ".svg", ".svgz", ".ai", ".eps", ".ico"]
# Video types supported
video_fi = [".webm", ".mpg", ".mp2", ".mpeg", ".mpe", ".mpv", ".ogg",".mp4", ".mp4v", ".m4v", ".avi", ".wmv", ".mov", ".qt", ".flv", ".swf", ".avchd"]
# Audio types supported
audio_fi = [".m4a", ".flac", "mp3", ".wav", ".wma", ".aac"]
# Document types supported
document_fi = [".doc", ".docx", ".odt",".pdf", ".xls", ".xlsx", ".ppt", ".pptx"]


def make_unique(dest, name):
    filename, extension = splitext(name)
    counter = 1

    # Condition to Files sharing names it will add a number at the end of the file's name
    while exists(f"{dest}/{name}"):
        name = f"{filename}({str(counter)}){extension}"
        counter += 1
    return name


def move_file(dest, entry, name):
    if exists(f"{dest}/{name}"):
        unique_name = make_unique(dest, name)
        oldName = join(dest, name)
        newName = join(dest, unique_name)
        rename(oldName, newName)

    move(entry, dest)


class MoverHandler(FileSystemEventHandler):
    # Function will run if the "source director" has any changes (ie the download folder)
    def on_modified(self, event):
        with scandir(source_dir) as entries:
            for entry in entries:
                name = entry.name
                self.check_audio_files(entry, name)
                self.check_video_files(entry, name)
                self.check_image_files(entry, name)
                self.check_document_files(entry, name)
    # Checks all Audio Files
    def check_audio_files(self, entry, name): 
        for audio_fi in audio_fi:
            if name.endswith(audio_fi) or name.endswith(audio_fi.upper()):
                if entry.stat().st_size < 10_000_000 or "SFX" in name:  
                    dest = dest_dir_sfx         #^-10 Megabytes
                else:
                    dest = dest_dir_music
                move_file(dest, entry, name)
                logging.info(f"Moved audio file: {name}")

    # Checks all Video Files
    def check_video_files(self, entry, name):  
        for video_fi in video_fi:
            if name.endswith(video_fi) or name.endswith(video_fi.upper()):
                move_file(dest_dir_video, entry, name)
                logging.info(f"Moved video file: {name}")

    # Checks all Image Files
    def check_image_files(self, entry, name):  
        for image_fi in image_fi:
            if name.endswith(image_fi) or name.endswith(image_fi.upper()):
                move_file(dest_dir_image, entry, name)
                logging.info(f"Moved image file: {name}")


    # Checks all Document Files
    def check_document_files(self, entry, name):  
        for documents_fi in document_fi:
            if name.endswith(documents_fi) or name.endswith(documents_fi.upper()):
                move_file(dest_dir_documents, entry, name)
                logging.info(f"Moved document file: {name}")

# From Watchdogs
if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO,
                        format='%(asctime)s - %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    path = source_dir
    event_handler = MoverHandler()
    observer = Observer()
    observer.schedule(event_handler, path, recursive=True)
    observer.start()
    try:
        while True:
            sleep(10)
    except KeyboardInterrupt:
        observer.stop()
    observer.join()