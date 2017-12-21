
def funkcja_a(arg1: str, arg2: dict, arg3: float=4.0) ->str:
    # arg1 = arg1.capitalize()
    klucze = arg2.keys()
    # is_int = arg3.is_integer()

    return klucze

funkcja_a([], {'imię': 'Jan'}, '4')

def funkcja_b(arg1: str, arg2: dict, arg3: float=4.0) ->str:
    arg1 = arg1.capitalize()
    klucze = arg2.keys()
    is_int = arg3.is_integer()

    return arg1

x = funkcja_b('Ala', {'imię': 'Jan'}, 44.0)
print(x)
