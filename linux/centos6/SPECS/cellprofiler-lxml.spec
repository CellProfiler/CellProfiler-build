%define pkgname cellprofiler-lxml
%define version 3.4.2
%define release 1
%define tarname lxml
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   lxml
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   BSD
URL:       http://lxml.de/
Packager:  Lee Kamentsky <leek@broadinstitute.org>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python cellprofiler-setuptools cellprofiler-six
Requires:  libxml2 libxslt
BuildRequires: cellprofiler-python cellprofiler-setuptools libxml2-devel libxslt-devel gcc-c++

%description
lxml installed under /usr/cellprofiler


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
%{pref}/lib/python2.7/site-packages/lxml
%{pref}/lib/python2.7/site-packages/lxml-%{version}-py2.7.egg-info
