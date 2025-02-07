#lets create a journal
with open("journal.txt", "w") as journal:
    while True: #infinite loop until q is pressed
        text = input("Enter a journal entry: (press q to quite): ")
        if text == "q":
            break
            journal.write(text+"\n") #need to add the new line
