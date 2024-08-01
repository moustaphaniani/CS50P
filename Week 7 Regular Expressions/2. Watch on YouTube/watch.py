import re
import sys


def main():
    print(parse(input("HTML: ")))


def parse(s):
    if reference := re.search(r"^<iframe.+https*://(?:www\.)*youtube.com/embed/(\w+).+iframe>", s):
        return f"https://youtu.be/{reference[1]}"
    else:
        return "None"


if __name__ == "__main__":
    main()
