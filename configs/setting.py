from typing import Literal, get_args
LanguageType = Literal["FASTEXPR"]
InstrumentType = Literal["EQUITY"]
RegionType = Literal["USA", "CHN"]
UniverseType = Literal["TOP3000", "TOP2000", "TOP1000", "TOP500", "TOP200"]
DelayType = Literal[0, 1]
NeutralizationType = Literal["NONE", "MARKET", "INDUSTRY", "SECTOR", "SUBINDUSTRY"]
DecayType = int
TruncationType = float
PasteUrizationType = Literal["ON", "OFF"]
UnitHandlingType = Literal["Verify"]
NanHandlingType = Literal["ON", "OFF"]