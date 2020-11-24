import fuzzy

from common import names

dmetaphone = fuzzy.DMetaphone(4)

for each in names:
    print("Name =>> {} and Conversion =>> {}".format(each, dmetaphone(each)))



