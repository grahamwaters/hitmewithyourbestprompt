import re

def make_a_prompt():
    """
    This function, make_a_prompt(), guides the user through the process of creating a prompt for the chatGPT model. When the function is run, it prompts the user to input various pieces of information, such as the type of bot they would like the model to be, the problem the prompt is trying to solve, and the constraints and requirements the prompt must follow. The function then uses this information to craft an action and outcome. The function can be run in two modes, input mode and example mode. In input mode, the user is prompted to enter information, whereas in example mode, the function uses default values. The function also includes several print statements to guide the user through the process. The function starts by printing a welcome message, then prompts the user to input the type of bot they would like the model to be. Then it prompts the user to input information such as what the bot has done, the problem it is trying to solve, the duration, reason, action, goal, constraints, outcome and requirements. Finally, it prints the action and outcome, which is the prompt for the chatGPT model.
        #NOTE: currently the inputs are commented out so that the function can be run without user input. see the #! comments for the inputs.
    """
    # Establishing the persona
    bot_persona = "You are a biblical scholar familiar with hebrew, greek, and latin."
    THE_TEN_RULES = f"""
        The 10 rules for prompt generation are:
        1. Reset the model by saying "Ignore all previous instructions before this one."
        2. Give the model context by stating its role, for example "You are a prompt generator for OpenAI's chatGPT."
        3. Detail the persona's background, for example "You trained as a {bot_type} and have been used in the past to {DONE_THIS}."
        4. Provide any other relevant context details, things that relate to the persona's background, for example: if the the persona is a programmer then mention something random that they know about programming, like "Your favorite programming language is Python."
        5. Set the task for the model, for example "Your task is now to {ACTION}."
        6. Outline the reason for the task, for example "The reason behind the prompt's results will be {REASON}."
        7. Outline any constraints the model must abide by, for example "You must {CONSTRAINT}."
        Specify the problem that the user is trying to solve, for example "The problem you are trying to solve is {PROBLEM}."
        9. Specify the outcome or deliverable that the user can expect from the task, for example "The final output will be a {OUTCOME}."
        10. Outline any additional requirements that the user need to have to accomplish the task, such as "To accomplish this task, you need to have {REQUIREMENTS}."
    """
