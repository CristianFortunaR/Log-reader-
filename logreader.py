from asyncio.windows_events import NULL
from secrets import choice
from tkinter.filedialog import askopenfilename

filename = askopenfilename()
option = int(input("Do you wanna select By? 1. Time and Date 2.prealm 3.Word 4.All] > "))

lines = []

result = open("result.txt", "w")

with open(filename) as f:
    lines = f.readlines()

if option == 1:
    optionfields = int(input("Do you wanna to select other fields: 0.No 1. Word 2.prealm 3.Both > "))
    if optionfields == 1:
        tad = input("Enter the hour here: exp[12:23:22]")
        word = input("Enter the word: ")
        count = 0
        for line in lines:
            if tad.capitalize() in line or tad.lower() in line and word.capitalize() in line or word.lower() in line or word.upper() in line:
                print(f"{tad} and {word} Found in line {count}: {line}")
                result.write(f"{tad} and {word} Found in line {count}: {line}")
            count += 1
        else:
            result.write(f"{tad} and {word} not found on file")
    elif optionfields == 2:
        tad = input("Enter the date here: exp[Mon Jun 24] >")
        prealm = int(input("Enter the prealm: "))
        count = 0
        for line in lines:
            if tad.lower in line or tad.capitalize and prealm in line:
                print(f"{tad} and {prealm} Found in line {count}: {line}")
                result.write(f"{tad} and {prealm} Found in line {count}: {line}")
            count += 1
    elif optionfields == 3:
        tad = input("Enter the date here: exp[Mon Jun 24] >")
        prealm = input("Enter the prealm: ")
        word = input("Enter your word: ")
        count = 0
        for line in lines:
            if tad in line and 'prealm_'+prealm in line and word in line:
                print(f"{tad} ,{prealm}, {word} Found in line {count}: {line}")
                result.write(f"{tad} ,{prealm}, {word} Found in line {count}: {line}")
            count += 1
    elif optionfields == 0:
        tad = input("Enter the date here: exp[Mon Jun 24] >")
        count = 0
        for line in lines:
            if tad in line:
                print(f"{tad} Found in line {count}: {line}")
                result.write(f"{tad} Found in line {count}: {line}")
            count += 1
elif option == 2:
    optionfields = int(input("Do you wanna to select other fields: 0.No 1.Time and Date 2.word 3.Both >"))
    if optionfields == 1:
        prealm = input("Enter the prealm:")
        tad = input("Enter the date here: exp[Mon Jun 24] >")
        count = 0
        for line in lines:
            if tad in line and 'prealm_'+prealm in line:
                print(f"{tad} and {prealm} Found in line {count}: {line}")
                result.write(f"{tad} and {prealm} Found in line {count}: {line}")
            count += 1
    elif optionfields == 2:
        prealm = input("Enter the prealm: ")
        word = input("Enter your word: ")
        count = 0
        for line in lines:
            if word in line and 'prealm_'+prealm in line:
                print(f"{word} and {prealm} Found in line {count}: {line}")
                result.write(f"{prealm}, {word}  Found in line {count}: {line}")
            count += 1
    elif optionfields == 3:
        tad = input("Enter the date here: exp[Mon Jun 24] >")
        prealm = input("Enter the prealm: ")
        word = input("Enter your word: ")
        count = 0
        for line in lines:
            if tad in line and 'prealm_'+prealm in line and word in line:
                print(f"{tad} ,{prealm}, {word} Found in line {count}: {line}")
                result.write(f"{tad} ,{prealm}, {word} Found in line {count}: {line}")
            count += 1
    elif optionfields == 0:
        prealm = input("Enter the prealm: ")
        count = 0
        for line in lines:
            if 'prealm_'+prealm in line:
                #print(f"{prealm} Found in line {count}: {line}")
                result.write(f"{prealm} Found in line {count}: {line}")
            count += 1
elif option == 3:
    optionfields = int(input("Do you wanna to select other fields: 0.No 1.Time and Date 2.prealm 3.Both >"))
    if optionfields == 1:
        word = input("Enter the word: >")
        tad = input("Enter the date here: exp[Mon Jun 24] >")
        count = 0
        for line in lines:
            if tad in line and word in line:
                print(f"{word}, {tad} Found in line {count}: {line}")
                result.write(f"{word}, {tad} Found in line {count}: {line}")
            count += 1
    elif optionfields == 2:
        word = input("Enter your word: ")
        prealm = input("Enter the prealm: ")
        count = 0
        for line in lines:
            if word in line and 'prealm_'+prealm in line:
                print(f"{word} and {prealm} Found in line {count}: {line}")
                result.write(f"prealm_{prealm}, {word}  Found in line {count}: {line}")
            count += 1
    elif optionfields == 3:
        tad = input("Enter the date here: exp[Mon Jun 24] >")
        prealm = input("Enter the prealm: ")
        word = input("Enter your word: ")
        count = 0
        for line in lines:
            if tad in line and 'prealm_'+prealm in line and word in line:
                print(f"{tad} ,{prealm}, {word} Found in line {count}: {line}")
                result.write(f"{tad} ,{prealm}, {word} Found in line {count}: {line}")
            count += 1
    elif optionfields == 0:
        word = input("Enter the word: ")
        count = 0
        for line in lines:
            if word.capitalize() in line or word.upper() in line or word.lower() in line:
                print(f"{word} Found in line {count}: {line}")
                result.write(f"{word} Found in line {count}: {line}")
            count += 1
elif option == 4:
    tad = input("Enter the date here: exp[Mon Jun 24] >")
    prealm = input("Enter the prealm: ")
    word = input("Enter your word: ")
    count = 0
    for line in lines:
        if tad and 'prealm_'+prealm and word in line:
            print(f"{tad} ,{prealm}, {word} Found in line {count}: {line}")
            result.write(f"{tad} ,{prealm}, {word} Found in line {count}: {line}")
        count += 1
elif option == 5:
    debugg = input("Enter the option: 1.Info 2.Debug  > ")
    if debugg == 1:
        count = 0
        for line in lines:
            if 'Info' or 'INFO' or 'info' in line:
                print(f"{debugg} found in line {count}: {line}")
                result.write(f"Info found in line {count}: {line}")
            count += 1
    elif debugg == 2:
        count = 0
        for line in lines:
            if 'Debug' or 'DEBUG' or 'debug' in line:
                print(f"Debugg found in line {count}: {line}")
                result.write(f"Debug found in line {count}: {line}")
            count += 1
