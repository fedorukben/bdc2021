
print("Enter mu+: ", end='')
mup = float(input())

print("Enter mu-: ", end='')
mun = float(input())

print("Enter f(mu+): ", end='')
fp = float(input())

print("Enter f(mu-): ", end='')
fn = float(input())

numer = (2 * fp) - (2 * fn)
denom = (mup * fp) + (mup * fn) - (mun * fp) - (mun * fn)

gamma = float(numer) / denom

print(f'Gamma is: {gamma}')