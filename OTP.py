# OTP Genearator

import random

print('Welcome to Your OTP(One Time Password) Generator')

chars = '0123456789'

number = input('Amount of OTP to generate: ')

number = int(number)

length = input('Input your OTP length: ')

length = int(length)

print('\nHere are your OTPs:')

for pwd in range(number):
  passwords = ''
  for c in range(length):
    passwords += random.choice(chars)
  print(passwords)
  
  
