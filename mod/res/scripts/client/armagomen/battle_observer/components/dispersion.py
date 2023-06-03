import aih_constants
from AvatarInputHandler import gun_marker_ctrl
from BattleReplay import g_replayCtrl, BattleReplay
from VehicleGunRotator import VehicleGunRotator
from armagomen.battle_observer.settings.default_settings import settings
from armagomen.constants import GLOBAL, DISPERSION
from armagomen.utils.common import overrideMethod, getPlayer
from constants import SERVER_TICK_LENGTH
from gui.Scaleform.daapi.view.battle.shared.crosshair import gm_factory
from gui.Scaleform.daapi.view.battle.shared.crosshair.container import CrosshairPanelContainer
from gui.Scaleform.genConsts.GUN_MARKER_VIEW_CONSTANTS import GUN_MARKER_VIEW_CONSTANTS as _CONSTANTS
from gui.battle_control.controllers.crosshair_proxy import CrosshairDataProxy

CLIENT = gun_marker_ctrl._MARKER_TYPE.CLIENT
SERVER = gun_marker_ctrl._MARKER_TYPE.SERVER

DEV_FACTORIES_COLLECTION = (
    gm_factory._DevControlMarkersFactory,
    gm_factory._OptionalMarkersFactory,
    gm_factory._EquipmentMarkersFactory
)
LINKAGES = {
    _CONSTANTS.DEBUG_SPG_GUN_MARKER_NAME: _CONSTANTS.GUN_MARKER_SPG_LINKAGE,
    _CONSTANTS.DEBUG_ARCADE_GUN_MARKER_NAME: _CONSTANTS.GUN_MARKER_LINKAGE,
    _CONSTANTS.DEBUG_SNIPER_GUN_MARKER_NAME: _CONSTANTS.GUN_MARKER_LINKAGE,
    _CONSTANTS.DEBUG_DUAL_GUN_ARCADE_MARKER_NAME: _CONSTANTS.DUAL_GUN_ARCADE_MARKER_LINKAGE,
    _CONSTANTS.DEBUG_DUAL_GUN_SNIPER_MARKER_NAME: _CONSTANTS.DUAL_GUN_SNIPER_MARKER_LINKAGE
}

gm_factory._GUN_MARKER_LINKAGES.update(LINKAGES)
aih_constants.GUN_MARKER_MIN_SIZE *= 0.5
aih_constants.SPG_GUN_MARKER_MIN_SIZE *= 0.5

DEFAULT_SPG_GUN_MARKER_SCALE_RATE = aih_constants.SPG_GUN_MARKER_SCALE_RATE


def setSPGMarkerScaleRate(rate, enabled):
    if enabled:
        aih_constants.SPG_GUN_MARKER_SCALE_RATE = DEFAULT_SPG_GUN_MARKER_SCALE_RATE * rate
    else:
        aih_constants.SPG_GUN_MARKER_SCALE_RATE = DEFAULT_SPG_GUN_MARKER_SCALE_RATE


class _DefaultGunMarkerController(gun_marker_ctrl._DefaultGunMarkerController):
    __scaleConfig = float(settings.dispersion_circle[DISPERSION.SCALE])

    def __updateScreenRatio(self):
        super(_DefaultGunMarkerController, self).__updateScreenRatio()
        self.__screenRatio *= self.__scaleConfig


class SPGController(gun_marker_ctrl._SPGGunMarkerController):
    __scaleConfig = float(settings.dispersion_circle[DISPERSION.SCALE])

    def _updateDispersionData(self):
        self._size *= self.__scaleConfig
        dispersionAngle = self._gunRotator.dispersionAngle * self.__scaleConfig
        isServerAim = self._gunMarkerType == SERVER
        if g_replayCtrl.isPlaying and g_replayCtrl.isClientReady:
            d, s = g_replayCtrl.getSPGGunMarkerParams()
            if d != -1 and s != -1:
                dispersionAngle = d
        elif g_replayCtrl.isRecording and (g_replayCtrl.isServerAim and isServerAim or not isServerAim):
            g_replayCtrl.setSPGGunMarkerParams(dispersionAngle, GLOBAL.ZERO)
        self._dataProvider.setupConicDispersion(dispersionAngle)


