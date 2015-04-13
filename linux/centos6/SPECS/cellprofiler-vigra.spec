%define pkgname cellprofiler-vigra
%define pyversion 2.7
%define version 1.7.1
%define release 2
%define tarname vigra
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   vigra
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}-src.tar.gz
License:   MIT
URL:       http://hci.iwr.uni-heidelberg.de/vigra/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python cellprofiler-numpy = 1.9.0 fftw cellprofiler-hdf5 cellprofiler-libpng cellprofiler-libtiff cellprofiler-libjpeg boost-python
BuildRequires: cellprofiler-python cellprofiler-numpy-devel = 1.9.0 fftw-devel cellprofiler-hdf5-devel cellprofiler-libpng-devel cellprofiler-libtiff-devel cellprofiler-libjpeg-devel boost-python-devel cmake gcc gcc-c++

%description
vigra installed under /usr/cellprofiler

%package -n %{pkgname}-devel
Summary:   vigra development files installed under /usr/cellprofiler
Group: Development/Libraries
Requires: %{pkgname} = %{version}

%description -n %{pkgname}-devel
vigra development files installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

cmake \
 -DCMAKE_INSTALL_PREFIX="%{pref}" \
 -DPYTHON_EXECUTABLE="%{pref}/bin/python" \
 -DPYTHON_LIBRARY="%{pref}/lib/libpython%{pyversion}.so" \
 -DCMAKE_PREFIX_PATH="%{pref}" \
 -DDEPENDENCY_SEARCH_PREFIX="%{pref};/usr/lib64" && \

make


%install

make install DESTDIR=$RPM_BUILD_ROOT


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/libvigraimpex.so
%{pref}/lib/libvigraimpex.so.3
%{pref}/lib/libvigraimpex.so.3.171
%{pref}/lib/python2.7/site-packages/vigra

%files -n %{pkgname}-devel
%defattr(-,root,root)
%{pref}/bin/vigra-config
%doc %{pref}/doc/vigra
%doc %{pref}/doc/vigranumpy
%{pref}/include/vigra
%{pref}/lib/vigra


