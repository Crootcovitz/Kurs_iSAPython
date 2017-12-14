import io
from contextlib import redirect_stdout

def get_print_output(tested_func, *args):
    # rezerwujemy miejsce w pamięci
    memory_buffer = io.StringIO()
    # *args - gdy nie wiemy, ile argumentów przyjmuje funkcja
    with redirect_stdout(memory_buffer):
        # przekierowanie printa do bufora
        tested_func(*args)
        # zwracamy
        return memory_buffer.getvalue()