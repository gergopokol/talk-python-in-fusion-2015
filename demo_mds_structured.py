import matplotlib.pyplot as plt
import xmds

# shot in PR98 PDB (freely accessible)
ds = xmds.read_mds('tokamak-profiledb.ccfe.ac.uk', 'pr98_jet', 19649)

# Attributes cannot be saved (bug?). The following does not work.
# ds.to_netcdf('pr98_jet_19649.nc')

# Make a copy and nullify attributes to be able to save the DataSet
ds_to_save = ds.copy()
for signal in ds_to_save:
    ds[signal].attrs = {}
ds_to_save.to_netcdf('pr98_jet_19649.nc')
