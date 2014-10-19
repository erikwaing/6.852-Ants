class board:
    
    def __init__(location, ants):
        self.treasure = location
        self.ants = ants

    def act():
        for ant in self.ants:
            ant.act()

    def check():
        for ant in self.ants:
            if ant.getLocation() == self.treasure:
                return True
        return False

    def runAnts():
        steps = 0
        while not self.check():
            self.act()
            steps += 1
        return steps
