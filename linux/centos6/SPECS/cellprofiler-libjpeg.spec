%define pkgname cellprofiler-libjpeg
%define version 8b
%define release 1
%define tarname jpegsrc
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   libjpeg
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}.v%{version}.tar.gz
License:   ?
URL:       ?
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
BuildRequires: gcc make

%description
libjpeg installed under /usr/cellprofiler

%package -n %{pkgname}-devel
Summary:   libjpeg development files installed under /usr/cellprofiler
Group: Development/Libraries
Requires: %{pkgname} = %{version}

%description -n %{pkgname}-devel
libjpeg development files installed under /usr/cellprofiler


%prep

%setup -q -n jpeg-%{version}


%build

./configure --prefix %{pref} CC="gcc" CPP="cpp"
make


%install

make prefix=$RPM_BUILD_ROOT%{pref} install

%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/bin/cjpeg
%{pref}/bin/djpeg
%{pref}/bin/jpegtran
%{pref}/bin/rdjpgcom
%{pref}/bin/wrjpgcom
%{pref}/lib/libjpeg.so
%{pref}/lib/libjpeg.so.8
%{pref}/lib/libjpeg.so.8.0.2
%doc %{pref}/share/man/man1/cjpeg.1
%doc %{pref}/share/man/man1/djpeg.1
%doc %{pref}/share/man/man1/jpegtran.1
%doc %{pref}/share/man/man1/rdjpgcom.1
%doc %{pref}/share/man/man1/wrjpgcom.1

%files -n %{pkgname}-devel
%defattr(-,root,root)
%{pref}/include/jconfig.h
%{pref}/include/jerror.h
%{pref}/include/jmorecfg.h
%{pref}/include/jpeglib.h
%{pref}/lib/libjpeg.a
%{pref}/lib/libjpeg.la
