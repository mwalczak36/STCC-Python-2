#Date: 10/15/24
#Author: Michael Walczak
#Real Estate Analyzer Module

import csv

def getDataInput(sFileName:str)->tuple[list, list]:
    with open(sFileName, "r") as file:
        reader = csv.reader(file)
        lstHeader = next(reader)
        lstData = [row for row in reader]
    return (lstHeader, lstData)

def main():
    lstHeader, lstData = getDataInput("RealEstateData.csv")

    lstCitys, lstPropertyTypes, lstPrices, dictCitys, dictZips, dictPropertyTypes = [], [], [], {}, {}, {}
   
    for row in lstData:

        sCity = row[1]
        sZip = row[2]
        sPropertyType = row[7]
        fPrice = float(row[8])

        if sCity not in lstCitys: lstCitys.append(sCity)
        if sPropertyType not in lstPropertyTypes: lstPropertyTypes.append(sPropertyType)
        lstPrices.append(fPrice)

        dictCitys[sCity] = dictCitys.get(sCity, 0) + fPrice
        dictZips[sZip] = dictZips.get(sZip, 0) + fPrice
        dictPropertyTypes[sPropertyType] = dictPropertyTypes.get(sPropertyType, 0) + fPrice

    print(f"\n{'Minimum':15s}{min(lstPrices):15,.2f}")
    print(f"{'Maximum':15s}{max(lstPrices):15,.2f}")
    print(f"{'Sum':15s}{sum(lstPrices):15,.2f}")
    print(f"{'Avg':15s}{sum(lstPrices)/len(lstPrices):15,.2f}")
    print(f"{'Median':15s}{(lambda lst: (sorted(lst)[len(lst) // 2] if len(lst) % 2 != 0 else (sorted(lst)[len(lst) // 2] + sorted(lst)[len(lst) // 2 - 1]) / 2)) (lstPrices):15,.2f}")

    print("\nSummary by Property Type:")
    for propertyType, fTotal in dictPropertyTypes.items(): print(f"{propertyType:15s}{fTotal:15,.2f}")
    print()

    for sCity, fTotal in dictCitys.items(): print(f"{sCity:15s}{fTotal:15,.2f}")
    print()

main()