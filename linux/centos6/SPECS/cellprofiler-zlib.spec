%define pkgname cellprofiler-zlib
%define version 1.2.5
%define release 1
%define tarname zlib
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   zlib installed under /usr/cellprofiler
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.bz2
License:   zlib and Boost
URL:       http://www.gzip.org/zlib/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
Group:     Development/Python
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
BuildRequires: make gcc

%description
zlib installed under /usr/cellprofiler

%package -n %{pkgname}-devel
Summary:   zlib development files installed under /usr/cellprofiler
Group: Development/Libraries
Requires: %{pkgname} = %{version}

%description -n %{pkgname}-devel
zlib development files installed under /usr/cellprofiler

%prep

%setup -q -n %{tarname}-%{version}


%build

./configure --prefix %{pref}
make


%install

make prefix=$RPM_BUILD_ROOT%{pref} install

%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/libz.so
%{pref}/lib/libz.so.1
%{pref}/lib/libz.so.1.2.5

%files -n %{pkgname}-devel
%defattr(-,root,root)
%{pref}/include/zconf.h
%{pref}/include/zlib.h
%{pref}/lib/libz.a
%{pref}/lib/pkgconfig/zlib.pc
%doc %{pref}/share/man/man3/zlib.3
