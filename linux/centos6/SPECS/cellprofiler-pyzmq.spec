%define pkgname cellprofiler-pyzmq
%define pyversion 2.7
%define epoch 2
%define version 2.1.11
%define release 1
%define tarname pyzmq
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   pyzmq installed under /usr/cellprofiler
Epoch:     %{epoch}
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   BSD or LGPL
URL:       http://github.com/zeromq/pyzmq
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python cellprofiler-zeromq
BuildRequires: cellprofiler-python gcc gcc-c++ cellprofiler-zeromq-devel cellprofiler-cython

%description
pyzmq installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}
#
# Required for building on Cython 0.19+
# See https://github.com/zeromq/pyzmq/commit/1aeb9a6313a81463bed6a1135f5e473322122009
#
patch -p0 <<EOF
diff -ru temp/pyzmq-2.1.11/zmq/utils/buffers.pxd pyzmq-2.1.11/zmq/utils/buffers.pxd
--- zmq/utils/buffers.pxd.orig	2011-12-19 01:22:40.000000000 -0500
+++ zmq/utils/buffers.pxd	2014-10-24 13:33:02.797520510 -0400
@@ -134,10 +134,11 @@
 
     cdef void *bptr = NULL
     cdef Py_ssize_t blen = 0, bitemlen = 0
-    cdef str bfmt = None
     cdef Py_buffer view
     cdef int flags = PyBUF_SIMPLE
     cdef int mode = 0
+    
+    bfmt = None
 
     mode = check_buffer(ob)
     if mode == 0:
@@ -173,7 +174,7 @@
                     bitemlen = ob.itemsize
                 except AttributeError:
                     if isinstance(ob, bytes):
-                        bfmt = "B"
+                        bfmt = b"B"
                         bitemlen = 1
                     else:
                         # nothing found
EOF

%build

%{pref}/bin/python setup.py build


%install

%{pref}/bin/python setup.py install --root=$RPM_BUILD_ROOT


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/python2.7/site-packages/zmq
%{pref}/lib/python2.7/site-packages/pyzmq-2.1.11-py2.7.egg-info
