from bs4 import BeautifulSoup

followers = []

# Read the HTML file
with open('followers.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find the first span with targeted class
all_follower_names = soup.find_all('span', class_='_ap3a _aaco _aacw _aacx _aad7 _aade')


for div in all_follower_names:
    followers.append(div.text)



followings = []

# Read the HTML file
with open('followings.html', 'r') as file:
    html_content = file.read()

soup = BeautifulSoup(html_content, 'html.parser')

# Find the first span with targeted class
all_following_names = soup.find_all('span', class_='_ap3a _aaco _aacw _aacx _aad7 _aade')


for div in all_following_names:
    followings.append(div.text)


only_followers = [x for x in followers if x not in followings]
only_followings = [x for x in followings if x not in followers]

print("Only Followers: ", only_followers)
print("Only Followings: ", only_followings)
