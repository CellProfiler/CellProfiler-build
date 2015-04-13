%define pkgname cellprofiler-setuptools
%define pyversion 2.7
%define version 1.1.6
%define release 1
%define tarname setuptools
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   setuptools
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   Python or ZPLv2.0
URL:       http://pypi.python.org/pypi/distribute
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python
BuildRequires: cellprofiler-python

%description
setuptools installed under /usr/cellprofiler


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
%{pref}/bin/easy_install
%{pref}/bin/easy_install-2.7
%{pref}/lib/python2.7/site-packages/_markerlib
%{pref}/lib/python2.7/site-packages/easy_install.py
%{pref}/lib/python2.7/site-packages/easy_install.pyc
%{pref}/lib/python2.7/site-packages/pkg_resources.py
%{pref}/lib/python2.7/site-packages/pkg_resources.pyc
%{pref}/lib/python2.7/site-packages/setuptools-1.1.6-py2.7.egg-info/
%{pref}/lib/python2.7/site-packages/setuptools/
