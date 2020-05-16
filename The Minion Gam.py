import itertools
def minion_game(s):


    l = list(s)
    global vowels
    vowels = 'AEIOU'
    Kevin = 0
    Kevin_l = []
    Stuart = 0
    Stuart_l =[]


    for i in range(len(s)):
        if s[i] in vowels:
            Kevin = Kevin + (len(s) - i)
        else:
            Stuart = Stuart + (len(s) - i)

    if Kevin > Stuart:
        print('Kevin '+str(Kevin))
    elif Kevin < Stuart:
        print('Stuart '+ str(Stuart))
    else:
        print('Draw')
if __name__ == '__main__':
    s = input()
    minion_game(s)
