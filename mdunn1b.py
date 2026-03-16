 marie dunn lab1 ctc 387

# user is asked to enter 6 bits in binary result display decimal equivalent

decimal = 0
bit1 = 0
bit2 = 0
bit3 = 0
bit4 = 0
bit5 = 0
bit6 = 0

bit1 = input("Enter the first digit: ")
while bit1 !="0" and bit1 !="1":
    print("Please enter only 0 or 1.")
    bit1 = input("Enter the first digit: ")
bit2 = input("Enter the second digit: ")
while bit2 !="0" and bit2 !="1":
    print("Please enter only 0 or 1.")
    bit2 = input("Enter the second digit: ")
bit3 = input("Enter the third digit: ")
while bit3 !="0" and bit3 !="1":
    print("Please enter only 0 or 1.")
    bit3 = input("Enter the third digit: ")
bit4 = input("Enter the fourth digit: ")
while bit4 !="0" and bit4 !="1":
    print("Please enter only 0 or 1.")
    bit4 = input("Enter the fourth digit: ")
bit5 = input("Enter the fifth digit: ")
while bit5 !="0" and bit5 !="1":
    print("Please enter only 0 or 1.")
    bit5 = input("Enter the fifth digit: ")
while bit6 !="0" and bit6 !="1":
    print("Please enter only 0 or 1.")
    bit6 = input("Enter the sixth digit: ")

decimal = (int(bit1)*32) + (int(bit2)*16) + (int(bit3)*8) + (int(bit4)*4) + (int(bit5)*2) + (int(bit6)*1)

print("decimal equivalent: ", decimal)
