#Date: 11/3/24
#Author: Michael Walczak
#Numerology Class Module

class Numerology:
    def __init__(self, sName:str, sDOB:str)->object:

        self.__sName = sName
        self.setDOB(sDOB)

        self.__dictCharacters = {("A", "J", "S"):1,
                                 ("B", "K", "T"):2,
                                 ("C", "L", "U"):3,
                                 ("D", "M", "V"):4,
                                 ("E", "N", "W"):5,
                                 ("F", "O", "X"):6,
                                 ("G", "P", "Y"):7,
                                 ("H", "Q", "Z"):8,
                                 ("I", "R")     :9}

    def _reduceNumberDecorator(func):
        def wrapper(self):
            iResult:int = func(self)
            def reduceNumber(iNumber:int):
                if iNumber < 10: return iNumber
                return reduceNumber(sum(int(digit) for digit in str(iNumber)))
            return reduceNumber(iResult)
        return wrapper

    def getName(self)->str: return self.__sName
    def getDOB(self)->str: return self.__sDOB

    def setName(self, sName:str)->None: self.__sName = sName
    def setDOB(self, sDOB:str)->None: 
        self.__sDOB = sDOB
        self.__nDOB = sDOB.replace("-", "").replace("/", "")
    
    @_reduceNumberDecorator
    def getLifePath(self)->int: return sum(int(sNum) for sNum in self.__nDOB)

    @_reduceNumberDecorator
    def getBirthDay(self)->int: return sum(int(digit) for digit in self.__nDOB[2:4])

    @_reduceNumberDecorator
    def getAttitude(self)->int: return sum(int(digit) for digit in self.__nDOB[:4])
    
    @_reduceNumberDecorator
    def getSoul(self)->int: return sum(value for sLetter in self.getName().upper() if sLetter in "AEIOU" for key, value in self.__dictCharacters.items() if sLetter in key)
    
    @_reduceNumberDecorator
    def getPersonality(self)->int: return sum(value for sLetter in self.getName().upper() if sLetter not in "AEIOU" for key, value in self.__dictCharacters.items() if sLetter in key)
    
    @_reduceNumberDecorator
    def getPower(self)->int: return self.getSoul() + self.getPersonality()

    Name = property(fget = getName,
                    fset = setName)
                  
    DOB = property(fget = getDOB,
                   fset = setDOB)

    def __str__(self): return \
        f"\n{'Name: ':15s}{self.Name}\
        \n{'DOB: ':15s}{self.DOB}\
        \n{'Life Path: ':15s}{self.getLifePath()}\
        \n{'Birth Day: ':15s}{self.getBirthDay()}\
        \n{'Attitude: ':15s}{self.getAttitude()}\
        \n{'Soul: ':15s}{self.getSoul()}\
        \n{'Personality: ':15s}{self.getPersonality()}\
        \n{'Power: ':15s}{self.getPower()}"