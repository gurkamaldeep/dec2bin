#Python script for inverting the binary value


print 'enter 0 to close'
while True:
    user_input = int(raw_input('Enter the decimal number:'))
    if user_input == 0:
        break
    else:
        dec_to_bin = bin(user_input)
        dec_to_bin = dec_to_bin[2:]
        print dec_to_bin[::-1]

