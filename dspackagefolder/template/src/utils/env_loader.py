from pathlib import Path
from dotenv import load_dotenv


def load_env_from_root(env_subpath: str = "ENVIRONMENT/.env") -> Path:
    """
    Search upward from this file to find ENVIRONMENT/.env and load it.

    Returns the path of the loaded env file.
    """

    current = Path(__file__).resolve()

    for parent in [current] + list(current.parents):
        env_path = parent / env_subpath
        if env_path.exists():
            load_dotenv(env_path)
            return env_path

    raise FileNotFoundError(f"{env_subpath} not found in any parent directory")
