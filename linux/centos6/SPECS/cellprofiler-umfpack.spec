%define pkgname cellprofiler-umfpack
%define version 5.5.1
%define release 1
%define tarname UMFPACK
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   umfpack
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
Source1:   CAMD-2.2.2.tar.gz
Source2:   CCOLAMD-2.7.3.tar.gz
Source3:   COLAMD-2.7.3.tar.gz
Source4:   CHOLMOD-1.7.2.tar.gz
Source5:   UFconfig-3.6.0.tar.gz
Source6:   AMD-2.2.2.tar.gz
License:   GPL
URL:       http://www.cise.ufl.edu/research/sparse/umfpack/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Requires:  lapack atlas blas
BuildRequires: lapack-devel atlas-devel blas-devel 
Prefix:    %{pref}

%description
umfpack installed under /usr/cellprofiler

%package -n %{pkgname}-devel
Summary:   umfpack development files installed under /usr/cellprofiler
Group: Development/Libraries
Requires: %{pkgname} = %{version}

%description -n %{pkgname}-devel
umfpack development files installed under /usr/cellprofiler


%prep

%setup -q -T -b 0 -c
%setup -q -T -D -a 1
%setup -q -T -D -a 2
%setup -q -T -D -a 3
%setup -q -T -D -a 4
%setup -q -T -D -a 5
%setup -q -T -D -a 6

%build

%define atlasprefix /usr/lib64/atlas
perl -pi -e 's@(^CHOLMOD_CONFIG )=.*@$1= -DNPARTITION@g' UFconfig/UFconfig.mk && \
perl -pi -e 's@(^CC )=.*@$1= gcc@g' UFconfig/UFconfig.mk && \
perl -pi -e 's@(^CFLAGS .*)@$1 -m64 -fPIC@g' UFconfig/UFconfig.mk && \
perl -pi -e 's@(^F77 )=.*@$1= gfortran@g' UFconfig/UFconfig.mk && \
perl -pi -e 's@(^F77FLAGS .*)@$1 -m64 -fPIC@g' UFconfig/UFconfig.mk && \
perl -pi -e 's@(^BLAS )=.*@$1= -L%{atlasprefix} -llapack -lblas -latlas -lgfortran@g' UFconfig/UFconfig.mk && \
perl -pi -e 's@(^LAPACK )=.*@$1= -L%{atlasprefix} -llapack -lblas -latlas -lgfortran@g' UFconfig/UFconfig.mk && \
perl -pi -e 's@(^METIS_PATH )=.*@$1= @g' UFconfig/UFconfig.mk && \
perl -pi -e 's@(^METIS )=.*@$1= @g' UFconfig/UFconfig.mk && \
perl -pi -e 's@(^INSTALL_LIB )=.*@$1= %{buildroot}%{pref}/lib@g' UFconfig/UFconfig.mk && \
perl -pi -e 's@(^INSTALL_INCLUDE )=.*@$1= %{buildroot}%{pref}/include@g' UFconfig/UFconfig.mk && \
cd %{tarname}
make


%install

cd %{tarname}
mkdir -p $RPM_BUILD_ROOT%{pref}/lib
mkdir -p $RPM_BUILD_ROOT%{pref}/include
make prefix=$RPM_BUILD_ROOT%{pref} install
cp -p "../AMD/Include/amd.h" "$RPM_BUILD_ROOT%{pref}/include/"
cp -p "../UFconfig/UFconfig.h" "$RPM_BUILD_ROOT%{pref}/include/"


%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)

%files -n %{pkgname}-devel
%defattr(-,root,root)
%{pref}/include/UFconfig.h
%{pref}/include/amd.h
%{pref}/include/umfpack.h
%{pref}/include/umfpack_col_to_triplet.h
%{pref}/include/umfpack_defaults.h
%{pref}/include/umfpack_free_numeric.h
%{pref}/include/umfpack_free_symbolic.h
%{pref}/include/umfpack_get_determinant.h
%{pref}/include/umfpack_get_lunz.h
%{pref}/include/umfpack_get_numeric.h
%{pref}/include/umfpack_get_symbolic.h
%{pref}/include/umfpack_global.h
%{pref}/include/umfpack_load_numeric.h
%{pref}/include/umfpack_load_symbolic.h
%{pref}/include/umfpack_numeric.h
%{pref}/include/umfpack_qsymbolic.h
%{pref}/include/umfpack_report_control.h
%{pref}/include/umfpack_report_info.h
%{pref}/include/umfpack_report_matrix.h
%{pref}/include/umfpack_report_numeric.h
%{pref}/include/umfpack_report_perm.h
%{pref}/include/umfpack_report_status.h
%{pref}/include/umfpack_report_symbolic.h
%{pref}/include/umfpack_report_triplet.h
%{pref}/include/umfpack_report_vector.h
%{pref}/include/umfpack_save_numeric.h
%{pref}/include/umfpack_save_symbolic.h
%{pref}/include/umfpack_scale.h
%{pref}/include/umfpack_solve.h
%{pref}/include/umfpack_symbolic.h
%{pref}/include/umfpack_tictoc.h
%{pref}/include/umfpack_timer.h
%{pref}/include/umfpack_transpose.h
%{pref}/include/umfpack_triplet_to_col.h
%{pref}/include/umfpack_wsolve.h
%{pref}/lib/libumfpack.5.5.1.a
%{pref}/lib/libumfpack.a
