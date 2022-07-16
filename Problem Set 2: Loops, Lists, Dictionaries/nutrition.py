# Define fruits dictionary containing the 20 fruits and their corresponding number of calories per portion
fruits = {
    'apple': 130,
    'avocado': 50,
    'banana': 110,
    'cantaloupe': 50,
    'grapefruit': 60,
    'grapes': 90,
    'honeydew': 50,
    'kiwifruit': 90,
    'lemon': 15,
    'lime': 20,
    'nectarine': 60,
    'orange': 80,
    'peach': 60,
    'pear': 100,
    'pineapple': 50,
    'plums': 70,
    'strawberries': 50,
    'sweet cherries': 100,
    'tangerine': 50,
    'watermelon': 80,
}

input = input('Enter a fruit: ').lower()

# Check if the user-inputted key is contained in the dictionary. If it is, then access its corresponding value in the dictionary.
if input in fruits:
    data = fruits.get(input)
    print(data)
else:
    pass
