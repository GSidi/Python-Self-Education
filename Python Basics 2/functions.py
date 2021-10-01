
def calculate_total(exp):
    
    total = 0
    for i in exp:
        total = total + i

    return total

george_list = [6541,321,231,8361]
jims_list = [9,87,9782,98,71]


moms_total = calculate_total(george_list)
dads_total = calculate_total(jims_list)

print("Moms total expenses are: ", moms_total)
print("Dads total expeses are: ", dads_total)