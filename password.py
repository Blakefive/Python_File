import math
def password(N):
    return math.trunc((N**0.5)*1000) - N
