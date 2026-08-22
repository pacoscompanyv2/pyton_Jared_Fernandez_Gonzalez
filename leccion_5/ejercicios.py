import random

# 1. lista con numero de la suerte (divisible entre 7)
def has_lucky_number(nums):
    return any([num % 7 == 0 for num in nums])

# 2. comparacion elemento a elemento
def elementwise_greater_than(L, thresh):
    return [x > thresh for x in L]

# 3. menu aburrido (mismo platillo dos dias seguidos)
def menu_is_boring(meals):
    for i in range(len(meals) - 1):
        if meals[i] == meals[i + 1]:
            return True
    return False

# 4. valor promedio de la maquina tragamonedas (monte carlo)
def play_slot_machine():
    return random.choice([0, 0, 0, 0, 1.5, 5, 20])

def estimate_average_slot_payout(n_runs):
    payouts = [play_slot_machine() - 1 for _ in range(n_runs)]
    return sum(payouts) / n_runs

if __name__ == "__main__":
    print(has_lucky_number([1, 2, 3, 14]))
    print(elementwise_greater_than([1, 2, 3, 4], 2))
    print(menu_is_boring(["pizza", "pizza", "tacos"]))
    print(estimate_average_slot_payout(100000))
