import  configs.setting as setting
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
        
    def get_settings():
        res = []
        for (region, universe) in [("USA", "TOP3000"), ("CHN", "TOP3000"), ("CHN", "TOP2000"), ("USA", "TOP1000"), ("USA", "TOP500"), ("USA", "TOP200")]:
            for delay in [1]:
                for neutralization in get_args(setting.NeutralizationType):
                    for decay in [0, 1, 3, 5, 7, 10, 14]:
                        for truncation in [0, 0.05, 0.1, 0.5, 1]:
                            for pasteurization in ["On"]:
                                for nan in ["Off"]:
                                    res.append(Setting.get_setting(region, universe, delay, neutralization, decay, truncation, pasteurization, nan))
        return res
                                        
                                        
                                        
