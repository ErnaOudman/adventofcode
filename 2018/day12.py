# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#initial = '#..#.#..##......###...###'
initial = '##..#..##....#..#..#..##.#.###.######..#..###.#.#..##.###.#.##..###..#.#..#.##.##..###.#.#...#.##..'

#instructions = [
#     '...## => #',
#     '..#.. => #',
#     '.#... => #',
#     '.#.#. => #',
#     '.#.## => #',
#     '.##.. => #',
#     '.#### => #',
#     '#.#.# => #',
#     '#.### => #',
#     '##.#. => #',
#     '##.## => #',
#     '###.. => #',
#     '###.# => #',
#     '####. => #',
#]
instructions = [
    '##### => #',
    '##.## => #',
    '..##. => .',
    '..#.# => .',
    '..### => #',
    '#..## => #',
    '.#.#. => #',
    '#.#.# => #',
    '#.##. => .',
    '####. => .',
    '#..#. => #',
    '..#.. => .',
    '.#### => .',
    '##.#. => #',
    '#...# => .',
    '.##.# => #',
    '#.### => .',
    '.#..# => #',
    '.#... => #',
    '.##.. => #',
    '.###. => .',
    '#.... => .',
    '###.. => .',
    '##..# => .',
    '...## => #',
    '##... => .',
    '..... => .',
    '....# => .',
    '###.# => #',
    '#.#.. => .',
    '.#.## => #',
    '...#. => .',
]

ins_dict = {x.split(' => ')[0]: x.split(' => ')[1] for x in instructions}

line = initial
final = 50000000000
i = 1
while i <= final:
    line = '.'*4 + line + 2*'.'
    nxt = []
    for s in range(0,len(line)):
        char = ins_dict.get(line[s:s+5], '.')
        nxt.append(char)
    line = ''.join(nxt)
#    print(i, line)
    i +=1
    

res = [pos-(final*2) for pos, char in enumerate(line) if char == '#']

print(sum(res))

#def next_gen(line, ins_dict = ins_dict, i=1, total=0):
#    start = '.'*2 + line + 2*'.'
#    nxtgen = []
#    for s in range(0,len(start)-2):
#        char = ins_dict.get(start[s:s+5], '.')
#        nxtgen.append(char)
#    nxtstring = ''.join(nxtgen)
##     print(i, nxtstring)
#    if i <20:
#        i += 1
#        return next_gen(nxtstring[1:-1], i=i, total=total)
#    else:
##         print('/n-------------/n')
#        return nxtstring
#    
#a= next_gen(initial)
#print(a)

