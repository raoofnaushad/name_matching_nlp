from pyjarowinkler.distance import get_jaro_distance
import editdistance

from common import names


name1 = "kale"
print("Querying name ", name1)



for each in names:
    print("Name =>> {} and jaro value =>> {} and levenshtein value =>> {}"\
        .format(each, get_jaro_distance(name1, each), editdistance.eval(name1, each)))



