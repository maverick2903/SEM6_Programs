

grid = [['L','G','D','B','A'],
        ['Q','M','H','E','C'],
        ['U','R','N','I','F'],
        ['X','V','S','O','K'],
        ['Z','Y','W','T','P']]

text = input('Enter the plaintext: ').upper()

text = text.replace('J','I') #converting j to i

sep_ch = []

change1 = 0
if len(text) % 2 != 0:
    change1 = 1
    text += 'X'

i = 0
while i < len(text)-1:
    if text[i] == text[i+1]:
        text = text[:i+1] + 'X' + text[i+1:]
    sep_ch.append(text[i] + text[i+1])
    i+=2
        
if len(text) % 2 != 0 and change1 == 0:
    sep_ch.append(text[-1]+'X')


final_ch = []

for c in sep_ch:
    c0 = []
    c1 = []
    for i in range(len(grid)):
        for j in range(len(grid)):
            if grid[i][j] == c[0]:
                c0.extend([i,j])
            if grid[i][j] == c[1]:
                c1.extend([i,j])
    
    if c0[0] == c1[0]: #In the same row
        if c[0] != grid[c0[0]][-1] and c[1] != grid[c1[0]][-1]:
            final_ch.append(grid[c0[0]][(c0[1]+1)%5] + grid[c1[0]][(c1[1]+1)%5])
            
    elif c0[1] == c1[1]: #In the same column
        if c[0] != grid[-1][c0[1]] and c[1] != grid[-1][c1[1]]:
            final_ch.append(grid[(c0[0]+1)%5][c0[1]] + grid[(c1[0]+1)%5][c1[1]])
            
    else:
        final_ch.append(grid[c0[0]][c1[1]] + grid[c1[0]][c0[1]])
        
print("The encrypted text is: "+"".join(final_ch))
