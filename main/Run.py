import numpy as np

from experement import Experement as Exp
from experement import Visualiser as Vis
from experement import FullScaleExperiment as Fse

# Start data X
x = np.array(Fse.x)
Vis.print_data("Start data X", x.transpose())

# Start data Y
y = np.array(Fse.y)
Vis.print_data("Start data Y", y.transpose())

# Standardization +1 -1
stand_x = Exp.standardization_pm(x)
Vis.print_data("Standardization data of X", stand_x.transpose())
Vis.print_data("Start data X", x.transpose())



# vis.printData("Data X", x)
# vis.printData("Data Y", y)