class DispersionCircle(object):
    CREATE = "createComponents"

    def __init__(self):
        self.enabled = False
        self.server = False
        self.replace = False
        settings.onModSettingsChanged += self.onModSettingsChanged
        overrideMethod(gm_factory, self.CREATE)(self.createOverrideComponents)
        overrideMethod(gm_factory, "overrideComponents")(self.createOverrideComponents)
        overrideMethod(gun_marker_ctrl, "createGunMarker")(self.createGunMarker)
        overrideMethod(gun_marker_ctrl, "useDefaultGunMarkers")(self.useDefaultGunMarkers)
        overrideMethod(gun_marker_ctrl, "useClientGunMarker")(self.useGunMarker)
        overrideMethod(gun_marker_ctrl, "useServerGunMarker")(self.useGunMarker)
        overrideMethod(VehicleGunRotator, "applySettings")(self.applySettings)
        overrideMethod(VehicleGunRotator, "setShotPosition")(self.setShotPosition)
        overrideMethod(CrosshairDataProxy, "__onServerGunMarkerStateChanged")(self.onServerGunMarkerStateChanged)
        overrideMethod(CrosshairPanelContainer, "setGunMarkerColor")(self.setGunMarkerColor)
        overrideMethod(BattleReplay, "setUseServerAim")(self.replaySetUseServerAim)

    def replaySetUseServerAim(self, base, replay, enabled):
        return base(replay, False if self.server else enabled)

    def createOverrideComponents(self, base, *args):
        if not self.server:
            return base(*args)
        player = getPlayer()
        player.enableServerAim(True)
        if base.__name__ == self.CREATE:
            return gm_factory._GunMarkersFactories(*DEV_FACTORIES_COLLECTION).create(*args)
        return gm_factory._GunMarkersFactories(*DEV_FACTORIES_COLLECTION).override(*args)

    def useDefaultGunMarkers(self, base, *args, **kwargs):
        return not self.server or base(*args, **kwargs)

    def useGunMarker(self, base, *args, **kwargs):
        return self.server or base(*args, **kwargs)

    def applySettings(self, base, *args, **kwargs):
        return None if self.server else base(*args, **kwargs)

    def setShotPosition(self, base, rotator, vehicleID, sPos, sVec, dispersionAngle, forceValueRefresh=False):
        base(rotator, vehicleID, sPos, sVec, dispersionAngle, forceValueRefresh=forceValueRefresh)
        if not self.server:
            return
        ePos, mDir, mSize, imSize, collData = \
            rotator._VehicleGunRotator__getGunMarkerPosition(sPos, sVec, rotator.getCurShotDispersionAngles())
        rotator._avatar.inputHandler.updateGunMarker2(ePos, mDir, (mSize, imSize), SERVER_TICK_LENGTH, collData)

    def onServerGunMarkerStateChanged(self, base, *args, **kwargs):
        return None if self.server else base(*args, **kwargs)

    def setGunMarkerColor(self, base, cr_panel, markerType, color):
        if self.server and markerType == CLIENT:
            base(cr_panel, SERVER, color)
        return base(cr_panel, markerType, color)

    def onModSettingsChanged(self, config, blockID):
        if blockID == DISPERSION.NAME:
            self.enabled = config[GLOBAL.ENABLED] and not g_replayCtrl.isPlaying
            if self.enabled:
                self.replace = config[DISPERSION.REPLACE]
                self.server = config[DISPERSION.SERVER]
            else:
                self.replace = False
                self.server = False
            setSPGMarkerScaleRate(config[DISPERSION.SCALE], self.server or self.replace)

    def createGunMarker(self, baseCreateGunMarker, isStrategic):
        if not self.enabled:
            return baseCreateGunMarker(isStrategic)
        factory = gun_marker_ctrl._GunMarkersDPFactory()
        if isStrategic:
            if self.replace:
                client = SPGController(CLIENT, factory.getClientSPGProvider())
            else:
                client = gun_marker_ctrl._SPGGunMarkerController(CLIENT, factory.getClientSPGProvider())
            server = SPGController(SERVER, factory.getServerSPGProvider())
        else:
            if self.replace:
                client = _DefaultGunMarkerController(CLIENT, factory.getClientProvider())
            else:
                client = gun_marker_ctrl._DefaultGunMarkerController(CLIENT, factory.getClientProvider())
            server = _DefaultGunMarkerController(SERVER, factory.getServerProvider())
        return gun_marker_ctrl._GunMarkersDecorator(client, server)


dispersion_circle = DispersionCircle()
