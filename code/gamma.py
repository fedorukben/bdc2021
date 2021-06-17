print("Please enter positive mu: ")
mup = float(input())
print("Please enter negative mu:")
mun = float(input())
print("Please enter f(positive mu):")
fp = float(input())
print("Please enter f(negative mu):")
fn = float(input())

top = (2 * fp) - (2 * fn)
bot = (mup * fp) + (mup * fn) - (mun * fp) - (mun * fn)

gamma = float(top) / bot

print(f'Gamma = {gamma}')