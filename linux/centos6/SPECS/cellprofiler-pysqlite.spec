%define pkgname cellprofiler-pysqlite
%define version 2.6.1
%define release 1
%define tarname pysqlite
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   pysqlite
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   zlib/libpng
URL:       https://pypi.python.org/pypi/pysqlite
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python cellprofiler-sqlite
BuildRequires: cellprofiler-sqlite-devel cellprofiler-python gcc

%description
pysqlite installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

env CFLAGS="-I%{pref}/include" \
    %{pref}/bin/python setup.py build


%install

%{pref}/bin/python setup.py install --root=$RPM_BUILD_ROOT


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/python2.7/site-packages/pysqlite-2.6.1-py2.7.egg-info
%{pref}/lib/python2.7/site-packages/pysqlite2
%doc %{pref}/pysqlite2-doc/install-source.txt
