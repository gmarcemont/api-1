from operator import itemgetter
import requests
import json

# Make an API call, and store the response.
url = 'https://hacker-news.firebaseio.com/v0/topstories.json'
r = requests.get(url)
print(f"Status code: {r.status_code}")

# Explore the structure of the data.
outfile = open('hn.json', 'w')

json.dump(r.json(), outfile, indent=4)

submission_ids = r.json()

url = 'https://hacker-news.firebaseio.com/v0/item/35457341.json'
r = requests.get(url)

outfile = open('hn2.json', 'w')
json.dump(r.json(), outfile)

for id in submission_ids[:11]:
    url = f"https://hacker-news.firebaseio.com/v0/item/{id}.json"
    r = requests.get(url)
    response_dict = r.json()
    submission_list = []
   # print(f'title: {response_dict["title"]}')
    # print(f'link: http://news.ycombinator.com/item?id={id}')
   # try:
    #    print(f"comments: {response_dict['descendants']}")
    # except:
    #   print(f"comments: 0")

    a_dict = {
        'title': response_dict["title"],
        'url': 'http://news.ycombinator.com/item?id={id}',
        'comments': response_dict['descendants']
    }

    submission_list.append(a_dict)


submission_list = sorted(
    submission_list, key=itemgetter('Comments'), reverse=True)

for d in submission_list:
    print(f"Title: {d['title']}")
    print(f"Link: {d['link']}")
    print(f"Comments: {d['Comments']}")
