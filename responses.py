import random


def get_response(message: str) -> str:
    p_message = message.lower()

    if p_message == '/quote':
        x = (random.randint(1, 5))
        if x == 1:
            return 'Yeah whatever kid.'
        if x == 2:
            return 'Ight cya'
        if x == 3:
            return 'Theres no good games to play'
        if x == 4:
            return 'Wheres Birknasty!?'
        if x == 5:
            'He aint gon be in Rush hour 3'

    if message == '/roll':
        return str(random.randint(1, 20))

    if p_message == '/help':
        return '`Here are the commands for Demi Discord Bot.\n' \
               '/roll will roll a 20 sided dice\n' \
               '/quote will quote Demi with one of his great sayings\n' \
               '`'
