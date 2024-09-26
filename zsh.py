import os
zshrc_path = os.path.join(os.path.expanduser('~'), '.zshrc')
os.chmod(zshrc_path, 0o644)