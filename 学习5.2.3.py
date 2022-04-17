lib import sha256

x = 5

y = 0

while sha256(str(x*y)).hexdigest()[-1] != "0":

    y += 1

print('The solution is y = '+str(y))
