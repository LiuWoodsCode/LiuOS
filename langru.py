import platform
import api
import socket
import random
import datetime
import logging
build_add = "07-21-23"
logging.info(f"Build date: {build_add}")
logging.info(f"API Version: {api.VerAPI}")
logging.info(f"LiuOS Version: {api.VerLiuOS}")

def set_fuckspez_remark():
    # Get the current date
    today = datetime.date.today()
    
    # Define the chances of each case
    chance_normal = 1 / 50
    chance_special = 1 / 7

    # Check if it's July 1st
    is_july_1st = today.month == 7 and today.day == 1

    # Check if it's a special day (July 1st)
    if is_july_1st:
        if random.random() < chance_special:
            variable = "RIP, Apollo for Reddit - "
        else:
            variable = None
    else:
        # Check for the normal case
        if random.random() < chance_normal:
            variable = "fuck u/spez - "
        else:
            variable = None

    if variable == None:
        variable = ""

    return variable

# Test the function
result = set_fuckspez_remark()

IsDebug = False
IsInternal = False
from termcolor import colored
def get_release_channel() :
    if IsInternal:
        return "Debug"
    else:
        return "Production"
hostname = socket.gethostname()
hostname_color = colored(f'Hello, World!', 'green', attrs=['reverse', 'blink'])
python = platform.python_version()
lowlevelos = platform.platform()
## Russian Language for LiuOS
CURRENT_LANG = "Rus"
LANG_VER = 0.1
CURRENT_LONG_LANG = "Russian (Russia)"
# Authentication
# Do not translate - ASCII Art
LINE1 =  colored(f'██▓     ██▓ █    ██  ▒█████    ██████ ', 'blue')
LINE4 =  colored(f'▓██▒   ▒▓██▒ ██  ▓██▒▒██▒  ██▒▒██    ▒ ', 'cyan')
LINE2 = colored(f'▒██░   ▒▒██▒▓██  ▒██░▒██░  ██▒░ ▓██▄   \n', 'magenta')
LINE3 = colored(f'▒██░   ░░██░▓▓█  ░██░▒██   ██░  ▒   ██▒\n░██████░░██░▒▒█████▓ ░ ████▓▒░▒██████▒▒\n░ ▒░▓   ░▓  ░▒▓▒ ▒ ▒ ░ ▒░▒░▒░ ▒ ▒▓▒ ▒ ░\n░ ░ ▒  ░ ▒ ░░░▒░ ░ ░   ░ ▒ ▒░ ░ ░▒  ░  \n  ░ ░  ░ ▒ ░ ░░░ ░ ░ ░ ░ ░ ▒  ░  ░  ░  \n    ░    ░     ░         ░ ░        ░', 'light_magenta')
# Ok, now continue.
OS_NAME_LOGIN = f"\n{LINE1}\n{LINE4}\n{LINE2}{LINE3}\n\n{result}{colored(f'LiuOS {api.VerLiuOS} от LiuWoodsCode', 'cyan')}\n"
CHANGE_CREDENTIAL_ALERT = "Вы не настроили учетные данные пользователя. Имя пользователя по умолчанию — \"username\", пароль — \"password\".\nПосле входа в систему выполните команду \"changecred\", чтобы изменить имя пользователя и пароль."
ENTER_USERNAME_CREATION = "Введите имя пользователя, оставьте поле пустым, чтобы использовать \"username\": "
ENTER_PASSWD_CREATION = "Введите пароль: "
ENTER_USERNAME_LOGIN = "Введите ваше имя пользователя: "
ENTER_PASSWD_LOGIN = "Введите ваш пароль: "
INCORRECT_LOGIN = "Неверные учетные данные. Проверьте Caps Lock и настройки локали, затем попробуйте снова."
SUCCESSFUL_LOGIN = "Вход в систему..."
FAKE_SUCCESSFUL_LOGIN = "[ФЕЙКОВЫЙ ВХОД] Вход в систему..."
BRUTE_FORCE_CRASH = "Слишком много попыток ввода пароля."
# Глобальные строки, которые могут использоваться в разных местах
SOURCE_FILE = "Исходный файл"
DEST_FILE = "Файл назначения"
# Тестовые строки для GitHub Actions
SAMPLE_ABC = "Rus - АБВГДЕЁЖЗИЙКЛНОПРСТУФХЦЧШЩЪЫЬЭЮЯабвгдеёжзийклнопрустыфхцчшщъыьэюя1234567890!@#$%^&*()-=[]\{}|;':,./<>?"
SAMPLE_STRING = "Генри Моррис = Eteled"
# LiuOS Shell
SHELL_PROMPT = "LiuOS $ "
SHELL_INTRO = f"LiuOS {api.VerLiuOS}, работает на ядре Python версии {python}.\nВведите help или ?, чтобы увидеть список доступных команд.\n"
HELP_HEADER = f"Команды LiuOS в текущей сборке ({api.VerLiuOS}). Введите \"help (команда)\", чтобы узнать подробности о команде."
COMMAND_NOT_FOUND = "команда не найдена"
# Команды  
# Смена учетных данных
CHANGECRED_ELEVATION_FAILED = "LiuOS не может изменить ваши учетные данные без повышения привилегий."
# Версия
OS_NAME_LOGO = f"\n{LINE1}\n{LINE4}\n{LINE2}{LINE3}"
VersionOutput = f"LiuOS {api.VerLiuOS}\nLiuOS API {api.VerAPI}\nЯзыковой пакет LiuOS {CURRENT_LANG} {LANG_VER}\nТип выпуска: {get_release_channel()}\n-----------------------\nВерсия ядра (Python): {python}\nНизкоуровневая ОС: {lowlevelos}"
# WebGet
CHECK_LOG = "Вывод запроса сохранен в вашем файле журнала."
# Завершение работы
LOGGING_OUT = "Выход из системы..."
# Обновления - Для будущего использования
UPDATECORE_RECOVERY = "восстановление"
RECOVERY_MODE_WARN = "Вы входите в режим восстановления. LiuWoodsCode не несет ответственности за любые повреждения, вызванные в режиме восстановления. Продолжайте на свой страх и риск."
UPDATING_MSG = "Обновление LiuOS..."
RECOVERY_START = "Запуск режима восстановления LiuOS..."
# Безопасность
CONFORM_RUN_FILE = colored(f'Вы собираетесь запустить файл команд.\n Он может содержать команды Shell/CMD/PowerShell или код на Python, который может быть опасным.\n\nВЫ ТОЧНО ХОТИТЕ ЗАПУСТИТЬ КОМАНДЫ В ЭТОМ ФАЙЛЕ?', 'red')
EXCEPTION_RUNLINE_TRY_AGAIN = "Хотите попробовать снова без обработчика сбоев? Ответьте y или n: "
SHUTDOWN_WARNING = "Вы действительно хотите выключить компьютер? \n\nY = Да\nN = Нет"
PASSWORD_CANNOT_PASSWORD = "Ваш пароль не может быть установлен как \"password\", так как это значение используется по умолчанию. Если вы оставите его таким, сообщение при входе в систему будет считать, что новые учетные данные не были установлены.\n\nВаш пароль был установлен как \"liuos\""
# Обработчик сбоев
PROG_HAS_CRASHED = "программа завершилась с ошибкой. Обратитесь к разработчику за дополнительной информацией. По крайней мере, это не так плохо, как Синдзи Аоба!"
OS_NAME_SPLASH = f"\n{LINE1}\n{LINE4}\n{LINE2}{LINE3}\n\n{SHELL_INTRO}"
