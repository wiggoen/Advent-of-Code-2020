'''
Advent of Code: Day 5 - Puzzle 1 & 2

F: "front"
B: "back"
L: "left"
R: "right"
'''

data = 'Day-05-input.txt'

seat_data = []
with open(data, 'r') as infile:
  seat_data = infile.read().splitlines()


def seven_bits(bit_sequence):
  factors = [2**6, 2**5, 2**4, 2**3, 2**2, 2, 1]
  bit_number = 0
  number_list = []

  for bit, F in zip(bit_sequence, factors):
    if bit == 'F':
      bit_number = 0
    if bit == 'B':
      bit_number = 1
    number_list.append(bit_number * F)

  return sum(tuple(number_list))


def three_bits(bit_sequence):
  factors = [2**2, 2, 1]
  bit_number = 0
  number_list = []

  for bit, F in zip(bit_sequence, factors):
    if bit == 'L':
      bit_number = 0
    if bit == 'R':
      bit_number = 1
    number_list.append(bit_number * F)

  return sum(tuple(number_list))


def max_seat_ID(seats):
  max_seat_id = 0

  for seat_id in seats:
    if seat_id > max_seat_id:
      max_seat_id = seat_id

  return max_seat_id


def seat_ID(seat_data):
  row = seven_bits(seat_data[:7])
  column = three_bits(seat_data[7:])
  seat_id = row * 8 + column
  return row, column, seat_id


# Answer --- Part 1 ---
seat_IDs = []
for seat in seat_data:
  row, column, seat_id = seat_ID(seat)
  seat_IDs.append(seat_id)

highest_seat_id = max_seat_ID(seat_IDs)
print('Highest seat ID: %d' % highest_seat_id)


# Answer --- Part 2 ---
def find_my_seat(seat_IDs):
  seats = sorted(seat_IDs)

  for n in range(seats[0], seats[-1]):
    if n not in seats:
      return n

my_seat = find_my_seat(seat_IDs)
print('My seat has ID: %d' % my_seat)


# Testcases
if __name__ == '__main__':
  test_seat_data = ["FBFBBFFRLR", "BFFFBBFRRR", "FFFBBBFRRR", "BBFFBBFRLL"]
  '''
    FBFBBFFRLR: row 44, column 5, seat ID 357.
    BFFFBBFRRR: row 70, column 7, seat ID 567.
    FFFBBBFRRR: row 14, column 7, seat ID 119.
    BBFFBBFRLL: row 102, column 4, seat ID 820.
  '''
  # Testcase --- Part 1 ---
  print('--- TEST ---')
  test_seats = []
  for seat in test_seat_data:
    test_row, test_column, test_seat_id = seat_ID(seat)
    test_seats.append(test_seat_id)
    print('row = %d, column = %d, seat_id = %s' % (test_row, test_column, test_seat_id))

  test_max_seat_id = max_seat_ID(test_seats)
  print('TEST: Highest seat ID: %d' % test_max_seat_id)
