user_input = input("Write something: ")
lower_string = ""
for c in user_input:
    if c.isupper():
        lower_string += c.lower()
    else:
        lower_string += c

print(lower_string)
