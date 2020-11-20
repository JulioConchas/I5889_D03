from io import open

## author: Julio Conchas
## email : conchasjiemenez@gmail.com

text_file=open("test_file.txt","r")
n_char=0
while 1:
    char = text_file.read(1)
    if not char:
        break

    n_char=n_char+1

text_file.close()

print("numero de caracteres: " + str(n_char))
