%define pkgname cellprofiler-qimage2ndarray
%define version 1.0
%define release 2
%define tarname qimage2ndarray
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   qimage2ndarray
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   BSD
URL:       http://kogs-www.informatik.uni-hamburg.de/~meine/software/qimage2ndarray/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-numpy = 1.9.0 cellprofiler-pyqt-x11-gpl cellprofiler-sip
BuildRequires: cellprofiler-pyqt-x11-gpl gcc gcc-c++ cellprofiler-sip-devel cellprofiler-numpy-devel = 1.9.0 qt4-devel 

%description
qimage2ndarray installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

%{pref}/bin/python setup.py build


%install

%{pref}/bin/python setup.py install --root=$RPM_BUILD_ROOT


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/python2.7/site-packages/qimage2ndarray-1.0-py2.7.egg-info
%{pref}/lib/python2.7/site-packages/qimage2ndarray
