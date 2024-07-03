import sys

from logic.number_to_words_converter import FrenchNumberToWordsConverter


def main():
    numbers = list(map(int, sys.argv[1:]))
    converter = FrenchNumberToWordsConverter()
    french_numbers = [converter.transform(number) for number in numbers]
    for num, fr_num in zip(numbers, french_numbers):
        print(f"{num} -> {fr_num}")


if __name__ == "__main__":
    main()
