toysprice = 10
phonesprice = 899
stationaryprice = 3
andvariable = "and"
toys = ["teddy bears", "puzzles",andvariable,"scrabble"]
phones = ["samsung phones","apple phones",andvariable,"motorola phones"]
stationary = ["notebooks","pens",andvariable,"pencils"]
shop = (toys[ : 3],phones[ : 3],stationary [ : 3])
what_customer_origanally_wants = input("What do you want, we have toys, phones, and stationery? ").casefold()
if what_customer_origanally_wants == "toys":
    print("We have" + str(toys))
    choice = input("Which one do you want?").casefold()
    if choice in toys:
        print("OK," + choice + " is for " + str(toysprice) + " pounds")
    else:
        print("Sorry.We don't have that")
elif what_customer_origanally_wants == "phones":
    print("We have" + str(phones))
    choice = input("Which one do you want?").casefold()
    if choice in phones:
        print("OK," + choice + " is for " + str(phonesprice) + " pounds")
    else:
        print("Sorry.We don't have that")
elif what_customer_origanally_wants == "stationary":
    print("We have" + str(stationary))
    choice = input("Which one do you want? " ).casefold()
    if choice in stationary:
        print("OK," + choice + " is for " + str(stationaryprice) + " pounds")
    else:
        print("Sorry.We don't have that")

