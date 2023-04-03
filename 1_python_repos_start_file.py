from plotly import offline
from plotly.graph_objs import Bar
import requests
import json

# Make an API call and store the response.
url = 'https://api.github.com/search/repositories?q=language:python&sort=stars'
headers = {'Accept': 'application/vnd.github.v3+json'}
r = requests.get(url, headers=headers)
print(f"Status code: {r.status_code}")

outfile = open('output.json', 'w')

response_dict = r.json()

json.dump(response_dict, outfile, indent=4)


list_of_repos = response_dict['items']

# Number of repos
print(f"Number of repos: {len(list_of_repos)}")

# first repo = dictionary
first_repo = list_of_repos[0]

# print all keys for first repo in the dictionary
# for key in first_repo:
#  print(key)

# print out information from first_repos:

# the name of the repo
print(f"Name: {first_repo['name']}")
# the owner
print(f"Owner: {first_repo['owner']['login']}")
# the number of stars
print(f"Number of stars: {first_repo['stargazers_count']}")
# the URL of the repo
print(f"URL of the repo: {first_repo['html_url']}")
# when it was created
print(f"Created: {first_repo['created_at']}")
# when it was last updated
print(f"Updated: {first_repo['updated_at']}")
# the description
print(f"Description: {first_repo['description']}")

repos, stars = [], []


# grab first 10 using slicing
for repo in list_of_repos[:10]:
    repos.append(repo['name'])
    stars.append(repo['stargazers_count'])

# importing graph to put information

data = [
    {
        "type": "bar",
        "x": repos,
        "y": stars,
        "marker": {
            "color": "rgb(60,100,150)",
                "line": {"width": 1.5, "color": "rgb(25,25,25)"},
        },
        "opacity": 0.6,
    }
]

my_layout = {
    "title": "Most-Starred Python Reps on Github",
    "xaxis": {"title": "Repository"},
    "yaxis": {"title": "Stars"}
}

fig = {"data": data, "layout": my_layout}

offline.plot(fig, filename="python_repos.html")
