import os

def run(abc_c):
    os.system(abc_c)


def main():
    adb_c = 'adb devices'
    print(type(run(adb_c)))




if __name__ == '__main__':
    main()
