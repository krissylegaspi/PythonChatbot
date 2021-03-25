import re
import random
class AlienBot:
    negative_res = ("n", "no", "nope", "nah", "naw", "nawh", "not a chance", "sorry", "maybe next time", "no thanks", "nty", "nothx")
    exit_commands = ("q", "quit", "pause", "exit", "goodbye", "bye", "later", "see ya", "see ya later", "cya later", "cya")
    random_questions = (
        "Why are you here? \n",
        "Are there many humans like you? \n",
        "How did you get here? \n",
        "What do you consume for sustenence? \n",
        "Is there intelligent life on this plant? \n",
        "Is there intelligent life elsewhere? \n",
        "Does Earth have a leader? \n",
        "What planets have you visited \n",
        "What technology do you have on this planet? \n"
    )

    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'',
            'cubed_intent': r'',
            'unsure_response_intent': r''
        }

    def greet(self):
        res = input("What is your name? \n")
        self.name = res

        will_help = input("Hi {}, I'm ET. I'm not from this planet. Will you help me learn about your planet? \n".format(res))

        if will_help in self.negative_res:
            print("Okay, have a nice Earth day! Goodbye. \n")
            return

        self.chat()

    def make_exit(self, reply):
        for words in self.exit_commands:
            if words in reply:
                print("Okay, have a nice Earth day! Goodbye. \n")
                return True

    def chat(self):
        reply = input(random.choice(self.random_questions)).lower()
        while not self.make_exit(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for intent, regex_pattern in self.alienbabble.items():
            regex = r'.*text.*'
            reply = r'This is text'
            found_match = re.match(regex, reply)
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
    
    def describe_planet_intent(self):
        responses = (
            "My planet is a utopia of diverse organisms and species. \n",
            "I am from Opidipus, the capital of the Wayward Galaxies. \n",
            "I am from a galaxy far away where our beings are far too advanced for the human body. \n",
            "I am from a world where currency is obsolete. \n"
        )
        return random.choice(responses)

eturing = AlienBot()
eturing.greet()
