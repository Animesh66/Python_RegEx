import re


search_string = "I am at the Taj hotel. Taj hotel is a very good hotel."


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

    search_pattern = re.search("hotel", search_string)
    print(search_pattern.start())
    search_itr = re.finditer("hotel", search_string)
    print(search_itr)
    # Split the string at every white-space character:
    search_split = re.split(r"\s", search_string)
    print(search_split)

python_regex()
