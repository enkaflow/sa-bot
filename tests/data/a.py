import requests
r = requests.get("http://skillattack.com/sa4/dancer_score.php?_=rival&ddrcode=51527333&style=0&difficulty=13")
print(r.text)
