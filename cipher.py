# Caesar cipher that shifts letters forward based on user input.
def encryption(plaintext, key):
  encryption_str = " "
  for i in plaintext:
    if i.isupper():
      temp = 65 + ((ord(i) - 65 + key) % 26)
      encryption_str = encryption_str + chr(temp)                            
    elif i.islower():
      temp = 97 + ((ord(i) - 97 + key) % 26)
      encryption_str = encryption_str + chr(temp)
    else:
      encryption_str = encryption_str + i
  print("The encrypted sentence is:", encryption_str)
plaintext = input("Please enter a sentence: ")
key = int(input("Please enter the number of spaces to shift: "))
encryption(plaintext, key)