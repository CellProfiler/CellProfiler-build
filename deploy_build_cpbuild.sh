#!/bin/bash
#
# This script will be run as the cpbuild user inside the virtual build
# machine.



function gitclone {
    cd /usr/CellProfiler/src
    git clone https://github.com/CellProfiler/CellProfiler.git
}

function makebindir {
    sudo mkdir -p /usr/CellProfiler/src
    sudo chmod 777 /usr/CellProfiler
    sudo chmod 777 /usr/CellProfiler/src
}

function yumstuff {
    sudo yum -y install python-setuptools gcc gcc-c++ wget vim gtk2-devel git svn gcc-gfortran cmake mesa-libGL mesa-libGL-devel blas atlas lapack blas-devel atlas-devel lapack-devel xorg-x11-xauth* xorg-x11-xkb-utils* unzip dejavu-lgc-sans-fonts qt-devel openssl openssl-devel xclock bzip2 bzip2-devel bzip2-libs libXtst
}

function makeall {
    export GITHOME=/usr/CellProfiler/src/CellProfiler
    export JAVA_HOME=$GITHOME/jdk1.7.0_21
    export LD_LIBRARY_PATH=$JAVA_HOME/jre/lib/amd64/server:/usr/CellProfiler/lib/
    export PATH=/usr/CellProfiler/bin:$PATH
    export HOSTTYPE=amd64
    export BLAS=/usr/lib64
    export LAPACK=/usr/lib64
    cd $GITHOME
    make -f Makefile.CP2.standard.64 all
    /usr/CellProfiler/bin/python -m easy_install pyzmq
    make -f Makefile.CP2.standard.64 all
}
function downloadjava {
    url='http://cellprofiler.org/linked_files/CPPackageHost/'
    javajdk='jdk-7u21-linux-x64.tar.gz'
    javajre='jre-7u21-linux-x64.tar.gz'
    javajdkrpm='jdk-7u21-linux-x64.rpm'
    javajrerpm='jre-7u21-linux-x64.rpm'
    cd /usr/CellProfiler/src/CellProfiler
    wget $url/$javajdk
}

function installjava {
    cd /usr/CellProfiler/src/CellProfiler
    tar xvf jdk-7u21-linux-x64.tar.gz
    cd jdk1.7.0_21
    unzip src.zip
}

function tarup {
    cd $HOME
    tar cvzf cellprofiler.tar.gz /usr/CellProfiler
}

function clean {
    cd /usr/CellProfiler/src/CellProfiler
    rm ./*.tar.gz
    rm ./*.tar.bz2
}

echo This is inside deploy_cpbuild.sh
#makebindir
#yumstuff
gitclone
downloadjava
installjava
makeall
clean
tarup
