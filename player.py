CHAR_NAME = None
CHAR_RACE = None
CHAR_ROLE = None


class Player:
    hp = 10


def name_input():
    global CHAR_NAME
    CHAR_NAME = input('Enter your name.\n')


def race_input():
    global CHAR_RACE
    CHAR_RACE = input('Choose your race.\n')


def role_input():
    global CHAR_ROLE
    CHAR_ROLE = input('Choose your role.\n')
