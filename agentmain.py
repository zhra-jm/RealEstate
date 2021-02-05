from constants import PROFILE_MAPPER
while input("you wanna add? ").lower() == "y":
    ask_house_or_apartment = input("house or apartment: ").lower()
    ask_rental_or_purchasable = input("rent or purchase: ").lower()
    input_tuple = (ask_house_or_apartment, ask_rental_or_purchasable)
    profileClass = PROFILE_MAPPER[input_tuple]
    profileClass.prompt()




