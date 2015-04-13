%define pkgname cellprofiler-pytz
%define version 2013.7
%define release 1
%define tarname pytz
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   pytz
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.bz2
License:   MIT
URL:       http://pythonhosted.org/pytz
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python
BuildRequires: cellprofiler-python

%description
pytz installed under /usr/cellprofiler


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
%{pref}/lib/python2.7/site-packages/pytz
%{pref}/lib/python2.7/site-packages/pytz-2013.7-py2.7.egg-info
