# Licensed under a 3-clause BSD style license - see LICENSE.rst

"""These are default parameters for some of the plotting functions in Imexam
Maybe it would be better to put these along with the imexam functions into
their own class which the connect class can import? Users could edit this file
to set their own defaults before installation, they could script something that
resets the dictionaries themselves, or we could create a method to let them set
from a json or text file maybe
"""

# aperture photometry parameters
aperphot_pars = {"function": ["aperphot", ],
                 "center": [True, "Center the object location using a 2d gaussian fit"],
                 "width": [5, "Width of sky annulus in pixels"],
                 "subsky": [True, "Subtract a sky background?"],
                 "skyrad": [15, "Distance to start sky annulus is pixels"],
                 "radius": [5, "Radius of aperture for star flux"],
                 "zmag": [25., "zeropoint for the magnitude calculation"],
                 }


# box statistics
report_stat_pars = {"function": ["report_stat", ],
                    "stat": ["median", "which numpy stat to return [median,min,max...must map to a numpy func]"],
                    "region_size": [5, "region size in pixels to use"],
                    }

# radial profile plots
radial_profile_pars = {"function": ["radial_profile", ],
                        "title": ["Radial Profile", "Title of the plot"],
                        "xlabel": ["Radius", "The string for the xaxis label"],
                        "ylabel": ["Summed Pixel Value", "The string for the yaxis label"],
                        "fitplot": [False,"Overplot profile fit?"],
                        "fittype":["Gaussian2D","Profile type to fit (Gaussian2D)"],
                        "center": [True, "Solve for center using 2d Gaussian? [bool]"],
                        "background": [True, "Subtract background? [bool]"],
                        "skyrad": [10., "Background inner radius in pixels, from center of object"],
                        "width": [5., "Background annulus width in pixels"],
                        "magzero": [25., "magnitude zero point"],
                        "rplot": [8., "Plotting radius in pixels"],
                        "pointmode": [True, "plot points instead of lines? [bool]"],
                        "marker": ["o", "The marker character to use, matplotlib style"],
                        "minflux": [0., "only measure flux above this value"],
                        "getdata": [True, "return the plotted data values"]
                        }

# curve of growth
curve_of_growth_pars = {"function": ["curve_of_growth", ],
                        "title": ["Curve of growth", "Title of the plot"],
                        "xlabel": ["radius", "The string for the xaxis label"],
                        "ylabel": ["Flux", "The string for the yaxis label"],
                        "center": [True, "Solve for center using 2d Gaussian? [bool]"],
                        "background": [True, "Fit and subtract background? [bool]"],
                        "buffer": [25., "Background inner radius in pixels,from center of star"],
                        "width": [5., "Background annulus width in pixels"],
                        "magzero": [25., "magnitude zero point"],
                        "rplot": [8., "Plotting radius in pixels"],
                        "pointmode": [True, "plot points instead of lines? [bool]"],
                        "marker": ["o", "The marker character to use, matplotlib style"],
                        "logx": [False, "log scale x-axis?"],
                        "logy": [False, "log scale y-axis?"],
                        "minflux": [0., "only measure flux above this value"],
                        "getdata": [True, "return the plotted data values"]
                        }

# surface plots
surface_pars = {"function": ["surface", ],
                "title": [None, "Title of the plot"],
                "xlabel": ["X", "The string for the xaxis label"],
                "ylabel": ["Y", "The string for the yaxis label"],
                "zlabel": [None, "Label for zaxis"],
                "ncolumns": [21, "Number of columns"],
                "nlines": [21, "Number of lines"],
                "azim": [None, "azimuthal viewing angle in degrees"],
                "floor": [None, "Minimum value to be contoured"],
                "ceiling": [None, "Maximum value to be contoured"],
                "stride": [1, "step size, higher vals will have less contour"],
                "cmap": ["RdBu", "colormap (matplotlib) for display"],
                "fancy": [True, "This aint your grandpas iraf"],
                }

