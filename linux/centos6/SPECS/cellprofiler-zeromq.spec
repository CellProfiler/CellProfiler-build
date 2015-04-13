%define tarname zeromq
%define pref /usr/cellprofiler
%define pkgname cellprofiler-zeromq

Name:           %{pkgname}
Version:        2.1.11
Release:        1
Summary:        Software library for fast, message-based applications

Group:          System Environment/Libraries
License:        LGPLv3+
URL:            http://www.zeromq.org
Source0:        %{tarname}-%{version}.tar.gz

BuildRequires:  glib2-devel
BuildRequires:  libuuid-devel
BuildRequires:  gcc make gcc-c++

BuildRoot: %{_tmppath}/%{pkgname}-buildroot


%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the ZeroMQ shared library.

%package devel
Summary:        Development files for %{name}
Group:          Development/Libraries
Requires: %{pkgname} = %{version}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.

%prep
%setup -q -n %{tarname}-%{version}

# Don't turn warnings into errors
sed -i "s/libzmq_werror=\"yes\"/libzmq_werror=\"no\"/g" \
    configure

%build
%configure --disable-static --prefix %{pref} CC="gcc" CPP="cpp"
make %{?_smp_mflags}

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot} INSTALL="install -p"

# remove *.la
rm %{buildroot}%{_libdir}/libzmq.la

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%doc AUTHORS ChangeLog COPYING COPYING.LESSER NEWS README
%{_libdir}/libzmq.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/libzmq.so
%{_libdir}/pkgconfig/libzmq.pc
%{_includedir}/zmq*
%{_mandir}/man3/zmq*
%{_mandir}/man7/zmq*
