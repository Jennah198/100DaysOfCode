#def greet(name):
#    print(f  "hello {name}")
#    print("how are you " + name)
#
#name = input("What is your name?")
#greet(name)


#Write your code below this line 👇
#import math
#def paint_calc(height, width, cover):
#    result = (math.ceil((height*width) / cover,))
#    return result
#
#
#
#
#
##Write your code above this line 👆
## Define a function called paint_calc() so that the code below works.
#
## 🚨 Don't change the code below 👇
#test_h = int(input("Height of wall: "))
#test_w = int(input("Width of wall: "))
#coverage = 5
#result=  paint_calc(height=test_h, width=test_w, cover=coverage)
#print(f"You will need {result} can of paint.")




alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n'
            , 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

#TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.

def encrypt(ntext, nshift):
    #TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift
    # amount and print the encrypted text.

    #e.g.
    #plain_text = "hello"
    #shift = 5
    #cipher_text = "mjqqt"
    #print output: "The encoded text is mjqqt"

    ##HINT: How do you get the index of an item in a list:
    #https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

    ##🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛

#TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.