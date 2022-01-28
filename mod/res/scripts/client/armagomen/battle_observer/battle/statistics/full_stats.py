from armagomen.battle_observer.meta.battle.stats_meta import StatsMeta, STATISTICS
from gui.Scaleform.genConsts.BATTLE_VIEW_ALIASES import BATTLE_VIEW_ALIASES


class FullStats(StatsMeta):

    def getPattern(self, isEnemy):
        return self.settings[STATISTICS.TAB_RIGHT] if isEnemy else self.settings[STATISTICS.TAB_LEFT], None

    def _updateVehicleData(self, isEnemy, vehicleID):
        if self.as_isComponentVisibleS(BATTLE_VIEW_ALIASES.FULL_STATS):
            super(FullStats, self)._updateVehicleData(isEnemy, vehicleID)

    def onExitBattlePage(self):
        pass

    def onEnterBattlePage(self):
        pass
