from armagomen.battle_observer.core.bo_constants import GLOBAL
from armagomen.battle_observer.meta.lobby.base_mod_meta import BaseModMeta


class DateTimesMeta(BaseModMeta):

    def __init__(self):
        super(DateTimesMeta, self).__init__()

    def as_setDateTimeS(self, text=GLOBAL.EMPTY_LINE):
        return self.flashObject.as_setDateTime(text) if self._isDAAPIInited() else None

    def as_setPremiumLeftS(self, timeLeft=GLOBAL.EMPTY_LINE):
        return self.flashObject.as_setPremiumLeft(timeLeft) if self._isDAAPIInited() else None