

# grid = [['L','G','D','B','A'],
#         ['Q','M','H','E','C'],
#         ['U','R','N','I','F'],
#         ['X','V','S','O','K'],
#         ['Z','Y','W','T','P']]

grid = [[]]

text = input('Enter the plaintext: ').upper().replace('J','I') #converting j to i

key = input('Enter the key: ').upper().replace('J','I')

# text = 'INSTRUMENTS'
# key = 'MONARCHY'

grid_row = 0
for k in key:
    # if the current row in the grid is full add a new row
    if len(grid[grid_row]) == 5:
        grid_row += 1
        grid.append([])

    if k not in ''.join(grid[grid_row]):
        grid[grid_row].append(k)

alphabet = 'ABCDEFGHIKLMNOPQRSTUVWXYZ'

# add the remaining alphabets to the grid
for a in alphabet:
    if a not in key:
        if len(grid[grid_row]) == 5:
            grid_row += 1
            grid.append([])

        grid[grid_row].append(a)        

print(grid)

def encryption(grid, text):
    sep_ch = []

    i = 0
    while i < len(text)-1: #making pairs of 2 from the text
        if text[i] == text[i+1]: #if consecutive letters same add an X in between
            text = text[:i+1] + 'Z' + text[i+1:]
        sep_ch.append(text[i] + text[i+1])
        i+=2
        
    if len(text) % 2 != 0 : #if length of text after modifying is odd, add an X at the end to make the final pair
        sep_ch.append(text[-1]+'Z')

    final_ch = []

    for c in sep_ch:
        #index of each character from the current pair
        c0 = []
        c1 = []

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == c[0]:
                    c0.extend([i,j])
                if grid[i][j] == c[1]:
                    c1.extend([i,j])
        
        if c0[0] == c1[0]: #In the same row
            final_ch.append(grid[c0[0]][(c0[1]+1)%5] + grid[c1[0]][(c1[1]+1)%5])
                
        elif c0[1] == c1[1]: #In the same column
            final_ch.append(grid[(c0[0]+1)%5][c0[1]] + grid[(c1[0]+1)%5][c1[1]])
                
        else:
            final_ch.append(grid[c0[0]][c1[1]] + grid[c1[0]][c0[1]])

    return final_ch

def decryption(grid, cipher):
    sep_ch = []

    i = 0
    while i < len(cipher)-1: #making pairs of 2 from the text
        sep_ch.append(cipher[i] + cipher[i+1])
        i+=2

    final_ch = []

    for c in sep_ch:
        #index of each character from the current pair
        c0 = []
        c1 = []

        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] == c[0]:
                    c0.extend([i,j])
                if grid[i][j] == c[1]:
                    c1.extend([i,j])
        
        if c0[0] == c1[0]: #In the same row
            final_ch.append(grid[c0[0]][(c0[1]-1)%5] + grid[c1[0]][(c1[1]-1)%5])
                
        elif c0[1] == c1[1]: #In the same column
            final_ch.append(grid[(c0[0]-1)%5][c0[1]] + grid[(c1[0]-1)%5][c1[1]])
                
        else:
            final_ch.append(grid[c0[0]][c1[1]] + grid[c1[0]][c0[1]])

    return final_ch

cipher = "".join(encryption(grid, text))        

print("The encrypted text is: "+ cipher)
print("The decrypted text is: "+"".join(decryption(grid, cipher)))
