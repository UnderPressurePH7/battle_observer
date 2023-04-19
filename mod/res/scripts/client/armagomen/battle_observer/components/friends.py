from PlayerEvents import g_playerEvents
from armagomen.battle_observer.core import viewSettings
from armagomen.battle_observer.settings.default_settings import settings
from armagomen.constants import MAIN, ANOTHER, GLOBAL
from armagomen.utils.common import overrideMethod, isReplay
from gui.battle_control.arena_info.arena_vos import VehicleTypeInfoVO
from messenger.gui.Scaleform.data.contacts_data_provider import _ContactsCategories
from messenger.storage import storage_getter

_cache = set()


def onGuiCacheSyncCompleted(ctx):
    _cache.clear()
    users = storage_getter(ANOTHER.USERS)().getList(_ContactsCategories().getCriteria())
    _cache.update(user._userID for user in users if not user.isIgnored())
    _cache.add(ctx.get(ANOTHER.DBID, GLOBAL.ZERO))


g_playerEvents.onGuiCacheSyncCompleted += onGuiCacheSyncCompleted


@overrideMethod(VehicleTypeInfoVO)
def new_VehicleArenaInfoVO(init, vTypeVo, *args, **kwargs):
    init(vTypeVo, *args, **kwargs)
    if not isReplay() and not viewSettings.gui.isInEpicRange() and settings.main[MAIN.SHOW_FRIENDS]:
        vTypeVo.isPremiumIGR |= kwargs.get(ANOTHER.ACCOUNT_DBID) in _cache


@overrideMethod(VehicleTypeInfoVO, "update")
def new_VehicleTypeInfoVO_update(update, vTypeVo, *args, **kwargs):
    if not isReplay() and not viewSettings.gui.isInEpicRange() and settings.main[MAIN.SHOW_FRIENDS]:
        result = update(vTypeVo, *args, **kwargs)
        if hasattr(vTypeVo, "isPremiumIGR"):
            vTypeVo.isPremiumIGR |= kwargs.get(ANOTHER.ACCOUNT_DBID) in _cache
        return result
    return update(vTypeVo, *args, **kwargs)
