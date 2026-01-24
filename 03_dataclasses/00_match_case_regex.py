import re

text = "123abc"

match text:
    case _ if re.fullmatch(r"\d+", text):
        print("same cyfry")
    case _ if re.match(r"\d+", text):
        print("zaczyna się od cyfr")
    case _ if re.match(r"[a-z]+", text):
        print("zaczyna się od liter")
    case _:
        print("coś innego")