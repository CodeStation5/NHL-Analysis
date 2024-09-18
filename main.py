from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://api-web.nhle.com"
TODAY_SCHEDULE_JSON = "/v1/schedule/now"
STANDINGS_NOW_JSON = "/v1/standings/now"
PLAYER_STATS_JSON = "https://api-web.nhle.com/v1/player/" #/PlayerID/landing

printer = PrettyPrinter()

data = get(BASE_URL + TODAY_SCHEDULE_JSON).json()
printer.pprint(data)