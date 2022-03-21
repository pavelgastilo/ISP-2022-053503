import os
import sys
from func import Words

try:
    try:
        N: int = int(input("Vvedite N: "))
        K: int = int(input("Vvedite K: "))
    except ValueError:
        print("value_error")
        sys.exit()
    if N == 0 or K == 0:
        raise ValueError("Nekorrektniy vvod")
    with open('text.txt', encoding="utf8") as file_to_open:
        if os.path.getsize('text.txt') == 0:
            raise EOFError("Pystoi fail")
        str_input: str = file_to_open.read()
        words: Words = Words(str_input, K, N)
        words.count_words()
        words.print_dict()
        print(f"\nMedian: {words.fdmedian()}")
        print(f"avg: {words.average()}\n")
        words.ngramms()
        words.top_k()
        file_to_open.close()

except ValueError as value_error:
    print(value_error)

except EOFError as pysto:
    print(pysto)
