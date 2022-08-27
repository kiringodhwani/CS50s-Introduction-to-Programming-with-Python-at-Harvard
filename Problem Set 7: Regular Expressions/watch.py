import re


def main():
    print(parse(input("HTML: ")))


def parse(s):
    # The goal of this program is to extract the URLs of YouTube videos that are embedded in HTML pages.
    # These urls are embedded in the src attribute of the pages, so the we must search for a string beginning with 'src='.
    # The URL, then, must start with 'http' or 'https' followed by '://'.
    # 'www.' before 'youtube.com/embed/' is optional.
    # Lastly, capture the string of characters/numbers at the end of the URL (i.e. 'xvFZjo5PgG0' in src='https://www.youtube.com/embed/xvFZjo5PgG0').
    if matches := re.search(r'src="https?://(?:www\.)?youtube\.com/embed/([a-zA-Z0-9]+)', s):
        shortened = 'https://youtu.be/' + matches.group(1)
        return shortened
    else:
        return None


if __name__ == "__main__":
    main()
