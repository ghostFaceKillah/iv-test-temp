import csv

snp_multiple = 50 

class TextDataFeed(object):
    def __init__(self, data_filename):
        self.dates = []
        self.signal = []
        self.currentDay = 0
        with open(data_filename, 'rb') as csvfile:
            quotes = csv.reader(csvfile, delimiter=',')
            # skip first line
            iter_quotes = iter(quotes)
            next(iter_quotes)
            for row in iter_quotes:
                self.dates.append(row[0])
                self.signal.append(float(row[1]))

    def getDataStream(self):
        for i in self.dates:
            self.currentDay += 1
            yield {'date':self.dates[self.currentDay-1],
                   'price':self.signal[self.currentDay-1],
                   'value':snp_multiple}

    

