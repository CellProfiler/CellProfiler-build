%define pkgname cellprofiler-jdk
%define pyversion 2.7
%define version 7u21
%define release 1
%define tarname jdk
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   jdk installed under /usr/cellprofiler
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}-linux-x64.tar.gz
License:   Oracle Binary Code License Agreement
URL:       http://www.oracle.com/technetwork/java/javase/jdk-7-readme-429198.html
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
#Requires:  cellprofiler-python
#BuildRequires: cellprofiler-python gcc

%description
jdk installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}1.7.0_21


%build

rm src.zip


%install

mkdir -p $RPM_BUILD_ROOT/%{pref}
cp -a . $RPM_BUILD_ROOT/%{pref}/jdk

%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/jdk
