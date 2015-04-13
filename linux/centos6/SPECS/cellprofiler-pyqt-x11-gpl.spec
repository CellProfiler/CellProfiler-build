%define pkgname cellprofiler-pyqt-x11-gpl
%define version 4.8.3
%define release 2
%define tarname PyQt-x11-gpl
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   pyqt installed under /usr/cellprofiler
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   GPLv3 or GPLv2 with exceptions
URL:       http://www.riverbankcomputing.com/software/pyqt/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-numpy = 1.9.0 cellprofiler-pyopengl-accelerate cellprofiler-pyopengl cellprofiler-sip qt4
BuildRequires: qt4-devel cellprofiler-sip-devel make gcc-c++   cellprofiler-numpy = 1.9.0 cellprofiler-pyopengl-accelerate cellprofiler-pyopengl 

%description
pyqt installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

%{pref}/bin/python configure.py --confirm-license -g -q /usr/bin/qmake-qt4
make


%install

make install DESTDIR=$RPM_BUILD_ROOT

%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/share/sip/PyQt4
%{pref}/bin/pyrcc4
%{pref}/bin/pylupdate4
%{pref}/bin/pyuic4
%{pref}/lib/python2.7/site-packages/PyQt4
