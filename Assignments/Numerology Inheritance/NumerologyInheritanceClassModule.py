#Date: 11/3/24
#Author: Michael Walczak
#Numerology Class Module

class Numerology:
    def __init__(self, sName:str, sDOB:str)->object:

        self.__sName = sName
        self.DOB = sDOB

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

    @property
    def Name(self)->str: return self.__sName

    @property
    def DOB(self)->str: return self.__sDOB

    @Name.setter
    def Name(self, sName:str)->None: self.__sName = sName

    @DOB.setter
    def DOB(self, sDOB:str)->None: 
        self.__sDOB = sDOB
        self.__nDOB = sDOB.replace("-", "").replace("/", "") # 03101995
    
    @_reduceNumberDecorator
    def _getLifePath(self)->int: return sum(int(sNum) for sNum in self.__nDOB)

    @_reduceNumberDecorator
    def _getBirthDay(self)->int: return sum(int(digit) for digit in self.__nDOB[2:4])

    @_reduceNumberDecorator
    def _getAttitude(self)->int: return sum(int(digit) for digit in self.__nDOB[:4])
    
    @_reduceNumberDecorator
    def _getSoul(self)->int: return sum(value for sLetter in self.Name.upper() if sLetter in "AEIOU" for key, value in self.__dictCharacters.items() if sLetter in key)
    
    @_reduceNumberDecorator
    def _getPersonality(self)->int: return sum(value for sLetter in self.Name.upper() if sLetter not in "AEIOU" for key, value in self.__dictCharacters.items() if sLetter in key)
    
    @_reduceNumberDecorator
    def _getPower(self)->int: return self._getSoul() + self._getPersonality()

    def __str__(self): return \
        f"\n{'Name: ':25s}{self.Name}\
        \n{'DOB: ':25s}{self.DOB}\
        \n{'Life Path: ':25s}{self._getLifePath()}\
        \n{'Birth Day: ':25s}{self._getBirthDay()}\
        \n{'Attitude: ':25s}{self._getAttitude()}\
        \n{'Soul: ':25s}{self._getSoul()}\
        \n{'Personality: ':25s}{self._getPersonality()}\
        \n{'Power: ':25s}{self._getPower()}"


class NumerologyExtended(Numerology):
    
    def __init__(self, sName: str, sDOB: str) -> object:

        Numerology.__init__(self, sName, sDOB)

        self.__lifePathDescriptions = {

            1: "The Independent: Wants to work/think for themselves",
            2: "The Mediator: Avoids conflict and wants love and harmony",
            3: "The Performer: Likes music, art and to perform or get attention",
            4: "The Teacher/Truth Seeker: Is meant to be a teacher or mentor and is truthful",
            5: "The Adventurer: Likes to travel and meet others, often a extrovert",
            6: "The Inner Child: Is meant to be a parent and/or one that is young at heart",
            7: "The Naturalist: Enjoy nature and water and alternative life paths, open to spirituality",
            8: "The Executive: Gravitates to money and power",
            9: "The Humanitarian: Helps others and/or experiences pain and learns the hard way"}

    def _getLifePathDescription(self)->str: return self.__lifePathDescriptions.get(self._getLifePath())

    def __str__(self): return \
        f"{Numerology.__str__(self)}\
        \n{'Life Path Description: ':25s}{self._getLifePathDescription()}\n"
