#Pull a list of users and write to a CSV file containing id and email

import requests
import csv

url = 'https://gorest.co.in/public-api/users'
params = {
	'status': 'active',
}

response = requests.get(url, params=params)

if response.status_code == 200:
	data = response.json()
	users = data['data']
	test_users = [user for user in users if 'test' in user['email']]
	if test_users:
		with open('test_users2.csv', mode='w', newline='') as file:
			writer = csv.writer(file)
			writer.writerow(['id', 'email'])
			for user in test_users:
				writer.writerow([user['id'], user['email']])
		print('CSV report generated successfully.')
	else:
		print('No users with "test" in the domain of their email addresses found.')
else:
	print('Failed to fetch data from API.')
