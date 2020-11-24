import fuzzy

from common import names


for each in names:
    print("Name =>> {} and Conversion =>> {}".format(each, fuzzy.nysiis(each)))



