from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api-web.nhle.com"
Today_JSON = "/v1/schedule/now"

printer = PrettyPrinter()

data = get(BASE_URL + Today_JSON).json()
printer.pprint(data)