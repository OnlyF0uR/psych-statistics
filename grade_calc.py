mc_correct = 25
oe_correct = 5

def grade_calc(a, b):
    return ((((a - 0.333*25)/(25 - 0.333*25))*25 + b) / 30) * 10

print(grade_calc(mc_correct, oe_correct))