# 0. color favorito
color = "blue"

# 1. area del circulo
pi = 3.14159
diameter = 3
radius = diameter / 2
area = pi * (radius * radius)

# 2. swap de variables
a = [1, 2, 3]
b = [3, 2, 1]
tmp = a
a = b
b = tmp

# 3a. parentesis -> resultado 1
r1 = (5 - 3) // 2

# 3b. parentesis -> resultado 0
r2 = (8 - 3) * (2 - (1 + 1))

# 4. candy smash
alice_candies = 121
bob_candies = 77
carol_candies = 109
to_smash = (alice_candies + bob_candies + carol_candies) % 3

if __name__ == "__main__":
    print(color)
    print(area)
    print(a, b)
    print(r1, r2)
    print(to_smash)
