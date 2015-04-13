%define pkgname cellprofiler-pandas
%define version 0.16.0
%define release 1
%define tarname pandas
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   pandas
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   BSD
URL:       http://pandas.pydata.org
Packager:  Lee Kamentsky <leek@broadinstitute.org>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-numpy = 1.9.0 cellprofiler-pytz cellprofiler-dateutil
BuildRequires: cellprofiler-numpy-devel = 1.9.0 gcc-c++ cellprofiler-pytz cellprofiler-dateutil

%description
pandas installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

env CFLAGS="$RPM_OPT_FLAGS" \
    PATH=%{pref}/bin:$PATH \
    %{pref}/bin/python setup.py build


%install

env CFLAGS="$RPM_OPT_FLAGS" \
    %{pref}/bin/python setup.py install --root $RPM_BUILD_ROOT


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/python2.7/site-packages/pandas
%{pref}/lib/python2.7/site-packages/pandas-%{version}-py2.7.egg-info
