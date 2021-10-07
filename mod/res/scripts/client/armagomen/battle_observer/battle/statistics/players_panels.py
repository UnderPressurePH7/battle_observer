from armagomen.battle_observer.core import settings
from armagomen.battle_observer.meta.battle.stats_meta import StatsMeta
from armagomen.battle_observer.statistics.statistic_wtr import getStatisticString
from armagomen.constants import VEHICLE_TYPES, STATISTICS


class PlayersPanelsStatistic(StatsMeta):

    def py_getStatisticString(self, accountDBID, vehicleID, cut):
        if cut:
            pattern = settings.statistics[STATISTICS.PANELS_LEFT_CUT] if self._arenaDP.isAlly(vehicleID) else \
                settings.statistics[STATISTICS.PANELS_RIGHT_CUT]
        else:
            pattern = settings.statistics[STATISTICS.PANELS_LEFT] if self._arenaDP.isAlly(vehicleID) else \
                settings.statistics[STATISTICS.PANELS_RIGHT]
        vInfoVO = self._arenaDP.getVehicleInfo(vehicleID)
        result = getStatisticString(accountDBID, self.statisticsData, vInfoVO.player.clanAbbrev)
        if result is not None:
            return pattern % result
        return None

    def py_getIconColor(self, vehicleID):
        vInfoVO = self._arenaDP.getVehicleInfo(vehicleID)
        return self.vehicle_types[VEHICLE_TYPES.CLASS_COLORS].get(vInfoVO.vehicleType.classTag)

    @staticmethod
    def py_getCutWidth():
        return settings.statistics[STATISTICS.PANELS_CUT_WIDTH]

    @staticmethod
    def py_getFullWidth():
        return settings.statistics[STATISTICS.PANELS_FULL_WIDTH]