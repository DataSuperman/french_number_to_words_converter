from abc import ABC, abstractmethod
from functools import lru_cache


class NumberToWordsConverter(ABC):

    @abstractmethod
    def convert(self, number: int) -> str:
        pass


class FrenchNumberToWordsConverter(NumberToWordsConverter):

    def __init__(self):
        self.units = ["zéro", "un", "deux", "trois", "quatre", "cinq", "six", "sept", "huit", "neuf", "dix",
                      "onze", "douze", "treize", "quatorze", "quinze", "seize"]
        self.tens = ["", "dix", "vingt", "trente", "quarante", "cinquante", "soixante"]
        self.special_cases = {71: "soixante-et-onze", 81: "quatre-vingt-un", 91: "quatre-vingt-onze",
                              80: "quatre-vingts"}
        self.plural_edge_cases = [100, 1000, 1000000]

    def transform(self, number: int) -> str:
        if number in self.plural_edge_cases:
            return self.convert(number)
        else:
            conversion = self.convert(number)
            output = conversion.split("-")[-1]
            if output in ["cent", "mille", "million"]:
                return conversion + "s"
            return conversion

    @lru_cache(maxsize=100)
    def convert(self, number: int) -> str:
        if number in self.special_cases:
            return self.special_cases[number]
        if number < 17:
            return self.units[number]
        if number < 20:
            return "dix-" + self.units[number - 10]
        if number == 20:
            return "vingt"
        elif number < 100:
            return self.convert_tens(number)
        elif number < 1000:
            return self.convert_hundreds(number)
        elif number < 1000000:
            return self.convert_thousands(number)
        else:
            return self.convert_large_numbers(number)

    def simple_tens(self, number: int) -> str:
        tens, unit = divmod(number, 10)
        if unit == 0:
            return self.tens[tens]
        elif unit == 1:
            return self.tens[tens] + "-et-un"
        else:
            return self.tens[tens] + "-" + self.units[unit]

    def convert_tens(self, number: int) -> str:
        if number < 70:
            return self.simple_tens(number)
        elif number < 80:
            return "soixante-" + self.simple_tens(number - 60)
        else:
            return "quatre-vingt-" + self.simple_tens(number - 80)

    def convert_hundreds(self, number: int) -> str:
        hundreds, remainder = divmod(number, 100)
        if hundreds == 1:
            return "cent" + ("-" + self.convert(remainder) if remainder else "")
        else:
            return self.units[hundreds] + "-cent" + ("-" + self.convert(remainder) if remainder else "")

    def convert_thousands(self, number: int) -> str :
        thousands, remainder = divmod(number, 1000)
        if thousands == 1:
            thousands_part = "mille"
        elif thousands > 16:
            thousands_part = self.convert(thousands) + "-mille"
        else:
            thousands_part = self.units[thousands] + "-mille"

        hundreds_part = self.convert(remainder)
        return thousands_part + ("-" + hundreds_part if remainder > 0 else "")

    def convert_large_numbers(self, number: int)-> str:
        if number < 1000000:
            return self.convert_large_below_million(number)
        elif number < 1000000000:
            return self.convert_large_below_billion(number)
        else:
            raise IndexError("Number too large to convert")

    def convert_large_below_million(self, number: int)-> str:
        thousands, remainder = divmod(number, 1000)
        thousands_part = self.convert(thousands) + "-mille" if thousands != 1 else "mille"
        return thousands_part + ("-" + self.convert(remainder) if remainder > 0 else "")

    def convert_large_below_billion(self, number: int) -> str:
        millions, remainder = divmod(number, 1000000)
        millions_part = self.convert(millions) + "-million"
        return millions_part + ("-" + self.convert_large_below_million(remainder) if remainder > 0 else "")


if __name__ == '__main__':
    # input = [0, 1, 5, 10, 11, 15, 20, 21, 30, 35, 50, 51, 68, 70, 75, 99, 100, 101, 105, 111, 123, 168, 171, 175,
    #          199, 200, 201, 555, 999, 1000, 1001, 1111, 1199, 1234, 1999, 2000, 2001, 2020, 2021, 2345, 9999, 10000,
    #          11111, 12345, 123456, 654321, 999999, 99999999]
    # for i in range(1, 100000000):
    #     print(i, FrenchNumberToWordsConverter().transform(i))
    print(FrenchNumberToWordsConverter().transform(-99999999))
