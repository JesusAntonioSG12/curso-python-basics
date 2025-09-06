
# For: Se usa cuando sabemos cuando va a terminar y se suele usar para trabajar con iterables
# While: Se usa cuando no sabemos cuando va a terminar

my_list = [35, 24, 62, 52, 12]

for element in my_list:
    print(element)

items = 0
while items < len(my_list):
    print(my_list[items])
    items += 1