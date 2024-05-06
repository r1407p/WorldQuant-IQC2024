import  configs.setting as setting
from configs import select_settings
from typing import get_args
class Setting:
    @staticmethod
    def get_setting(region: setting.LanguageType, 
                    universe: setting.UniverseType,
                    delay: setting.DelayType,
                    neutralization: setting.NeutralizationType, 
                    decay: int,
                    truncation: setting.TruncationType,
                    pasteurization: setting.PasteUrizationType,
                    nan: setting.NanHandlingType):
        return {
            "language":"FASTEXPR",
            "instrumentType":"EQUITY",
            "region":region,
            "nanHandling":nan,
            "delay":delay,
            "universe":universe,
            "truncation":truncation,
            "unitHandling":"VERIFY",
            "pasteurization":pasteurization,
            "decay":decay,
            "neutralization":neutralization,
            "visualization":False
        }
        
    @staticmethod
    def get_settings():
        res = []
        # [("USA", "TOP3000"), ("CHN", "TOP3000"), ("CHN", "TOP2000"), ("USA", "TOP1000"), ("USA", "TOP500"), ("USA", "TOP200")]:
        for (region, universe) in select_settings.SELECT_REGION_UNIVERSE:
            for delay in select_settings.SELECT_DELAY:
                for neutralization in select_settings.SELECT_NEUTRALIZATION:
                    for decay in select_settings.SELECT_DECAY:
                        for truncation in select_settings.SELECT_TRUNCATION:
                            for pasteurization in ["ON"]:
                                for nan in ["OFF"]:
                                    res.append(Setting.get_setting(region, universe, delay, neutralization, decay, truncation, pasteurization, nan))
        return res
                                        
                                        
                                        
