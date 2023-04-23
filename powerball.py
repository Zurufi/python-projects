import random

"""
Ali Alzurufi

This program simulates the Powerball Lottery and provides users with the opportunity to experience the odds of winning. 
By accurately mimicking the Powerball Lottery process, users can gain a deeper understanding of the challenges involved in winning. 
This program offers a fun and educational experience for those interested in the Powerball Lottery.

Date: 03/22/23

"""


class Player:
    def __init__(self, balance):
        """
        Initializes the Player object with a given balance.
        """
        self.balance = balance

    def spending(self, amount):
        """
        Reduces the player's balance by a given amount.
        """
        self.balance -= amount

    def winner(self, amount):
        """
        Increases the player's balance by a given amount.
        """
        self.balance += amount

    def get_balance(self) -> int:
        """
        Returns the player's current balance.
        """
        return self.balance


def generate_powerball():
    """
    Generates a list of 5 random numbers between 1 and 69, and a random number between 1 and 26 for the powerball.
    Returns the list of numbers as strings.
    """
    powerball = []

    for _ in range(5):
        powerball.append(str(random.randint(1, 69)))

    powerball.append(str(random.randint(1, 26)))

    return powerball


def get_valid_input(prompt: str, validation):
    """
    Takes a prompt and a validation function as input, and repeatedly prompts the user for input until
    the input passes the validation function.
    Returns the validated input.
    """
    while True:
        user_input = input(prompt)

        if validation(user_input):
            return user_input

        else:
            print("Invalid Input. Try again")
            print()
            continue


def is_valid_whiteball(white_ball: str) -> str:
    """
    Takes a string representing a set of five numbers separated by spaces.
    Returns True if the string contains exactly five numbers between 1 and 69, False otherwise.
    """
    balls = white_ball.split()

    if len(balls) != 5:
        return False

    for ball in balls:
        if not ball.isdigit() or not 1 <= int(ball) <= 69:
            return False

    return True


def is_valid_redball(red_ball: str):
    """
    Takes a string representing a single number.
    Returns True if the number is between 1 and 26, False otherwise.
    """
    return red_ball.isdigit() and 1 <= int(red_ball) <= 26


def valid_ticket(ticket: str):
    """
    Takes a string representing a ticket number.
    Returns True if the number is either 1 or 2, False otherwise.
    """
    return ticket.isdigit() and 1 <= int(ticket) <= 2


def prizes(matched_balls, powerball, jackpot_amount):
    """
    Takes the number of matched balls, a boolean indicating whether the powerball matches,
    and the current jackpot amount as input.
    Determines the prize amount based on the number of matched balls and the powerball, using the given prize table.
    Prints the prize amount and returns it.
    """
    prize_table = {
        (0, True): 4,
        (1, True): 4,
        (2, True): 7,
        (3, False): 7,
        (3, True): 100,
        (4, False): 100,
        (4, True): 50_000,
        (5, False): 1_000_000,
        (5, True): jackpot_amount
    }

    if (matched_balls, powerball) in prize_table:
        amount = prize_table[(matched_balls, powerball)]
        print(f"Congrats, you've won ${amount:,}")
        return amount

    else:
        print("You've lost!")
        return 0


def prize_multiplied(matched_balls, powerball):
    """
    Takes the number of matched balls and a boolean indicating whether the powerball matches as input.
    Determines the prize amount based on the number of matched balls and the powerball, using the given prize table
    and a random multiplier based on the current jackpot amount.
    Returns the prize amount.
    """
    jackpot = 100_000_000

    if jackpot < 150_000_000:
        multiplier = 10

    else:
        multiplier = random.randint(2, 5)

    prize_table = {
        (0, True): 4 * multiplier,
        (1, True): 4 * multiplier,
        (2, True): 7 * multiplier,
        (3, False): 7 * multiplier,
        (3, True): 100 * multiplier,
        (4, False): 100 * multiplier,
        (4, True): 50_000 * multiplier,
        (5, False): 1_000_000,
        (5, True): jackpot
    }

    if (matched_balls, powerball) in prize_table:
        amount = prize_table[(matched_balls, powerball)]
        print(f"Congrats, you've won ${amount:,}")
        return amount

    else:
        print("You've lost!")
        return 0


