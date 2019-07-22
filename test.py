from service import *

def main():

    file_transfer = SetUp()
    file_transfer.copy_file()
    file_transfer.get_file()

if __name__ == "__main__":
    main()
