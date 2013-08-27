#!/bin/bash
#
# This script will be run as the root user inside the virtual build
# machine.

mkdir /usr/CellProfiler
chown cpbuild:cpbuild /usr/CellProfiler

yum -q -y install python-setuptools gcc gcc-c++ wget vim gtk2-devel git svn gcc-gfortran cmake mesa-libGL mesa-libGL-devel blas atlas lapack blas-devel atlas-devel lapack-devel xorg-x11-xauth* xorg-x11-xkb-utils* unzip dejavu-lgc-sans-fonts qt-devel openssl openssl-devel xclock bzip2 bzip2-devel bzip2-libs libXtst make
