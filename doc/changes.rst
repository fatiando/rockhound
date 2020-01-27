.. _changes:

Changelog
=========

Version 0.2.0
-------------

*Released on: 2020/01/27*

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3627166.svg
   :target: https://doi.org/10.5281/zenodo.3627166

New models and datasets:

- Slab2 model [SLAB2]_ (`#62 <https://github.com/fatiando/rockhound/pull/62>`__)

New features:

- Load Bedmap2 datasets as Dask arrays to reduce memory consumption by
  reading the downloaded files in chunks.
  (`#45 <https://github.com/fatiando/rockhound/pull/45>`__)

Maintenance:

- Add GitHub template for requesting new datasets or models.
  (`#41 <https://github.com/fatiando/rockhound/pull/41>`__)
- Update CI scripts and fix linting errors.
  (`#55 <https://github.com/fatiando/rockhound/pull/55>`__)
- Use napoleon instead of numpydoc and unpin Sphinx on requirements.
  (`#60 <https://github.com/fatiando/rockhound/pull/60>`__)
- Fix typo on multiple files.
  (`#64 <https://github.com/fatiando/rockhound/pull/64>`__)
- Disable unwanted pylint warnings.
  (`#65 <https://github.com/fatiando/rockhound/pull/65>`__)
- Wrap docstrings to 79 characters per line and check with flake8.
  (`#68 <https://github.com/fatiando/rockhound/pull/68>`__)

This release contains contributions from:

- Santiago Soler
- Agustina Pesce
- Leonardo Uieda


Version 0.1.0
-------------

*Released on: 2019/05/21*

.. image:: https://zenodo.org/badge/DOI/10.5281/zenodo.3086002.svg
   :target: https://doi.org/10.5281/zenodo.3086002

Fist release of Rockhound. Easily download geophysical models and datasets (PREM,
CRUST1.0, ETOPO1 and more) and load them into Python data structures (pandas, numpy,
xarray).

Available models and datasets:

- ETOPO1 [AmanteEakins2009]_
- PREM [Dziewonsky1981]_
- Bedmap2 [BEDMAP2]_
- Age of the oceanic lithosphere [Muller2008]_

Features:

- Use `Pooch <https://www.fatiando.org/pooch>`__ to download remote files, check if they
  are not corrupted and decompress files if necessary.
