from decouple import Config, RepositoryIni
from logic import play_game

config = Config(repository=RepositoryIni('settings.ini'))

min_num = config.get('min_number', cast=int)
max_num = config.get('max_number', cast=int)
attempts = config.get('attempts', cast=int)
balance = config.get('start_balance', cast=int)

play_game(min_num, max_num, attempts, balance)
