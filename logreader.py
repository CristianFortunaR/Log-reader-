word = "Error"
word2 = "teste"

lines = []

result = open("result.txt", "w")

with open('teste.txt') as f:
    lines = f.readlines()

count = 0
for line in lines:
    if  word in line or word2 in line:
        print(f"{word} Found in line {count}: {line}")
        result.write(f"{word} Found in line {count}: {line}")
    count += 1
   