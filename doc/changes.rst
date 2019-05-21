.. _changes:

Changelog
=========

Version 0.1.0
-------------

*Released on: 2019/05/21*

Fist release of Rockhound. Easily download geophysical models and datasets (PREM,
CRUST1.0, ETOPO1 and more) and load them into Python data structures (pandas, numpy,
xarray).

Available models and datasets:

- ETOPO1 [AmanteEakins2009]_
- PREM [Dziewonsky1981]_
- Bedmap2 [BEDMAP2]_
- Age of the oceanic lithosphere [Muller2008]_

Features:

- Use Pooch to download remote files, check if they are not corrupted and uncompress
  files if necessary.
