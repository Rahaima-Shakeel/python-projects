import random

print ("Welcome to your Password Generator")

chars = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*()-_=+[]{}|;:'\",.<>?/";

number = int(input("Amount of passwords to generate: "))

length = int(input("Input your password length: "))

print("\nhere are your passwords: ")

for pwd in range(number):
    passwords = ""
    for c in range(length):
        passwords += random.choice(chars)
    
    print(passwords)