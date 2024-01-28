import os #for clear function

logo = '''
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

bidders_dict = {}

bidders = 1
while bidders != 0 :
    os.system('cls||clear')
    print(logo)
    name = input("What is your name?: ")
    bid_amount = int(input("What is your bid?: $"))

    bidders_dict[name] = bid_amount

    next_bidder = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
    if(next_bidder == "no") :
        bidders = 0

winner_name = ""
winner_bid = 0

for i in bidders_dict :
    if(winner_bid < bidders_dict[i]) :
        winner_bid = bidders_dict[i]
        winner_name = i

print(f"The winner is {winner_name} with bid of ${winner_bid}")
