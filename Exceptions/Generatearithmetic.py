try:
    num = 25 / 0  #  ZeroDivisionError
except ZeroDivisionError as e:
    print(f"Arithmetic Exception: {e}")