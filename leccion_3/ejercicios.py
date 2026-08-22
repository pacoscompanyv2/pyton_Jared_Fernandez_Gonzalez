# 1. sign
def sign(number):
    if number < 0:
        return -1
    elif number > 0:
        return 1
    else:
        return 0

# 2. concise_is_negative (una linea)
def concise_is_negative(number):
    return number < 0

# 3. onionless
def onionless(ketchup, mustard, onion):
    """Devuelve si el cliente no quiere cebolla."""
    return not onion

# 5a. quiere todo
def wants_all_toppings(ketchup, mustard, onion):
    return ketchup and mustard and onion

# 5b. quiere plain
def wants_plain_hotdog(ketchup, mustard, onion):
    return not ketchup and not mustard and not onion

# 5c. exactamente una salsa
def exactly_one_sauce(ketchup, mustard, onion):
    return ketchup != mustard

# 6. exactamente un topping
def exactly_one_topping(ketchup, mustard, onion):
    return (ketchup + mustard + onion) == 1

# mensaje con singular/plural
def splitting_message(total_candies):
    return "Splitting " + str(total_candies) + (" candy" if total_candies == 1 else " candies")

if __name__ == "__main__":
    print(sign(-5), sign(0), sign(5))
    print(concise_is_negative(-3))
    print(onionless(True, True, False))
    print(wants_all_toppings(True, True, True))
    print(wants_plain_hotdog(False, False, False))
    print(exactly_one_sauce(True, False, False))
    print(exactly_one_topping(0, 1, 0))
    print(splitting_message(1))
    print(splitting_message(5))
