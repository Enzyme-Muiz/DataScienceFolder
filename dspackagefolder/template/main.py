

##### This is a template for making src available in any folder.
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.utils.logging_config import setup_logger
from src.utils.config_loader import load_config

###### Set up logger
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.utils.logging_config import setup_logger

logger = setup_logger(__name__, base_filename="pipeline")

logger.info("Started run")
logger.error("Failure occurred")

#logging = setup_logging()


### Load config
import sys
from pathlib import Path

sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.utils.config_loader import load_config
config = load_config()
print(config)



### Load env variables
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parents[1]))
from src.utils.env_loader import load_env_from_root
env_path = load_env_from_root()
print(f"Loaded env variables from: {env_path}")