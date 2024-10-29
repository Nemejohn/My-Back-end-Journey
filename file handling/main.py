'''file = open('file handling/edit.txt', 'r')
content = file.read()
print(content)
file.close()'''

'''file = open('file handling/edit.txt' , 'w')
new_text = file.write('I love games \n')
file.close

file = open('file handling/edit.txt' , 'a')
file.write('I love food \n ')

file = open('file handling/edit.txt' , 'r')
content = file.read()
print(content)
file.close()'''

# the with statement:
# allows us 

# with open('file handling/text.html', 'r') as file:
#     reader = file.read()
#     print(reader)

# with open('file handling/text.html', 'w') as file:
#     file.write('Backend development going on now. \n')

# with open('file handling/happy-man-using-his-smartphone-while-home_23-2148793535.jpg', 'rb') as file:
#     binary_content = file.read()
#     print(binary_content)


from PIL import Image
with Image.open("file handling/happy-man-using-his-smartphone-while-home_23-2148793535.jpg") as im:
    im.rotate(0).show()