%define pkgname cellprofiler-python
%define version 2.7.2
%define release 1
%define tarname Python
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   python installed under /usr/cellprofiler
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.bz2
License:   Python
URL:       http://www.python.org/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-zlib cellprofiler-sqlite db4 openssl bzip2 gdbm ncurses readline
BuildRequires: gcc make   cellprofiler-zlib-devel cellprofiler-sqlite-devel db4-devel openssl-devel bzip2-devel gdbm-devel ncurses-devel readline-devel
Autoreq:   0

%description
python installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

./configure --prefix %{pref} --enable-shared \
--enable-unicode=ucs4 \
LDFLAGS="-L%{pref} -Wl,-rpath %{pref}/lib"

make


%install

make install DESTDIR=$RPM_BUILD_ROOT

# Fix the interpreter path in binaries installed by distutils 
# (which changes them by itself)
# Make sure we preserve the file permissions
for fixed in %{buildroot}%{_bindir}/pydoc; do
    sed 's,#!.*/python$,#!%{_bindir}/env python%{pybasever},' $fixed > $fixed- \
        && cat $fixed- > $fixed && rm -f $fixed-
done

%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/python2.7
%{pref}/lib/libpython2.7.so.1.0
%{pref}/lib/pkgconfig/python-2.7.pc
%doc %{pref}/share/man/man1/python2.7.1
%{pref}/bin/python2.7-config
%{pref}/bin/pydoc
%{pref}/bin/python2.7
%{pref}/bin/python
%{pref}/bin/2to3
%{pref}/bin/smtpd.py
%{pref}/bin/idle
%{pref}/bin/python-config
%{pref}/lib/libpython2.7.so
%{pref}/lib/pkgconfig/python.pc
%{pref}/include/python2.7


