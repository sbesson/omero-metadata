#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
   Metadata plugin

   Copyright 2015 Glencoe Software, Inc. All rights reserved.
   Use is subject to license terms supplied in LICENSE.txt

"""

from omero_cli_metadata import MetadataControl, HELP
try:
    register("metadata", MetadataControl, HELP)
except NameError:
    if __name__ == "__main__":
        cli = CLI()
        cli.register("metadata", MetadataControl, HELP)
        cli.invoke(sys.argv[1:])
