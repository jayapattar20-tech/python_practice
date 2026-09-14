
def check_marks(marks):
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

def square(n):
    return n*n
print(square(5))
print(square(10))
print(square(1))
print(square(6))
print(square(3))

def is_even(n):
    if n%2==0:
        return True
    else:
        return False
print(is_even(45))
print(is_even(42))


def average(num):
    sum=0
    for i in num:
        sum+=i
    return sum/len(num)
#avg=average(num)/num
num=(10,20,30,40)
print(average(num))

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

def longest_word(words):
    long=len(words[0])
    long_word=words[0]
    for word in words:
        if len(word)>long:
            long=len(word)
            long_word=word

    return long_word
#words = ["qwedsc", "asd", "ij"]
words = ["apple", "kiwi"]
print(longest_word(words))

nums = [1, 2, 2, 3, 4, 4, 5]
print(set(nums))


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

marks = {"Jay": 85, "Ravi": 42, "Priya": 91, "Anil": 38}
for key,value in marks.items():
    if marks[key]<40:
        print(key)