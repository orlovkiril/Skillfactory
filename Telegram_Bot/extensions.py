import requests
import json
from config import keys


class ConversionException(Exception):
    pass

class Converter:
    @staticmethod
    def get_price(quote, base, amount):
        try:
            amount = float(amount)
        except ValueError:
            raise ConversionException('Неверно указана сумма.'
                                      '\nПодсказка: вводите десятичные дроби через точку')

        try:
            quote in keys[quote]
        except KeyError:
            raise ConversionException(f'Валюты "{quote}" нет в списке доступных для конвертации')

        try:
            base in keys[base]
        except KeyError:
            raise ConversionException(f'Валюты "{base}" нет в списке доступных для конвертации')

        url = f"https://api.apilayer.com/exchangerates_data/convert?to={keys[base]}&from={keys[quote]}&amount={amount}"
        payload = {}
        headers = {
            "apikey": "2jVTRKQXs5kRzRvIbQNCKH7P5EuiOIWY"
        }
        r = requests.request("GET", url, headers=headers, data=payload)
        result = json.loads(r.content)['result']

        return result