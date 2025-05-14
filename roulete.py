import random

def assign_task(activities):
    names = ["Anuar", "Abraham", "Sebas"]
    result = {}
    for i in range(100):
        rand_activity = random.choice(activities)
        result[rand_activity] = names[i % 3]

    return result

activities = ['Practica backtracking b)', 'Practica A* a)', 'Practica A* b) y c)', 'Practica Dijkstra a) y b)', 'Practica Dijkstra c)']
print(assign_task(activities))