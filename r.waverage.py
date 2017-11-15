#!/usr/bin/env python

########################################################################

#

# MODULE:       r.waverage

# AUTHOR:       Yang Lei

# PURPOSE:      To form a weighted average using raster algebra

# COPYRIGHT:    (C) 2017 Yang Lei

#               This program is free software under the GNU General

#               Public License (>=v2). Read the file COPYING that

#               comes with GRASS for details.

#

########################################################################

#%module

#% description: Form a weighted average of two rasters (5*a + 3*b)/8.0

#% keyword: raster

#% keyword: algebra

#% keyword: weighted average

#%end

#%option G_OPT_R_INPUT

#% key: araster

#% description: Name of input raster a in an expression (5*a + 3*b)/8.0

#%end

#%option G_OPT_R_INPUT

#% key: braster

#% description: Name of input raster b in an expression (5*a + 3*b)/8.0

#%end

#%option G_OPT_R_OUTPUT

#%end



import sys



import grass.script as gscript



def main():

    options, flags = gscript.parser()

    araster = options['araster']

    braster = options['braster']

    output = options['output']



    gscript.mapcalc('{r} = 5*{a}/0.8 + 3*{b}/0.8'.format(r=output, a=araster, b=braster))



    return 0



if __name__ == "__main__":

    sys.exit(main())
