import logging
from pathlib import Path
from datetime import datetime


def setup_logger(
    name: str = "app_logger",
    log_dir: str = "logs",
    base_filename: str = "app",
    level: int = logging.INFO,
) -> logging.Logger:
    """
    Configure logger with timestamped log filename and datetime in messages.
    """

    logger = logging.getLogger(name)
    logger.setLevel(level)

    # Prevent duplicate handlers if called multiple times
    if logger.handlers:
        return logger

    # ---- create timestamped filename ----
    timestamp = datetime.now().strftime("%Y-%m-%d_%H-%M-%S")
    project_root = Path(__file__).resolve().parents[2]
    log_path = project_root / "logs"
    print(f"Log file will be saved to: {log_path / f'{base_filename}_{timestamp}.log'}")
    log_path.mkdir(parents=True, exist_ok=True)

    log_file = log_path / f"{base_filename}_{timestamp}.log"

    # ---- formatter with datetime ----
    formatter = logging.Formatter(
        fmt="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
        datefmt="%Y-%m-%d %H:%M:%S",
    )

    # ---- console handler ----
    ch = logging.StreamHandler()
    ch.setFormatter(formatter)
    logger.addHandler(ch)

    # ---- file handler ----
    fh = logging.FileHandler(log_file)
    fh.setFormatter(formatter)
    logger.addHandler(fh)

    return logger
