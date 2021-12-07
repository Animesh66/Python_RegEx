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

    # Searches for the first match and returns a matched object
    search_pattern = re.search("hotel", search_string)
    print(search_pattern.span())
    print(search_pattern.start())
    print(search_pattern.end())
    print(search_pattern.group())
    print(search_pattern.string)
    search_itr = re.finditer("hotel", search_string)
    print(search_itr)  # return an iterator Matched object in the printed memory location
    for sh_st in search_itr:
        print(sh_st.start())
        print(sh_st.end())
    # Split the string at first two white-space character:
    search_split = re.split(r"\s", search_string, 2)
    print(search_split)
    # Replace first 2 white-spaces characters with the digit "9"
    search_sub = re.sub(r"\s", "9", search_string, 2)
    print(search_sub)


python_regex()
