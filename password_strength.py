import sys
import string


def get_password_from_command_line():
    return sys.argv[1] if len(sys.argv) > 1 else input('Введите пароль : ')


def get_password_strength(password):
    password_strength = 10

    if len(password) < 8:
        password_strength -= 3

    # символы должны быть в разных регистрах и хотя бы одна цифра
    upper = any(char in string.ascii_uppercase for char in password)
    lower = any(char in string.ascii_lowercase for char in password)
    number = any(char in string.digits for char in password)
    if not (upper and lower and number):
        password_strength -= 3

    # хотя бы 1 спецсимвол
    special_char = not all(
        char in string.ascii_uppercase or char in string.ascii_lowercase or char in string.digits for char in password)
    if not special_char:
        password_strength -= 3

    return password_strength


if __name__ == '__main__':
    password = get_password_from_command_line()
    if not password:
        print('А где пароль?')
        sys.exit()
    print(get_password_strength(password))
