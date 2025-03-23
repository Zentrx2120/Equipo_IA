import random

def assign_task(activities):
    names = ["Anuar", "Abraham", "Sebas"]
    result = {}
    for i in range(100):
        rand_activity = random.choice(activities)
        result[rand_activity] = names[i % 3]

    return result

activities = ['Practica 1', 'Practica 2', 'Practica 3']
print(assign_task(activities))