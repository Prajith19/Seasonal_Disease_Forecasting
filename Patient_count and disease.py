import numpy as np
import pandas as pd

data=pd.read_csv("D:/combined/newtest.csv")
che = pd.read_csv("D:\combined\chennai.csv")
mad = pd.read_csv("D:\combined\madurai.csv")
tan = pd.read_csv("D:/combined/tanjore.csv")
tot = pd.read_csv("D:/combined/total.csv")
desicion = pd.read_csv("D:/combined/decision.csv")


#Leap Year
def is_leap_year(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                return True
            else:
                return False
        else:
            return True
    else:
        return False
    
#monthly average
print("Facility data available:- chennai, madurai, tanjore")
print("[to know the total_count type 'total_count']")    
res = []
facility = input("Enter the facility name:- ")
given_month = int(input("Enter the month-: "))
word_month=[]
if given_month == 1:
    word_month = 'January'
elif given_month == 2:
    word_month = "February"
elif given_month == 3:
    word_month = "March"
elif given_month == 4:
    word_month = 'April'
elif given_month == 5:
    word_month = 'May'
elif given_month == 6:
    word_month = 'June'
elif given_month == 7:
    word_month = 'July'
elif given_month == 8:
    word_month = 'August'
elif given_month == 9:
    word_month = 'September'
elif given_month == 10:
    word_month = 'October'
elif given_month == 11:
    word_month = 'November'
elif given_month == 12:
    word_month = 'December'
    
year = int(input("Enter the year:- "))
if given_month in [1,3,5,7,8,10,12]:
  days = 31
elif given_month in [4,6,9,11]:
  days = 30
else:
  days = 28

def find_ind(given_month,j,i):
  return data[data['admit_date'] == str(given_month)+'/'+str(j)+'/'+str(i)].index[0]

for i in range(1970,2023):
  prev = 0
  for j in range(1,days+1):
    index = find_ind(given_month,j,i)
    prev += data[facility][index]

  if given_month == 2 and is_leap_year(i):
    index = find_ind(2,29,i)
    prev += data[facility][index]
  res.append(prev)
print("             ")
print(f'Raw data:- {res}')
avg = sum(res)/len(res)
avg_round = round(avg,0)
print("                 ")
print(f'Mentioned facility:- {facility}')
print(f'Predicted patients in {word_month}:- {avg_round}')

#Disease vise monthly average (chennai)
print("                        ")
print("Disease data available:- flu, covid, malaria, others")
if facility == "chennai":
    res = []
    summa = []
    loop = True
    while loop:
        facility = input("Enter the Disease name:- ")
        if given_month in [1,3,5,7,8,10,12]:
          days = 31
        elif given_month in [4,6,9,11]:
          days = 30
        else:
          days = 28
    
        def find_ind(given_month,j,i):
          return che[che['admit_date'] == str(given_month)+'/'+str(j)+'/'+str(i)].index[0]
    
        for i in range(1970,2023):
          prev = 0
          for j in range(1,days+1):
            index = find_ind(given_month,j,i)
            prev += che[facility][index]
    
          if given_month == 2 and is_leap_year(i):
            index = find_ind(2,29,i)
            prev += che[facility][index]
          res.append(prev)
        print("          ")
        print(f'Raw data:- {res}')
        avg = sum(res)/len(res)
        avg_round = round(avg,0)
        print("                 ")
        print(f'Mentioned Disease:- {facility}')
        print(f'Predicted patients in {word_month}:- {avg_round}')
        end = input("Want to continue(Y/N):- ").upper()
        if end == 'Y':
            res.clear()
            summa.append(avg_round)
        elif end == 'N':
            summa.append(avg_round)
            loop = False
        else:
            res.clear()
            summa.append(avg_round)

#Disease vise monthly average (madurai)            
elif facility == "madurai":
    res = []
    summa = []
    loop = True
    while loop:
        facility = input("Enter the Disease name:- ")
        if given_month in [1,3,5,7,8,10,12]:
          days = 31
        elif given_month in [4,6,9,11]:
          days = 30
        else:
          days = 28
    
        def find_ind(given_month,j,i):
          return mad[mad['admit_date'] == str(given_month)+'/'+str(j)+'/'+str(i)].index[0]
    
        for i in range(1970,2023):
          prev = 0
          for j in range(1,days+1):
            index = find_ind(given_month,j,i)
            prev += mad[facility][index]
    
          if given_month == 2 and is_leap_year(i):
            index = find_ind(2,29,i)
            prev += mad[facility][index]
          res.append(prev)
        print("           ")
        print(f'Raw data:- {res}')
        avg = sum(res)/len(res)
        avg_round = round(avg,0)
        print("                 ")
        print(f'Mentioned Disease:- {facility}')
        print(f'Predicted patients in {word_month}:- {avg_round}')
        end = input("Want to continue(Y/N):- ").upper()
        if end == 'Y':
            res.clear()
            summa.append(avg_round)
        elif end == 'N':
            summa.append(avg_round)
            loop = False
        else:
            res.clear()
            summa.append(avg_round)
            

#Disease vise monthly average (tanjore)
elif facility == "tanjore":
    res = []
    summa = []
    loop = True
    while loop:
        facility = input("Enter the Disease name:- ")
        if given_month in [1,3,5,7,8,10,12]:
          days = 31
        elif given_month in [4,6,9,11]:
          days = 30
        else:
          days = 28
    
        def find_ind(given_month,j,i):
          return tan[tan['admit_date'] == str(given_month)+'/'+str(j)+'/'+str(i)].index[0]
    
        for i in range(1970,2023):
          prev = 0
          for j in range(1,days+1):
            index = find_ind(given_month,j,i)
            prev += tan[facility][index]
    
          if given_month == 2 and is_leap_year(i):
            index = find_ind(2,29,i)
            prev += tan[facility][index]
          res.append(prev)
        print("         ")
        print(f'Raw data:- {res}')
        avg = sum(res)/len(res)
        avg_round = round(avg,0)
        print("                 ")
        print(f'Mentioned Disease:- {facility}')
        print(f'Predicted patients in {word_month}:- {avg_round}')
        end = input("Want to continue(Y/N):- ").upper()
        if end == 'Y':
            res.clear()
            summa.append(avg_round)
        elif end == 'N':
            summa.append(avg_round)
            loop = False
        else:
            res.clear()
            summa.append(avg_round)

#Disease vise monthly average (total_count)
elif facility == "total_count":
    res = []
    summa = []
    loop = True
    while loop:
        facility = input("Enter the Disease name:- ")
        if given_month in [1,3,5,7,8,10,12]:
          days = 31
        elif given_month in [4,6,9,11]:
          days = 30
        else:
          days = 28
    
        def find_ind(given_month,j,i):
          return tot[tot['admit_date'] == str(given_month)+'/'+str(j)+'/'+str(i)].index[0]
    
        for i in range(1970,2023):
          prev = 0
          for j in range(1,days+1):
            index = find_ind(given_month,j,i)
            prev += tot[facility][index]
    
          if given_month == 2 and is_leap_year(i):
            index = find_ind(2,29,i)
            prev += tot[facility][index]
          res.append(prev)
        print("          ")
        print(f'Raw data:- {res}')
        avg = sum(res)/len(res)
        avg_round = round(avg,0)
        print("                 ")
        print(f'Mentioned Disease:- {facility}')
        print(f'Predicted patients in {word_month}:- {avg_round}')
        end = input("Want to continue(Y/N):- ").upper()
        if end == 'Y':
            res.clear()
            summa.append(avg_round)
        elif end == 'N':
            summa.append(avg_round)
            loop = False
        else:
            res.clear()
            summa.append(avg_round)




#Prediction of the highest disease in that month    
ind = desicion.drop('admit_date',axis='columns')
indep = ind.drop('highest',axis='columns')

d = desicion.drop('admit_date',axis='columns')
de = d.drop('flu',axis='columns')
dep = de.drop('covid',axis='columns')
depe = dep.drop('malaria',axis='columns')
dept = depe.drop('others',axis='columns')
from sklearn import tree
model=tree.DecisionTreeClassifier()

model.fit(indep,dept)
model.score(indep,dept)

#visualization    
from sklearn import tree
import matplotlib.pyplot as plt
fig = fig = plt.figure(figsize=(300,50))
print(tree.plot_tree((model),filled=1))
    
print("                                                                              ")
print(f'Predicted Flu count:- {summa[0]}')
print(f'Predicted Covid count:- {summa[1]}')
print(f'Predicted Malaria count:- {summa[2]}')
print(f'Predicted Other Disease count:- {summa[3]}')

decision = model.predict([summa])

print("                ")
if decision == 1:
    print(f'Description:- Flu is predicted to be more in {word_month} {year}')
elif decision == 2:
    print(f'Description:- Covid is predicted to be more in {word_month} {year}')
elif decision == 3:
    print(f'Description:- Malaria is predicted to be more in {word_month} {year}')
elif decision == 4:
    print(f'Description:- Other Diseases are predicted to be more in {word_month} {year}')
    
    


    
