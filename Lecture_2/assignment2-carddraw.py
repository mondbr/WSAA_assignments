import requests


# shuffle the deck of cards
# get the deck id
url = "https://deckofcardsapi.com/api/deck/new/shuffle/?deck_count=1"
response = requests.get(url)

#extract the deck id
data = response.json()
deck_id = data["deck_id"]

# print the deck id
print(f"Deck shuffled, deck id is {deck_id}")

# draw 5 cards
draw_url = f"https://deckofcardsapi.com/api/deck/{deck_id}/draw/?count=5"
draw_response = requests.get(draw_url)

# extract the cards
cards = draw_response.json()["cards"]

# print the cards
print("You drew:")
for card in cards:
    value = card["value"]
    suit = card["suit"]
    print(f"{value} of {suit}")


