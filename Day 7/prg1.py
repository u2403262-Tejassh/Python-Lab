import csv
male_count = 0
female_count = 0
survived = 0
print("DISPLAYING DATABASE:\n")
with open("titanic.csv",'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        print(row)
        if row[1] == '1':
            survived+=1
        if row[4] == "male":
            male_count+=1
        if row[4] == "female":
            female_count+=1
print("Number of males: ",male_count)
print("Number of females: ",female_count)
print("DISPLAYING FEMALE DETAILS:\n")
with open("titanic.csv",'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
        if row[4] == "female":
            print(row)
print("Number of survivors: ",survived)
print("DISPLAYING SURVIVOR DETAILS:\n")
with open("titanic.csv",'r') as file:
    csv_reader = csv.reader(file)
    for row in csv_reader:
            if row[1] == '1':
                print(row)
