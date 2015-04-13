%define pkgname cellprofiler-h5py
%define version 2.2.0
%define release 2
%define pref /usr/cellprofiler
%define tarname h5py

Name:      %{pkgname}
Summary:   h5py installed under /usr/cellprofiler
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   ?
URL:       ?
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
Group:     ?
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-zlib cellprofiler-numpy = 1.9.0 cellprofiler-hdf5
BuildRequires: cellprofiler-numpy-devel = 1.9.0 gcc cellprofiler-hdf5-devel cellprofiler-cython

%description
h5py installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build


env CFLAGS="-I%{pref}/include" \
    %{pref}/bin/python setup.py build --hdf5=%{pref}


%install

%{pref}/bin/python setup.py install --root=$RPM_BUILD_ROOT

%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
   /usr/cellprofiler/lib/python2.7/site-packages/h5py-2.2.0-py2.7.egg-info
   /usr/cellprofiler/lib/python2.7/site-packages/h5py
