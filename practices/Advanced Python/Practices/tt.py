# x = ''
# for i in range(0, len(word)):
#     if word[i] not in x:
#         x += word[i]
#         print(word[i] , "=>", word.count(word[i]))


# def get_available_letters(letters_guessed):
#     available_letters = ''
#     for char in letters_guessed.ascii_lowercase:
#         if char not in letters_guessed:
#             available_letters += char
#     return available_letters

# x = get_available_letters('ramesh pradhan')
# print(x)
list1, list2 = ['C++','Java', 'Python'], [456, 700, 200]
print ("Max value element : ", max(list1))
print ("Max value element : ", max(list2))