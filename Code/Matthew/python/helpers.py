


def get_int(message, error_message='invalid value!'):
    while True:
        try:
            user_input = input(message)
            user_input = int(user_input)
            return user_input
        except ValueError:
            print(error_message)


if __name__ == '__main__':
    age = get_int('what is your age? ')
    print(age)