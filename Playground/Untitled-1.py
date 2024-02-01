def power_mod(base, exponent, mod):
    result = 1
    base = base % mod

    while exponent > 0:
        # If exponent is odd, multiply base with result
        if exponent % 2 == 1:
            result = (result * base) % mod

        # exponent must be even now
        exponent //= 2
        base = (base * base) % mod

    return result

base = 661578
exponent = 584939
modulus = 988027

result = power_mod(base, exponent, modulus)
print("Result:", result)
