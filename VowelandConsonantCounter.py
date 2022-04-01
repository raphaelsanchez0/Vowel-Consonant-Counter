import PySimpleGUI as sg                        # Part 1 - The import

sg.theme("BlueMono")
# Define the window's contents
layout = [  [sg.Text("Please enter a string")],     
            [sg.InputText(key="-userInput-")],
            [sg.Checkbox("Vowels including Y and W?", default = True, key = "-vowelsCheckbox-")],
            [sg.Text("Vowels:"),sg.Text(key = "-inputVowels-")],
            [sg.Text("Consonants:"),sg.Text(key = "-inputConsonants-")],
            [sg.Button("Count"),sg.Button("Clear")] ]

# Create the window
window = sg.Window('Vowel & Consonant Counter', layout)     

# Display and interact with the Window

vowels  = ['A','E','I','O','U']
vowelsWithwAndy= ['A','E','I','O','U','Y','W']
consonants = ['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z']
constantssWithwAndy =['B', 'C', 'D', 'F', 'G', 'H', 'J', 'K', 'L', 'M', 'N', 'P', 'Q', 'R', 'S', 'T', 'V', 'X', 'Z','Y','W']

while True:
    event, values = window.read()    
    if event == "Count":
        userInputString = values["-userInput-"].upper()
        numOfVowels = 0
        numOfConsonants = 0
        if values["-vowelsCheckbox-"]:
            for i in userInputString:
                for j in vowelsWithwAndy:
                    if i == j:
                        numOfVowels +=1
                for j in consonants:
                    if i == j:
                        numOfConsonants +=1
        else:
            for i in userInputString:
                for j in vowels:
                    if i == j:
                        numOfVowels +=1
                for j in constantssWithwAndy:
                    if i == j:
                        numOfConsonants +=1
        window["-inputVowels-"].update(numOfVowels)
        window["-inputConsonants-"].update(numOfConsonants)
    
    if event == "Clear":
        window["-userInput-"].update("")
        window["-inputVowels-"].update("")
        window["-inputConsonants-"].update("")

    if event == sg.WIN_CLOSED: #closes window if x is pressed
        break

window.close()                             
