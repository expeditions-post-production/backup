import os
import sys


PROJECT_ROOT = os.path.abspath("..")
sys.path.append(PROJECT_ROOT)

from api.pages import app


if __name__ == "__main__":
    app.run()
