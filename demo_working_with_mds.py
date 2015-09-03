import MDSplus as mds

conn = mds.Connection('tokamak-profiledb.ccfe.ac.uk')
conn.openTree('pr98_jet', 19649)  # shot in PR98 PDB (freely accessible)

ip = conn.get(r'\top.oned:ip')
tip = conn.get(r'dim_of(\top.oned:ip)')
ip_units = conn.get(r'units_of(\top.oned:ip)')
tip_units = conn.get(r'units_of(dim_of(\top.oned:ip))')

ne = conn.get(r'\top.twod:ne')
rne = conn.get(r'dim_of(\top.twod:ne,0)')
tne = conn.get(r'dim_of(\top.twod:ne,1)')
rne_units = conn.get(r'units_of(dim_of(\top.twod:ne,0))')
tne_units = conn.get(r'units_of(dim_of(\top.twod:ne,1))')
