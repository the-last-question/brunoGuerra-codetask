def checkPerfectNumber(Number):
    SumDivisors = 0
    for i in range(1, Number):
        if(Number % i == 0): SumDivisors = SumDivisors + i

    if (SumDivisors == Number): return True
    else: return False

def main():
    print("--------------------------------")
    print("Numeros perfeitos entre 1 e 10000:")
    for i in range(1, 10000):
        if(checkPerfectNumber(i)): print(" %d é um numero perfeito" %i)
    
main()