def check_ticket_price(matched_balls, powerball, ticket, jackpot_amount):
    """
    Takes the number of matched balls, a boolean indicating whether the powerball matches,
    a ticket number, and the current jackpot amount as input.
    Determines the price of the ticket based on the ticket number.
    If the ticket number is 1, calls the prizes function to determine the prize amount.
    If the ticket number is 2, calls the prize_multiplied function to determine the prize amount.
    Returns the prize amount.
    """
    if int(ticket) == 1:
        cash_prize = prizes(matched_balls, powerball, jackpot_amount)
        return cash_prize

    elif int(ticket) == 2:
        cash_prize_multiplied = prize_multiplied(matched_balls, powerball)
        return cash_prize_multiplied


def jackpot_result(player_ticket, jackpot_ticket, jackpot_amount):
    """
    Takes the player's ticket, the winning ticket, and the current jackpot amount as input.
    Compares the two tickets. If they match, prints a message indicating the player has won the jackpot and exits.
    If they do not match, increases the jackpot amount by $10,000,000 and prints the new jackpot amount.
    Returns the new jackpot amount.
    """
    if player_ticket != jackpot_ticket:
        jackpot_amount += 10_000_000
        print(f"Jackpot: ${jackpot_amount:,}")

    elif player_ticket == jackpot_ticket:
        print("You've hit the Jackpot! ")
        exit(0)

    return jackpot_amount


def check_spending(ticket: str):
    """
    Takes a ticket number as input.
    Returns the price of the ticket based on the ticket number.
    """
    if int(ticket) == 1:
        return 2

    elif int(ticket) == 2:
        return 3


def verify_amount(amount: str):
    """
    Takes an amount as input.
    Returns True if the amount is a valid integer between 2 and 100, False otherwise.
    """
    return amount.isdigit() and 2 <= int(amount) <= 100


def get_player_ticket():
    """
    Prompts the user to enter their ticket numbers.
    Validates the input using the is_valid_whiteball and is_valid_redball functions.
    Returns the validated input as a list of strings.
    """
    white_balls = get_valid_input(
        "Enter five numbers for white balls separated by a space: ", is_valid_whiteball).split()

    red_ball = get_valid_input(
        "Enter a number for the red ball: ", is_valid_redball).split()

    return white_balls + red_ball


def play_lottery():
    """
    Main function that runs the lottery game.
    """

    jackpot_amount = 100_000_000
    # Prompt user for starting amount and create player object
    amount = get_valid_input(
        "Enter starting amount between $2-100: $", verify_amount)
    player = Player(int(amount))

    # Loop through game rounds while player has balance
    while True:
        # Display current balance
        print(f"Balance: ${player.get_balance():,}")

        # Check for insufficient funds or no balance
        if player.get_balance() == 0:
            print("You are out of money! Game over")
            break

        elif player.get_balance() < 2:
            print("You have insufficient funds! Game over")
            break

        # Prompt user for type of ticket and check price
        ticket = get_valid_input(
            "Enter 1 for a basic ticket ($2), or enter 2 for a PowerPlay ticket ($3): ", valid_ticket)
        print()
        ticket_price = check_spending(ticket)

        # Check for insufficient funds for PowerPlay ticket
        if ticket_price == 3 and player.get_balance() == 2:
            print("You do not have enough to get the PowerPlay")
            continue

        # Check if player has enough funds to purchase ticket
        if ticket_price > player.get_balance():
            print("You do not have enough money to purchase a ticket! Game over")
            break

        # Subtract ticket price from player balance
        player.spending(ticket_price)

        # Generate player and jackpot tickets
        player_ticket = get_player_ticket()
        jackpot_ticket = generate_powerball()

        # Display player and winning tickets
        print()
        print("Your ticket:     ", *player_ticket)
        print("Winning numbers: ", *jackpot_ticket)
        print()

        # Determine number of matched balls and if Powerball matches
        matched_balls = len(
            set(player_ticket[:-1]).intersection(set(jackpot_ticket[:-1])))
        powerball = player_ticket[-1] == jackpot_ticket[-1]

        # Award player winnings and update jackpot amount
        player.winner(check_ticket_price(
            matched_balls, powerball, ticket, jackpot_amount))
        jackpot_amount = jackpot_result(
            player_ticket, jackpot_ticket, jackpot_amount)

        # Prompt user to continue playing or quit
        response = input("Press any key to continue playing, or 'q' to quit: ")
        if response.lower() in ['q', 'quit']:
            break
        print()


play_lottery()
