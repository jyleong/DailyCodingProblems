import random


R_SQUARED = 1 # x^2 + y^2 = r^2
def estimate_pi(n):
    num_in = 0
    num_total = 0
    for i in range(n):
        x = random.uniform(0,1)
        y = random.uniform(0,1)
        area = x * x + y * y
        if area <= R_SQUARED:
            num_in += 1
        num_total += 1
    return 4 * num_in / num_total


print("Estimate PI with 100: ", estimate_pi(100))

print("Estimate PI with 1000: ", estimate_pi(1000))

print("Estimate PI with 5000: ", estimate_pi(5000))

print("Estimate PI with 10000: ", estimate_pi(10000))

print("Estimate PI with 30000: ", estimate_pi(30000))

print("Estimate PI with 40000: ", estimate_pi(40000))




