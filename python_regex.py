import re


search_string = "I am at the Taj hotel"


def python_regex():
    # Check if the string starts with "The":
    x = re.findall("\AThe", search_string)
    print(x)
    if x:
        print("Yes, there is a match!")
    else:
        print("No match")

    # Check if "Ta" is present at the beginning of a WORD:
    y = re.findall(r"\bTa", search_string)

    print(y)

    if y:
        print("Yes," + y[0] + " is there is in string: " + search_string)
    else:
        print("No match")

    # Check if the string has any a, r, or n characters:

    z = re.findall("[tel]", search_string)

    print(z)

    if z:
        print("Yes, there is at least one match!")
    else:
        print("No match")


python_regex()
