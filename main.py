#2
import logging

def write_file(fill_path, data):
    try:
        with open(fill_path, 'w') as file:
            file.write(data)
        logging.info(f"dani z file {fill_path} zchitano")
    except Exception as e:
        logging.error(f'stalas pomilka y {fill_path} file {e}')

logging.basicConfig(level=logging.INFO)
write_file("output.txt", input("vvedit sho treba vpisaty v file: "))