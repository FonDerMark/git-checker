import os
from pathlib import Path
import subprocess

BASE_DIR = Path(__file__).resolve().parent.parent.parent
current_folder_path = os.path.dirname(os.path.abspath(__file__))
SCRIPT_PATH = os.path.join(current_folder_path, 'git_checker.py')
FILE_PATH = os.path.join(current_folder_path, 'commit_info.json')
HOOKS_FOLDER = os.path.join(BASE_DIR, ".git", "hooks")


def set_hooks_path():
    subprocess.run(["git", "config", "core.hooksPath", HOOKS_FOLDER])


def create_prepare_commit_msg_hook():
    hook_script = f"""#!/bin/sh
# .git/hooks/prepare-commit-msg

COMMIT_MSG_FILE=$1
COMMIT_MSG=$(cat "$COMMIT_MSG_FILE")

python3 "{SCRIPT_PATH}" "$COMMIT_MSG"
"""
    hook_path = os.path.join(HOOKS_FOLDER, "prepare-commit-msg")
    os.makedirs(os.path.dirname(hook_path), exist_ok=True)
    with open(hook_path, "w") as f:
        f.write(hook_script)

    os.chmod(hook_path, 0o755)


def create_post_commit_hook():
    hook_script = f"""#!/bin/sh
# .git/hooks/post-commit

SAVED_COMMIT_MSG="{FILE_PATH}"

git add "$SAVED_COMMIT_MSG"

git commit --amend --no-edit
"""
    hook_path = os.path.join(HOOKS_FOLDER, "post-commit")
    os.makedirs(os.path.dirname(hook_path), exist_ok=True)
    with open(hook_path, "w") as f:
        f.write(hook_script)
    os.chmod(hook_path, 0o755)


set_hooks_path()
create_prepare_commit_msg_hook()
create_post_commit_hook()
