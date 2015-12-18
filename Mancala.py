"""
Student facing implement of solitaire version of Mancala - Tchoukaillon
Goal: Move as many seeds from given houses into the store
In GUI, you make ask computer AI to make move or click to attempt a legal move
"""

from tkinter import *

class SolitaireMancala:
    """
    Simple class that implements Solitaire Mancala
    """
    
    def __init__(self):
        """
        Create Mancala game with empty store and no houses
        """
        self.configuration = [0]
        
    
    def set_board(self, configuration):
        """
        Take the list configuration of initial number of seeds for given houses
        house zero corresponds to the store and is on right
        houses are number in ascending order from right to left
        """
        my_rev_list = list(configuration)
        # my_rev_list.reverse()
        self.configuration = my_rev_list
    
    def __str__(self):
        """
        Return string representation for Mancala board
        """
        my_str =""
	# we print store on right hand side
	# so reverse the order on the print out
        my_mancala_board = list(self.configuration)
        my_mancala_board.reverse()
        for seed in my_mancala_board:
            my_str += str(seed) + ", "
        my_str = my_str.rstrip()
        my_str = my_str.rstrip(',')

        return my_str
    
    def get_num_seeds(self, house_num):
        """
        Return the number of seeds in given house on board
        """
        return(self.configuration[house_num])

    def is_game_won(self):
        """
        Check to see if all houses but house zero are empty
        """
        game_won = True
        for house_num in range(len(self.configuration)-1):
            if ((house_num >0) and (self.configuration[house_num] != 0)):
                game_won = False
        return(game_won)
    
    def is_legal_move(self, house_num):
        """
        Check whether a given move is legal
        """
	# get seeds from the given house number
        # we should have one and only one seed put in last house. 
        # Since we index the store and houses from right to left 
        # starting at zero for the store, moving the seeds from a 
        # particular house is legal exactly when the number of seeds 
        # in the house matches the house's index.
        num_seeds_in_house = self.get_num_seeds(house_num)
        if (num_seeds_in_house == house_num):
            return True
        else:
            return False
    
    def apply_move(self, house_num):
        """
        Move all of the stones from house to lower/left houses
        Last seed must be played in the store (house zero)
        """
        if (self.is_legal_move(house_num)):
            num_seeds = self.get_num_seeds(house_num)
            # zero the house which we are taking the seeds from
            self.configuration[house_num] = 0
            # apply the seeds to the other houses
            for seed in range(num_seeds):
                house_num -= 1
                self.configuration[house_num] += 1
        else:
            print("illegal move")

    def choose_move(self):
        """
        Return the house for the next shortest legal move
        Shortest means legal move from house closest to store
        Note that using a longer legal move would make smaller illegal
        If no legal move, return house zero
        """
        found_move = False
        for house_num in range(len(self.configuration)-1):
            if ((self.is_legal_move(house_num)) and (house_num != 0)):
                found_move = True
                return house_num
        
        if (found_move == False):
            return (0)
        
    
    def plan_moves(self):
        """
        Return a sequence (list) of legal moves based on the following heuristic: 
		After each move, move the seeds in the house closest to the store 
		when given a choice of legal moves
        Not used in GUI version, only for machine testing
        """
        return []
 

# Create tests to check the correctness of your code

def test_mancala():
    """
    Test code for Solitaire Mancala
    """
    
    my_game = SolitaireMancala()
    print("Testing init - Computed:", my_game, "Expected: [0]")
    
    config1 = [0, 0, 1, 1, 3, 5, 0]    
    my_game.set_board(config1)
    #print(str(my_game))
    
    print("Testing set_board - Computed:", str(my_game), "Expected:", str([0, 5, 3, 1, 1, 0, 0]))
    print("Testing get_num_seeds - Computed:", my_game.get_num_seeds(1), "Expected:", config1[1])
    print("Testing get_num_seeds - Computed:", my_game.get_num_seeds(3), "Expected:", config1[3])
    print("Testing get_num_seeds - Computed:", my_game.get_num_seeds(5), "Expected:", config1[5])

    # add more tests here
    # only legal move at start with config1 is house_num 5
    print("Testing legal moves - Computed:", my_game.is_legal_move(5), "Expected:", "True")
    print("Testing legal moves - Computed:", my_game.is_legal_move(4), "Expected:", "False")
    print("Testing legal moves - Computed:", my_game.is_legal_move(1), "Expected:", "False")

    # test that we get the right correct move back
    house_num_of_move = my_game.choose_move()
    print("Testing best move - Computed:", str(house_num_of_move), "Expected:", "5")
    # test the play move function, start with only valid play
    my_game.apply_move(5)
    print("Testing move, House 5, - Computed;", str(my_game), "Expected:", str([0,0,4,2,2,1,1]))
    print("Testing game won functions - Computed:", my_game.is_game_won(), "Expected:", "False")

    # test that we get the next right move back
    house_num_of_move = my_game.choose_move()
    print("Testing best move - Computed:", str(house_num_of_move), "Expected:", "1")
    my_game.apply_move(1)
    print("Testing move, House 1, - Computed;", str(my_game), "Expected:", str([0,0,4,2,2,0,2]))
    print("Testing game won functions - Computed:", my_game.is_game_won(), "Expected:", "False")
    
    my_game.apply_move(2)
    print("Testing move, House 2, - Computed;", str(my_game), "Expected:", str([0,0,4,2,0,1,3]))
    print("Testing game won functions - Computed:", my_game.is_game_won(), "Expected:", "False")

    my_game.apply_move(1)
    print("Testing move, House 2, - Computed;", str(my_game), "Expected:", str([0,0,4,2,0,0,4]))
    print("Testing game won functions - Computed:", my_game.is_game_won(), "Expected:", "False")

    my_game.apply_move(4)
    print("Testing move, House 2, - Computed;", str(my_game), "Expected:", str([0,0,0,3,1,1,5]))
    print("Testing game won functions - Computed:", my_game.is_game_won(), "Expected:", "False")

    my_game.apply_move(1)
    print("Testing move, House 2, - Computed;", str(my_game), "Expected:", str([0,0,0,3,1,0,6]))
    print("Testing game won functions - Computed:", my_game.is_game_won(), "Expected:", "False")

    my_game.apply_move(3)
    print("Testing move, House 2, - Computed;", str(my_game), "Expected:", str([0,0,0,0,2,1,7]))
    print("Testing game won functions - Computed:", my_game.is_game_won(), "Expected:", "False")

    my_game.apply_move(1)
    print("Testing move, House 2, - Computed;", str(my_game), "Expected:", str([0,0,0,0,2,0,8]))
    print("Testing game won functions - Computed:", my_game.is_game_won(), "Expected:", "False")

    my_game.apply_move(2)
    print("Testing move, House 2, - Computed;", str(my_game), "Expected:", str([0,0,0,0,0,1,9]))
    print("Testing game won functions - Computed:", my_game.is_game_won(), "Expected:", "False")

    my_game.apply_move(1)
    print("Testing move, House 2, - Computed;", str(my_game), "Expected:", str([0,0,0,0,0,0,10]))
    print("Testing game won functions - Computed:", my_game.is_game_won(), "Expected:", "True")
    
    
test_mancala()

root = Tk()

w = Label(root, text="Hello, world!")
w.pack()

root.mainloop()

# Import GUI code once you feel your code is correct
# import poc_mancala_gui
# poc_mancala_gui.run_gui(SolitaireMancala())

