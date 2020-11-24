import fuzzy

from common import names

soundx = fuzzy.Soundex(4)

for each in names:
    print("Name =>> {} and Conversion =>> {}".format(each, soundx(each)))



