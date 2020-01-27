.. _registry:

Where are my data?
==================

The model and dataset files are downloaded automatically by :mod:`pooch` to the default
cache location on your operating system. The location varies depending on your system
and configuration. We provide the :func:`rockhound.data_location` function that will
return the data storage location on your system.

You can overwrite the local storage directory by setting the ``ROCKHOUND_DATA_DIR``
environment variable to the desired path.

All data fetching functions (see :ref:`api`) take an optional ``load=True`` argument.
Setting it to ``False`` will tell the function to return the path to the data file
instead of loading it into a Python variable.
Use this to figure out where specific data files are and in case you wish to load the
data yourself.
