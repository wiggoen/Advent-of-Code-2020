'''
Advent of Code: Day 6 - Puzzle 1 & 2
'''


data = 'Day-06-input.txt'

customs_declaration_forms = []
with open(data, 'r') as infile:
  customs_declaration_forms = infile.read().split('\n\n')

for i in range(len(customs_declaration_forms)):
  customs_declaration_forms[i] = customs_declaration_forms[i].replace('\n', ' ')


def read_letters(customs_declaration_forms_data):
  sum_of_counts = 0

  for characters in customs_declaration_forms_data:
    letters = list(set(characters))
    letters = list(filter(lambda item: item.strip(), letters))  # remove empty string
    sum_of_counts += len(letters)

  return sum_of_counts


# Answer --- Part 1 ---
sum_of_counts_of_yes = read_letters(customs_declaration_forms)
print('The sum of counts of yes is: {}'.format(sum_of_counts_of_yes))


def read_group_letters(customs_declaration_forms_data):
  sum_of_group_counts = 0

  for characters in customs_declaration_forms_data:
    letter_list = characters.split(' ')

    if len(letter_list) == 1:
      letter_set = list(set(letter_list))
      number_of_letters = len(letter_set[0])
      sum_of_group_counts += number_of_letters
    else:
      first_answer = letter_list[0]
      group_length = len(letter_list)

      for letter in first_answer:
        count = 1
        for entry in letter_list[1:]:
          if letter in entry:
            count += 1
        if count == group_length:
          sum_of_group_counts += 1

  return sum_of_group_counts


# Answer --- Part 2 ---
sum_of_group_counts_of_yes = read_group_letters(customs_declaration_forms)
print('The sum of group counts of yes is: {}'.format(sum_of_group_counts_of_yes))


# Testcases
if __name__ == '__main__':
  test_input = ['abc', 'a b c', 'ab ac', 'a a a a', 'b']

  # Testcase --- Part 1 ---
  test_P1_answer = 11
  test_sum_of_counts = read_letters(test_input)
  assert test_sum_of_counts == test_P1_answer
  print('TEST P1: The sum of counts of yes is: {}'.format(test_sum_of_counts))

  # Testcase --- Part 2 ---
  test_P2_answer = 6
  test_sum_of_counts_P2 = read_group_letters(test_input)
  assert test_sum_of_counts_P2 == test_P2_answer
  print('TEST P2: The sum of group counts of yes is: {}'.format(test_sum_of_counts_P2))