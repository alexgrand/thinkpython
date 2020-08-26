def right_justify(word):
    spaces_num = 70
    intend = spaces_num - len(word)

    print(' ' * intend + word)

right_justify('monty')