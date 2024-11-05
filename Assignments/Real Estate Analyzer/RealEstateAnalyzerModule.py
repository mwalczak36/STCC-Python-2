#Date: 10/15/24
#Author: Michael Walczak
#Real Estate Analyzer Module

import csv

def getDataInput(sFileName:str)->tuple[list, list[list]]:
    with open(sFileName, "r") as file:
        reader = csv.reader(file)
        lstHeader = next(reader)
        lstData = [row for row in reader]
    return (lstHeader, lstData)

def getMedian(lstListOfNumbers:list)->float:

    lstListOfNumbers.sort()
    iListLength = len(lstListOfNumbers)
    if iListLength % 2 == 0: fMedian = (lstListOfNumbers[(iListLength // 2) - 1] + lstListOfNumbers[iListLength // 2]) / 2
    else: fMedian = lstListOfNumbers[iListLength // 2]
    return fMedian

def main():
    
    lstHeader, lstData = getDataInput("RealEstateData.csv")
    lstCitys, lstPropertyTypes, lstPrices, dictCitys, dictZips, dictPropertyTypes = [], [], [], {}, {}, {}

    for row in lstData:
        sCity, sZip, sPropertyType, fPrice = row[1], row[2], row[7], float(row[8])
        if sCity not in lstCitys: lstCitys.append(sCity)
        if sPropertyType not in lstPropertyTypes: lstPropertyTypes.append(sPropertyType)
        lstPrices.append(fPrice)
        dictCitys[sCity] = dictCitys.get(sCity, 0) + fPrice
        dictZips[sZip] = dictZips.get(sZip, 0) + fPrice
        dictPropertyTypes[sPropertyType] = dictPropertyTypes.get(sPropertyType, 0) + fPrice

    print(f"\n{'Minimum':20s}{min(lstPrices):15,.2f}")
    print(f"{'Maximum':20s}{max(lstPrices):15,.2f}")
    print(f"{'Sum':20s}{sum(lstPrices):15,.2f}")
    print(f"{'Avg':20s}{sum(lstPrices)/len(lstPrices):15,.2f}")
    print(f"{'Median':20s}{(lambda lst: (sorted(lst)[len(lst) // 2] if len(lst) % 2 != 0 else (sorted(lst)[len(lst) // 2] + sorted(lst)[len(lst) // 2 - 1]) / 2)) (lstPrices):15,.2f}")
    
    print("\nSummary by Property Type:")
    for propertyType, fTotal in dictPropertyTypes.items(): print(f"{propertyType:20s}{fTotal:15,.2f}")
    
    print("\nSummary by City:")
    for sCity, fTotal in dictCitys.items(): print(f"{sCity:20s}{fTotal:15,.2f}")
    
    print("\nSummary by Zips:")
    for sZip, fTotal in dictZips.items(): print(f"{sZip:20s}{fTotal:15,.2f}")
main()