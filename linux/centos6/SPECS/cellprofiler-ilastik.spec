%define pkgname cellprofiler-ilastik
%define pyversion 2.7
%define version 0.5.05
%define release 4
%define tarname ilastik
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   ilastik
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-v%{version}.tar.gz
Patch0:    ilastik-uifiles.diff
License:   BSD
URL:       http://klimt.iwr.uni-heidelberg.de/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python cellprofiler-numpy = 1.9.0 fftw cellprofiler-hdf5 cellprofiler-libpng cellprofiler-libtiff cellprofiler-libjpeg boost-python cellprofiler-vigra cellprofiler-pyopengl cellprofiler-pyopengl-accelerate cellprofiler-pyqt-x11-gpl cellprofiler-qimage2ndarray
BuildRequires: cellprofiler-python cellprofiler-numpy-devel = 1.9.0 fftw-devel cellprofiler-hdf5-devel cellprofiler-libpng-devel cellprofiler-libtiff-devel cellprofiler-libjpeg-devel boost-python-devel cmake cellprofiler-setuptools

%description
ilastik installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-v%{version}
%patch0

%build

%{pref}/bin/python setup.py build


%install

%{pref}/bin/python setup.py install --root=$RPM_BUILD_ROOT


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/python2.7/site-packages/ilastik
%{pref}/lib/python2.7/site-packages/ilastik-0.5-py2.7.egg-info
%{pref}/lib/python2.7/site-packages/ilastik/gui/classifierSelectionDlg.ui
%{pref}/lib/python2.7/site-packages/ilastik/modules/project_gui/gui/dlgProject.ui
%{pref}/lib/python2.7/site-packages/ilastik/modules/project_gui/gui/dlgChannels.ui
%{pref}/lib/python2.7/site-packages/ilastik/modules/classification/gui/classifierSelectionDlg.ui
%{pref}/lib/python2.7/site-packages/ilastik/modules/classification/gui/dlgFeature.ui
