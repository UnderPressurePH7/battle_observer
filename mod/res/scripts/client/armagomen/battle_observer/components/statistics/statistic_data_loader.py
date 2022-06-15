import copy
import random

import constants
from armagomen.battle_observer.core import settings
from armagomen.constants import MAIN
from armagomen.utils.common import urlResponse, logDebug, logInfo, logError
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider

region = constants.AUTH_REALM.lower()
if region == "na":
    region = "com"


def getArenaDP():
    sessionProvider = dependency.instance(IBattleSessionProvider)
    if sessionProvider is not None:
        arenaDP = sessionProvider.getArenaDP()
        if arenaDP is not None:
            return arenaDP
        logError("StatisticsDataLoader getArenaDP: arenaDP is {}".format(arenaDP))
    logError("StatisticsDataLoader getArenaDP: sessionProvider is {}".format(sessionProvider))


class StatisticsDataLoader(object):
    URL = "https://api.worldoftanks.{}/wot/account/info/?".format(region)
    SEPARATOR = "%2C"
    FIELDS = SEPARATOR.join(("statistics.random.wins", "statistics.random.battles", "global_rating", "nickname"))
    API_KEY = ("ffa0979342d69fe92970571918cc59b6", "76b3c385f1485e1fee1642c1e287c0ce")
    STAT_URL = "{url}application_id={key}&account_id={ids}&extra=statistics.random&fields={fields}&language=en".format(
        url=URL, key=random.choice(API_KEY), ids="{ids}", fields=FIELDS)

    def __init__(self):
        self.cache = {}
        self.enabled = region in ["ru", "eu", "com", "asia"] and not settings.xvmInstalled
        if settings.xvmInstalled:
            logInfo("StatisticsDataLoader: statistics/icons/minimap module is disabled, XVM is installed")

    def request(self, databaseIDS):
        result = urlResponse(self.STAT_URL.format(ids=self.SEPARATOR.join(str(_id) for _id in databaseIDS)))
        if result is not None:
            result = result.get("data")
        if settings.main[MAIN.DEBUG]:
            logDebug("StatisticsDataLoader: request result: data={}".format(result))
        return result

    def setCachedStatisticData(self):
        arenaDP = getArenaDP()
        if arenaDP is None or not self.enabled:
            return
        toRequest = []
        for vInfo in arenaDP.getVehiclesInfoIterator():
            if vInfo.player.accountDBID and vInfo.player.accountDBID not in self.cache:
                toRequest.append(vInfo.player.accountDBID)
        if toRequest:
            if settings.main[MAIN.DEBUG]:
                logDebug("StatisticsDataLoader: START request data: ids={}, len={} ".format(toRequest, len(toRequest)))
            data = self.request(toRequest)
            if data is not None:
                for _id, value in data.iteritems():
                    self.cache[int(_id)] = copy.deepcopy(value)
            if settings.main[MAIN.DEBUG]:
                logDebug("StatisticsDataLoader: FINISH request data")

    def getStatisticForUser(self, databaseID):
        return self.cache.get(databaseID)

    def clear(self):
        self.cache.clear()


statisticLoader = StatisticsDataLoader()
