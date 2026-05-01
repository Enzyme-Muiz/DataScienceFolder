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

    try:
        if not project_dir.exists():
            raise FileNotFoundError(f"{project_dir} does not exist")
    except Exception as e:
        print(f"❌ Invalid project directory: {e}")
        return

    def run(cmd: list[str]):
        try:
            subprocess.check_call(cmd, cwd=project_dir)
        except subprocess.CalledProcessError as e:
            print(f"❌ Command failed: {' '.join(cmd)}\n{e}")
        except FileNotFoundError as e:
            print(f"❌ Command not found: {cmd[0]}\n{e}")
        except Exception as e:
            print(f"❌ Unexpected error running {' '.join(cmd)}: {e}")

    # 1️⃣ Install uv if missing
    try:
        subprocess.check_call([sys.executable, "-m", "uv", "--version"])
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            print("Installing uv...")
            subprocess.check_call([sys.executable, "-m", "pip", "install", "uv"])
        except Exception as e:
            print(f"❌ Failed to install uv: {e}")

    # 2️⃣ Initialise uv project if pyproject.toml is missing
    try:
        pyproject = project_dir / "pyproject.toml"
        if not pyproject.exists():
            print("Initialising uv project...")
            run(["uv", "init"])
    except Exception as e:
        print(f"❌ Error during uv init: {e}")

    # 3️⃣ Add requirements.txt using uv
    try:
        requirements = project_dir / "requirements.txt"
        if requirements.exists():
            run(["uv", "add", "-r", "requirements.txt"])
        else:
            print("requirements.txt not found — skipping uv add")
    except Exception as e:
        print(f"❌ Error adding requirements: {e}")

    # 4️⃣ Install pre-commit if missing
    try:
        subprocess.check_call(["pre-commit", "--version"])
    except (subprocess.CalledProcessError, FileNotFoundError):
        try:
            print("Installing pre-commit...")
            subprocess.check_call(
                [sys.executable, "-m", "pip", "install", "pre-commit"]
            )
        except Exception as e:
            print(f"❌ Failed to install pre-commit: {e}")

    # 5️⃣ Install pre-commit hooks
    try:
        run(["git", "init"])
        run(["pre-commit", "install"])
    except Exception as e:
        print(f"❌ Error setting up pre-commit hooks: {e}")

    # 6️⃣ Create ENVIRONMENT folder and .env file
    try:
        env_folder = project_dir / "ENVIRONMENT"
        env_folder.mkdir(parents=True, exist_ok=True)

        env_file = env_folder / ".env"
        if not env_file.exists():
            env_file.write_text("# Environment variables\n", encoding="utf-8")
            print(f"Created {env_file}")
        else:
            print(f"{env_file} already exists")

        gitignore_file = env_folder / ".gitignore"
        if not gitignore_file.exists():
            gitignore_file.write_text("*/\n", encoding="utf-8")
            print(f"Created {gitignore_file}")
        else:
            print(f"{gitignore_file} already exists")

    except Exception as e:
        print(f"❌ Error creating environment files: {e}")

    # 7️⃣ Create GitHub Actions workflow
    try:
        github_workflows = project_dir / ".github" / "workflows"
        github_workflows.mkdir(parents=True, exist_ok=True)

        precommit_workflow = github_workflows / "pre-commit.yml"

        if not precommit_workflow.exists():
            precommit_workflow.write_text(
                """name: Pre-commit

on:
  push:
  pull_request:

jobs:
  pre-commit:
    runs-on: ubuntu-latest

    steps:
      - name: Checkout code
        uses: actions/checkout@v4

      - name: Set up Python
        uses: actions/setup-python@v5
        with:
          python-version: "3.11"

      - name: Install dependencies
        run: |
          pip install pre-commit

      - name: Run pre-commit
        run: |
          pre-commit run --all-files
""",
                encoding="utf-8",
            )
            print(f"Created GitHub Actions workflow at {precommit_workflow}")
        else:
            print(f"{precommit_workflow} already exists")

    except Exception as e:
        print(f"❌ Error creating GitHub workflow: {e}")

    # 7️⃣ Create GitHub Actions workflow
    try:
        precommit_workflow = project_dir / ".pre-commit-config.yaml"

        if not precommit_workflow.exists():
            precommit_workflow.write_text(
                """repos:
 - repo: https://github.com/kynan/nbstripout
   rev: 0.6.1
   hooks:
     - id: nbstripout
 - repo: https://github.com/Yelp/detect-secrets
   rev: v1.5.0
   hooks:
     - id: detect-secrets
 - repo: https://github.com/psf/black
   rev: 24.4.2
   hooks:
     - id: black
""",
                encoding="utf-8",
            )
            print(f"Created pre-commit configuration at {precommit_workflow}")
        else:
            print(f"{precommit_workflow} already exists")

    except Exception as e:
        print(f"❌ Error creating pre-commit configuration: {e}")

    print("✅ Project environment setup complete")
