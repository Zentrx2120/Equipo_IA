"""
b) Sin preguntarle al usuario y evaluando en automatico, graficar la trayectoria del robot
"""

import random
import matplotlib.pyplot as plt
import numpy as np

# Verify if the robot can't advnace 
def end(row, col):
  # Border bottom
  if row + 1 == h:
    return True

  # Between 2 walls and the left border
  if col - 1 < 0 and map[row, col + 1] == 0 and map[row + 1, col] == 0:
    return True

  # Between 2 walls and the right border
  if col + 1 == w and map[row, col - 1] == 0 and map[row + 1, col] == 0:
    return True

  # Between 3 walls
  if (col < w - 1) and (map[row, col - 1] == 0 and map[row, col + 1] == 0 and map[row + 1, col] == 0):
    return True
  
  return False


def move(col):
  direction = random.randint(-1, 1)
  if map[row, col + direction] == 0:
    return col
  if col + direction < 0:
    direction = 1
  if col + direction == w:
    direction = -1

  print(f"Turning {'Right' if direction == 1 else 'Left'}({row}, {col})")
  col += direction
  return col


# Initial position
row = 0
col = 5

map = np.array([
      [1, 0, 1, 0, 0, 1, 0, 0],
      [1, 0, 1, 0, 0, 1, 0, 0],
      [1, 0, 1, 0, 1, 1, 1, 1],
      [1, 0, 1, 0, 1, 0, 0, 1],
      [1, 1, 1, 1, 1, 0, 0, 0],
      [1, 0, 1, 1, 1, 1, 1, 0],
      [0, 0, 1, 0, 0, 0, 1, 1],
      [1, 1, 1, 1, 1, 0, 0, 1],
      [1, 1, 0, 0, 1, 0, 0, 1]
    ])

# Initialize map
dotColor = 'green'
plt.imshow(map, cmap='gray', origin= 'lower')
plt.scatter(col, row, color = dotColor)

# Map dimention
h = np.shape(map)[0]
w = np.shape(map)[1]

print(f"Initial position: ({row}, {col})\n")

# While the robot isn't stuck
while not end(row, col):
  if row < h - 1: # Avoid array out of boundaries
    nextCell = map[row + 1, col]
    if nextCell == 0:
      col = move(col)
      plt.scatter(col, row, color = dotColor)
    else: 
      row += 1
      print(f"Moving forward({row}, {col})")
      plt.scatter(col, row, color = dotColor)

plt.show()
