import dataclasses

@dataclasses.dataclass
class LogConfig:
    log_name: str
    log_dir: str
    log_level: int
    propagate: bool = False
