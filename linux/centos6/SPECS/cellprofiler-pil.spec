%define pkgname cellprofiler-pil
%define pyversion 2.7
%define version 1.1.7
%define release 2
%define tarname Imaging
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   pil installed under /usr/cellprofiler
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   Python
URL:       http://www.pythonware.com/products/pil/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-python cellprofiler-libpng cellprofiler-libjpeg cellprofiler-libtiff
BuildRequires: gcc   cellprofiler-python cellprofiler-libpng-devel cellprofiler-libjpeg-devel cellprofiler-libtiff-devel cellprofiler-zlib-devel

%description
pil installed under /usr/cellprofiler


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
%{pref}/lib/python2.7/site-packages/PIL
%{pref}/bin/pilconvert.py
%{pref}/bin/pildriver.py
%{pref}/bin/pilfile.py
%{pref}/bin/pilfont.py
%{pref}/bin/pilprint.py
%{pref}/lib/python2.7/site-packages/PIL.pth
