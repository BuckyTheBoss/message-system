import json


MESSAGE_FILE_PATH = 'data/messages.json'


def get_all_messages():
    '''Get a list of all the messages, loaded from the json file.'''
    with open('data/messages.json') as file:
        messages = json.load(file) 
    return messages


def save_messages(messages):
    '''Save the given messages (list) to the json file.'''
    with open('data/messages.json', 'w') as file:
        json.dump(messages, file)
    print('messages saved')


def get_messages(username):
    '''Get a list of all messages which are addressed to the given user.'''
    all_messages = get_all_messages()
    user_messages = []
    for message in all_messages:
        if message['to'] == username:
            user_messages.append(message)

    return user_messages



def get_message(id):
    '''Get the message with the given id.
    Return it if found, otherwise return None.'''
    all_messages = get_all_messages()
    for message in all_messages:
        if message['id'] == id:
            return message
    else:
        return None



def get_next_id(messages):
    max_id = 0
    for message in messages:
        if message['id'] > max_id:
            max_id = message['id']
    return max_id + 1


def add(message):
    all_messages = get_all_messages()
    all_messages.append(message)
    save_messages(all_messages)
    '''Add the given message to the list of all messages.
    Then save the updated list of messages to the json file.
    Be sure that the new message also includes an id!'''

def get_sent_messages(username):
    '''Get a list of all messages which are addressed to the given user.'''
    all_messages = get_all_messages()
    user_messages = []
    for message in all_messages:
        if message['from'] == username:
            user_messages.append(message)

    return user_messages