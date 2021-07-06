import json
import requests
from config import keys

class ConverterException(Exception):
    pass
class Convertor:
    @staticmethod
    def get_price(values):
        if len(values) != 3:
            raise ConverterException('Falscher Wertenanzahl!')
        quote, base, amount = values

        if quote == base:
            raise ConverterException(f'Gleiche Währung wird nicht konvertiert!{base}')
        try:
            quote_formatted = keys[quote]
        except KeyError:
            raise ConverterException(f'Konvertirung ist nicht möglich!{quote}')
        try:
            base_formatted = keys[base]
        except KeyError:
            raise ConverterException(f'Konvertirung ist nicht möglich!{base}')

        try:
            amount = float(amount)
        except ValueError:
            raise ConverterException(f'Der Betrag wird nicht bearbeitet!{amount}')
        r = requests.get(f'https://api.exchangeratesapi.io/latest?base={quote_formatted}&symbols={base_formatted}')
        result = float(json.loads(r.content)['rates'][base_formatted])*amount
        total = round(result,3)