def do_stuff(num=0):
    try:
        if not num:  # if receive None or '', convert to 0
            num = 0
        return int(num) + 5
    except ValueError as err:
        return err
