#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".
    
#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
    #Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
        #Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("../Mail Merge Project Start/Input/Names/invited_names.txt") as file:
    list_names = file.readlines()
n = 0
for i in list_names:
    with open("../Mail Merge Project Start/Input/Letters/starting_letter.txt") as letter:
        content = letter.read()
        new = content.replace("[name]", list_names[n].strip())

    with open(f"../Mail Merge Project Start/Output/letter_for_{list_names[n].strip()}.txt", mode="w") as nibu:
        nibu.write(new)
    n += 1