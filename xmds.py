""" Read MDS tree data into xray DataArray """
import xray
import MDSplus as mds


_SIGNALS = [
    r'\top.oned:ip',
    r'\top.oned:pnbi',
    r'\top.oned:zeff',

    # r'\top.twod:q',
    r'\top.twod:te',
    r'\top.twod:ti',
    r'\top.twod:ne',
]


def read_mds(host, tree, shot, signals=None):
    """ Connect to host and read the signals from the MDS tree of the specified
    shot.
    """
    assert isinstance(host, str)
    assert isinstance(tree, str)
    assert isinstance(shot, int)

    signals = signals if signals else _SIGNALS

    conn = mds.Connection(host)
    conn.openTree(tree, shot)

    darrays = {}
    for signal in signals:
        darrays[_name(signal)] = _read_one_signal(conn, signal)

    conn.closeTree(tree, shot)

    return xray.Dataset(darrays)


def _name(signal):
    """ Get a signal name """
    return signal.split(':')[1]


def _read_one_signal(connection, signal):
    """ Read one signal through the connection """
    if 'oned' in signal:
        dimensions = {0: 'time'}
    elif 'twod' in signal:
        dimensions = {0: 'rho', 1: 'time'}
    else:
        raise NotImplementedError

    data = connection.get(signal)

    coords = {}
    units = {}
    for i in xrange(2):
        dim = r'dim_of({}, {})'.format(signal, i)
        unit = r'units_of({})'.format(dim)

        try:
            coords[dimensions[i]] = connection.get(dim)
            units[dimensions[i]] = connection.get(unit)
        except mds.MdsException:
            break

    # FIXME why do we need the transpose here?
    return xray.DataArray(data.T, coords, attrs={'units': units})
