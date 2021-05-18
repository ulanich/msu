
k = 1.4

density = lambda m, ro: ro*(k+1)*m**2/((k-1)*m**2+2)

M = [3.03,3.19,3.26]
RO = [8,8,8]
for i in range(len(M)):
    print(density(M[i], RO[i]))