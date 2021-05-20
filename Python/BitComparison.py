'''
Bit Difference

Task: Find the number of bits that differ between two 32bit integers
the standard "int" type in most languages).

Example:
|        |        |
| ------ | ------ |
| 101010 |     42 |
| 110011 |     51 |
| SDDSSD |        |


S -> Same bit
D -> Different bit

Your program should output something like "between 51 and 42, 3 bits differ"

Bonus Points: What are the indeces of the differing bits (right to left, starting at 0)

Restrictions: No pre-built bit operation libraries may be used
Optional Restriction: only use bitwise operators in your program
&, |, ^, ~, and, or, xor and not respectively in most languages) for calculations.
'''

def bitDifference(int1, int2):
    bin2 = "{0:b}".format(int1)
    bin3 = "{0:b}".format(int2)
    #print(bin2 + ' ' +bin3) debugging step - correct binary conversions
    d_bit_index = ''
    d_bit_tracker = 0

    #step through bits and compare
    for i in range(0,6):
        if (bin2[i] != bin3[i]):
            print('D')
            d_bit_index += str(i) + ' '
            d_bit_tracker += 1
        else:
            print('S')
    print('Between the integers ' + str(int1) + ' and ' + str(int2) + ' ' + str(d_bit_tracker) + ' bits are different.')
    print('The differing bits are at indices: ' + d_bit_index)
