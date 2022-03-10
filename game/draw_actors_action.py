from itertools import cycle
from action import Action


class DrawActorsAction(Action):
    """
    An output action that draws all the actors.
    
    The responsibility of DrawActorsAction is to draw all the actors.

    Attributes:
        _video_service (VideoService): An instance of VideoService.
    """

    def __init__(self, video_service):
        """Constructs a new DrawActorsAction using the specified VideoService.
        
        Args:
            video_service (VideoService): An instance of VideoService.
        """
        self._video_service = video_service

    def execute(self, cast, script):
        """Executes the draw actors action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        scores = cast.get_first_actor("scores")  # change from get_first_actor to get_actor
        #score1 = scores[0]
        #score2 = scores[1]
        #score1_points = score1.add_points(0)
        #score2_points = score2.add_points(0)
                
        food = cast.get_first_actor("foods")
        cycles = cast.get_actors("cycles")
        cycle1 = cycles[0]
        cycle2 = cycles[1]
        cycle1_segments = cycle1.get_segments()
        cycle2_segments = cycle2.get_segments()
        messages = cast.get_actors("messages")

        self._video_service.clear_buffer()
        self._video_service.draw_actors(cycle1_segments)
        self._video_service.draw_actors(cycle2_segments)# Change from actor to actors
        self._video_service.draw_actor(scores)
        #self._video_service.draw_actors(score1_points)
        #self._video_service.draw_actors(score2_points)
        self._video_service.draw_actors(messages, True)
        self._video_service.flush_buffer()