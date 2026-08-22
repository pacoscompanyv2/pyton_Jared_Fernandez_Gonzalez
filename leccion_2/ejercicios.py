# 1. redondear a 2 decimales
def round_to_two_places(num):
    return round(num, 2)

# 2. ndigits negativo en round()
def test_negative_ndigits():
    print(round(338424, -1))
    print(round(338424, -2))
    print(round(338424, -3))

# 3. to_smash con num_friends opcional
def to_smash(total_candies, num_friends=3):
    """Numero de dulces sobrantes al repartir entre num_friends amigos."""
    return total_candies % num_friends

# 4. codigo con errores, corregido
def round_to_two_places_fixed(num):
    return round(num, 2)

def smallest_abs(x, y):
    return min(abs(x), abs(y))

def f(x):
    y = abs(x)
    return y

if __name__ == "__main__":
    print(round_to_two_places(9.9999))
    test_negative_ndigits()
    print(to_smash(91))
    print(to_smash(91, 4))
    print(smallest_abs(-10, 5))
    print(f(5))
