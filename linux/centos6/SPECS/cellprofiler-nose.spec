%define pkgname cellprofiler-nose
%define pyversion 2.7
%define version 1.3.4
%define release 1
%define tarname nose
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   nose
Version:   %{version}
Release:   %{release}
Source0:   https://pypi.python.org/packages/source/n/nose/nose-1.3.4.tar.gz
License:   GNU LGPL
URL:       https://pypi.python.org/pypi/nose
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python
BuildRequires: cellprofiler-python

%description
nose installed under /usr/cellprofiler


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
%{pref}/lib/python2.7/site-packages/nose-1.3.4-py2.7.egg-info/
%{pref}/lib/python2.7/site-packages/nose/
%{pref}/bin/nosetests
%{pref}/man/man1/nosetests.1

