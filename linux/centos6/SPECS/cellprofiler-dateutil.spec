%define pkgname cellprofiler-dateutil
%define version 2.2
%define release 2
%define tarname python-dateutil
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   dateutil
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   Simplified BSD
URL:       http://labix.org/python-dateutil
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python cellprofiler-setuptools cellprofiler-six
BuildRequires: cellprofiler-python cellprofiler-setuptools

%description
dateutil installed under /usr/cellprofiler


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
%{pref}/lib/python2.7/site-packages/dateutil
%{pref}/lib/python2.7/site-packages/python_dateutil-2.2-py2.7.egg-info
