# Import of the csv library
import collections
from collections import Counter
from csv import DictReader


def fruit():
    table = list()
    dict_list = []
    type_count = set()

    # Read in the csv for parsing
    with open("basket.csv", "r") as read_obj:
        csv_dict_reader = DictReader(read_obj)

        for row in csv_dict_reader:
            fruit_count = int(row["size"])
            types_of_fruit = row["name"]
            table.append(fruit_count)
            total = sum(table)
            type_count.add(types_of_fruit)
            dict_list.append(row)

        result = Counter()
        for d in dict_list:
            result[d["name"]] += int(d["size"])
            new_result = result.most_common()

        print("Total number of fruit: " + str(total))
        print("\n")
        print("Types of fruit: " + str(len(type_count)))
        print("\n")
        print("The number of each type of fruit in descending order\n")
        for index, tuple in enumerate(new_result):
            name = tuple[0]
            size = tuple[1]
            print(name + ":", size)
            print("\n")

        print("The characteristics (size, color, shape, etc.) of each fruit by type\n")
        cnt = collections.defaultdict(int)
        for r in dict_list:
            cnt[(r["name"], r["color"], r["shape"])] += int(r["size"])
        new_dict = dict(cnt)
        print(new_dict)
        print("\n")
        print("Have any fruit been in the basket for over 3 days")
        for sub in dict_list:
            for key in sub:
                sub["days"] = int(sub["days"])
            if sub["days"] > 3:
                print(sub, " is over 3 days old")


# Pass name of a properly formatted csv with its
# extension as a string. e.g. "basket.csv"
fruit()