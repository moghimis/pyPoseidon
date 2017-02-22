import numpy as np
import sys
from netCDF4 import Dataset

def writenc(filename,lat,lon,uval,vval,pval,tstamp,t0):

 ni=lon.shape[0]
 nj=lat.shape[0]

 rootgrp = Dataset(filename, 'w', format='NETCDF3_64BIT')
 lats = rootgrp.createDimension('LAT', nj)
 lons = rootgrp.createDimension('LON', ni)
 time = rootgrp.createDimension('TIME', None)


 longitudes = rootgrp.createVariable('LON','f8',('LON',))
 latitudes = rootgrp.createVariable('LAT','f8',('LAT',))
 u = rootgrp.createVariable('U','f8',('TIME','LON','LAT'))
 v = rootgrp.createVariable('V','f8',('TIME','LON','LAT'))
 times = rootgrp.createVariable('TIME','f8',('TIME',))
 p = rootgrp.createVariable('P','f8',('TIME','LON','LAT'))

 rootgrp.description = ''
 rootgrp.history = 'DELFT3D - JRC Ispra European Commission'
 rootgrp.source = 'netCDF4 python module tutorial'
 latitudes.units = 'degrees_north'
 latitudes.point_spacing = 'even'
 longitudes.units = 'degrees_east'
 longitudes.point_spacing = 'even'
 u.units = 'm/s'
 v.units = 'm/s'
 p.units = 'm'
 times.units = 'hours since {}'.format(t0)


 p[:]=pval
 times[:]=tstamp
 latitudes[:]=lat
 longitudes[:]=lon
 u[:]=uval
 v[:]=vval

 rootgrp.close()

