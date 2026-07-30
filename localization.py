localization = {
    'ru': {
        'username_field': "Введите никнейм в Dota/Steam", 
        'title': "Статистика Dota 2", 
        'search_button': "Найти", 
        'status_text': "Введите никнейм", 
        'status_finding': "Ищем игрока...", 
        'status_finish': "Почти готово...", 
        'status_error_failed': "Подключение не удалось. Пожалуйста, проверьте подключение", 
        'status_error_not_found': "Игрок не найден", 
        'status_error_not_found_games': "Игры не найдены — профиль может быть закрыт", 
        'info': "Аккаунт ID: {account_id}\nНайдено матчей: {matches_data}"
    },
    "en": {
        'username_field': "Enter your Steam username", 
        'title': "Dota 2 Statistic", 
        'search_button': "Find", 
        'status_text': "Enter your username", 
        'status_finding': "Finding the player...", 
        'status_finish': "Almost there..." ,
        'status_error_failed': "Connection failed. Please, check your internet connection and try again", 
        'status_error_not_found': "Player not found", 
        'status_error_not_found_games': "Matches not found - Profile may be closed",
        'info': "Account ID: {account_id}\nMatches found: {matches_data}"
    }
}

lang = 'ru'

def t(k) -> str:
    return localization[lang][k]

def set_lang(langg: str):
    global lang
    if langg in localization:
        lang = langg
