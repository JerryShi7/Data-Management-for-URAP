import csv
import pandas


# print("start solving utf-8 problem")
# paths = [
# '10final.csv',
# '11final.csv',
# '12final.csv',
# '13final.csv'
# ]

# for path in paths:
#     with open(path, 'r', encoding='utf-8', errors='ignore') as infile, open(path[:-4] + '2.csv', 'w') as outfile:
#          inputs = csv.reader(infile)
#          output = csv.writer(outfile)
#          for index, row in enumerate(inputs):
#              # Create file with no header
#              output.writerow(row)

# print("finish solving")

#TO DO NUMBER 3
print("Start Read")
df = pandas.read_csv("sc141a_combined.csv")
y98 = pandas.read_csv('98final.csv')
print("Middle Read 1")
y99 = pandas.read_csv('99final.csv')
y00 = pandas.read_csv('00final.csv')
y01 = pandas.read_csv('01final.csv')
y02 = pandas.read_csv('02final.csv')
y03 = pandas.read_csv('03final.csv')# look at errors in the 03 and 04 files at least
y04 = pandas.read_csv('04final.csv')
y05 = pandas.read_csv('05final.csv')
print("Middle Read 2")
y06 = pandas.read_csv('06final.csv')
y07 = pandas.read_csv('07final.csv')
y08 = pandas.read_csv('08final.csv')
y09 = pandas.read_csv('09final.csv')
y10 = pandas.read_csv('10final2.csv')
print("Middle Read 3")
y11 = pandas.read_csv('11final2.csv')
y12 = pandas.read_csv('12final2.csv')
y13 = pandas.read_csv('13final2.csv')
print("Final Read")

dfnew = pandas.DataFrame({'SCH_NAME_NO_SPACES':df['SCH_NAME_NO_SPACES'],
                          'SCH_NAME':df['SCH_NAME']})
print("dataframing for 98")
y98new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y98['SCH_NAME_NO_SPACES'],
                           'NCESSCH98':y98['NCESSCH98'],
                           'STATUS98':y98['STATUS98']})
print("dataframing for 99")
y99new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y99['SCH_NAME_NO_SPACES'],
                           'NCESSCH99':y99['NCESSCH99'],
                           'STATUS99':y99['STATUS99']})
print("dataframing for 00")
y00new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y00['SCH_NAME_NO_SPACES'],
                           'NCESSCH00':y00['NCESSCH00'],
                           'STATUS00':y00['STATUS00']})
print("dataframing for 01")
y01new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y01['SCH_NAME_NO_SPACES'],
                           'NCESSCH01':y01['NCESSCH01'],
                           'STATUS01':y01['STATUS01']})
print("dataframing for 02")
y02new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y02['SCH_NAME_NO_SPACES'],
                           'NCESSCH02':y02['NCESSCH02'],
                           'STATUS02':y02['STATUS02']})
print("dataframing for 03")
y03new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y03['SCH_NAME_NO_SPACES'],
                           'NCESSCH03':y03['NCESSCH03'],
                           'STATUS03':y03['STATUS03']})
print("dataframing for 04")
y04new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y04['SCH_NAME_NO_SPACES'],
                           'NCESSCH04':y04['NCESSCH04'],
                           'STATUS04':y04['STATUS04']})
print("dataframing for 05")
y05new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y05['SCH_NAME_NO_SPACES'],
                           'NCESSCH05':y05['NCESSCH05'],
                           'STATUS05':y05['STATUS05']})
print("dataframing for 06")
y06new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y06['SCH_NAME_NO_SPACES'],
                           'NCESSCH06':y06['NCESSCH06'],
                           'STATUS06':y06['STATUS06']})
print("dataframing for 07")
y07new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y07['SCH_NAME_NO_SPACES'],
                           'NCESSCH07':y07['NCESSCH07'],
                           'STATUS07':y07['STATUS07']})
print("dataframing for 08")
y08new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y08['SCH_NAME_NO_SPACES'],
                           'NCESSCH08':y08['NCESSCH08'],
                           'STATUS08':y08['STATUS08']})
print("dataframing for 09")
y09new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y09['SCH_NAME_NO_SPACES'],
                           'NCESSCH09':y09['NCESSCH09'],
                           'STATUS09':y09['STATUS09']})
print("dataframing for 10")
y10new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y10['SCH_NAME_NO_SPACES'],
                           'NCESSCH10':y10['NCESSCH10'],
                           'STATUS10':y10['STATUS10']})
print("dataframing for 11")
y11new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y11['SCH_NAME_NO_SPACES'],
                           'NCESSCH11':y11['NCESSCH11'],
                           'STATUS11':y11['STATUS11']})
print("dataframing for 12")
y12new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y12['SCH_NAME_NO_SPACES'],
                           'NCESSCH12':y12['NCESSCH12'],
                           'STATUS12':y12['STATUS12']})
print("dataframing for 13")
y13new = pandas.DataFrame({'SCH_NAME_NO_SPACES':y13['SCH_NAME_NO_SPACES'],
                           'NCESSCH13':y13['NCESSCH13'],
                           'STATUS13':y13['STATUS13']})
# dfold = df.loc[:, df.columns != 'SCH_NAME']

#print(type(dfnew), type(dfold), type(y11))
print("Merging 1")
#dfnew.to_csv("dfnew.csv", index = False)
result = pandas.merge(dfnew, y98new, on='SCH_NAME_NO_SPACES')
# print("Merging 2")
# result = pandas.merge(result, y99new, how='left', on='SCH_NAME_NO_SPACES')
# print("Merging 3")
# result = pandas.merge(result, y00new, how='left', on='SCH_NAME_NO_SPACES')
# #result.to_csv("finaloutput11.csv", index = False)
# print("Merging 4")
# result = pandas.merge(result, y01new, how='left', on='SCH_NAME_NO_SPACES')
# print("Merging 5")
# result = pandas.merge(result, y02new, how='left', on='SCH_NAME_NO_SPACES')
# print("Merging 6")
# result = pandas.merge(result, y03new, how='left', on='SCH_NAME_NO_SPACES')
# print("Merging 7")
# result = pandas.merge(result, y04new, how='left', on='SCH_NAME_NO_SPACES')
# print("Merging 8")
# result = pandas.merge(result, y05new, how='left', on='SCH_NAME_NO_SPACES')
# print("Merging 9")
# result = pandas.merge(result, y06new, how='left', on='SCH_NAME_NO_SPACES')
# print("Merging 10")
# result = pandas.merge(result, y07new, how='left', on='SCH_NAME_NO_SPACES')
# print("Merging 11")
# result = pandas.merge(result, y08new, how='left', on='SCH_NAME_NO_SPACES')
# print("Merging 12")
# result = pandas.merge(result, y09new, how='left', on='SCH_NAME_NO_SPACES')
# print("Merging 13")
# result = pandas.merge(result, y10new, how='left', on='SCH_NAME_NO_SPACES')
# print("MMerging14")
# result = pandas.merge(result, y11new, how='left', on='SCH_NAME_NO_SPACES')
# print("Merging 15")
# result = pandas.merge(result, y12new, how='left', on='SCH_NAME_NO_SPACES')
# print("Merging 16")
# result = pandas.merge(result, y13new, how='left', on='SCH_NAME_NO_SPACES')
print("Done Merge")
# 
#result = pandas.append([dfold, result], axis = 1)

# print('start')
result.to_csv("finaloutput11.csv", index = False)
print('finish')











