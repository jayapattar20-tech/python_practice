
"""def check_marks(marks):
    if marks>=40:
        return "pass"
    else:
        return "fail"

#marks=int(input("enter the marks "))
print(check_marks(78))
print(check_marks(0))
print(check_marks(29))   

messages = ["claim your prize now", " claim meeting at 5pm", "urgent kyc verification needed", "lunch tomorrow?"]

def count_urgent(messages):
    count=0
    for mess in messages:
        if "urgent" not in mess and "claim" not in mess:
            continue
        else:
            count+=1
    return count

print(count_urgent(messages))

scam_msg={
    "text":"urgent kyc verification needed",
    "is_scam":True,
    "reason":"use urgency and KYC scam keywords"
}
for key,value in scam_msg.items():
    print(key,":",value)




def show_scams(data):
    scams=[]
    for items in data:
        if items["is_scam"]==True:
            scams.append(items)
    return scams
        
data = [
    {"text": "claim your prize now", "is_scam": True, "reason": "urgent claim language"},
    {"text": "meeting at 5pm", "is_scam": False, "reason": "normal message"},
    {"text": "urgent kyc verification needed", "is_scam": True, "reason": "urgent + kyc keyword"},
    {"text": "lunch tomorrow?", "is_scam": False, "reason": "normal message"},
]
res=show_scams(data)
for r in res:
    print(r["text"],"-",r["reason"])
#print(show_scams(data))

#Q1
def square(n):
    return n*n
print(square(5))
print(square(10))
print(square(1))
print(square(6))
print(square(3))

#q2
def is_even(n):
    if n%2==0:
        return True
    else:
        return False
print(is_even(45))
print(is_even(42))

#Q3. Write a function average(numbers) that takes a list of numbers and returns their average.
def average(num):
    sum=0
    for i in num:
        sum+=i
    return sum/len(num)
num=(10,20,30,40)
print(average(num))

#Q4. Given nums = [4, 9, 2, 7, 1, 8], write code to find and print the largest and smallest number without using max()/min() (use a loop instead — builds real understanding).
nums = [4, 9, 2, 7, 1, 8]
large=nums[0]
small=nums[0]
def find(nums):
    large=nums[0]
    small=nums[0]
    for i in nums:
        if i<small:
            small=i
        #return small
        if i>large:
            large=i
        #return large
    return small,large

smallest,largest=find(nums)
print(smallest)
print(largest)

#Q5. Given a list of words, write a function longest_word(words) that returns the longest word in the list.
def longest_word(words):
    long=len(words[0])
    long_word=words[0]
    for word in words:
        if len(word)>long:
            long=len(word)
            long_word=word

    return long_word

words = ["apple", "kiwi"]
print(longest_word(words))

#Q6. Remove all duplicate values from a list nums = [1, 2, 2, 3, 4, 4, 5] and print the result (hint: look up what a set is).
nums = [1, 2, 2, 3, 4, 4, 5]
print(set(nums))

#Q7. Create a dictionary that counts how many times each word appears in this sentence:
sentence = "urgent urgent claim now claim your prize now"
new_sen=sentence.split()
print(new_sen)
freq={}
for word in new_sen:
    if word not in freq:
        freq[word]=1
    else:
        freq[word]+=1
print(freq)

#Q8. Given this dictionary of student marks:
#marks = {"Jay": 85, "Ravi": 42, "Priya": 91, "Anil": 38}
#Write code to print only the names who scored below 40 (fail cases).
marks = {"Jay": 85, "Ravi": 42, "Priya": 91, "Anil": 38}
for key,value in marks.items():
    if marks[key]<40:
        print(key)

#Q9: Write a function find_triggers(message, keywords) that returns a list of which keywords were actually found in the message.
keywords = ["urgent", "claim", "verify", "kyc", "prize", "winner"]
message = ["urgent kyc verification needed to claim your prize","you are the winner, now"]
def find_triggers(message, keywords):
    found=[]
    for key in keywords:
        if key in message:
            found.append(key)
    return found

def classify(message, keywords):
    match=find_triggers(message,keywords)
    if len(match)>=2:
        return {"is_spam":True,"matched":match}
    else:
        return{"is_spam":False,"matched":match}
for msg in message:
    res=classify(msg,keywords)
    print(res) 
# to-do-list code 
tasks = []
task=0
def add(tasks,task):
    tasks.append({"task":task,"done":False})
def view(tasks):
    if len(tasks)==0:
        print("no task yet")
    else:
        print("your tasks are :",tasks)
def remove(tasks,taskno):
    if taskno<1 or taskno>len(tasks):
        print("invalid task no")
    else:
        del tasks[taskno-1]
def done(tasks,taskdone):
    if taskdone<1 or taskdone>len(tasks):
        print("invalid taskno")
    else:
        tasks[taskdone-1]["done"]=True
    

while True:
    print("1.add task\n2.view task\n3.remove task\n4.exit")
    choice=input("enter your choice:")
    if choice=="1":
        task=input("enter the task")
        add(tasks,task)
    elif choice=="2":
        view(tasks)
    elif choice=="3":
        taskno=int(input("enter choice no to remove"))
        remove(tasks,taskno)
    elif choice=="4":
        print("goodbye!")
        break
    elif choice=="5":
        taskdone=int(input("enter task done number"))
        done(tasks,taskdone)
    else:
        print("invalid choice")

tasks = []

def add(tasks, task):
    tasks.append({"task": task, "done": False})

def view(tasks):
    if len(tasks) == 0:
        print("no task yet")
    else:
        for i, t in enumerate(tasks, start=1):
            status = "✔" if t["done"] else "✘"
            print(f"{i}. {t['task']} [{status}]")

def remove(tasks, taskno):
    if taskno < 1 or taskno > len(tasks):
        print("invalid task no")
    else:
        del tasks[taskno-1]

def done(tasks, taskdone):
    if taskdone < 1 or taskdone > len(tasks):
        print("invalid task no")
    else:
        tasks[taskdone-1]["done"] = True

while True:
    print("1.add task\n2.view task\n3.remove task\n4.exit\n5.mark task done")
    choice = input("enter your choice:")
    if choice == "1":
        task = input("enter the task")
        add(tasks, task)
    elif choice == "2":
        view(tasks)
    elif choice == "3":
        taskno = int(input("enter choice no to remove"))
        remove(tasks, taskno)
    elif choice == "4":
        print("goodbye!")
        break
    elif choice == "5":
        taskdone = int(input("enter task done number"))
        done(tasks, taskdone)
    else:
        print("invalid choice")

with open("notes.txt","w") as file:
    file.write("this is my first line")
    file.write("\n")
    file.write("this is file handling")

with open("notes.txt","r") as file:
    content=file.read()
    print(content)

with open("notes.txt","r") as file:
    for line in file:
        print(line.strip())
        

with open("notes.txt","a") as file:
    file.write("adding new line to file ")

with open("notes.txt","r") as file:
    for line in file:
        print(line.strip())

import csv
with open("message.csv","w",newline="")as file:
    writer=csv.writer(file)
    writer.writerow(["message","is_scam"])
    writer.writerow(["claim your prize","True"])
    writer.writerow(["meeting at 5pm","False"])

with open("message.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        print(row)


tasks = []

def add(tasks, task):
    tasks.append({"task": task, "done": False})
    with open("tasks.txt","a") as file:
        file.write(task)

def view(tasks):
    if len(tasks) == 0:
        print("no task yet")
    else:
        for i, t in enumerate(tasks, start=1):
            status = "✔" if t["done"] else "✘"
            print(f"{i}. {t['task']} [{status}]")

def remove(tasks, taskno):
    if taskno < 1 or taskno > len(tasks):
        print("invalid task no")
    else:
        del tasks[taskno-1]

def done(tasks, taskdone):
    if taskdone < 1 or taskdone > len(tasks):
        print("invalid task no")
    else:
        tasks[taskdone-1]["done"] = True

while True:
    print("1.add task\n2.view task\n3.remove task\n4.exit\n5.mark task done")
    choice = input("enter your choice:")
    if choice == "1":
        task = input("enter the task")
        add(tasks, task)
    elif choice == "2":
        view(tasks)
    elif choice == "3":
        taskno = int(input("enter choice no to remove"))
        remove(tasks, taskno)
    elif choice == "4":
        print("goodbye!")
        break
    elif choice == "5":
        taskdone = int(input("enter task done number"))
        done(tasks, taskdone)
    else:
        print("invalid choice")

with open("tasks.txt","r") as file:
    tasklist=file.readlines()
    print(tasklist)
import csv

with open("messages.csv","w",newline="") as file:
    writer=csv.writer(file)
    writer.writerow(["message","is_scam"])
    writer.writerow(["claim your prize now", "True"])
    writer.writerow(["meeting at 5pm", "False"])
    writer.writerow(["claim your prize now", "True"])
    writer.writerow(["meeting at 5pm", "False"])
    writer.writerow(["claim your prize now", "True"])
    writer.writerow(["meeting at 5pm", "False"])

with open("messages.csv","r") as file:
    reader=csv.reader(file)
    for row in reader:
        if row[1]=="true":
            print(row)"""
        
    
#import csv
import pandas as pd
df=pd.read_csv("messages.csv")
#print(df)
print(df.head())
print(df.columns)
print(df["message"])



scam_only=df[df["is_scam"]=="True"]
print(scam_only)

print(df["is_scam"].value_counts())
sorted=df.sort_values("message")
print(sorted)