import json
import requests
from config import keys
class APIException(Exception):
    pass
class Converter:
    @staticmethod
    def convert(quote: str, base: str, amount: str):
        if quote == base:
            raise APIException(f'Невозможно перевести в одну валюту {base}.')

        try:
            quote_ticker = keys[quote]
        except KeyError:
            raise APIException(f'Неизвестная валюта {quote}')

        try:
            base_ticker = keys[base]
        except KeyError:
            raise APIException(f'Неизвестная валюта {base}')

        try:
            amount = float(amount)
        except ValueError:
            raise APIException(f'Неизвестное кол - во валюта {amount}')

        r = requests.get(f"https://min-api.cryptocompare.com/data/price?fsym={quote_ticker}&tsyms={base_ticker}")
        total_base = json.loads(r.content)[keys[base]]
        return total_base
