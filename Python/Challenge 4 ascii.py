'''
File statistics:
Write a program that reads a (plain text) file (which can be specified in any way you want
(cmdline parameter, gotten at runtime, ....))
Your program should read the file and then output how often every (ascii)
character appears in the file and output another file called <original name>.stats, which contains the results

Restrictions: /

Bonus points:
>make your program with all of unicode
>Have an option to ignore case (read in from your comand line, e.g. "-i")

Example:
Hello world ->
H x1
e x1
l x3
o x2
<space> x1
w x2
r x1

(You can format your output however you want, given it's easily readable)
'''

def asciiStats(file='challengedefault.txt', ignore_case=0):
    read_file = open(file, 'r+')
    ascii_list = []
    for line in read_file:
        for ch in line:
            ascii_list.append(ch)

    print(ascii_list)
        
