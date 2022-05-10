import random

with open('10000-english-words.txt','r') as f:
	data = f.read().split('\n')
data = [row for row in data if len(row) > 2]



def generated_pass(length=4):
	passw = []

	for i in range(length):
		word = random.choice(data)
		if random.random() > .5: word = word[0].upper()+word[1:]
		if random.random() > .5: word += str(random.randint(0,9))
		passw.append(word)

	return '.'.join(passw)

password = generated_pass()

print("password:")
print(password)