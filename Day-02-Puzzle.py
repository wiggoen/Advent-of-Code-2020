'''
Advent of Code: Day 2 - Puzzle 1 & 2
'''

data = 'Day-02-Puzzle-input.txt'

passwords = []
with open(data, 'r') as infile:
  passwords = infile.read().splitlines()


def valid_passwords(password_list):
  number_of_valid_passwords = 0

  low_number = 0
  high_number = 0
  letter = None
  password = None

  for line in password_list:
    parts = line.split(':')
    policy, password = parts
    numbers, letter = policy.split(' ')
    low_number, high_number = numbers.split('-')
    low_number = int(low_number)
    high_number = int(high_number)
    password = password.strip()

    count = 0
    for character in password:
      if character == letter:
        count += 1

    if count >= low_number and count <= high_number:
      number_of_valid_passwords += 1

  return number_of_valid_passwords


# Answer --- Part 1 ---
number_of_valid_passwords = valid_passwords(passwords)
print("Number of valid passwords: %d" % number_of_valid_passwords)


def official_valid_passwords(password_list):
  number_of_valid_passwords_P2 = 0

  low_number = 0
  high_number = 0
  letter = None
  password = None

  for line in password_list:
    parts = line.split(':')
    policy, password = parts
    numbers, letter = policy.split(' ')
    low_number, high_number = numbers.split('-')
    low_number = int(low_number)
    high_number = int(high_number)
    password = password.strip()

    if (letter == password[low_number - 1] and not letter == password[high_number - 1]) or (not letter == password[low_number - 1] and letter == password[high_number - 1]):
      number_of_valid_passwords_P2 += 1

  return number_of_valid_passwords_P2


# Answer --- Part 2 ---
number_of_official_valid_passwords = official_valid_passwords(passwords)
print("Number of official valid passwords: %d" % number_of_official_valid_passwords)


# Testcases
if __name__ == '__main__':
  test_passwords = ["1-3 a: abcde", "1-3 b: cdefg", "2-9 c: ccccccccc"]

  # Testcase --- Part 1 ---
  number_of_test_passwords_P1 = valid_passwords(test_passwords)
  number_of_test_passwords_valid = 2
  print("Number of valid test passwords P1: %d" % number_of_test_passwords_P1)
  assert number_of_test_passwords_valid == number_of_test_passwords_P1

  # Testcase --- Part 2 ---
  number_of_test_passwords_P2 = official_valid_passwords(test_passwords)
  number_of_test_passwords_valid_P2 = 1
  print("Number of valid test passwords P2: %d" % number_of_test_passwords_P2)
  assert number_of_test_passwords_valid_P2 == number_of_test_passwords_P2