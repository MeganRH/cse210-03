import constants
from actor import Actor

class Score(Actor):
    
    def __init__(self): #add another parameter "color"
        super().__init__()
        
        self._pointsP1 = 0
        self._pointsP2 = 0
        
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._pointsP1 += points
        self._pointsP2 += points
        
        self.set_text(f"   -- Red Player -- : {self._pointsP1}                                                                                               -- Bue Player -- : {self._pointsP2} ")
        '''
        else:
            self._points += points
            self.set_text(f"Player 2: {self._points}")
        '''
