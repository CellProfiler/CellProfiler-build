%define pkgname cellprofiler-cellh5
%define version 1.2.0
%define release 3
%define tarname cellh5
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   cellh5
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   BSD
URL:       http://github.com/CellH5/cellh5
Packager:  Lee Kamentsky <leek@broadinstitute.org>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-h5py cellprofiler-pandas cellprofiler-matplotlib
Requires:  cellprofiler-scikit-learn cellprofiler-lxml
BuildRequires: cellprofiler-numpy-devel = 1.9.0 gcc-c++ cellprofiler-pandas
BuildRequires: cellprofiler-h5py cellprofiler-matplotlib
BuildRequires: cellprofiler-scikit-learn cellprofiler-lxml

%description
cellh5 installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

env CFLAGS="$RPM_OPT_FLAGS" \
    PATH=%{pref}/bin:$PATH \
    %{pref}/bin/python setup.py build


%install

env CFLAGS="$RPM_OPT_FLAGS" \
    %{pref}/bin/python setup.py install --root $RPM_BUILD_ROOT


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/python2.7/site-packages/cellh5.py
%{pref}/lib/python2.7/site-packages/cellh5.pyc
%{pref}/lib/python2.7/site-packages/cellh5write.py
%{pref}/lib/python2.7/site-packages/cellh5write.pyc
%{pref}/lib/python2.7/site-packages/hmm_wrapper
%{pref}/lib/python2.7/site-packages/cellh5-%{version}-py2.7.egg-info
