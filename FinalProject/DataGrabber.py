from nba_api.stats.static import teams
from nba_api.stats.static import players
# FOR SURE USING ^
from nba_api.stats.endpoints import commonplayerinfo
from nba_api.stats.endpoints import teaminfocommon

# Handles processing data from NBA API
class DataGrabber:
    @staticmethod
    def convert(value):
        types = [int,float,str] # order needs to be this way
        if value == '':
            return None
        for t in types:
            try:
                return t(value)
            except:
                pass