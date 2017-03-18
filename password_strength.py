import sys, os, getpass
import string


def get_password_from_command_line():
    return sys.argv[1] if len(sys.argv) > 1 else getpass.getpass("Введите ваш пароль: ")


def clear_console():
    os.system('cls' if os.name == 'nt' else 'clear')


def get_password_strength(password):
    password_strength = 10

    if len(password) < 8:
        password_strength -= 3

    has_upper_case = any(char in string.ascii_uppercase for char in password)
    has_lower_case = any(char in string.ascii_lowercase for char in password)
    has_number = any(char in string.digits for char in password)
    if not (has_upper_case and has_lower_case and has_number):
        password_strength -= 3

    has_special_char = not all(
        char in string.ascii_uppercase + string.ascii_lowercase + string.digits for char in password)
    if not has_special_char:
        password_strength -= 3

    return password_strength


if __name__ == '__main__':
    password = get_password_from_command_line()
    if not password:
        print('А где пароль?')
        sys.exit(1)
    clear_console()
    print('Оценка (от 1 до 10):', get_password_strength(password))
