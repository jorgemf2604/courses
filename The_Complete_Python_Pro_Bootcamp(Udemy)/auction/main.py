more_bidders = None
keep_asking = True
list_bidders = []


def print_welcome():
    print("👩‍⚖️👩‍⚖️👩‍⚖️ Welcome to the Secret Auction Program!! 👩‍⚖️👩‍⚖️👩‍⚖️")


def ask_user_info():
    user_name = input("What is your name? ")
    user_bid = int(input("What is your bid? "))
    new_bidder = {"name": user_name, "bid": user_bid}
    list_bidders.append(new_bidder)


def ask_if_more_bidders():
    global keep_asking
    more_bidders = input(
        "Are there any other bidders? Type 'yes' or 'no'. ")
    if more_bidders == 'no':
        keep_asking = False


def check_winner():
    highest_bid = 0
    highest_bidder = None
    for bidder in list_bidders:
        if bidder["bid"] > highest_bid:
            highest_bid = bidder["bid"]
            highest_bidder = bidder["name"]
    print(f"The winner is {highest_bidder} with a bid of ${highest_bid}")


def main():
    # globals
    global keep_asking
    global more_bidders
    global list_bidders

    print_welcome()
    while keep_asking:
        ask_user_info()
        ask_if_more_bidders()
    check_winner()


main()
