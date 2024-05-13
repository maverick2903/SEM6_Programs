text = 'Hello my name is Varun'
text_binary = ''
for letter in text:
  text_binary += bin(ord(letter))[2:]
print(f'Binary input : {text_binary[:20]}..\n')

padding = 512 - 64 - (len(text_binary)%512)
print(f'Padding needed = {padding} bits\n')

lengthInBinary = len(bin(len(text_binary))[2:])
text_padded = text_binary + '1' + '0'*(padding-1) + '0'*(64-lengthInBinary) +bin(len(text_binary))[2:]
print(f'Padded input is : {text_padded[0:20]}..')
print(f'Length of padded input is : {len(text_padded)}\n')

#inititialize Chaining variables 
A = '0x01234567'
B = '0x89ABCDEF'
C = '0XFEDCBA98'
D = '0x76543210'
print(f'Chaining variables are : {A,B,C,D}\n')

#Seperate the 512 bit padded input into 32 bit blocks
blocks = []
for i in range(0,len(text_padded),32):
  blocks.append(text_padded[i:i+32])
print(f"32 Bit Blocks : {blocks}")
print(f"Number of 32 Bit Blocks : {len(blocks)} \n")

keys = ['0xe0a5e0a5', '0x465a465a', '0xf737d44a', '0x6728bd47', 
        '0xb779d44a', '0x470bd44a', '0x34f2d44a', '0xbd47bd47', 
        '0xc7ab1a7f', '0xd44ad44a', '0xaa85bd47', '0x1f91d44a', 
        '0x6e541a7f', '0xdb1f1a7f', '0x13961a7f', '0x1a7f1a7f']

def f(b,c,d):
  return hex((int(b,16) & int(c,16)) | (~int(b,16) & int(d,16)))

a, b, c, d = A, B, C, D
for i in range(16):
  f_bcd = f(b,c,d) 
  a = hex((int(a,16) + int(f_bcd,16)) % int('0xffffffff',16))
  a = hex((int(a,16) + int(blocks[i],2)) % int(int('0xffffffff',16))) #msg
  a = hex((int(a,16) + int(keys[i],16)) % int(int('0xffffffff',16))) #key
  bin_a = bin(int(a,16))[2:]
  a = bin_a[5:]+bin_a[:5] #Left shift by 5
  a = hex((int(a,2)+int(b,16))%int('0xffffffff',16)) #add B

  #LEFT SHIFT
  a,b,c,d = d,a,b,c

hashed_msg = ''
for i in [a,b,c,d]:
  binary = bin(int(a,16))[2:]
  n = len(binary)
  binary = '0'*(32-n) + binary
  hashed_msg += binary
print(f"Message Digest is : {hex(int(hashed_msg,2))}")
print(f"Length of Message Digest is : {len(hashed_msg)}")