def pre_sell_tickets():

    #Create initial Variables
    total_tickets = 20
    total_buyers = 0

    # Create loop for selling tickets
    while total_tickets > 0:

            #prompt user to enter desired amount of tickets
            desired_tickets = int(input("Enter the number of tickets you want to buy up to 4: "))

            if desired_tickets < 1 or desired_tickets >  4:
                print("you may only buy between 1 and 4 tickets.")
                continue

            if desired_tickets > total_tickets:
                print(f"There are only {total_tickets} available.")
                continue

            total_tickets -= desired_tickets
            total_buyers += 1

            print(f"Tickets purchased: {desired_tickets}")
            print(f"Remaining tickets: {total_tickets}")

    print("tickets have been sold out.")
    print(f"Total number of buyers: {total_buyers}")

pre_sell_tickets()