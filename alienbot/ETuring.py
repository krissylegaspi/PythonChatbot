class AlienBot:
    negative_res = ("n", "no", "nope", "nah", "naw", "nawh", "not a chance", "sorry", "maybe next time", "no thanks", "nty", "nothx")
    exit_commands = ("q", "quit", "pause", "exit", "goodbye", "bye", "later", "see ya", "see ya later", "cya later", "cya")
    random_questions = (
        "Why are you here?",
        "Are there many humans like you?",
        "How did you get here?",
        "What do you consume for sustenence?",
        "Is there intelligent life on this plant?",
        "Is there intelligent life elsewhere?",
        "Does Earth have a leader?",
        "What planets have you visited",
        "What technology do you have on this planet?"
    )

    def __init__(self):
        self.alienbabble = {
            'describe_planet_intent': r'',
            'answer_why_intent': r'',
            'cubed_intent': r''
        }

    def greet(self):
        res = input("What is your name? \n")
        self.name = res

        will_help = input("Hi {}, I'm ET. I'm not from this planet. Will you help me learn about your planet? \n".format(res))

        if will_help in self.negative_res:
            print("Okay, have a nice Earth day! Goodbye. \n")
            return

        self.chat()

eturing = AlienBot()
eturing.greet()
