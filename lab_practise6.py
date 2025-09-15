user_input = input("Write something: ")
user_words = user_input.split()
good_word = True
count = 0

for word in user_words:
    for c in word:
        if not c.lower().isalpha():
            good_word = False
    if good_word is True:
        count += 1

print(count)