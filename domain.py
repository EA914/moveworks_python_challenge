#Pull a list of users from the API and their count by unique email domain and write to a CSV file

import requests
import csv
from collections import defaultdict
url = 'https://gorest.co.in/public-api/users'

response = requests.get(url)

if response.status_code == 200:
	data = response.json()
	users = data['data']
	#count the number of users for each domain
	domain_count = defaultdict(int)
	for user in users:
		email_domain = user['email'].split('.')[-1]
		domain_count[email_domain] += 1
	
	with open('emaildomaincount2.csv', mode='w', newline='') as file:
		writer = csv.writer(file)
		writer.writerow(['email_domain', 'user_count'])
		for domain, count in domain_count.items():
			writer.writerow([domain,count])
		
	print('CSV report success')
else:
	print('Failure')