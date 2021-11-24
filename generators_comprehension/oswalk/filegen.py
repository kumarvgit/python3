import os


def os_walk():
    root = "music"

    for path, directory, files in os.walk(root, topdown=True):
        print(path)
        for f in files:
            print("\t{}".format(f))


if __name__ == "__main__":
    print("From main")
    os_walk()
