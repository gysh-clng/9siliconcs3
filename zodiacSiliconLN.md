# Guayesha Citlalli V. Calanog
# 9 - Silicon
# Chinese Zodiac Sign - Graded Activity

# The requirements are the following:
This program should:
1. Ask the user to enter a birth year.
2. Utilize the year 1900 as its baseline.
3. Reject years earlier than said baseline year by displaying a proper error message for invalid years.
4. Upon appropriate input, determine the Chinese zodiac sign via the 12-year cycle.
5. However, this should only consider the inputted birth year.

# My Python Code

# The user will input their birth year.
BY = int(input("Enter your birth year: "))

# This part will confirm whether the inputted year is valid for evaluation.
if BY < 1900:
    print("Invalid Year, it should not be earlier than 1900.")
else:
    # List of zodiac signs starting from Rat.
    ZS = [
        "Rat (鼠 / Shǔ)",
        "Ox (牛 / Niú)",
        "Tiger (虎 / Hǔ)",
        "Rabbit (兔 / Tù)",
        "Dragon (龙 / Lóng)",
        "Snake (蛇 / Shé)",
        "Horse (马 / Mǎ)",
        "Goat (羊 / Yáng)",
        "Monkey (猴 / Hóu)",
        "Rooster (鸡 / Jī)",
        "Dog (狗 / Gǒu)",
        "Pig (猪 / Zhū)"
    ]

    # This will deduce the user's zodiac sign.
    Z = (BY - 1900) % 12
    
    print("Your Chinese Zodiac Sign is:", ZS[Z])
