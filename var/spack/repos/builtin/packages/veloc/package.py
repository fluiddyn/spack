# Copyright 2013-2018 Lawrence Livermore National Security, LLC and other
# Spack Project Developers. See the top-level COPYRIGHT file for details.
#
# SPDX-License-Identifier: (Apache-2.0 OR MIT)

from spack import *


class Veloc(CMakePackage):
    """Very-Low Overhead Checkpointing System. VELOC is a multi-level
    checkpoint-restart runtime for HPC supercomputing infrastructures"""

    homepage = "https://github.com/ECP-VeloC/VELOC"
    url      = "https://github.com/ECP-VeloC/VELOC/archive/veloc-1.0rc1.zip"
    git      = "https://github.com/ecp-veloc/veloc.git"

    tags = ['ecp']

    version('master', branch='master')
    version('1.0',    '98fe2d9abd2a1b53d7a52267dab91fae', preferred=True)
    version('1.0rc1', 'c6db0de56b5b865183b1fa719ac74c1d')

    depends_on('boost~atomic~chrono~clanglibcpp~date_time~debug~exception'
               '~filesystem~graph~icu~iostreams~locale~log~math~mpi'
               '~multithreaded~numpy~program_options~python~random~regex'
               '~serialization~shared~signals~singlethreaded~system'
               '~taggedlayout~test~thread~timer~versionedlayout~wave')
    depends_on('libpthread-stubs')
    depends_on('mpi')
    depends_on('er')
    depends_on('axl')
    depends_on('cmake@3.9:', type='build')

    conflicts('%gcc@:4.9.3')

    # requires C++11
    def flag_handler(self, name, flags):
        flags = list(flags)
        if name == 'cxxflags':
            flags.append(self.compiler.cxx11_flag)
        return (None, None, flags)

    def cmake_args(self):
        args = [
            "-DWITH_AXL_PREFIX=%s" % self.spec['axl'].prefix,
            "-DWITH_ER_PREFIX=%s" % self.spec['er'].prefix,
            "-DBOOST_ROOT=%s" % self.spec['boost'].prefix,
            "-DMPI_CXX_COMPILER=%s" % self.spec['mpi'].mpicxx
        ]

        return args
