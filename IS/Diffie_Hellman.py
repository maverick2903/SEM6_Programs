g = int(input('Public Key G: '))
p = int(input('Public Key P: '))

# Private key a
a = int(input('Private Key a: '))
# Private key b
b = int(input('Private Key b: '))

# Key generated for a
Xa = pow(g, a, p)

# Key generated for b
Xb = pow(g, b, p)

print('Generated Keys:')
print('Key for a:', Xa)
print('Key for b:', Xb)

# Symmetric keys generated
Ka = pow(Xb, a, p)
Kb = pow(Xa, b, p)

print('Symmetric Keys:')
print('Key for a:', Ka)
print('Key for b:', Kb)
