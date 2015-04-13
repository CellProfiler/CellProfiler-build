%define pkgname cellprofiler-javabridge
%define version 1.0.9
%define release 2
%define tarname javabridge
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   dateutil
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   BSD
URL:       http://github.com/CellProfiler/python-javabridge/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python cellprofiler-setuptools cellprofiler-numpy = 1.9.0 java-1.6.0-openjdk-devel
BuildRequires: cellprofiler-python cellprofiler-setuptools cellprofiler-numpy = 1.9.0 gcc python-devel java-1.6.0-openjdk-devel cellprofiler-numpy-devel = 1.9.0

%description
python-javabridge installed under /usr/cellprofiler


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
%{pref}/lib/python2.7/site-packages/javabridge
%{pref}/lib/python2.7/site-packages/javabridge-%{version}-py2.7.egg-info
