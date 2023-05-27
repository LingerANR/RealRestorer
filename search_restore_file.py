from colorama import init, Fore, Back, Style
import os
import glob

def search_file():
    file_path = "../backups"  # Reemplaza con la ruta a la file_path donde quieres buscar los archivos
    search_word = input(f"{Fore.YELLOW}Search Word:{Style.RESET_ALL} ")
    patron = f"{file_path}/{search_word}*"
    file_found = glob.glob(patron)
    # import pdb;pdb.set_trace()

    if file_found:
        file_complete_name = os.path.splitext(file_found[0])[0]
        file_name_array = file_complete_name.split("/")
        final_name = file_name_array[len(file_name_array) - 1]
        print(f"{Fore.GREEN}FILE FOUND:{Style.RESET_ALL}", final_name)
        return final_name
    else:
        print(f"{Fore.RED}No files were found matching the specified name.{Style.RESET_ALL}")
        return None
