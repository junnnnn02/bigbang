# Create a script to iterate through 1 to 100 and replace any number divisible by 3 with the word
# BIG number divisible by 5 with the word BANG. If the number is divisible by 3 and 5, replace it
# with BIG BANG. Generate the array and output to ‘output.json’ file with result as follow:

# [“1”, “2”, “BIG”, “4”, “BANG”, “BIG”, “7”, “8”, “BIG”, “BANG”, “11”, “BIG”, “13”, “14”, “BIGBANG”,
# .... all the way to 100]

import json

result = list()

for i in range (1, 101):

    if i % 3 == 0 and i % 5 == 0:
        result.append("BIGBANG")

    elif i % 3 == 0:
        result.append("BIG")

    elif i % 5 == 0:
        result.append("BANG")

    else:
        result.append(str(i))


with open('output.json', 'w') as f:
    json.dump(result, f)