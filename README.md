# Iver3-Motor-CMD-Analysis
OceanServer Iver3 autonomous underwater vehicle log analyzer. For finding relationship between power and speed.
This python based program uses pandas, numpy, sklearn, matplotlib and the PyQt4 framework.
The program will load an Iver3 mission log file and allow the user to filter out certain mission legs depending on depth from surface and leg time. Once filtered the vehicle speed table and power table can be generated. It is crucial to load a mission log where the vehicle is traveling a range of speeds. The larger the range the more accurate the regression analysis will be. Both for speed and power.
