g = int(input('Public Key G: '))
p = int(input('Public Key P: '))

# Private key a
a = int(input('Private Key a: '))
# Private key b
b = int(input('Private Key b: '))

# Key generated for a
x = pow(g, a, p)

# Key generated for b
y = pow(g, b, p)

print('Generated Keys:')
print('Key for a:', x)
print('Key for b:', y)

# Symmetric keys generated
ka = pow(y, a, p)
kb = pow(x, b, p)

print('Symmetric Keys:')
print('Key for a:', ka)
print('Key for b:', kb)
