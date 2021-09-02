"""
Magic 8-ball fortune teller


"""
import random

def fortune_getter_bool(answernumber):
    if answernumber == 0:
        return 'it is certain'
    elif answernumber == 1:
        return 'it is decidedly so'
    elif answernumber == 2:
        return 'yes'
    elif answernumber == 3:
        return 'reply hazy try again'
    elif answernumber == 4:
        return 'ask again later'
    elif answernumber == 5:
        return 'concentrate and ask again'
    elif answernumber == 6:
        return 'my reply is no'
    elif answernumber == 7:
        return 'outlook not so good'
    elif answernumber == 8:
        return 'very doubtful'

def fortune_getter_list():
    messages = ['it is certain', 
                'it is decidedly so', 
                'yes',
                'reply hazy try again',
                'ask again later',
                'concentrate and ask again',
                'my reply is no',
                'outlook not so good',
                'very doubtful']
    
    idx = random.randint(0, len(messages) - 1)
    
    return messages[idx]
    








