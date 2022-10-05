from collections import defaultdict, namedtuple

from armagomen.battle_observer.settings.default_settings import settings
from armagomen.constants import MAIN
from armagomen.utils.common import overrideMethod, callback, cancelCallback
from gui.Scaleform.daapi.view.lobby.header.LobbyHeader import LobbyHeader
from gui.impl import backport
from gui.impl.gen import R
from helpers.time_utils import getTimeDeltaFromNow, makeLocalServerTime, ONE_DAY, ONE_HOUR, ONE_MINUTE

TEMPLATES = namedtuple("TEMPLATES", ("DAYS", "HOURS"))(
    "<font face='$TitleFont' size='16' color='#FAFAFA'>%(days)d %(timeMetric)s. %(hours)02d:%(min)02d:%(sec)02d</font>",
    "<font face='$TitleFont' size='16' color='#FAFAFA'>%(hours)02d %(timeMetric)s. %(min)02d:%(sec)02d</font>"
)


class PremiumTime(object):

    def __init__(self):
        self.callback = None
        self.macros = defaultdict(int)
        overrideMethod(LobbyHeader, "as_setPremiumParamsS")(self.startCallback)
        overrideMethod(LobbyHeader, "_removeListeners")(self._removeListeners)

    def _getPremiumLabelText(self, timeDelta):
        delta = float(getTimeDeltaFromNow(makeLocalServerTime(timeDelta)))
        self.macros["days"], delta = divmod(delta, ONE_DAY)
        self.macros["hours"], delta = divmod(delta, ONE_HOUR)
        self.macros["min"], self.macros["sec"] = divmod(delta, ONE_MINUTE)
        if timeDelta > ONE_DAY:
            timeMetric = backport.text(R.strings.menu.header.account.premium.days())
            template = TEMPLATES.DAYS
        else:
            timeMetric = backport.text(R.strings.menu.header.account.premium.hours())
            template = TEMPLATES.HOURS
        self.macros["timeMetric"] = timeMetric
        return template % self.macros

    def startCallback(self, base, header, data):
        self.stopCallback()
        if settings.main[MAIN.PREMIUM_TIME] and header.itemsCache.items.stats.isPremium:
            self.callback = callback(1.0, self.startCallback, base, header, data)
            data["doLabel"] = self._getPremiumLabelText(header.itemsCache.items.stats.activePremiumExpiryTime)
        base(header, data)

    def stopCallback(self):
        if self.callback is not None:
            cancelCallback(self.callback)
            self.callback = None

    def _removeListeners(self, base, header):
        self.stopCallback()
        return base(header)


p_time = PremiumTime()
