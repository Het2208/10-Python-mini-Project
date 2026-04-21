# Weak:
# - Length < 6
# - or missing 3 out of 4 (upper/lower/digit/symbol)
# - or repetitive pattern
#
# Medium:
# - Length 6-10
# - Has 3 types (upper/lower/digit/symbol)
# - No dictionary match
#
# Strong:
# - Length > 10
# - Includes all 4 categories
# - No repetition, dictionary weakness


def passStrength(password):
    print()
    hasupper = any(ch.isupper() for ch in password)
    haslower = any(ch.islower() for ch in password)
    hasnumber = any(ch.isdigit() for ch in password)
    hasspecial = any(ch in "!@#$%^&*()_+-=" for ch in password)

    types = hasupper + haslower + hasnumber + hasspecial

    # repetitive pattern detection
    hasRepeat = (password[:len(password)//2] * 2 == password)

    # WEAK
    if len(password) < 6 or types <= 1 or hasRepeat:
        print(f"{'X' * len(password)} is Weak Password")
        return

    # MEDIUM
    if 6 <= len(password) <= 10 and types == 3 and not hasRepeat:
        print(f"{'X' * len(password)} is Medium Password")
        return

    # STRONG
    if len(password) > 10 and types == 4 and not hasRepeat:
        print(f"{'X' * len(password)} is Strong Password")
        return

    # FALLBACK CASE → Medium for types=2 or non-strong

    print(f"{'X' * len(password)} is Medium Password")


def main():
    print('*' * 40)
    print("Welcome to Password Strength Checker")
    print('*' * 40)
    password = input("Enter your password: ")
    print('*' * 40)
    passStrength(password)
main()
