#Date: 10/12/24
#Author: Michael Walczak
#Input Prompt Validation Module
def validateNumericInput(sPrompt:str = "Enter Number: ", bAllowZero:bool = False)->tuple[float, bool]:
    fNumber = -1
    while (bAllowZero and fNumber < 0) or (not bAllowZero and fNumber <= 0):
        try: fNumber = float(input(sPrompt))
        except ValueError: print("Invalid input.")
    return (fNumber, bAllowZero)