%define pkgname cellprofiler-six
%define version 1.4.1
%define release 1
%define tarname six
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   six
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   MIT
URL:       http://pypi.python.org/pypi/six/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python
BuildRequires: cellprofiler-python

%description
six installed under /usr/cellprofiler


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
%{pref}/lib/python2.7/site-packages/six.py
%{pref}/lib/python2.7/site-packages/six.pyc
%{pref}/lib/python2.7/site-packages/six-1.4.1-py2.7.egg-info
