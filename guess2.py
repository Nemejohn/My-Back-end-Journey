# command = ""
# started = False
# while True:
#     car_game = input('> ').lower()
#     if car_game == 'start':
#         if started:
#             print ('Car has started already...')
#         else:
#             started = True
#             print ('Car started...')
#     elif car_game == 'stop':
#         if not started:
#             print ('Car has stopped already')
#         else:
#             started = False
#             print ('Car stopped...')
#     elif car_game == 'help':
#         print ('''
# start - to start the car.
# stop - to stop the car.
# quit - to quit game.
# ''')
#     elif car_game == 'quit':
#         break
#     else:
#         print ("Sorry, I don't understand...")


shopping_cart = [10, 20, 30]
total = 0
for products in shopping_cart:
    total += products
print (f'Total price: {total}')

for x in range(4):
    for y in range(3):
        print (f'({x}, {y})')


numbers = [2, 2, 2, 5]
for x_count in numbers:
    print ('x' * x_count)

names_list = ['Josh', 'Mosh', 'Eli', 'Peter', 'Felix']
print (names_list [2:])

