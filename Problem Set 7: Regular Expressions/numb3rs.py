import re

def main():
    print(validate(input("IPv4 Address: ")))


def validate(ip):
    # Capture the four numbers in the IP address next to the periods
    if matches := re.search(r'^([0-9]+)\.([0-9]+)\.([0-9]+)\.([0-9]+)$', ip):

        # Make sure that all four of the numbers in the IP address are between 0 and 255, inclusive.
        for i in range(1,5):
            if int(matches.group(i)) < 0 or int(matches.group(i)) > 255:
                return False
    else:
        return False

    return True


if __name__ == "__main__":
    main()
