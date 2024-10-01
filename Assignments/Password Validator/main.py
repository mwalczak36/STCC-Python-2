#Date: 9/30/24
#Author: Michael Walczak
#Password Validator

sName = input("Enter first and last name: ").title() #1
#sName = "michael walczak".title()
sInitials = sName[0] + sName[sName.find(" ") + 1] #4
sPassword = ""

bIsValid = bLength = bPass = bInitials = bUpper = bLower = bDigit = bSpecial = bCount = False

while not bIsValid: #2
    dictCharacters = {}
    sPassword = input("Enter Password: ") #3
    if not sPassword: break

    bLength = True if len(sPassword) in range(8, 13) else print("Password must be between 8 and 12 characters.") #5
    bPass = True if not sPassword.lower().startswith("pass") else print("Password can't start with Pass") #6
    bInitials = True if not sInitials.lower() in sPassword.lower() else print("Password must not contain user initials") #11

    for char in sPassword:
        if char.isupper():   bUpper = True
        if char.islower():   bLower = True
        if char.isdigit():   bDigit = True
        if char in "!@#$%^": bSpecial = True
        iCount = sPassword.lower().count(char)
        if iCount > 1: dictCharacters[char.lower()] = iCount

    if not bUpper: print("Password must contain at least 1 uppercase letter.") #7
    if not bLower: print("Password must contain at least 1 lowercase letter.") #8
    if not bDigit: print("Password must contain at least 1 number.") #9
    if not bSpecial: print("Password must contain at least 1 of these special characters: ! @ # $ % ^ ") #10
    bCount = True if not bool(dictCharacters) else print(f"These characters occur twice:\n{dictCharacters}") #12

    if bLength and bPass and bInitials and bUpper and bLower and bDigit and bSpecial and bCount: bIsValid = True
print(f"\nName: {sName}\nInitails: {sInitials}\nPassword: {sPassword}")
print("Password is valid and OK to use\n")