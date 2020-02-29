import os
import sys


PROJECT_ROOT = os.path.abspath("..")
sys.path.append(PROJECT_ROOT)

from FieldTrips.pages import app


if __name__ == "__main__":
    app.run()
