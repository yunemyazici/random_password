import random
import re

def main():
    vowels = "aeiouAEIOU"
    consonants = "bcdfghjklmnpqrstwvxyzBCDFGHJKLMNPQRSTWVXYZ"
    numbers = "1234567890"
    characters = "-=~!@#$%^&*()_+`[]{};:ZXCVBNMzxcvbnm<>,./?"
    choices = [vowels, consonants, numbers, characters]

    how_long = input("how long do you want your password to be?: ")
    a = re.search(r"[0-9]+", how_long)
    while not a:
        print("please enter a number")
        how_long = input("how long do you want your password to be?: ")
        a = re.search(r"[0-9]+", how_long)

    password = []

    loop = int(how_long)

    while (loop>0):
        which = random.choice(choices)
        index = random.randint(0,len(which)-1)
        password.append(which[index])
        loop-=1


    generated_password = "".join(password)
    print(f"{generated_password}")

if __name__ == "__main__":
    main()
