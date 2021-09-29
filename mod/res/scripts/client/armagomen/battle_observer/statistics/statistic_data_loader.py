import copy

import constants
from armagomen.utils.common import urlResponse

region = constants.AUTH_REALM.lower()
statisticEnabled = region in ["ru", "eu", "na", "asia"]
if region == "na":
    region = "com"

if statisticEnabled:
    URL = "https://api.worldoftanks.{}/wot/account/info/?".format(region)
    API_KEY = "application_id=2a7b45c57d9197bfa7fcb0e342673292&account_id="
    STAT_URL = "{url}{key}{ids}&extra=statistics.random&fields=statistics.random&" \
               "language=en".format(url=URL, key=API_KEY, ids="{ids}")
    WTR = "{url}{key}{ids}&fields=global_rating&language=en".format(url=URL, key=API_KEY, ids="{ids}")
    SEPARATOR = "%2C"
    CACHE = {}
    WTR_CACHE = {}


def normalizeIDS(databaseIDS):
    return (str(databaseID) for databaseID in databaseIDS if databaseID)


def getCachedStatisticData(databaseIDS, update=True):
    if not statisticEnabled:
        return
    databaseIDS = [databaseID for databaseID in databaseIDS if databaseID not in CACHE]
    if not update or not databaseIDS:
        return CACHE
    result = urlResponse(STAT_URL.format(ids=SEPARATOR.join(normalizeIDS(databaseIDS))))
    if not result:
        return CACHE
    data = result.get("data")
    if data:
        for databaseID, value in data.iteritems():
            CACHE[int(databaseID)] = copy.deepcopy(value["statistics"]["random"])
    return CACHE


def getStatisticData(databaseIDS):
    if not statisticEnabled:
        return
    result = urlResponse(STAT_URL.format(ids=SEPARATOR.join(normalizeIDS(databaseIDS))))
    if not result:
        return {}
    data = result.get("data")
    if data:
        return {int(databaseID): value["statistics"]["random"] for databaseID, value in data.iteritems()}


def getCachedWTR(databaseIDS, update=True):
    if not statisticEnabled:
        return
    databaseIDS = [databaseID for databaseID in databaseIDS if databaseID not in CACHE]
    if not update or not databaseIDS:
        return WTR_CACHE
    result = urlResponse(WTR.format(ids=SEPARATOR.join(normalizeIDS(databaseIDS))))
    if not result:
        return WTR_CACHE
    data = result.get("data")
    if data:
        for databaseID, value in data.iteritems():
            WTR_CACHE[int(databaseID)] = int(value["global_rating"])
    return WTR_CACHE


def getWTRRating(databaseIDS):
    if not statisticEnabled:
        return
    result = urlResponse(WTR.format(ids=SEPARATOR.join(normalizeIDS(databaseIDS))))
    data = result.get("data")
    if data:
        return {int(databaseID): int(value[u"global_rating"]) for databaseID, value in data.iteritems()}