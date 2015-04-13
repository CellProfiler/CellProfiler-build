%define pkgname cellprofiler
%define pyversion 2.7
%define version 2.1.1
%define release 2
%define tarname CellProfiler-%{version}
%define pref /usr/cellprofiler
%define python %{pref}/bin/python

Name:      %{pkgname}
Summary:   Cell image analysis software
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}.tar.gz
Patch0:    cellprofiler-frozen.diff
License:   GPLv2
URL:       http://www.cellprofiler.org/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-cython = 0.20.2-1
Requires:  cellprofiler-python = 2.7.2-1
Requires:  cellprofiler-dateutil = 2.2-1
Requires:  cellprofiler-decorator = 3.2.0-1
Requires:  cellprofiler-h5py = 2.2.0-2
Requires:  cellprofiler-hdf5 = 1.8.10patch1-1
Requires:  cellprofiler-ilastik = 0.5.05-4
Requires:  cellprofiler-jdk = 7u21-1
Requires:  cellprofiler-libjpeg = 8b-1
Requires:  cellprofiler-libpng = 1.4.5-1
Requires:  cellprofiler-libtiff = 3.9.4-1
Requires:  cellprofiler-matplotlib = 1.0.1-2
Requires:  cellprofiler-mysqlpython = 1.2.3-1
Requires:  cellprofiler-numpy = 1.9.0-1
Requires:  cellprofiler-pil = 1.1.7-2
Requires:  cellprofiler-pyopengl = 3.0.1-3
Requires:  cellprofiler-pyqt-x11-gpl = 4.8.3-2
Requires:  cellprofiler-pysqlite = 2.6.1-1
Requires:  cellprofiler-pytz = 2013.7-1
Requires:  cellprofiler-pyzmq = 2:2.1.11-1
Requires:  cellprofiler-qimage2ndarray = 1.0-2
Requires:  cellprofiler-scikit-learn = 0.15.2-2
Requires:  cellprofiler-scipy = 0.13.2-1
Requires:  cellprofiler-setuptools = 1.1.6-1
Requires:  cellprofiler-vigra = 1.7.1-2
Requires:  cellprofiler-wxpython = 2.8.11.0-1
Requires:  xorg-x11-fonts-Type1 liberation-fonts-common liberation-sans-fonts
Requires:  cellprofiler-nose

BuildRequires: gcc
BuildRequires: cellprofiler-hdf5-devel = 1.8.10patch1-1
BuildRequires: cellprofiler-numpy-devel = 1.9.0-1
BuildRequires: cellprofiler-cython = 0.20.2-1
BuildRequires: cellprofiler-python = 2.7.2-1
BuildRequires:  cellprofiler-dateutil = 2.2-1
BuildRequires:  cellprofiler-decorator = 3.2.0-1
BuildRequires:  cellprofiler-h5py = 2.2.0-2
BuildRequires:  cellprofiler-hdf5 = 1.8.10patch1-1
BuildRequires:  cellprofiler-ilastik = 0.5.05-4
BuildRequires:  cellprofiler-jdk = 7u21-1
BuildRequires:  cellprofiler-libjpeg = 8b-1
BuildRequires:  cellprofiler-libpng = 1.4.5-1
BuildRequires:  cellprofiler-libtiff = 3.9.4-1
BuildRequires:  cellprofiler-matplotlib = 1.0.1-2
BuildRequires:  cellprofiler-mysqlpython = 1.2.3-1
BuildRequires:  cellprofiler-numpy = 1.9.0-1
BuildRequires:  cellprofiler-pil = 1.1.7-2
BuildRequires:  cellprofiler-pyopengl = 3.0.1-3
BuildRequires:  cellprofiler-pyqt-x11-gpl = 4.8.3-2
BuildRequires:  cellprofiler-pysqlite = 2.6.1-1
BuildRequires:  cellprofiler-pytz = 2013.7-1
BuildRequires:  cellprofiler-pyzmq = 2:2.1.11-1
BuildRequires:  cellprofiler-qimage2ndarray = 1.0-2
BuildRequires:  cellprofiler-scikit-learn = 0.15.2-2
BuildRequires:  cellprofiler-scipy = 0.13.2-1
BuildRequires:  cellprofiler-setuptools = 1.1.6-1
BuildRequires:  cellprofiler-vigra = 1.7.1-2
BuildRequires:  cellprofiler-wxpython = 2.8.11.0-1

