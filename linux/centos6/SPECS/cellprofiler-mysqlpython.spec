%define pkgname cellprofiler-mysqlpython
%define version 1.2.3
%define release 1
%define tarname MySQL-python
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   mysqlpython
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   GPLv2+
URL:       http://sourceforge.net/projects/mysql-python/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python
BuildRequires: mysql mysql-devel cellprofiler-setuptools gcc

%description
mysqlpython installed under /usr/cellprofiler


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
%{pref}/lib/python2.7/site-packages/MySQL_python-1.2.3-py2.7.egg-info
%{pref}/lib/python2.7/site-packages/MySQLdb
%{pref}/lib/python2.7/site-packages/_mysql.so
%{pref}/lib/python2.7/site-packages/_mysql_exceptions.py
%{pref}/lib/python2.7/site-packages/_mysql_exceptions.pyc
