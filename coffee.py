print("Welcome to the cafe!")

def coffee_bot():
    size = get_size()
    drink_type = get_drink_type()
    temp = icedhot()

    print("Alright, that's a {} {} {}!".format(size, temp, drink_type))

    extras()
    another()

def end():
    name = input("Can I get your name please?\n")
    print("Thanks, {}! Your order will be ready shortly.".format(name))
    return

def print_message():
    print("I'm sorry, I did not understand your selection. Please enter the corresponding letter for your response.")

def get_size():
    res = input("What size drink can I get for you?\n [a] Small\n [b] Medium\n [c] Large\n")

    if res == 'a':
        return 'small'
    elif res == 'b':
        return 'medium'
    elif res == 'c':
        return 'large'
    else:
        print_message()
        return get_size()

def get_drink_type():
    res = input("What type of drink would you like?\n [a] Brewed Coffee\n [b] Mocha\n [c] Latte\n ")

    if res == 'a':
        return 'brewed coffee'
    elif res == 'b':
        return 'mocha'
    elif res == 'c':
        return order_latte()
    else:
        print_message()
        return get_drink_type()

def order_latte():
    res = input("And what kind of milk for your latte?\n [a] 2% milk\n [b] Non-fat milk\n [c] Soy-milk\n ")

    if res == 'a':
        return 'latte'
    elif res == 'b':
        return 'non-fat latte'
    elif res == 'c':
        return 'soy latte'
    else:
        print_message()
        return order_latte()

def extras():
    res = input("Would you like a plastic cup or did you bring your own reusable cup?\n [a] I'll need a cup.\n [b] I brought my own.\n")

    if res == 'a':
        print("Okay, no problem! We'll get you a plastic cup.")
    elif res == 'b':
        print("Great! We'll fill your reusable cup.")
    else:
        print_message()
        return extras()

def icedhot():
    res = input("Would you like your drink iced or hot?\n [a] Iced\n [b] Hot\n")

    if res == 'a':
        return 'iced'
    elif res == 'b':
        return 'hot'
    else:
        print_message()
        return icedhot()

def yes():
    print("Of course!")
    coffee_bot()

def another():
    res = input("Would you like to order anything else?\n [a] Yes\n [b] No\n")

    if res == 'a':
        return yes()
    if res == 'b':
        return end()
    else:
        print_message()
        return another()

coffee_bot()