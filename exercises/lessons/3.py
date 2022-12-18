presents = []
for i in range(1, 11):
    present = int(input("Enter present value: "))
    presents.append(present)

list_sum = sum(presents)
average_present = list_sum / len(presents)

above_average_presents = []
for present in presents:
    if present > average_present:
        above_average_presents.append(present)

print("sum:", list_sum)
print("average:", average_present)
print("presents above average:", len(above_average_presents))
