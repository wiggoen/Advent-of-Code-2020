'''
Advent of Code: Day 3 - Puzzle 1 & 2
'''

data = 'Day-03-input.txt'

biome_map = []
with open(data, 'r') as infile:
  biome_map = infile.read().splitlines()



def toboggan_travel(biome_map, right, down):
  number_of_rows = len(biome_map)
  number_of_columns = (len(biome_map[0]))

  count = 0
  row = down
  column = right
  for line in biome_map:
    if row >= number_of_rows:
      break
    if column >= number_of_columns:
      column = column - number_of_columns

    location = biome_map[row][column]

    if location == "#":
      count += 1

    row += down
    column += right

  return count


# Answer --- Part 1 ---
right = 3
down = 1
number_of_trees = toboggan_travel(biome_map, right, down)
print("Number of trees encountered: %d" % number_of_trees)


# Answer --- Part 2 ---
product = 1
right = [1, 3, 5, 7, 1]
down = [1, 1, 1, 1, 2]

for right_number, down_number in zip(right, down):
  product *= toboggan_travel(biome_map, right_number, down_number)

print("Multiplication of number of trees encountered: %d" % product)


# Testcases
if __name__ == '__main__':
  test_map = ["..##.......",
              "#...#...#..",
              ".#....#..#.",
              "..#.#...#.#",
              ".#...##..#.",
              "..#.##.....",
              ".#.#.#....#",
              ".#........#",
              "#.##...#...",
              "#...##....#",
              ".#..#...#.#"]

  # Testcase --- Part 1 ---
  right = 3
  down = 1
  test_travel_P1 = toboggan_travel(test_map, right, down)
  print("TEST P1. Number of trees encountered: %d" % test_travel_P1)

  # Testcase --- Part 2 ---
  test_product = 1
  right = [1, 3, 5, 7, 1]
  down = [1, 1, 1, 1, 2]

  for right_number, down_number in zip(right, down):
    test_product *= toboggan_travel(test_map, right_number, down_number)

  print("TEST P2. Multiplication of number of trees encountered: %d" % test_product)