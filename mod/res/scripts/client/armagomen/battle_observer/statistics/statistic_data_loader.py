import copy

import constants
from armagomen.utils.common import urlResponse

region = constants.AUTH_REALM.lower()
statisticEnabled = region in ["ru", "eu", "na", "asia"]
if region == "na":
    region = "com"

if statisticEnabled:
    URL = "https://api.worldoftanks.{}/wot/account/info/?".format(region)
    SEPARATOR = "%2C"
    FIELDS = SEPARATOR.join(("statistics.random.wins", "statistics.random.battles", "global_rating"))
    API_KEY = "application_id=2a7b45c57d9197bfa7fcb0e342673292&account_id="
    STAT_URL = "{url}{key}{ids}&extra=statistics.random&fields={fields}&" \
               "language=en".format(url=URL, key=API_KEY, ids="{ids}", fields=FIELDS)
    CACHE = {}
    WTR_CACHE = {}


def request(databaseIDS):
    result = urlResponse(STAT_URL.format(ids=SEPARATOR.join(str(_id) for _id in databaseIDS)))
    return result.get("data", None)


def getCachedStatisticData(databaseIDS):
    if not statisticEnabled:
        return
    notZeroIds = tuple(_id for _id in databaseIDS if _id)
    toRequest = tuple(_id for _id in notZeroIds if _id not in CACHE)
    if toRequest:
        data = request(toRequest)
        if data is not None:
            for _id, value in data.iteritems():
                CACHE[int(_id)] = copy.deepcopy(value)
    return {_id: CACHE[_id] for _id in notZeroIds if _id in CACHE}
