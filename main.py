import os
import subprocess
import sys


def keyboard_interrupt_hook(exctype, value, traceback):
    """keyboard interrupt handler."""
    if exctype == KeyboardInterrupt:
        print("The process has been stopped")
    else:
        sys.__excepthook__(exctype, value, traceback)
sys.excepthook = keyboard_interrupt_hook


def pre_reloader():
    """accepting and validating arguments."""
    paths = sys.argv
    if len(paths) != 3:
        print(f"ArgumentsException: {len(paths) - 1} arguments was/were given, 2 needed.")
        return

    path_to_dir = paths[1]
    path_to_file = paths[2]

    if not os.path.isdir(path_to_dir):
        print(f"CutomArgumentException: first arguments must be correct dir path.")
        return

    if not os.path.isfile(path_to_file):
        print(f"CustomArgumentException: second arguments must be correct file path.")
        return

    print(reloader(path_to_dir, path_to_file))


def reloader(path_to_dir: str, path_to_file: str):
    """process reloader."""
    p = subprocess.Popen(f"python3 {path_to_file}", shell=True)

    last_mtime = {}
    dirs = os.listdir(path_to_dir)

    while 1:
        for fname in dirs:
            if fname == "__pycache__":
                continue

            t = os.path.getmtime(f"{path_to_dir}/{fname}")

            if last_mtime.get(fname):
                if last_mtime.get(fname) < t:
                    p.kill()
                    p = subprocess.Popen(f"python3 {path_to_file}", shell=True)

            last_mtime[fname] = t


def main():
    pre_reloader()


if __name__ == '__main__':
    main()