# fit of line in image using model
line_fit_pars = {"function": ["line_fit", ],
                 "func": ["Gaussian1D", "function for fitting (see available)"],
                 "title": ["Fit line", "Title of the plot"],
                 "xlabel": ["Column", "The string for the xaxis label"],
                 "ylabel": ["Flux", "The string for the yaxis label"],
                 "background": [False, "Solve for background? [bool]"],
                 "width": [10.0, "Background  width in pixels"],
                 "xorder": [0, "Background terms to fit, 0=median"],
                 "rplot": [15, "Plotting radius in pixels"],
                 "pointmode": [True, "plot points instead of lines? [bool]"],
                 "logx": [False, "log scale x-axis?"],
                 "logy": [False, "log scale y-axis?"],
                 "center": [True, "Recenter around the local max"],
                 }

# fit of column in image using model
column_fit_pars = {"function": ["column_fit", ],
                   "func": ["Gaussian1D", "function for fitting (see available)"],
                   "title": ["Fit 1D to the column", "Title of the plot"],
                   "xlabel": ["Line", "The string for the xaxis label"],
                   "ylabel": ["Flux", "The string for the yaxis label"],
                   "background": [False, "Solve for background? [bool]"],
                   "width": [10.0, "Background  width in pixels"],
                   "xorder": [0, "Background terms to fit, 0=median"],
                   "rplot": [20., "Plotting radius in pixels"],
                   "pointmode": [True, "plot points instead of lines? [bool]"],
                   "logx": [False, "log scale x-axis?"],
                   "logy": [False, "log scale y-axis?"],
                   "center": [True, "Recenter around the local max"],
                   }

# contour plots
contour_pars = {"function": ["contour", ],
                "title": ["Contour plot in region around pixel location", "Title of the plot"],
                "xlabel": ["x", "The string for the xaxis label"],
                "ylabel": ["y", "The string for the yaxis label"],
                "ncolumns": [15, "Number of columns"],
                "nlines": [15, "Number of lines"],
                "floor": [None, "Minimum value to be contoured"],
                "ceiling": [None, "Maximum value to be contoured"],
                "ncontours": [8, "Number of contours to be drawn"],
                "linestyle": ["--", "matplotlib linestyle"],
                "label": [True, "Label major contours with their values? [bool]"],
                "cmap": ["RdBu", "Colormap (matplotlib style) for image"],
                }

# histogram of values contained in a box
histogram_pars = {"function": ["histogram", ],
                  "title": ["Histogram", "Title of the plot"],
                  "xlabel": ["Flux (bin)", "The string for the xaxis label"],
                  "ylabel": ["Count", "The string for the yaxis label"],
                  "ncolumns": [21, "Number of columns"],
                  "nlines": [21, "Number of lines"],
                  "nbins": [100, "Number of bins"],
                  "z1": [None, "Minimum histogram intensity"],
                  "z2": [None, "Maximum histogram intensity"],
                  "pointmode": [True, "plot points instead of lines? [bool]"],
                  "marker": ["o", "The marker character to use, matplotlib style"],
                  "logx": [False, "log scale x-axis?"],
                  "logy": [False, "log scale y-axis?"],
                  }


# plots the values in a line
lineplot_pars = {"function": ["linefit", ],
                 "title": ["Data values for selected line", "Title of the plot"],
                 "xlabel": ["Column", "The string for the xaxis label"],
                 "ylabel": ["Pixel Value", "The string for the yaxis label"],
                 "pointmode": [False, "plot points instead of lines? [bool]"],
                 "marker": ["o", "The marker character to use, matplotlib style"],
                 "logx": [False, "log scale x-axis?"],
                 "logy": [False, "log scale y-axis?"],
                 "xmin": [0, "xaxis min value"],
                 "xmax": [None, "xaxis max value"],
                 "ymin": [0, "yaxis min value"],
                 "ymax": [None, "yaxis max value"],
                 }
# plot the values in a column
colplot_pars = {"function": ["colfit", ],
                "title": ["Data values for selected column", "Title of the plot"],
                "xlabel": ["Line", "The string for the xaxis label"],
                "ylabel": ["Pixel Value", "The string for the yaxis label"],
                "pointmode": [False, "plot points instead of lines? [bool]"],
                "marker": ["o", "The marker character to use, matplotlib style"],
                "logx": [False, "log scale x-axis?"],
                "logy": [False, "log scale y-axis?"],
                "xmin": [0, "xaxis min value"],
                "xmax": [None, "xaxis max value"],
                "ymin": [0, "yaxis min value"],
                "ymax": [None, "yaxis max value"],
                }

# cut out a smaller image user the pointer location
cutout_pars = {"function": ["cutout", ],
               "size": [20, "size of the image to cutout"],
               }
