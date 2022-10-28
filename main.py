import os
import subprocess
import asyncio


def main(dir_name: str):
    p = subprocess.Popen("python3 /Users/ilya/Documents/GitHub/Chords-WebApp/Chords-WebApp/bot.py",
                         shell=True)

    last_mtime = {}
    dirs = os.listdir(dir_name)

    while 1:
        print("again")
        for fname in dirs:
            if fname == "__pycache__":
                continue

            t = os.path.getmtime(f"{dir_name}/{fname}")

            if last_mtime.get(fname):
                if last_mtime.get(fname) < t:

                    p = subprocess.Popen("python3 /Users/ilya/Documents/GitHub/Chords-WebApp/Chords-WebApp/bot.py",
                                         shell=True)

            last_mtime[fname] = t


if __name__ == '__main__':
    main(input())
