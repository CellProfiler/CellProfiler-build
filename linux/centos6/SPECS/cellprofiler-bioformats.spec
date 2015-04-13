%define pkgname cellprofiler-bioformats
%define version 1.0.4
%define release 1
%define tarname python-bioformats
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   dateutil
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   BSD
URL:       http://github.com/CellProfiler/python-bioformats/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-javabridge cellprofiler-setuptools
BuildRequires: cellprofiler-javabridge cellprofiler-setuptools

%description
python-bioformats installed under /usr/cellprofiler


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
%{pref}/lib/python2.7/site-packages/bioformats
%{pref}/lib/python2.7/site-packages/python_bioformats-%{version}-py2.7.egg-info
