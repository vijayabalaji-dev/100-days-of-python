# logo
logo = """           
 ,adPPYba, ,adPPYYba,  ,adPPYba, ,adPPYba, ,adPPYYba, 8b,dPPYba,  
a8"     "" ""     `Y8 a8P_____88 I8[    "" ""     `Y8 88P'   "Y8  
8b         ,adPPPPP88 8PP"""""""  `"Y8ba,  ,adPPPPP88 88          
"8a,   ,aa 88,    ,88 "8b,   ,aa aa    ]8I 88,    ,88 88          
 `"Ybbd8"' `"8bbdP"Y8  `"Ybbd8"' `"YbbdP"' `"8bbdP"Y8 88   
            88             88                                 
           ""             88                                 
                          88                                 
 ,adPPYba, 88 8b,dPPYba,  88,dPPYba,   ,adPPYba, 8b,dPPYba,  
a8"     "" 88 88P'    "8a 88P'    "8a a8P_____88 88P'   "Y8  
8b         88 88       d8 88       88 8PP""""""" 88          
"8a,   ,aa 88 88b,   ,a8" 88       88 "8b,   ,aa 88          
 `"Ybbd8"' 88 88`YbbdP"'  88       88  `"Ybbd8"' 88          
              88                                             
              88           
"""

# program starts
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#shifter shiftes the alphabet.
def shifter(shift):
  shifted = []
  for i in range(shift - 1,len(alphabet)):
    shifted.append(alphabet[i])
  for j in range(0,shift + 1):
    shifted.append(alphabet[j])
  return shifted

#function that encrypts the text
def encrypt(text,shift):
  shifted = shifter(shift)
  enc = ""
  for letter in text:
    if letter not in alphabet:
      enc += letter
    else:
      index = alphabet.index(letter)
      enc += shifted[index]
  print(f"The encoded text is {enc}")

#function that decrypts the text
def decrypt(text,shift):
  shifted = shifter(shift)
  dyc = ""
  for letter in text:
    if letter not in alphabet:
      dyc += letter
    else:
      index = shifted.index(letter)
      dyc += alphabet[index]
  print(f"The decoded text is {dyc}")
   
#exit variable
exiter = False
print(logo)
while not exiter:
  direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: and type 'exit' to exit\n").strip()
  if direction == "encode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 25:
      shift %= 26
    encrypt(text = text,shift = shift)
  elif direction == "exit":
    print("Program exits ..... durrr .......")
    exiter = True
  elif direction == "decode":
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 25:
      shift %= 26
    decrypt(text = text, shift = shift)
  else:
    exiter = True

   
