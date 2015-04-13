%define pkgname cellprofiler-matplotlib
%define pyversion 2.7
%define version 1.0.1
%define release 2
%define tarname matplotlib
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   matplotlib
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   Python
URL:       http://sourceforge.net/projects/matplotlib
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  freetype cellprofiler-libpng cellprofiler-libtiff cellprofiler-libjpeg cellprofiler-python cellprofiler-numpy = 1.9.0 cellprofiler-wxpython2.8-gtk2-unicode cellprofiler-six cellprofiler-dateutil cellprofiler-pytz cellprofiler-six
BuildRequires: gcc gcc-c++ freetype-devel cellprofiler-python cellprofiler-numpy-devel = 1.9.0 fftw-devel cellprofiler-hdf5-devel cellprofiler-libpng-devel cellprofiler-libtiff-devel cellprofiler-libjpeg-devel boost-python-devel cmake cellprofiler-setuptools cellprofiler-wxpython2.8-devel-gtk2-unicode cellprofiler-six

%description
matplotlib installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

cat > setup.cfg <<EOF
# Rename this file to setup.cfg to modify matplotlib's
# build options.

[egg_info]

[directories]
# Uncomment to override the default basedir in setupext.py.
# This can be a single directory or a comma-delimited list of directories.
basedirlist = /usr/cellprofiler,/usr

[status]
# To suppress display of the dependencies and their versions
# at the top of the build log, uncomment the following line:
#suppress = False

[packages]
# There are a number of subpackages of matplotlib that are considered
# optional.  They are all installed by default, but they may be turned
# off here.
#
tests = False
sample_data = False
#toolkits = True

[provide_packages]
pytz = False
dateutil = False
six = False

[gui_support]
# Matplotlib supports multiple GUI toolkits, including Cocoa,
# GTK, Fltk, MacOSX, Qt, Qt4, Tk, and WX. Support for many of
# these toolkits requires AGG, the Anti-Grain Geometry library,
# which is provided by matplotlib and built by default.
#
# Some backends are written in pure Python, and others require
# extension code to be compiled. By default, matplotlib checks for
# these GUI toolkits during installation and, if present, compiles the
# required extensions to support the toolkit.
#
# - GTK 2.x support of any kind requires the GTK runtime environment
#   headers and PyGTK.
# - Tk support requires Tk development headers and Tkinter.
# - Mac OSX backend requires the Cocoa headers included with XCode.
# - Windowing is MS-Windows specific, and requires the "windows.h"
#   header.
#
# The other GUI toolkits do not require any extension code, and can be
# used as long as the libraries are installed on your system --
# therefore they are installed unconditionally.
#
# You can uncomment any the following lines to change this
# behavior. Acceptible values are:
#
#     True: build the extension. Exits with a warning if the
#           required dependencies are not available
#     False: do not build the extension
#     auto: build if the required dependencies are available,
#           otherwise skip silently. This is the default
#           behavior
#
agg = True
cairo = False
gtk = False
gtk3agg = False
gtk3cairo = False
gtkagg = False
macosx = False
pyside = False
qt4agg = True
tkagg = False
windowing = False
wxagg = True

[rc_options]
# User-configurable options
#
# Default backend, one of: Agg, Cairo, CocoaAgg, GTK, GTKAgg, GTKCairo,
# FltkAgg, MacOSX, Pdf, Ps, QtAgg, Qt4Agg, SVG, TkAgg, WX, WXAgg.
#
# The Agg, Ps, Pdf and SVG backends do not require external
# dependencies. Do not choose GTK, GTKAgg, GTKCairo, MacOSX, or TkAgg
# if you have disabled the relevent extension modules.  Agg will be used
# by default.
#
backend = WX
#
EOF
env PATH=%{pref}/bin:$PATH \
    PKG_CONFIG_PATH=%{pref}/lib/pkgconfig:/usr/lib/pkgconfig \
    CPPFLAGS="-I%{pref}/include" \
    LDFLAGS="-L%{pref}/lib" \
%{pref}/bin/python setup.py build


%install

%{pref}/bin/python setup.py install --root=$RPM_BUILD_ROOT


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/python2.7/site-packages/pylab.pyc
%{pref}/lib/python2.7/site-packages/matplotlib-1.0.1-py2.7.egg-info
%{pref}/lib/python2.7/site-packages/pylab.py
%{pref}/lib/python2.7/site-packages/matplotlib
%{pref}/lib/python2.7/site-packages/mpl_toolkits

