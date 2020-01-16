"""
PROBLEM_STATEMENT

Kevin and Stuart want to play the 'The Minion Game'.

Game Rules

Both players are given the same string, .
Both players have to make substrings using the letters of the string.
Stuart has to make words starting with consonants.
Kevin has to make words starting with vowels.
The game ends when both players have made all possible substrings.

Scoring
A player gets +1 point for each occurrence of the substring in the string.

For Example:
String  = BANANA
Kevin's vowel beginning word = ANA
Here, ANA occurs twice in BANANA. Hence, Kevin will get 2 Points.

Input Format

A single line of input containing the string .
Note: The string  will contain only uppercase letters: .

Output Format

Print one line: the name of the winner and their score separated by a space.

If the game is a draw, print Draw.
"""

def make_substring(string, index):
    return len(string) - index

def minion_game(string):
    stuart_count = kevin_count = 0
    for i in range(len(string)):
        if string[i] in ('A', 'E', 'I','O', 'U'):
            kevin_count += make_substring(string, i)
        else:
            stuart_count += make_substring(string, i)
    if stuart_count > kevin_count:
        print("Stuart", stuart_count)
    elif stuart_count == kevin_count:
        print("Draw")
    else:
        print("Kevin", kevin_count)
    
if __name__ == '__main__':
    s = input()
    minion_game(s)