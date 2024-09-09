from tkinter import messagebox


def show_hint(self):
    possible_moves = []
    # Calculate possible moves for the current player
    for coin in self.robo_store:
        # Check if the coin can move forward
        if self.temp[coin-1] + self.move_red_counter <= 106:
            possible_moves.append((coin, self.temp[coin-1] + self.move_red_counter))
        # Check if the coin can capture an opponent's coin
        for opponent_coin in self.sky_blue_coin_position:
            if self.temp[coin-1] + self.move_red_counter == opponent_coin:
                possible_moves.append((coin, opponent_coin))
    
    # Display the two possible moves to the user
    if len(possible_moves) >= 2:
        move1 = possible_moves[0]
        move2 = possible_moves[1]
        messagebox.showinfo("Hint", f"Possible moves: {move1} or {move2}")
    else:
        messagebox.showinfo("Hint", "No possible moves found")