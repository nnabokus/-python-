import string

user_input = input("Write down the range:")

start = user_input[0]
end = user_input[2]

letters = string.ascii_letters

start_i = letters.index(start)
end_i = letters.index(end)

result = ""
for i in range(start_i, end_i + 1):
    result += letters[i]

print(result)
