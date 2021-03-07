s=input("enter the string")
characterCount=0
wordCount=1
for a in s :
    characterCount=characterCount+1 
    if(a==' '):
        wordCount=wordCount+1
print("number of words",wordCount)
print("number of characters",characterCount)

