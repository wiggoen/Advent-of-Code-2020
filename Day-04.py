'''
Advent of Code: Day 4 - Puzzle 1 & 2

byr (Birth Year)
iyr (Issue Year)
eyr (Expiration Year)
hgt (Height)
hcl (Hair Color)
ecl (Eye Color)
pid (Passport ID)
cid (Country ID)
'''

import re


data = 'Day-04-input.txt'

passport_data = []
with open(data, 'r') as infile:
  passport_data = infile.read().split('\n\n')

for i in range(len(passport_data)):
  passport_data[i] = passport_data[i].replace('\n', ' ')

passport_fields = ['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']  # 'cid' is optional



def validate_passport(passport_data):
  number_of_valid_passports = 0
  number_of_passport_fields_required = len(passport_fields)
  for line in passport_data:
    passport = {}
    valid_passport = False
    elements = line.split(' ')
    counter = 0
    for item in elements:
      key, value = item.split(':')
      passport[key] = value
    for field in passport_fields:
      if field in passport:
        counter += 1
    if counter == number_of_passport_fields_required:
      number_of_valid_passports += 1

  return number_of_valid_passports


# Answer --- Part 1 ---
number_of_valid_passports = validate_passport(passport_data)
print('Number of valid passports = %d' % number_of_valid_passports)



def better_passport_validation(passport_data):
  number_of_valid_passports = 0
  number_of_passport_fields_required = len(passport_fields)
  eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']

  for line in passport_data:
    passport = {}
    valid_passport = False
    elements = line.split(' ')
    counter = 0
    for item in elements:
      key, value = item.split(':')
      passport[key] = value

    if 'byr' in passport and (int(passport['byr']) >= 1920 and int(passport['byr']) <= 2002):
      counter += 1
    if 'iyr' in passport and (int(passport['iyr']) >= 2010 and int(passport['iyr']) <= 2020):
      counter += 1
    if 'eyr' in passport and (int(passport['eyr']) >= 2020 and int(passport['eyr']) <= 2030):
      counter += 1
    if 'hgt' in passport:
      pattern = re.match('([0-9]*)([a-z]*)', passport['hgt'])
      height = int(pattern.group(1))
      length_unit = pattern.group(2)
      if 'cm' == length_unit and (height >= 150 and height <= 193):
        counter += 1
      elif 'in' == length_unit and (height >= 59 and height <= 76):
        counter += 1
    if 'hcl' in passport:
      pattern = re.match('^\#([0-9a-f]{6})', passport['hcl'])
      if pattern is not None:
        counter += 1
    if 'ecl' in passport and passport['ecl'] in eye_colors:
      counter += 1
    if 'pid' in passport:
      pattern = re.match('([0-9]{9}$)', passport['pid'])
      if pattern is not None:
        counter += 1

    if counter == number_of_passport_fields_required:
      number_of_valid_passports += 1

  return number_of_valid_passports


# Answer --- Part 2 ---
number_of_valid_passports_P2 = better_passport_validation(passport_data)
print('Number of valid passports = %d' % number_of_valid_passports_P2)


# Testcases
if __name__ == '__main__':
  test_passport_data = ['ecl:gry pid:860033327 eyr:2020 hcl:#fffffd byr:1937 iyr:2017 cid:147 hgt:183cm',
                        'iyr:2013 ecl:amb cid:350 eyr:2023 pid:028048884 hcl:#cfa07d byr:1929',
                        'hcl:#ae17e1 iyr:2013 eyr:2024 ecl:brn pid:760753108 byr:1931 hgt:179cm',
                        'hcl:#cfa07d eyr:2025 pid:166559648 iyr:2011 ecl:brn hgt:59in']

  # Testcase --- Part 1 ---
  test_number_of_valid_passports = validate_passport(test_passport_data)
  print('TEST P1: Number of valid passports = %d' % test_number_of_valid_passports)