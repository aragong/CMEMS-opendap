"""Access to several Met-ocean products/providers"""

__author__ = "German Aragón Caminero"
__copyright__ = "(C) German Aragón Caminero"
__credits__ = ["German Aragón Caminero"]
__license__ = "GNU General Public License, Version 3"
__maintainer__ = "German Aragon"
__email__ = "german dot aragon at ihcantabria dot com"
__version__ = "0.2.0"


from .cmems import CmemsOpendap
from .noaa import NoaaOpendap
