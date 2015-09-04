Reproducible graphs, reproducible science
=========================================

These are the scripts presented on 2015/09/04 at a workshop Python in Fusion.

The following modules need to be installed:

* matplotlib & numpy
* MDSplus Python interface [1] 
* xray [2]

[1] http://www.mdsplus.org/index.php/Documentation:Users:MDSobjects:Python
[2] http://xray.readthedocs.org

Presentation
------------

The scripts were presented in the following order

1. demo_working_environment.py
2. demo_working_with_mds.py
3. demo_mds_structured.py
4. demo_dataset.py

Note about MDSplus
------------------

Make sure that the MDSplus shared libaries can be found when the MDSplus Python
module is loaded.  You may need to tune the LD_LIBRARY_PATH parameter

    $ export LD_LIBRARY_PATH=/usr/local/mdsplus/lib:$LD_LIBRARY_PATH
