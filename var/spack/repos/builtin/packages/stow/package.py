# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Stow(AutotoolsPackage):
    """GNU Stow: a symlink farm manager

       GNU Stow is a symlink farm manager which takes distinct
       packages of software and/or data located in separate
       directories on the filesystem, and makes them appear to be
       installed in the same place."""

    homepage = "https://www.gnu.org/software/stow/"
    url      = "https://ftpmirror.gnu.org/stow/stow-2.2.2.tar.bz2"

    version('2.2.2', 'af1e1de9d973c835bee80c745b5ee849')
    version('2.2.0', '5bb56592eff9aaf9dfb6c975b3004240')
    version('2.1.3', '533651c25b29c3630f01d0be33849a7c')
    version('2.1.2', '0b8154a2165e4004ddc9579e3499af98')
    version('2.1.1', '882d2490d05723b4b78029c2973775d3')
    version('2.1.0', 'aa3a2389b6cbf3bd555e15c80a0be6ab')

    depends_on('perl@5.6.1:')
