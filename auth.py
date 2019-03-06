import json


USERS_FILE_PATH = 'data/users.json'


def login(username, password):
	'''Load all users from the json file.
	If a user is found with a matching username AND password,
	return True. Otherwise, return False.'''
	with open('data/users.json') as file:
		users = json.load(file) 
	for user in users:
		if username == user['username'] and password == user['password']:
			return True
	else:
		return False
	
def get_users():
	with open('data/users.json') as file:
		users = json.load(file)
	user_list = [] 
	for user in users:
		user_list.append(user['username'])
	return user_list