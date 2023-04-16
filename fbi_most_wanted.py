import requests
import json

url = 'https://api.fbi.gov/wanted/v1/list'
r = requests.get(url)
print(f"Status Code: {r.status_code}")

outfile = open('fbi_most_wanted.json', 'w')

# create variable for json file requests
fbi_most_wanted = r.json()

# dump file into json file
json.dump(fbi_most_wanted, outfile, indent=4)

for data in fbi_most_wanted['items']:
    # prevent error when looking for age variable
    try:
        age = int(data['age_min'])
        if age < 25:
            correct_age = age
    except:
        age = 'No age available'

    if data['subjects'] == ['ViCAP Missing Persons'] and correct_age == age:
        print(f"Name: {data['title']}")
        print(f"FBI Direct Link: {data['files'][0]['url']}")
        print(f"Gender: {data['sex']}")
        print("Age: ", age)
        print(f"Eye Color: {data['eyes']}")
        print(f"Hair Color: {data['hair']}")
        print(f"Weight: {data['weight_min']}")
        print()
