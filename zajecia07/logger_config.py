import logging

def setup_logging():
    # Utwórz logger
    logger = logging.getLogger('my_logger')
    logger.setLevel(logging.DEBUG)

    # Utwórz formatery
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

    # Utwórz handler do pliku
    file_handler = logging.FileHandler('app.log')
    file_handler.setLevel(logging.DEBUG)
    file_handler.setFormatter(formatter)

    # Utwórz handler do konsoli
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.DEBUG)
    console_handler.setFormatter(formatter)

    # Dodaj handlery do loggera
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

# Inicjalizacja loggera
logger = setup_logging()
