%define pkgname cellprofiler-pyopengl-accelerate
%define version 3.0.1
%define release 1
%define tarname PyOpenGL-accelerate
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   PyOpenGL-accelerate installed under /usr/cellprofiler
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   BSD
URL:       http://pyopengl.sourceforge.net/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python
BuildRequires:  cellprofiler-python gcc

%description
PyOpenGL-accelerate installed under /usr/cellprofiler


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
%{pref}/lib/python2.7/site-packages/OpenGL_accelerate
%{pref}/lib/python2.7/site-packages/PyOpenGL_accelerate-3.0.1-py2.7.egg-info
