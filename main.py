import random

def dice_number(faces,n):
    results =[]
    for i in range(1, 4):
        dice = random.randint(1,faces)
        results.append(dice)

    results_str = " - ".join(str(result) for result in results)
    return [results_str,len(results)]

print(f"You roll {dice_number(20,3)[1]} and the results are {dice_number(20,3)[0]}")