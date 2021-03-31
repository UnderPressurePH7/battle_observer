from PlayerEvents import g_playerEvents
from armagomen.battle_observer.core import settings
from armagomen.battle_observer.core.bo_constants import ALIAS_TO_CONFIG_NAME, MAIN
from armagomen.utils.common import logInfo, getPlayer
from gui.Scaleform.framework.entities.BaseDAAPIComponent import BaseDAAPIComponent
from helpers import dependency
from skeletons.gui.battle_session import IBattleSessionProvider
from gui.shared.personality import ServicesLocator


class BaseModMeta(BaseDAAPIComponent):
    sessionProvider = dependency.descriptor(IBattleSessionProvider)
    settingsCore = ServicesLocator.settingsCore
    settings = settings

    def __init__(self):
        super(BaseModMeta, self).__init__()
        self._isReplay = self.sessionProvider.isReplayPlaying
        self._arenaDP = self.sessionProvider.getArenaDP()
        self._arenaVisitor = self.sessionProvider.arenaVisitor
        self._player = getPlayer()

    @staticmethod
    def getShadowSettings():
        return settings.shadow_settings

    @staticmethod
    def getConfig():
        return settings

    def onDragFinished(self, x, y):
        config_name = ALIAS_TO_CONFIG_NAME[self.getAlias()]
        data = getattr(settings, config_name, None)
        data["x"] = x
        data["y"] = y

    def _populate(self):
        super(BaseModMeta, self)._populate()
        g_playerEvents.onAvatarReady += self.onEnterBattlePage
        g_playerEvents.onAvatarBecomeNonPlayer += self.onExitBattlePage
        if self._isDAAPIInited():
            self.flashObject.setCompVisible(False)
            self._name = self.getAlias()
            if settings.main[MAIN.DEBUG]:
                logInfo("battle module '%s' loaded" % self.getAlias())

    def _dispose(self):
        g_playerEvents.onAvatarReady -= self.onEnterBattlePage
        g_playerEvents.onAvatarBecomeNonPlayer -= self.onExitBattlePage
        super(BaseModMeta, self)._dispose()
        if settings.main[MAIN.DEBUG]:
            logInfo("battle module '%s' destroyed" % self.getAlias())

    def onEnterBattlePage(self):
        self._player = getPlayer()
        if self._isDAAPIInited():
            self.flashObject.setCompVisible(True)

    def onExitBattlePage(self):
        if self._isDAAPIInited():
            self.flashObject.setCompVisible(False)

    def as_startUpdateS(self, *args):
        return self.flashObject.as_startUpdate(*args) if self._isDAAPIInited() else None

    def as_colorBlindS(self, enabled):
        return self.flashObject.as_colorBlind(enabled) if self._isDAAPIInited() else None

    def as_onControlModeChangedS(self, mode):
        return self.flashObject.as_onControlModeChanged(mode) if self._isDAAPIInited() else None
