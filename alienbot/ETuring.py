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
        "What planets have you visited? \n",
        "What technology do you have on this planet? \n"
    )

    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'.*\s*your planet.*',
            'answer_why_intent': r'why\sare.*',
            'cubed_intent': r'.*cube.*(\d+)',
            'how_intent': r'how\s.*',
            'curious_intent': r'.*\s*curious.*',
            'my_turn_intent': r'ask\sme.*',
            'add_intent': r'.*(\d+).*plus.*(\d+)'
            # 'unsure_response_intent': r''
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
        while not self.negative_res(reply):
            reply = input(self.match_reply(reply))

    def match_reply(self, reply):
        for key, value in self.alienbabble.items():
            intent = key
            regex_pattern = value
            found_match = re.match(regex_pattern, reply)
            # Add more intents
            if found_match and intent == 'describe_planet_intent':
                return self.describe_planet_intent()
            elif found_match and intent == 'answer_why_intent':
                return self.answer_why_intent()
            elif found_match and intent == 'cubed_intent':
                return self.cubed_intent(found_match.groups()[0])
            elif found_match and intent == 'how_intent':
                return self.how_intent()
            elif found_match and intent == 'curious_intent':
                return self.curious_intent()
            elif found_match and intent == 'my_turn_intent':
                return self.my_turn_intent()
            elif found_match and intent == 'add_intent':
                return self.add_intent((found_match.groups()[0]),(found_match.groups()[0]))
            # elif found_match and intent == 'unsure_response_intent':
            #     return self.unsure_response_intent()
            # else:
            #     return
        return self.no_match_intent()
    
    def describe_planet_intent(self):
        responses = (
            "My planet is a utopia of diverse organisms and species. \n",
            "I am from South 4 Legion, the capital of the Gamvid Galaxies. \n",
            "I am from a galaxy far away where our beings are far too advanced for the human body. \n",
            "I am from a world where currency is obsolete. \n"
        )
        return random.choice(responses)

    def answer_why_intent(self):
        responses = (
            "I come in peace. \n",
            "I am here to collect data on your planet and its inhabitants. \n",
            "I heard the coffee is good. \n",
            "I was bored of my planet. \n",
            "I wanted to go sight-seeing. \n"
        )
        return random.choice(responses)

    def cubed_intent(self, number):
        number = int(number)
        cubed_number = number ** 3
        return "The cube of {} is {}. \n".format(number, cubed_number)

    def how_intent(self):
        responses = (
            "Our technology is advanced. \n",
            "In my world, this is not unusual. \n",
            "We are the all-knowing. \n"
        )
        return random.choice(responses)

    def curious_intent(self):
        responses = (
            "Curiousity killed the cat. \n",
            "Knowledge is power. \n",
            "One day, you will find out. Maybe. \n",
            "Look up cryopreservation. See for yourself. \n"
        )
        return random.choice(responses)

    def my_turn_intent(self):
        self.chat()

    def add_intent(self, number1, number2):
        number1 = int(number1)
        number2 = int(number2)
        added = number1 + number2
        return "The sum of {} and {} is {}. \n".format(number1, number2, added)

    def no_match_intent(self):
        responses = (
            "Please tell me more. \n",
            "Tell me more! \n",
            "Why do you say that? \n",
            "I see. Can you elaborate? \n",
            "Interesting. Can you tell me more? \n",
            "I see. How do you think? \n",
            "Why? \n",
            "How do you think I feel when you say that? \n"
        )
        return random.choice(responses)

    def unsure_response_intent(self):
        responses = (
            "I'm not sure if I understand. \n",
            "Can you explain another way? \n",
            "I didn't catch that. Can you elaborate? \n"
        )
        return random.choice(responses)

ETuring = AlienBot()
ETuring.greet()
