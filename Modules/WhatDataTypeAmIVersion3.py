#Author:  Prof. Candido
#Purpose: What Data Type Am I

def getDataType(sToCheck):
    try:     
        # if both the same the number is an int need it here in case you enter 0
        if int(sToCheck) == float(sToCheck):
            return int(sToCheck), 'int'
    except:
       # if not int check to see if it is a float:
       try:
            return float(sToCheck), 'float'
       # it must between a bool and a string: 
       except:
            if sToCheck in ["True","False"]:
               return True if sToCheck == "True" else False, 'boolean'
            else:
                # it must a string: 
                return sToCheck, 'str'


