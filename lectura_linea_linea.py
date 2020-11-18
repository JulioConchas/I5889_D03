from io import open

## author: Julio Conchas
## email : conchasjiemenez@gmail.com

text_file=open("test_file.txt","r")

text_lines = text_file.readlines()

text_file.close()

print("numero de lineas: " + str(len(text_lines)))
print(text_lines)
