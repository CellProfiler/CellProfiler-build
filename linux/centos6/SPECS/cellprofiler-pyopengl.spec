%define pkgname cellprofiler-pyopengl
%define version 3.0.1
%define release 3
%define tarname PyOpenGL
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   pyopengl
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
Patch0:    %{tarname}-numeric.diff
License:   BSD
URL:       http://pyopengl.sourceforge.net/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python mesa-libGL cellprofiler-numpy = 1.9.0
BuildRequires: cellprofiler-numpy-devel = 1.9.0

%description
pyopengl installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}
%patch0

%build

%{pref}/bin/python setup.py build


%install

%{pref}/bin/python setup.py install --root=$RPM_BUILD_ROOT


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/python2.7/site-packages/OpenGL
%{pref}/lib/python2.7/site-packages/PyOpenGL-3.0.1-py2.7.egg-info

