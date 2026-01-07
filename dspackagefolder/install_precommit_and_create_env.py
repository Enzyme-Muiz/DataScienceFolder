## install uv
## uv add requirements.txt
## install pre-commit
## pre-commit install
## creeate env file into the new folder


import subprocess
import sys
from pathlib import Path


def setup_project_environment(project_dir: str | Path = "."):
    project_dir = Path(project_dir).resolve()

    if not project_dir.exists():
        raise FileNotFoundError(f"{project_dir} does not exist")

    def run(cmd: list[str]):
        subprocess.check_call(cmd, cwd=project_dir)

    # 1️⃣ Install uv if missing
    try:
        subprocess.check_call([sys.executable, "-m", "uv", "--version"])
    except subprocess.CalledProcessError:
        print("Installing uv...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "uv"])

    # 2️⃣ Initialise uv project if pyproject.toml is missing
    pyproject = project_dir / "pyproject.toml"
    if not pyproject.exists():
        print("Initialising uv project...")
        run(["uv", "init"])

    # 3️⃣ Add requirements.txt using uv
    requirements = project_dir / "requirements.txt"
    if requirements.exists():
        run(["uv", "add",  "-r", "requirements.txt"])
    else:
        print("requirements.txt not found — skipping uv add")

    # 4️⃣ Install pre-commit if missing
    try:
        subprocess.check_call(["pre-commit", "--version"])
    except (subprocess.CalledProcessError, FileNotFoundError):
        print("Installing pre-commit...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pre-commit"])

    # 5️⃣ Install pre-commit hooks
    run(["git", "init"])  # Ensure git repo is initialized
    run(["pre-commit", "install"])

    # 6️⃣ Create .env file
    env_file = project_dir / ".env"
    if not env_file.exists():
        env_file.write_text("# Environment variables\n")
        print(f"Created {env_file}")
    else:
        print(".env already exists")

    print("✅ Project environment setup complete")

