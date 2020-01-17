"""
You are given a string S. Suppose a character 'c' occurs consecutively X times in the string. Replace these consecutive occurrences of the 
character 'c' with (X, c) in the string.

For a better understanding of the problem, check the explanation.

Input Format

A single line of input consisting of the string S.

Output Format

A single line of output consisting of the modified string.

Constraints

All the characters of S denote integers between 0 and 9.

Sample Input

1222311

Sample Output

(1, 1) (3, 2) (1, 3) (2, 1)

"""

string = input()
temp_count = 1
output_arr = []
for i in range(len(string)-1):
    if string[i] == string[i+1]:
        temp_count+=1
    else:
        output_arr.append((temp_count, int(string[i])))
        temp_count = 1
output_arr.append((temp_count, int(string[-1])))
print(*output_arr, sep = " ")
