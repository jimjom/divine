from TradeQuerier import TradeQuerier

class DealFinder:

    def __init__(self, discordClient):
        self.discordClient = discordClient

    def findDeals(self):

        querier = TradeQuerier()
        file = open("queries.txt", "r")   

        for line in file:
            print(querier.queryTrade(line))

        return (0,1)