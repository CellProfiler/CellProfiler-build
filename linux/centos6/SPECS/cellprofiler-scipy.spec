%define pkgname cellprofiler-scipy
%define version 0.13.2
%define release 1
%define tarname scipy
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   scipy
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   BSD and Boost and Public Domain
URL:       http://www.scipy.org
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-numpy = 1.9.0
BuildRequires: cellprofiler-numpy-devel = 1.9.0 cellprofiler-swig blas-devel lapack-devel atlas-devel gcc-c++

%description
scipy installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

env ATLAS=%{pref}/lib FFTW=%{pref}/lib BLAS=%{pref}/lib \
    LAPACK=%{pref}/lib CFLAGS="$RPM_OPT_FLAGS" \
    PATH=%{pref}/bin:$PATH \
    %{pref}/bin/python setup.py build --fcompiler=gfortran 


%install

#%{pref}/bin/python setup.py install --skip-build --root $RPM_BUILD_ROOT
env ATLAS=%{pref}/lib FFTW=%{pref}/lib BLAS=%{pref}/lib \
    LAPACK=%{pref}/lib CFLAGS="$RPM_OPT_FLAGS" \
    %{pref}/bin/python setup.py install --root $RPM_BUILD_ROOT


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/python2.7/site-packages/scipy
%{pref}/lib/python2.7/site-packages/scipy-0.13.2-py2.7.egg-info
