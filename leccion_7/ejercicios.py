# 1. embellecer grafica (matplotlib Axes)
def prettify_graph(graph):
    """Agrega titulo, ajusta eje y y su etiqueta."""
    graph.set_title("Results of 500 slot machine pulls")
    graph.set_ylim(bottom=0)
    graph.set_ylabel("Balance")
    ticks = graph.get_yticks()
    new_labels = ["${}".format(int(amt)) for amt in ticks]
    graph.set_yticklabels(new_labels)

# 2. items de corredores ganadores (corregido, sin sombrear 'i')
def best_items(racers):
    winner_item_counts = {}
    for idx in range(len(racers)):
        racer = racers[idx]
        if racer["finish"] == 1:
            for item in racer["items"]:
                if item not in winner_item_counts:
                    winner_item_counts[item] = 0
                winner_item_counts[item] += 1
        if racer["name"] is None:
            print("WARNING: corredor sin nombre en iteracion {}/{} (racer = {})".format(
                idx + 1, len(racers), racer))
    return winner_item_counts

# 3. comparar manos de blackjack
def hand_total(hand):
    total = 0
    aces = 0
    for card in hand:
        if card in ["J", "Q", "K"]:
            total += 10
        elif card == "A":
            total += 11
            aces += 1
        else:
            total += int(card)
    while total > 21 and aces > 0:
        total -= 10
        aces -= 1
    return total

def blackjack_hand_greater_than(hand_1, hand_2):
    total_1 = hand_total(hand_1)
    total_2 = hand_total(hand_2)
    return total_1 <= 21 and (total_1 > total_2 or total_2 > 21)

if __name__ == "__main__":
    sample = [
        {"name": "Peach", "items": ["green shell", "banana", "green shell"], "finish": 3},
        {"name": "Bowser", "items": ["green shell"], "finish": 1},
        {"name": None, "items": ["mushroom"], "finish": 2},
        {"name": "Toad", "items": ["green shell", "mushroom"], "finish": 1},
    ]
    print(best_items(sample))
    print(blackjack_hand_greater_than(["K"], ["3", "4"]))
    print(blackjack_hand_greater_than(["K"], ["10"]))
