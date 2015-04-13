%define pkgname cellprofiler-sqlite
%define version autoconf3070500
%define release 1
%define tarname_with_version sqlite-autoconf-3070500
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   sqlite installed under /usr/cellprofiler
Version:   %{version}
Release:   %{release}
Source0:   %{tarname_with_version}.tar.gz
License:   Public Domain
URL:       http://www.sqlite.org/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-zlib
BuildRequires: gcc make

%description
sqlite installed under /usr/cellprofiler


%package -n %{pkgname}-devel
Summary:   sqlite development files installed under /usr/cellprofiler
Group: Development/Libraries
Requires: %{pkgname} = %{version}

%description -n %{pkgname}-devel
sqlite development files installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname_with_version}


%build

./configure --prefix %{pref} LDFLAGS="-L%{pref}/lib"
make


%install

make prefix=$RPM_BUILD_ROOT%{pref} install

%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/bin/sqlite3
%{pref}/lib/libsqlite3.so
%{pref}/lib/libsqlite3.so.0
%{pref}/lib/libsqlite3.so.0.8.6
%doc %{pref}/share/man/man1/sqlite3.1

%files -n %{pkgname}-devel
%defattr(-,root,root)
%{pref}/include/sqlite3.h
%{pref}/include/sqlite3ext.h
%{pref}/lib/libsqlite3.a
%{pref}/lib/libsqlite3.la
%{pref}/lib/pkgconfig/sqlite3.pc

