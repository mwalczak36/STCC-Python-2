#Date: 10/9/24
#Author: Michael Walczak
#Inter Planetary Weights Module

import pickle

def loadDictionary(sFileName:str)->tuple[dict]:
    dictPlanetHistory = {}
    try:
        with open(sFileName, "rb") as file: dictPlanetHistory = pickle.load(file) #3
    except: print("No file found")
    if input("Would you like to see the history? y/n: ").lower() == "y": #4
        dictWeights:dict
        for name, dictWeights in dictPlanetHistory.items():
            print(f"\n{name}, here are your weights on Solar System's planets")
            for planet, weight in dictWeights.items():
                print(f"Weight on {planet:10s} {weight:10,.2f}") #7
    return (dictPlanetHistory,)

def validateNumericInput(sPrompt:str, bAllowZero:bool = False)->tuple[float, bool]:
    fNumber = -1
    while (bAllowZero and fNumber < 0) or (not bAllowZero and fNumber <= 0):
        try: fNumber = float(input(sPrompt))
        except ValueError: print("Invalid input.")
    return (fNumber, bAllowZero)

def getEntrys(dictPlanetHistory:dict, sFileName:str):

    dictPlanetWeightFactors = { #2

        "Mercury" :0.38,
        "Venus"   :0.91, 
        "Moon"    :0.165, 
        "Mars"    :0.38, 
        "Jupiter" :2.34, 
        "Saturn"  :0.93, 
        "Uranus"  :0.92, 
        "Neptune" :1.12, 
        "Pluto"   :0.066
    }

    while True: #5
        sName = input("Enter a name: ").title()
        if not sName: break
        if sName in dictPlanetHistory: continue
        fWeight = validateNumericInput("Enter Weight: ")[0]
        dictPlanetHistory[sName] = {planet : fWeight * factor for planet, factor in dictPlanetWeightFactors.items()}

    with open(sFileName, "wb") as file: pickle.dump(dictPlanetHistory, file) #6