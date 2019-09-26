#Simple program to encode and decode base64 strings
#Created by NightShade

import base64
import sys

exit_message = 'Good Bye! Stay Tuned for New Tools and Updates...!'

def main():
    
    print()
    print()

    print('#####::::Simple Python Script to Encode and Decode Base64 Strings::::#####')
    print('@@@---====>Created By :::NightShade::: <====---@@@')
    
    print()
    
    choice = input('Do you want to Decode[d] or Encode[e] or Quit[q]: ')
    
    print()

    if choice == 'd':
        decode_function()
    elif choice == 'e':
        encode_function()
    elif choice == 'q':
        print()
        print(exit_message)
        sys.exit()
    else:
        print()
        print('Sorry, Invalid Option')
        sys.exit()

def decode_function():
    #----Base64 Decode----#
    try:
        encoded_string = input('Encoded String : ')
        decoded_string = base64.b64decode(encoded_string.encode('ascii'))
        print (decoded_string.decode('ascii'))
        print()
    except:
        print('Invalid Input')

def encode_function():
    #----Base64 Encode----#
    try:
        decoded_string = input('Decoded String : ')
        encoded_string = base64.b64encode(decoded_string.encode('ascii'))
        print (encoded_string.decode('ascii'))
        print()
    except:
        print('Invalid Input')

main()

while 1==1:
    menu_option = input('Go back to main menu : Yes[y]/No[n]')
    if menu_option == 'y':
        main()
    else:
        print()
        print(exit_message)
        sys.exit()
