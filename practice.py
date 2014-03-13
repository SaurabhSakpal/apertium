import sys
li = sys.argv
S = li[1]
wo = S.split(" ")
words = [];
for i in range(len(wo)):
    if len(wo[i])>0:
        words.append(wo[i]);
print words
subseg = [];
for i in range(len(words)):
    temp = words[i];
    subseg.append(words[i])
    j = 1;
    while (i+j)<len((words)):
        temp = temp+" "+words[i+j];
        j = j+1
        subseg.append(temp)
print subseg
    
        
