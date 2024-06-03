import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent.parent

'''
Можно захардкодить тут хуки с которыми эксперимент был.
'''

HOOKS = [
    "prepare-commit-msg",
    "pre-commit",
    "post-commit"
]


def uninstall_hooks():
    for hook in HOOKS:
        hook_path = os.path.join(BASE_DIR, ".git", "hooks", hook)
        if os.path.exists(hook_path):
            os.remove(hook_path)
            print(f"{hook} удален.")
        else:
            print(f"{hook} не найден.")
    print("Хуки удалены")


if __name__ == "__main__":
    uninstall_hooks()
