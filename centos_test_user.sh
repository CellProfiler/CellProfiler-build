#/bin/bash
        

function untarstuff {
    sudo cp ~/cellprofiler.tar.gz /
    sudo tar xvf /cellprofiler.tar.gz /
}

function yumstuff {
    sudo yum -y install gtk2-devel mesa-libGL mesa-libGL-devel blas atlas lapack blas-devel atlas-devel lapack-devel xorg-x11-xauth* xorg-x11-xkb-utils* qt-devel openssl openssl-devel xclock *Xvfb* svn
}

function runtests {
    /usr/CellProfiler/src/CellProfiler/shortcuts/cellprofiler -t
}

#untarstuff
#yumstuff
runtests
