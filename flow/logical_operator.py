is_magician = True
is_expert = False

def get_msg(is_magician, is_export):
    if not is_magician:
        return 'you need magic powers'

    if not is_export:
        return "at least you'are getting there"

    return "you are a master magician"

print(get_msg(is_magician, is_expert))


