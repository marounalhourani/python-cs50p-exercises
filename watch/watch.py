import re
import sys


def main():
    html = input("HTML: ").strip()
    print(parse(html))


def parse(s):
    if matches := re.search(r"src=\"https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9\-!@#$%^&*]+)", s):
        src = s.index('src="') + 5
    else:
        return "None"
    correct_url = "https://youtu.be/" + matches.group(1)
    return correct_url


if __name__ == "__main__":
    main()