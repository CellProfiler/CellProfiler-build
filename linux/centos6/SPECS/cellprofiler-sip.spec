%define pkgname cellprofiler-sip
%define version 4.12.1
%define release 1
%define tarname sip
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   sip
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   Python
URL:       http://www.riverbankcomputing.com/software/sip/intro
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python
BuildRequires:  cellprofiler-python gcc gcc-c++

%description
sip installed under /usr/cellprofiler

%package -n %{pkgname}-devel
Summary:   sip development files installed under /usr/cellprofiler
Group: Development/Libraries
Requires: %{pkgname} = %{version}

%description -n %{pkgname}-devel
sip development files installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

%{pref}/bin/python configure.py 
make


%install

make install DESTDIR=$RPM_BUILD_ROOT

%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/bin/sip
%{pref}/lib/python2.7/site-packages/sip.so
%{pref}/lib/python2.7/site-packages/sipconfig.py
%{pref}/lib/python2.7/site-packages/sipdistutils.py

%files -n %{pkgname}-devel
%defattr(-,root,root)
%{pref}/include/python2.7/sip.h
