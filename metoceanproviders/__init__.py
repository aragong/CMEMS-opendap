"""Access to several Met-ocean products/providers"""

__author__ = "German Aragón Caminero"
__copyright__ = "(C) 2021 E.U. Copernicus Marine Service Information"
__credits__ = ["E.U. Copernicus Marine Service Information"]
__license__ = "MIT License - You must cite this source"
__maintainer__ = "German Aragon"
__email__ = "servicedesk dot cmems at mercator hyphen ocean dot eu"
__version__ = "0.1.0"

import os
from dotenv import load_dotenv

dotenv_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), ".env")
load_dotenv(dotenv_path)