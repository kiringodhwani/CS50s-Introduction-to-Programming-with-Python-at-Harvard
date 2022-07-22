# Main function
def main():
    # Take in input, call convert, print resulting string
    s = input('Enter input: ')
    s = convert(s)
    print(s)

# Converts :) and :( to their emoji equivalents
def convert(c):
    # Use replace() function to replace ':)' and ':('
    c = c.replace(':)','🙂')
    c = c.replace(':(','🙁')
    return c;

main()
