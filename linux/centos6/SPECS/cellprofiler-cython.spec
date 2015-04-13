%define pkgname cellprofiler-cython
%define pyversion 2.7
%define version 0.20.2
%define release 1
%define tarname Cython
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   cython installed under /usr/cellprofiler
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   ?
URL:       ?
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python
BuildRequires: cellprofiler-python gcc

%description
cython installed under /usr/cellprofiler


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
%{pref}/lib/python2.7/site-packages/pyximport
%{pref}/lib/python2.7/site-packages/Cython
%{pref}/lib/python2.7/site-packages/cython.py
%{pref}/lib/python2.7/site-packages/cython.pyc
%{pref}/lib/python2.7/site-packages/Cython-0.20.2-py2.7.egg-info
%{pref}/bin/cython
%{pref}/bin/cygdb

