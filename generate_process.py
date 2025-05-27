import os
from text_to_audio import text_to_speech_file
import time
import subprocess


def text_to_audio(folder):
    with open(f"user_uploads/{folder}/desc.txt") as f:
        text = f.read()
    print(text, folder)
    text_to_speech_file(text, folder)


def videoCreation(folder):
    command = f"""ffmpeg -f concat -safe 0 -i user_uploads/{folder}/input.txt -i user_uploads/{folder}/audio.mp3 -vf "scale=1080:1920:force_original_aspect_ratio=decrease,pad=1080:1920:(ow-iw)/2:(oh-ih)/2:black" -c:v libx264 -c:a aac -shortest -r 30 -pix_fmt yuv420p static/reels/{folder}.mp4"""
    subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    while True:
        print("Processing Folder")
        with open("done.txt", "r") as f:
            done_folders = [line.strip() for line in f.readlines()]
        # with open("done.txt", "r") as f:
        #     done_folders = f.readline()

        # done_folders = [f.strip() for f in done_folders]
        folders = os.listdir("user_uploads")
        for folder in folders:
            if folder not in done_folders:
                text_to_audio(folder)
                videoCreation(folder)
                with open("done.txt", "a") as f:
                    f.write(folder + "\n")
        time.sleep(4)
# iska matlab hai with.open() se hum done.txt me jo completed genration hai vidoe s ka uss ka naam store krwa lenge
#  folders = os.listdir se humne user_folder ke under jitne bhi filders bane hai uska detail le liye
# for loop me hum ek ek karke iterate kr rhe hai folders me of check kar rhe ki jo folder humre done.txt m,e nhi hai ( matlab jiska video genrate nhi hua hai ) uska video generate krdo , sabse pehele text_to_audio phir video create kro
