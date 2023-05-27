from header import print_banner
from search_restore_file import search_file
from commands import execute_commands

def main():
    print_banner()
    final_name = search_file()
    if final_name:
        execute_commands(final_name)

if __name__ == "__main__":
    main()
