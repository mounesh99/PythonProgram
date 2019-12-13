''' Kevin and Stuart want to play the 'The Minion Game'
    Game Rules:
    Both players are given the same string, $.
    Both players have to make substrings using the letters of the string $.
    Stuart has to make words starting with consonants.
    Kevin has to make words starting with vowels.
    The game ends when both players have made all possible substrings.

    Scoring:
    A player gets +1 point for each occurrence of the substring in the string $.
    For Example:
    String $ = BANANA
    Kevin's vowel beginning word = ANA
    Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.'''
    
str=input().strip()
list1=list(str)
string=''
k=0
s=0
for i in range(0,len(list1)):
    if list1[i] in ['a','e','i','o','u','A','E','I','O','U']:
        k=k+len(list1)-(i+1)+1
        print(i,'kelvin',k,'Len of list1',len(list1))
    else:
        s=s+len(list1)-(i+1)+1
        print(i,'staurt',s,'len of list1',len(list1))
print('"kelvin count:"',k,'"\nStaurt count:"',s)
if k>s:
    print('Kelvin:',k)
elif s>k:
    print('sruart:',s)
else:
    print('Draw')
                   
               

