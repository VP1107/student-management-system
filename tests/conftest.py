import os
import sys

# Make the project root importable so tests can `import schema`, `import model`, etc.
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
if ROOT_DIR not in sys.path:
    sys.path.insert(0, ROOT_DIR)

# database.py reads DATABASE_URL at import time; give it a harmless default
# so importing it (directly or via main.py) doesn't fail in CI.
os.environ.setdefault("DATABASE_URL", "sqlite:///:memory:")
