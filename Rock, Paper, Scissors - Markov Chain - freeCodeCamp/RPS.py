import itertools
import random

moves = ['R', 'P', 'S']

play_order_dict = {''.join(seq): 0 for seq in itertools.product(moves, repeat=5)}
def player(prev_play, opponent_history=[],
    play_order = [play_order_dict]):

    if not prev_play:
        prev_play = 'S'
    opponent_history.append(prev_play)

    if len(opponent_history) >= 5:
        last_five = "".join(opponent_history[-5:])
        play_order[0][last_five] += 1
    
    if len(opponent_history) >= 4:
        last_four = "".join(opponent_history[-4:])

        potential_plays = [
            last_four + "R",
            last_four + "P",
            last_four + "S",
        ]

        sub_order = {
            k: play_order[0][k]
            for k in potential_plays if k in play_order[0]
        }
        prediction = max(sub_order, key=sub_order.get)[-1:]

    else:
        # Fallback for first 1-2 moves
        prediction = random.choice(['R','P','S'])

    ideal_response = {'P': 'S', 'R': 'P', 'S': 'R'}
    return ideal_response[prediction]