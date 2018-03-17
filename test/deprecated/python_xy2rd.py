# Load the WCS information from a fits header, and use it
# to convert pixel coordinates to world coordinates.

from __future__ import division, print_function

import numpy as np
from astropy import wcs
from astropy.io import fits
import sys
from drizzlepac import pixtosky


def xy2rd(filename):
    # pixtosky.xy2rd(filename, 0, 0, hms=False)
    # Load the FITS hdulist using astropy.io.fits
    hdulist = fits.open(filename)

    # Parse the WCS keywords in the primary HDU
    w = wcs.WCS(hdulist[0].header)

    # Print out the "name" of the WCS, as defined in the FITS header
    # print(w.wcs.name)

    # Print out all of the settings that were parsed from the header
    # w.wcs.print_contents()

    # Three pixel coordinates of interest.
    # Note we've silently assumed a NAXIS=2 image here
    x = [0, 1, 2, 3, 4]
    y = [0, 1, 2, 3, 4]
    # Convert pixel coordinates to world coordinates
    # The second argument is "origin" -- in this case we're declaring we
    # have 1-based (Fortran-like) coordinates.
    ra, dec = w.wcs_pix2world(x, y, 1)
    # Convert the same coordinates back to pixel coordinates.
    x2, y2 = w.wcs_world2pix(ra,dec,1)
    # print(pixcrd2)

    # These should be the same as the original pixel coordinates, modulo
    # some floating-point error.
    print(x, y)
    print(x2, y2)
    assert np.max(np.abs(x - x2)) < 1e-6
    assert np.max(np.abs(y - y2)) < 1e-6


if __name__ == '__main__':
    xy2rd(sys.argv[-1])
