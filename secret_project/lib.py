import random


def try_me(name, question):
    random_number = random.randint(1, 9)
    answer = ""
    random_number = random.randint(1, 9)
    if random_number == 1:
        answer = "Yes - definitely."
    elif random_number == 2:
        answer = "It is decidedly so."
    elif random_number == 3:
        answer = "Without a doubt."
    elif random_number == 4:
        answer = "Raply hazy, try again."
    elif random_number == 5:
        answer = "Ask again later."
    elif random_number == 6:
        answer = "Better not to tell you now."
    elif random_number == 7:
        answer = "My sources say no."
    elif random_number == 8:
        answer = "Outlook not so good."
    elif random_number == 9:
        answer = "Very doubtful."
    else:
        answer = "Error"
    return f"{name} asks {question}.... and the mighty Magic Ball's answer is: {answer}"
