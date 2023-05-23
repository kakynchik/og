import random
import logging

logging.basicConfig(filename='random_numbers.log', level=logging.DEBUG,
                    format='%(asctime)s - %(levelname)s - %(message)s')

def generate_random_numbers(file_path, count):
    try:
        with open(file_path, 'w') as file:
            for i in range(1, count + 1):
                random_number = random.randint(1, 100)
                file.write(f'{i}. {random_number}\n')
                logging.info(f'Generated random number: {random_number}')
            logging.info(f'Successfully generated and saved {count} random numbers.')
    except Exception as e:
        logging.error(f'Error occurred: {str(e)}')

file_path = 'random_numbers.txt'
number_count = 10

generate_random_numbers(file_path, number_count)