%description
Cell image analysis software

%prep

%setup -q -n %{tarname}

# Patch for issue 1235
#
patch -p0 <<EOF
--- cellprofiler/cpmath/threshold.py    2014-07-23 13:39:57.000000000 -0400
+++ cellprofiler/cpmath/threshold.py 2014-10-27 16:21:40.719976873 -0400
@@ -417,7 +417,7 @@
     # data
     #
     r = np.random.RandomState()
-    r.seed(cropped_image[:100].tolist())
+    r.seed(np.frombuffer(cropped_image[:100].data, np.uint8).tolist())
     for data in (
         r.permutation(cropped_image)[0:(len(cropped_image) / 10)],
         cropped_image):
EOF

%build

PATH=%{pref}/bin:%{pref}/jdk/bin:$PATH \
    LD_LIBRARY_PATH=%{pref}/jdk/lib:%{pref}/jdk/jre/lib/amd64/server: \
    JAVA_HOME=%{pref}/jdk \
    python CellProfiler.py --build-and-exit
PATH=%{pref}/bin:%{pref}/jdk/bin:$PATH \
    LD_LIBRARY_PATH=%{pref}/jdk/lib:%{pref}/jdk/jre/lib/amd64/server: \
    JAVA_HOME=%{pref}/jdk \
    MAVEN_OPTS="-Xmx1024m" \
    python external_dependencies.py -o

patch <<EOF
--- CellProfiler.py.orig	2013-10-16 20:59:07.459360385 -0400
+++ CellProfiler.py	2013-10-16 20:16:34.079360393 -0400
@@ -20,6 +20,8 @@
 import tempfile
 from cStringIO import StringIO
 
+sys.frozen = True
+
 if sys.platform.startswith('win'):
     # This recipe is largely from zmq which seems to need this magic
     # in order to import in frozen mode - a topic the developers never
EOF

%install

mkdir -p $RPM_BUILD_ROOT%{pref}/src
cp -a . $RPM_BUILD_ROOT%{pref}/src/CellProfiler

(cd cellprofiler/utilities && PATH=%{pref}/bin:%{pref}/jdk/bin:$PATH \
    LD_LIBRARY_PATH=%{pref}/jdk/lib:%{pref}/jdk/jre/lib/amd64/server \
    JAVA_HOME=%{pref}/jdk \
%{python} setup.py install --root=$RPM_BUILD_ROOT)

(cd cellprofiler/cpmath && PATH=%{pref}/bin:$PATH \
%{python} setup.py install --root=$RPM_BUILD_ROOT)

echo "version_string = '`date +%%Y-%%m-%%dT%%H:%%M:%%S` %{version}'" > $RPM_BUILD_ROOT%{pref}/src/CellProfiler/cellprofiler/frozen_version.py

mkdir -p $RPM_BUILD_ROOT/usr/bin
cp usr-bin-cellprofiler $RPM_BUILD_ROOT/usr/bin/cellprofiler
chmod 755 $RPM_BUILD_ROOT/usr/bin/cellprofiler

%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/src/CellProfiler
%{pref}/lib/python%{pyversion}/site-packages/_convex_hull.so
%{pref}/lib/python%{pyversion}/site-packages/_cpmorphology.so
%{pref}/lib/python%{pyversion}/site-packages/_cpmorphology2.so
%{pref}/lib/python%{pyversion}/site-packages/_filter.so
%{pref}/lib/python%{pyversion}/site-packages/javabridge.so
%{pref}/lib/python%{pyversion}/site-packages/_lapjv.so
%{pref}/lib/python%{pyversion}/site-packages/_propagate.so
%{pref}/lib/python%{pyversion}/site-packages/_watershed.so
%{pref}/lib/python%{pyversion}/site-packages/cpmath-0.0.0-py2.7.egg-info
%{pref}/lib/python%{pyversion}/site-packages/utilities-0.0.0-py2.7.egg-info
/usr/bin/cellprofiler
