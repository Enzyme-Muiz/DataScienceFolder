from pathlib import Path
import tomllib   # Python 3.11+
# use: import tomli as tomllib   # if Python <= 3.10


def load_config(config_name: str = ".config/example.toml") -> dict:
    """
    Load config.toml from project root regardless of where this is imported from.
    """

    current = Path(__file__).resolve()

    for parent in [current] + list(current.parents):
        candidate = parent / config_name
        if candidate.exists():
            with open(candidate, "rb") as f:
                return tomllib.load(f)

    raise FileNotFoundError(f"{config_name} not found in any parent directory")
