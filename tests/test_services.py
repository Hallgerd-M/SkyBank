import pytest

from src.services import investment_bank


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


def test_investment_bank():
    assert investment_bank("2019-09", transactions, 50) == [{"investment_bank": 71.23}]
    assert investment_bank("2019-09", transactions, 10) == [{"investment_bank": 11.23}]


# def test_investment_bank():
#    assert investment_bank("2019-09", transactions, 100) == [{'investment_bank': 121.23}]
