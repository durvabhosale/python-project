logo = r'''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''
print(logo)
def find_highest_bidder(bid_list):
    highest_bid = 0
    winner = ""

    for name in bid_list:
        bid = bid_list[name]

        if bid > highest_bid:
            highest_bid = bid
            winner = name

    print(f"The winner is {winner} with a bid of ${highest_bid}")


bids = {}
continue_bid = True

while continue_bid:
    name = input("Enter your name: ")
    bid = int(input("Please enter your bid: $"))

    bids[name] = bid

    choice = input("Are there any other bidders? (yes/no): ").lower()
    print(f"\n" * 20)
    if choice == "no":
        continue_bid = False

find_highest_bidder(bids)
