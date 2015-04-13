%define pkgname cellprofiler-scikit-learn
%define version 0.15.2
%define release 2
%define tarname scikit-learn
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   scikit-learn
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   BSD
URL:       http://scikit-learn.org
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-numpy = 1.9.0 cellprofiler-scipy
BuildRequires: cellprofiler-numpy-devel = 1.9.0 gcc-c++

%description
scikit-learn installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version}


%build

env CFLAGS="$RPM_OPT_FLAGS" \
    PATH=%{pref}/bin:$PATH \
    %{pref}/bin/python setup.py build


%install

#%{pref}/bin/python setup.py install --skip-build --root $RPM_BUILD_ROOT
env CFLAGS="$RPM_OPT_FLAGS" \
    %{pref}/bin/python setup.py install --root $RPM_BUILD_ROOT


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/lib/python2.7/site-packages/sklearn
%{pref}/lib/python2.7/site-packages/scikit_learn-%{version}-py2.7.egg-info
