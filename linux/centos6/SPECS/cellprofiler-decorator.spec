%define pkgname cellprofiler-decorator
%define version 3.2.0
%define release 1
%define tarname decorator
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   decorator
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   BSD
URL:       http://www.phyast.pitt.edu/~micheles/python/documentation.html
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python
BuildRequires: cellprofiler-python

%description
decorator installed under /usr/cellprofiler


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
%{pref}/lib/python2.7/site-packages/decorator-3.2.0-py2.7.egg-info
%{pref}/lib/python2.7/site-packages/decorator.py
%{pref}/lib/python2.7/site-packages/decorator.pyc
