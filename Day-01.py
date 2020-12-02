'''
Advent of Code: Day 1 - Puzzle 1 & 2
'''

data = 'Day-01-Puzzle-input.txt'

expense_report = []
with open(data, 'r') as infile:
  expense_report = infile.read().splitlines()


# Make string numbers in list into integers
expense_report = [int(n) for n in expense_report]


def sum_2_to_2020(expense_report):
  for a in expense_report[:-1]:
    for b in expense_report[1:]:
      if a + b == 2020:
        return a, b, a * b


# Answer --- Part 1 ---
a, b, answer = sum_2_to_2020(expense_report)
print('The two entries are %d + %d = 2020, and the product is: %d' % (a, b, answer))


def sum_3_to_2020(expense_report):
  for a in expense_report[:-1]:
    for b in expense_report[1:]:
      for c in expense_report[2:]:
        if a + b + c == 2020:
          return a, b, c, a * b * c


# Answer --- Part 2 ---
a, b, c, answer = sum_3_to_2020(expense_report)
print('The three entries are %d + %d + %d = 2020, and the product is: %d' % (a, b, c, answer))


# Testcases
if __name__ == '__main__':
  expense_report_test = [1721, 979, 366, 299, 675, 1456]

  # Testcase --- Part 1 ---
  expense_report_test_answer_P1 = 514579
  a, b, test_answer_P1 = sum_2_to_2020(expense_report_test)
  assert expense_report_test_answer_P1 == test_answer_P1

  # Testcase --- Part 2 ---
  expense_report_test_answer_P2 = 241861950
  a, b, c, test_answer_P2 = sum_3_to_2020(expense_report_test)
  assert expense_report_test_answer_P2 == test_answer_P2