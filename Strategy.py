class SNPStrategy(object):
    def __init__(self, params):
        self.memory = []
        # self.date = []
        self.price = []
        self.signal_window = params['signal_window']
        self.max_position = params['max_position']
        self.wait_period = params['wait_period']
        self.day_counter = 0
        self.current_pos = 0

    def computeSignal(self, day):
        # save data
        # self.dates.append(day['date']) 
        # ambiguous task statement :( 40 trading or real world days?
        self.price.append(day['price'])
        self.day_counter += 1
        if self.day_counter <= self.wait_period:
            return 0
        else:
            if self.price >  max(self.price[-41:-1]):
                self.current_pos = self.max_position
            elif self.price <  min(self.price[-41:-1]):
                self.current_pos = -self.max_position
            return self.current_pos
