from pathlib import Path
import shutil
import importlib.resources as resources
import sys
from dspackagefolder.install_precommit_and_create_env import setup_project_environment

def create_ds_folder(folder_name: str = "dsframework"):
    # 1️⃣ Create destination folder
    # 2️⃣ Locate the template folder INSIDE the package
    with resources.path("dspackagefolder", "template") as template_path:
        target = Path(folder_name)

        if target.exists():
            print(f"Folder already exists: {target}")
            return

        # 3️⃣ Copy template into destination
        shutil.copytree(template_path, target)

    print(f"Project created at: {target.resolve()}")
    # 4️⃣ Setup project environment
    setup_project_environment(target)
    print("🎉 Setup complete! Happy coding!")



def create_ds_folder_cli():
    # 1️⃣ Create destination folder
    # dest_root = Path("dspackagefolder")
    # dest_root.mkdir(exist_ok=True)
    project_name = sys.argv[1] if len(sys.argv) > 1 else "data_science_project"
    # 2️⃣ Locate the template folder INSIDE the package
    with resources.path("dspackagefolder", "template") as template_path:
        target = Path(project_name)

        if target.exists():
            print(f"Folder already exists: {target}")
            return

        # 3️⃣ Copy template into destination
        shutil.copytree(template_path, target)

    print(f"Project created at: {target.resolve()}")
    # 4️⃣ Setup project environment
    setup_project_environment(project_name)
    print("🎉 Setup complete! Happy coding!")
