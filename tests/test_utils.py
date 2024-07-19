from unittest.mock import patch

import pytest

from src.utils import (
    fetch_and_show_currency_rates,
    get_card_number_list,
    get_cashback_sum,
    get_greeting,
    get_operations_sum,
    get_xlsx_data_dict,
    show_cards,
    show_top_5_transactions,
)


@pytest.fixture
def transactions():
    return [
        {
            "operation_date": "27.09.2019 13:05:37",
            "payment_date": "29.09.2019",
            "card_number": "*7197",
            "status": "OK",
            "operation_sum": -144.45,
            "operation_cur": "RUB",
            "payment_sum": -144.45,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Супермаркеты",
            "MCC": 5499.0,
            "description": "Колхоз",
            "Bonus": 2,
            "Invest_bank": 0,
            "rounded_operation_sum": 144.45,
        },
        {
            "operation_date": "27.09.2019 04:17:51",
            "payment_date": "27.09.2019",
            "card_number": "*4556",
            "status": "OK",
            "operation_sum": 1000.0,
            "operation_cur": "RUB",
            "payment_sum": 1000.0,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Бонусы",
            "MCC": 0,
            "description": 'Пополнение. Тинькофф Банк. Бонус по акции "Приведи друга"',
            "Bonus": 0,
            "Invest_bank": 0,
            "rounded_operation_sum": 1000.0,
        },
        {
            "operation_date": "26.09.2019 18:12:45",
            "payment_date": "26.09.2019",
            "card_number": "*4556",
            "status": "OK",
            "operation_sum": 250.0,
            "operation_cur": "RUB",
            "payment_sum": 250.0,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Пополнения",
            "MCC": 0,
            "description": "Пополнение через Альфа-Банк",
            "Bonus": 0,
            "Invest_bank": 0,
            "rounded_operation_sum": 250.0,
        },
        {
            "operation_date": "26.09.2019 17:42:59",
            "payment_date": "28.09.2019",
            "card_number": "*7197",
            "status": "OK",
            "operation_sum": -177.1,
            "operation_cur": "RUB",
            "payment_sum": -177.1,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Супермаркеты",
            "MCC": 5411.0,
            "description": "SPAR",
            "Bonus": 3,
            "Invest_bank": 0,
            "rounded_operation_sum": 177.1,
        },
        {
            "operation_date": "26.09.2019 11:57:20",
            "payment_date": "27.09.2019",
            "card_number": "*7197",
            "status": "OK",
            "operation_sum": -357.22,
            "operation_cur": "RUB",
            "payment_sum": -357.22,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Отели",
            "MCC": 7011.0,
            "description": "Dongying Luxury Blue Hori",
            "Bonus": 7,
            "Invest_bank": 0,
            "rounded_operation_sum": 357.22,
        },
    ]


def test_get_xlsx_data_dict():
    assert get_xlsx_data_dict("../data/operations_1.xlsx") == [
        {
            "operation_date": "30.12.2021 14:48:25",
            "payment_date": "30.12.2021",
            "card_number": "*7197",
            "status": "OK",
            "operation_sum": -349.0,
            "operation_cur": "RUB",
            "payment_sum": -349.0,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Канцтовары",
            "MCC": 5943,
            "description": "Mitrankov M.V.",
            "Bonus": 6,
            "Invest_bank": 0,
            "rounded_operation_sum": 349.0,
        },
        {
            "operation_date": "29.12.2021 16:22:08",
            "payment_date": "29.12.2021",
            "card_number": "*5091",
            "status": "OK",
            "operation_sum": -120.0,
            "operation_cur": "RUB",
            "payment_sum": -120.0,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Фастфуд",
            "MCC": 5814,
            "description": "Mouse Tail",
            "Bonus": 1,
            "Invest_bank": 0,
            "rounded_operation_sum": 120.0,
        },
        {
            "operation_date": "27.12.2021 18:31:43",
            "payment_date": "27.12.2021",
            "card_number": "*4665",
            "status": "OK",
            "operation_sum": -123.0,
            "operation_cur": "RUB",
            "payment_sum": -123.0,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Аптеки",
            "MCC": 5912,
            "description": "Apteka 23",
            "Bonus": 1,
            "Invest_bank": 0,
            "rounded_operation_sum": 123.0,
        },
        {
            "operation_date": "26.12.2021 22:09:56",
            "payment_date": "27.12.2021",
            "card_number": "*5091",
            "status": "OK",
            "operation_sum": -415.32,
            "operation_cur": "RUB",
            "payment_sum": -415.32,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Фастфуд",
            "MCC": 7512,
            "description": "Ситидрайв",
            "Bonus": 20,
            "Invest_bank": 0,
            "rounded_operation_sum": 415.32,
        },
    ]
    assert get_xlsx_data_dict("../data/operations_2.xlsx") == [
        {
            "operation_date": "26.12.2021 22:09:56",
            "payment_date": "27.12.2021",
            "card_number": "*5091",
            "status": "OK",
            "operation_sum": -415.32,
            "operation_cur": "RUB",
            "payment_sum": -415.32,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Каршеринг",
            "MCC": 7512,
            "description": "Ситидрайв",
            "Bonus": 20,
            "Invest_bank": 0,
            "rounded_operation_sum": 415.32,
        },
        {
            "operation_date": "25.12.2021 22:21:49",
            "payment_date": "26.12.2021",
            "card_number": "*5091",
            "status": "OK",
            "operation_sum": -218.07,
            "operation_cur": "RUB",
            "payment_sum": -218.07,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Каршеринг",
            "MCC": 7512,
            "description": "Ситидрайв",
            "Bonus": 10,
            "Invest_bank": 0,
            "rounded_operation_sum": 218.07,
        },
        {
            "operation_date": "24.12.2021 19:53:32",
            "payment_date": "25.12.2021",
            "card_number": "*7197",
            "status": "OK",
            "operation_sum": -78.0,
            "operation_cur": "RUB",
            "payment_sum": -78.0,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Госуслуги",
            "MCC": 9402,
            "description": "Почта России",
            "Bonus": 1,
            "Invest_bank": 0,
            "rounded_operation_sum": 78.0,
        },
        {
            "operation_date": "23.12.2021 17:00:31",
            "payment_date": "23.12.2021",
            "card_number": "*7197",
            "status": "OK",
            "operation_sum": -201.0,
            "operation_cur": "RUB",
            "payment_sum": -201.0,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Канцтовары",
            "MCC": 5943,
            "description": "IP Mitrankov M V",
            "Bonus": 4,
            "Invest_bank": 0,
            "rounded_operation_sum": 201.0,
        },
        {
            "operation_date": "22.12.2021 23:23:01",
            "payment_date": "23.12.2021",
            "card_number": "*5091",
            "status": "OK",
            "operation_sum": -26.19,
            "operation_cur": "RUB",
            "payment_sum": -26.19,
            "payment_cur": "RUB",
            "cashback": 0,
            "category": "Каршеринг",
            "MCC": 7512,
            "description": "Ситидрайв",
            "Bonus": 1,
            "Invest_bank": 0,
            "rounded_operation_sum": 26.19,
        },
    ]
    assert get_xlsx_data_dict("wrong_file.xlsx") == "File can't be read"


