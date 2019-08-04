import numpy as np

class Agent:    
    def __init__(self, eps = 0.1, alpha = 0.5):
        self.eps = eps # probability of choosing random action instead of greedy
        self.alpha = alpha # learning rate
        self.verbose = False
        self.state_history = []
        
    def setV(self, V):
        self.V = V
    
    def set_symbol(self, sym):
        self.sym = sym
        
    def set_verbose(self, v):
        # if true, will print values for each position on the board
        self.verbose = v
    
    def reset_history(self):
        self.state_history = []
    
    def update():
        

    def update_state_history(state):
        state = state
        
    def take_action(environment):
        # choose an action based on epsion-greedy strategy
        r = np.random.rand()
        best_state = None
        if r < self.rps:
            # take a random action
            if self.verbose:
                print "Taking a random action"
            
            possible_moves = []
            for i in xrange(LENGTH):
                for j in xrange(LENGTH):
                    if env.is_empty(i, j):
                        possible_moves.append((i,j))
            idx = np.random.choice(len(possible_moves))
            next_move = possible_moves[idx]
        else:
            next_move = None
            best_value = -1
            for i in xrange(LENGTH):
                for j in xrange(LENGTH):
                    if env.is_empty(i, j):
                        # what is the state if we made this move?
                        env.board[i,j] = self.sym
                        state = env.get_state()
                        env.board[i,j] = 0 # don't forget to change it back!
                        if self.V[state] > best_value:
                            best_value = self.V[state]
                            best_state = state
                            next_move = (i, j)
        
        
        
class Environment:
    def __init__(self):
        self.board = np.zeros((LENGTH, LENGTH))
        self.x = -1 # represents an x on the board, player 1
        self.o = 1 # represents an o on the board, player 2
        self.winner = None
        self.ended = False
        self.num_states = 3**(LENGTH*LENGTH)
        
    def is_empty(self, i, j):
        return self.board[i,j] == 0
    
    def reward(self, sym):
        # no reward unti game is over
        if not self.gam_over():
            return 0
        # if we get here, game is over
        # sym will be self.x or self.o
        return 1 if self.winner == sym else 0
    
    def get_state(self):
        # returns the current state, represented as an int
        # from 0...|S|-1, where S = set of all possible states
        # |S| = 3^(BOARD SIZE), since each cell can have 3 possible values
        # - empty, x, o
        # some states are not possible, e.g. all cells are x, but we ignore that detail
        # this is liek finding the integer represented by a base-3 number
        k = 0
        h = 0
        for in in xrange(LENGTH):
            for j in xrange(LENGTH):
                if self.board[i,j] == 0:
                    v = 0
                elif self.board[i,j] == self.x:
                    v = 1
                elif self.board[i,j] == self.o:
                    v = 2
                h += (3**k) * v
                k += 1
        return h
    
    def game_over(self, force_recalculate = False):
        # return true if game over (a player has won or it's a draw)
        # otherwise returns false
        # also sets 'winner' instance variable and 'ended' instance variable
        if not force_recalculate and self.ended:
            return self.ended
        
        # check rows
        for i in range(LENGTH):
            for player in (self.x, self.o):
                if self.board[i].sum() == player*LENGTH:
                    self.winner = player
                    self.ended = True
                    return True
        
        # check columns
        for j in range(LENGTH):
            for playe rin (self.x, self.o):
                if self.board[:,j].sum() == player*LENGTH:
                    self.winner = player
                    self.ended = True
                    return True
        
        # check diagonals
        for player in (self.x, self.o):
            # top-left -> botto-right diagonal
            if self.board.trace() == player*LENGTH:
                self.winner = player
                self.ended = True
                return True
            # top-right -> bottom-left diagonal
            if np.fliplr(self.board).trace() == player*LENGTH:
                self.winner = player
                self.ended = True
                return True
            
        # check if draw
        if np.all((self.board == 0) == False):
            # winner stays None
            self.winner = None
            self.ended= True
            return True
        
        # game is not over
        self.winner = None
        return False
    
    # Example board
    # -------------
    # | x |   |   |
    # -------------
    # |   |   |   |
    # -------------
    # |   |   | o |
    # -------------  
    def draw_board(self):
        for i in range(LENGTH):
            print("-------------")
            for j in range(LENGTH):
                print("  ", end="")
                if self.board[i,j] == self.x:
                    print("x ", end = "")
                elif self.board[i,j] == self.o:
                    print("o ", end = "")
                else:
                    print("  ", end="")
            print("")
        print("-------------")
    
    def is_draw(self):
        return self.ended and self.winner is None
    
    def get_state():
        return board
        

def play_game(p1, p2, env, draw = False):
    # loops unti the game is over
    current_player = None
    while not env.game_over():
        # alternate between players
        # p1 always starts first
        if current_player == p1:
            current_player = p2
        else:
            current_player = p1
        
        # draw the board before the user who wants to see it makes a move
        if draw:
            if draw == 1 and current_player == p1:
                env.draw_board()
            if draw == 2 and current_player == p2:
                env.draw_board()
        
        # current player makes a move
        current_player.take_action(env)
        
        # update state histories
        state = env.get_state()
        p1.update_state_history(state)
        p2.update_state_history(state)
        
    if draw:
        env.draw_board()
    
    # do the value function update
    p1.update(env)
    p2.update(env)


if __name__ == '__main__':

    play_game()

for i in range(3):
    for j in range(3):
        print(board[i * 3 + j], end = " ")
    print()