"""
Ali Alzurufi

This program is a macronutrients calculator that enables users to calculate their own macronutrient intake and keep track of it. 
The program prompts users with a series of questions to determine their ideal macronutrient intake. 
This information can be used to help users create meal plans that align with their fitness goals, track their progress over time, 
and make informed decisions about their dietary habits.

Date: 03/15/23

"""


class Macros:
    """
    A class for calculating macronutrient requirements based on user inputs.

    """

    def get_calories(self, weight: int, goal: int, activity_level: int) -> int:
        """
        Calculates the number of calories required per day based on user inputs.

        """
        calories_mult = {
            (1, 1): 11,
            (1, 2): 13,
            (1, 3): 15,
            (2, 1): 13,
            (2, 2): 15,
            (2, 3): 19,
            (3, 1): 15,
            (3, 2): 17,
            (3, 3): 20
        }

        calories = weight * calories_mult[(goal, activity_level)]
        return calories

    def get_macros(self, body_type: int, calories: int) -> tuple:
        """
        Calculates the macronutrient requirements (protein, carbs, and fats) based on user inputs.

        """
        if body_type == 1:
            protein_grams = round((calories * 0.25) / 4)
            carbs_grams = round((calories * 0.55) / 4)
            fats_grams = round((calories * 0.20) / 9)

        elif body_type == 2:
            protein_grams = round((calories * 0.30) / 4)
            carbs_grams = round((calories * 0.40) / 4)
            fats_grams = round((calories * 0.30) / 9)

        elif body_type == 3:
            protein_grams = round((calories * 0.35) / 4)
            carbs_grams = round((calories * 0.25) / 4)
            fats_grams = round((calories * 0.40) / 9)

        return protein_grams, carbs_grams, fats_grams


def get_user_input(user_input: str, validation, type_=int) -> int:
    """
    Get input from user and validate it.

    """
    while True:
        value = input(user_input)

        try:
            value = type_(value)
        except ValueError:
            print("Error: Enter a valid value.")
            print()
            continue

        if validation(value):
            return value

        else:
            print("Error: Enter a valid input. ")
            print()


def valid_user_weight(user_weight: int):
    """
    Valid user input for weight
    """
    return 1 <= user_weight <= 800


def valid_fitness_goal(user_fitness_goal: int):
    """
    Valid user input for fitness goals
    """
    return 1 <= user_fitness_goal <= 3


def valid_activity_level(user_activity_level: int):
    """
    Valid user input for activity level
    """
    return 1 <= user_activity_level <= 3


def valid_body_type(user_body_type: int):
    """
    Valid user input for body type
    """
    return 1 <= user_body_type <= 3


def main():
    """
    The main function takes user input for weight, fitness goal, activity level, and body type to calculate
    the recommended daily macronutrient intake using the Macros class.

    """

    # Create an instance of the Macros class and dictionaries mapping values for fitness goals, activity levels, and body types
    user_macros = Macros()

    fitness_dict = {
        1: 'Lose Weight',
        2: 'Maintain Weight',
        3: 'Gain Weight'
    }

    activity_dict = {
        1: 'Minimal Exercise',
        2: 'Active Exercise',
        3: 'Very Active Exercise'
    }

    body_type_dict = {
        1: 'Ectomorph',
        2: 'Mesomorph',
        3: 'Endomorph'
    }

    # Prompt user for input and display options for fitness goals, activity levels, and body types
    fitness_prompt = "Enter your fitness goal: "
    for key, value in fitness_dict.items():
        fitness_prompt += f"({key}. {value}) "

    activity_prompt = "Enter your activity level: "
    for key, value in activity_dict.items():
        activity_prompt += f"({key}. {value}) "

    body_prompt = "Enter your body type: "
    for key, value in body_type_dict.items():
        body_prompt += f"({key}. {value}) "

    # Get user input for weight, fitness goal, activity level, and body type
    weight = get_user_input("Enter your weight: ", valid_user_weight, int)
    print()

    fitness_goal = get_user_input(
        f"{fitness_prompt}: ", valid_fitness_goal, int)
    print()

    activity_level = get_user_input(
        f"{activity_prompt}: ", valid_activity_level, int)
    print()

    body_type = get_user_input(f"{body_prompt}: ", valid_body_type, int)
    print()

    # Calculate daily caloric needs and macronutrient recommendations based on user input
    calories = user_macros.get_calories(weight, fitness_goal, activity_level)
    protein_grams, carbs_grams, fats_grams = user_macros.get_macros(
        body_type, calories)

    # Display results to the user
    print(f"Your weight is: {weight} lbs")
    print(f"Your fitness goal is: {fitness_dict[fitness_goal]}")
    print(f"Your activity level is: {activity_dict[activity_level]}")
    print(f"Your body type is: {body_type_dict[body_type]}")
    print()
    print(f"Recommended Calorie Intake: {calories}Kcal")
    print(
        f"Recommended Protein Intake: {protein_grams}g \nRecommended Carb Intake: {carbs_grams}g \nRecommended Fat Intake: {fats_grams}g")


main()
