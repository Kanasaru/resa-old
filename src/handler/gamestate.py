class GameStateHandler(object):
    def __init__(self):
        self.start_game = False
        self.load_game = False
        self.leave_game = False
        self.options = False
        self.start_editor = False
        self.leave_game = False
        self.exit_game = False
        self.map_load = False
        self.pause_game = False
        self.building = False
        self.building_size = (3, 3)
        self.place = False
        self.place_on = None