def test_get_greeting():
    assert get_greeting("2024-07-16 18:38:44.341897") == "Добрый вечер"
    assert get_greeting("2024-07-16 00:38:44.341897") == "Доброй ночи"
    assert get_greeting("2024-07-16 07:38:44.341897") == "Доброе утро"
    assert get_greeting("2024-07-16 14:38:44.341897") == "Добрый день"


def test_get_card_number_list(transactions):
    assert get_card_number_list(transactions) == ["*7197", "*4556"]


def test_get_operations_sum(transactions):
    assert get_operations_sum("2019-09-30", transactions, "*7197") == 678, 77
    assert get_operations_sum("2019-09-30", transactions, "*4556") == 0


@pytest.mark.parametrize(
    "x, expected", [(1056.45, 10.56), (9387.67, 93.88), (334.34, 3.34)]
)
def test_get_cashback_sum(x, expected):
    assert get_cashback_sum(x) == expected


def test_show_cards(transactions):
    assert show_cards("2019-09-30", transactions) == [
        {"last_digits": "7197", "total_spent": 678.77, "cashback": 6.79},
        {"last_digits": "4556", "total_spent": 0, "cashback": 0.0},
    ]


def test_show_top_5_transactions(transactions):
    assert show_top_5_transactions("2019-09-30", transactions) == [
        {
            "date": "27.09.2019",
            "amount": 1000.0,
            "category": "Бонусы",
            "description": 'Пополнение. Тинькофф Банк. Бонус по акции "Приведи друга"',
        },
        {
            "date": "27.09.2019",
            "amount": 357.22,
            "category": "Отели",
            "description": "Dongying Luxury Blue Hori",
        },
        {
            "date": "26.09.2019",
            "amount": 250.0,
            "category": "Пополнения",
            "description": "Пополнение через Альфа-Банк",
        },
        {
            "date": "28.09.2019",
            "amount": 177.1,
            "category": "Супермаркеты",
            "description": "SPAR",
        },
        {
            "date": "29.09.2019",
            "amount": 144.45,
            "category": "Супермаркеты",
            "description": "Колхоз",
        },
    ]


@patch("requests.get")
def test_fetch_and_show_currency_rates(mock_get):
    mock_get.return_value.json.return_value = {
        "success": True,
        "timestamp": 1721173697,
        "base": "RUB",
        "date": "2024-07-16",
        "rates": {"USD": 0.011299, "EUR": 0.010365},
    }
    assert (
        fetch_and_show_currency_rates()
        == "[{'currency': 'USD', 'rate': 88.5}, {'currency': 'EUR', 'rate': 96.48}]"
    )
    mock_get.assert_called_once_with(
        "https://api.apilayer.com/exchangerates_data/latest?symbols=USD,EUR&base=RUB",
        headers={"apikey": "JtLfCNxDRLiKVnZqkNZ8ET2TNVZPJLlx"},
    )
