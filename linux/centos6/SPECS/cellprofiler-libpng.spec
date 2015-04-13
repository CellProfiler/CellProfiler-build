%define pkgname cellprofiler-libpng
%define version 1.4.5
%define release 1
%define tarname libpng
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   libpng
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.bz2
License:   zlib
URL:       http://www.libpng.org/pub/png/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires: cellprofiler-zlib
BuildRequires: cellprofiler-zlib cellprofiler-zlib-devel gcc

%description
libpng installed under /usr/cellprofiler

%package -n %{pkgname}-devel
Summary:   libpng development files installed under /usr/cellprofiler
Group: Development/Libraries
Requires: %{pkgname} = %{version}

%description -n %{pkgname}-devel
libpng development files installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

./configure --prefix %{pref} LDFLAGS="-L%{pref}/lib" CFLAGS="-I%{pref}/include"
make CFLAGS=-I/usr/cellprofiler/include


%install

make prefix=$RPM_BUILD_ROOT%{pref} install

%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/libpng14.so
%{pref}/lib/libpng14.so.14
%{pref}/lib/libpng14.so.14.5.0
%doc %{pref}/share/man/man5/png.5
%{pref}/lib/libpng.so

%files -n %{pkgname}-devel
%defattr(-,root,root)
%{pref}/bin/libpng-config
%{pref}/bin/libpng14-config
%{pref}/include/libpng14/png.h
%{pref}/include/libpng14/pngconf.h
%{pref}/include/png.h
%{pref}/include/pngconf.h
%{pref}/lib/libpng.a
%{pref}/lib/libpng.la
%{pref}/lib/libpng14.a
%{pref}/lib/libpng14.la
%{pref}/lib/pkgconfig/libpng.pc
%{pref}/lib/pkgconfig/libpng14.pc
%doc %{pref}/share/man/man3/libpng.3
%doc %{pref}/share/man/man3/libpngpf.3

