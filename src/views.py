import json
import logging

from src.utils import (fetch_and_show_currency_rates, get_greeting,
                       get_xlsx_data_dict, show_cards, show_top_5_transactions)

logger = logging.getLogger("main_page.log")
file_handler = logging.FileHandler("main_page.log", "w")
file_formatter = logging.Formatter('%(asctime)s %(levelname)s: %(message)s')
file_handler.setFormatter(file_formatter)
logger.addHandler(file_handler)
logger.setLevel(logging.INFO)

def main_page(date: str):
    """Записывает информацию для Главной страницы в файл json"""
    logger.info("Start")
    logger.info("Converting Excel file to list of dictionaries")
    transactions = get_xlsx_data_dict("../data/operations.xlsx")
    logger.info("Getting greeting")
    greeting = get_greeting(date)
    logger.info("Getting card info")
    cards = show_cards(date, transactions)
    logger.info("Getting top transactions")
    top_transcations = show_top_5_transactions(date, transactions)
    logger.info("Getting currency_rates")
    currency_rates = fetch_and_show_currency_rates()
    logger.info("Creating dictionary of dictionaries")
    main_dict = {}
    main_dict["greeting"] = greeting
    main_dict["cards"] = cards
    main_dict["top_transcations"] = top_transcations
    main_dict["currency_rates"] = currency_rates
    logger.info("Writing info into json-file")
    with open("main.json", "w", encoding="utf-8") as f:
        json.dump(main_dict, f, ensure_ascii=False, indent=4)
    logger.info("Stop")
    return main_dict


if __name__ == "__main__":
    result = main_page("2021-12-31 23:59:59")
    print(result)
