'''
Using the Python language, have the function LongestWord(sen)
take the sen parameter being passed and return the largest word in the string.
If there are two or more words that are the same length,
return the first word from the string with that length.
Ignore punctuation and assume sen will not be empty.
'''

def LongestWord(sen): 

    # Make arrays and variables
    sentencearray = sen.split(" ")
    newarray = []
    longestword = ""
    arraycount = 0
    for w in sentencearray: # For every word in sentence array do:
        newarray.append("")
        for ch in w:        # For every character in word do:
            if ch.isalpha(): # Ignore punctuation
                newarray[arraycount] += ch
        arraycount += 1
    
    for w in newarray:
        if len(w) > len(longestword):
            longestword = w
            
    return longestword
    
# Function call  
print LongestWord(raw_input())  
