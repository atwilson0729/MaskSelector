import pandas as pd
data = pd.read_csv("MasksWithFeatures_4_20_2021_225.csv")
data = data.assign(score = 0)

answerList = ['reusable', 'cotton', 'large', 'mens', 'blue', '2-ply', 'adjustable']
# size 8
#color 9
# material 10
# filter type 11
# gender 12
# dispos 13
# earloop 14
# score 15
filters = {'disposability': ['disposable', 'reusable', 'NA'],
           'material': ['non-woven melt-spray', 'NA', 'mixed material', 'polyester', 'cotton', 'melt-blown', 'spandex'],
           'size': ['adult', 'large', 'childrens', 'universal', 'medium', 'suitable for most', 'small', 'one size fits most', 'girl', 'boy', 'x-large'],
           'gender': ['unisex', 'mens', 'womens', 'boys', 'girls'],
           'color': ['blue', 'red', 'black', 'various', 'NA', 'colorful', 'grey', 'purple', 'pink', 'floral', 'green', 'navy', 'yellow', 'plaid', 'grey'],
           'filter type': ['3 layer', 'NA', '3-ply', '3 ply', 'kn95', '3-layers', 'filter pocket', '2-ply', '5-ply', '4-ply', '4 ply'],
           'earloop':['elastic', 'NA', 'adjustable']}

# This function scores each item in the dataset
# Different features have different weights based on the importance
def score(filterList):
    newDf = data.copy()
    for i, row in newDf.iterrows():
        if row[13] == filterList[0]: #disposability
            newDf.at[i, 'score'] += 3
        if filterList[0] == 'reusable': #pass if disposable
            if filterList[1] in str(row[10]): #material
                newDf.at[i, 'score'] += 1
        if filterList[2] in str(row[8]): #size
            newDf.at[i, 'score'] += 2
        if row[12] == filterList[3]: #gender
            newDf.at[i, 'score'] += 1
        if row[9] == filterList[4]: #color
            newDf.at[i, 'score'] += 1
        if row[11] == filterList[5]: #filtertype
            newDf.at[i, 'score'] += 1
        if row[14] == filterList[6]: #earloops
            newDf.at[i, 'score'] += 1

    return newDf

def sort(copyDf):
    copyDf.sort_values(by = 'score', ascending=False, inplace = True)
    return copyDf

def top10(copyDf):
    n = 0
    topStr = ''
    for i, row in copyDf.iterrows():
        topStr += '\nhttps://www.amazon.com' + copyDf.at[i, 'link']
        n += 1
        if n == 10:
            return topStr
dataScore = score(answerList)
sortedDf = sort(dataScore)
print(top10(sortedDf))

# print(sortedDf.head(n = 25))

print(sortedDf.keys())
uniqSize = sortedDf['size'].unique()
print(uniqSize, ', ')
uniqColor = sortedDf['color'].unique()
print(uniqColor, ', ')
uniqMaterial = sortedDf['material'].unique()
print(uniqMaterial, ', ')
uniqFilter = sortedDf['filter type'].unique()
print(uniqFilter, ', ')
uniqGender = sortedDf['gender'].unique()
print(uniqGender, ', ')
uniqDispos = sortedDf['disposability'].unique()
print(uniqDispos, ', ')
uniqEarloop = sortedDf['earloop'].unique()
print(uniqEarloop, ', ')

csvOut = sortedDf.to_csv("Sorted_material_5_7.csv", index = True)

