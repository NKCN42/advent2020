expenses = []
with open("input.txt", 'r') as f: 
	for l in f.readlines(): 
		expenses.append(int(l))

#print(expenses)

for i in range(0, len(expenses)): 
	for j in range(i+1, len(expenses)): 
		for k in range(j+1, len(expenses)): 
			if (expenses[i] + expenses[j] + expenses[k] == 2020):
				print(expenses[i]*expenses[j]*expenses[k])