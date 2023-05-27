
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:"))
p=0
def encrypt(text, shift):
   enc = ""
   for letter in text:
       pos = alphabet.index(letter)
       new_pos = pos + shift
       if new_pos > 25:
           p = shift-(25-pos)-1
           lett = alphabet[p]
           enc += lett           
       else:
           let = alphabet[new_pos]
           enc +=let
   print(enc)

def decrypt(text, shift):
    en = ""
    for t in text:
      po = alphabet.index(t)
      new_po = po - shift
      if new_po > 25:
          l = alphabet[shift+(25-po)-1]
          en += l           
      else:
          leti = alphabet[new_po]
          en +=leti
    print(en)


if direction == "encode":
    encrypt(text,shift)
else:
    decrypt(text, shift)











