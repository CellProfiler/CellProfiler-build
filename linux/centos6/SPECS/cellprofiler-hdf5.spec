%define pkgname cellprofiler-hdf5
%define version 1.8.10patch1
%define version_with_hyphen 1.8.10-patch1
%define release 1
%define tarname hdf5
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   hdf5
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version_with_hyphen}.tar.bz2
License:   BSD
URL:       http://www.hdfgroup.org/HDF5/release/obtainsrc.html
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Requires:  cellprofiler-zlib
Prefix:    %{pref}
BuildRequires: gcc-c++ gcc-gfortran make cellprofiler-zlib-devel

%description
hdf5 installed under /usr/cellprofiler

%package -n %{pkgname}-devel
Summary:   %{pkgname} development files installed under /usr/cellprofiler
Group: Development/Libraries
Requires: %{pkgname} = %{version}

%description -n %{pkgname}-devel
%{pkgname} development files installed under /usr/cellprofiler


%prep

%setup -q -n %{tarname}-%{version_with_hyphen}


%build

./configure \
 --prefix="%{pref}" \
 --with-pic \
 --enable-hl \
 --enable-cxx \
 --enable-fortran \
 --enable-production \
 --with-zlib="%{pref}"

make


%install

make prefix=$RPM_BUILD_ROOT%{pref} install

%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files -n %{pkgname}
%defattr(-,root,root)
%{pref}/bin/gif2h5
%{pref}/bin/h52gif
%{pref}/bin/h5c++
%{pref}/bin/h5cc
%{pref}/bin/h5copy
%{pref}/bin/h5debug
%{pref}/bin/h5diff
%{pref}/bin/h5dump
%{pref}/bin/h5fc
%{pref}/bin/h5import
%{pref}/bin/h5jam
%{pref}/bin/h5ls
%{pref}/bin/h5mkgrp
%{pref}/bin/h5perf_serial
%{pref}/bin/h5redeploy
%{pref}/bin/h5repack
%{pref}/bin/h5repart
%{pref}/bin/h5stat
%{pref}/bin/h5unjam
%{pref}/lib/libhdf5.so
%{pref}/lib/libhdf5.so.7
%{pref}/lib/libhdf5.so.7.0.4
%{pref}/lib/libhdf5_cpp.so
%{pref}/lib/libhdf5_cpp.so.7
%{pref}/lib/libhdf5_cpp.so.7.0.4
%{pref}/lib/libhdf5_fortran.so
%{pref}/lib/libhdf5_fortran.so.7
%{pref}/lib/libhdf5_fortran.so.7.0.4
%{pref}/lib/libhdf5_hl.so
%{pref}/lib/libhdf5_hl.so.7
%{pref}/lib/libhdf5_hl.so.7.0.4
%{pref}/lib/libhdf5_hl_cpp.so
%{pref}/lib/libhdf5_hl_cpp.so.7
%{pref}/lib/libhdf5_hl_cpp.so.7.0.4
%{pref}/lib/libhdf5hl_fortran.so
%{pref}/lib/libhdf5hl_fortran.so.7
%{pref}/lib/libhdf5hl_fortran.so.7.0.4

%files -n %{pkgname}-devel
%defattr(-,root,root)
%{pref}/include/H5ACpublic.h
%{pref}/include/H5AbstractDs.h
%{pref}/include/H5Apublic.h
%{pref}/include/H5ArrayType.h
%{pref}/include/H5AtomType.h
%{pref}/include/H5Attribute.h
%{pref}/include/H5Classes.h
%{pref}/include/H5CommonFG.h
%{pref}/include/H5CompType.h
%{pref}/include/H5Cpp.h
%{pref}/include/H5CppDoc.h
%{pref}/include/H5Cpublic.h
%{pref}/include/H5DSpublic.h
%{pref}/include/H5DataSet.h
%{pref}/include/H5DataSpace.h
%{pref}/include/H5DataType.h
%{pref}/include/H5DcreatProp.h
%{pref}/include/H5Dpublic.h
%{pref}/include/H5DxferProp.h
%{pref}/include/H5EnumType.h
%{pref}/include/H5Epubgen.h
%{pref}/include/H5Epublic.h
%{pref}/include/H5Exception.h
%{pref}/include/H5FDcore.h
%{pref}/include/H5FDdirect.h
%{pref}/include/H5FDfamily.h
%{pref}/include/H5FDlog.h
%{pref}/include/H5FDmpi.h
%{pref}/include/H5FDmpio.h
%{pref}/include/H5FDmpiposix.h
%{pref}/include/H5FDmulti.h
%{pref}/include/H5FDpublic.h
%{pref}/include/H5FDsec2.h
%{pref}/include/H5FDstdio.h
%{pref}/include/H5FaccProp.h
%{pref}/include/H5FcreatProp.h
%{pref}/include/H5File.h
%{pref}/include/H5FloatType.h
%{pref}/include/H5Fpublic.h
%{pref}/include/H5Gpublic.h
%{pref}/include/H5Group.h
%{pref}/include/H5IMpublic.h
%{pref}/include/H5IdComponent.h
%{pref}/include/H5Include.h
%{pref}/include/H5IntType.h
%{pref}/include/H5Ipublic.h
%{pref}/include/H5LTpublic.h
%{pref}/include/H5Library.h
%{pref}/include/H5Lpublic.h
%{pref}/include/H5MMpublic.h
%{pref}/include/H5Object.h
%{pref}/include/H5Opublic.h
%{pref}/include/H5PTpublic.h
%{pref}/include/H5PacketTable.h
%{pref}/include/H5Ppublic.h
%{pref}/include/H5PredType.h
%{pref}/include/H5PropList.h
%{pref}/include/H5Rpublic.h
%{pref}/include/H5Spublic.h
%{pref}/include/H5StrType.h
%{pref}/include/H5TBpublic.h
%{pref}/include/H5Tpublic.h
%{pref}/include/H5VarLenType.h
%{pref}/include/H5Zpublic.h
%{pref}/include/H5api_adpt.h
%{pref}/include/H5f90i.h
%{pref}/include/H5f90i_gen.h
%{pref}/include/H5overflow.h
%{pref}/include/H5pubconf.h
%{pref}/include/H5public.h
%{pref}/include/H5version.h
%{pref}/include/h5_dble_interface.mod
%{pref}/include/h5a.mod
%{pref}/include/h5a_provisional.mod
%{pref}/include/h5d.mod
%{pref}/include/h5d_provisional.mod
%{pref}/include/h5ds.mod
%{pref}/include/h5e.mod
%{pref}/include/h5e_provisional.mod
%{pref}/include/h5f.mod
%{pref}/include/h5fortran_types.mod
%{pref}/include/h5g.mod
%{pref}/include/h5global.mod
%{pref}/include/h5i.mod
%{pref}/include/h5im.mod
%{pref}/include/h5l.mod
%{pref}/include/h5l_provisional.mod
%{pref}/include/h5lib.mod
%{pref}/include/h5lib_provisional.mod
%{pref}/include/h5lt.mod
%{pref}/include/h5o.mod
%{pref}/include/h5o_provisional.mod
%{pref}/include/h5p.mod
%{pref}/include/h5p_provisional.mod
%{pref}/include/h5r.mod
%{pref}/include/h5r_provisional.mod
%{pref}/include/h5s.mod
%{pref}/include/h5t.mod
%{pref}/include/h5t_provisional.mod
%{pref}/include/h5tb.mod
%{pref}/include/h5z.mod
%{pref}/include/hdf5.h
%{pref}/include/hdf5.mod
%{pref}/include/hdf5_hl.h
%{pref}/lib/libhdf5.a
%{pref}/lib/libhdf5.la
%{pref}/lib/libhdf5.settings
%{pref}/lib/libhdf5_cpp.a
%{pref}/lib/libhdf5_cpp.la
%{pref}/lib/libhdf5_fortran.a
%{pref}/lib/libhdf5_fortran.la
%{pref}/lib/libhdf5_hl.a
%{pref}/lib/libhdf5_hl.la
%{pref}/lib/libhdf5_hl_cpp.a
%{pref}/lib/libhdf5_hl_cpp.la
%{pref}/lib/libhdf5hl_fortran.a
%{pref}/lib/libhdf5hl_fortran.la
%doc %{pref}/share/hdf5_examples/README
%doc %{pref}/share/hdf5_examples/c++/chunks.cpp
%doc %{pref}/share/hdf5_examples/c++/compound.cpp
%doc %{pref}/share/hdf5_examples/c++/create.cpp
%doc %{pref}/share/hdf5_examples/c++/extend_ds.cpp
%doc %{pref}/share/hdf5_examples/c++/h5group.cpp
%doc %{pref}/share/hdf5_examples/c++/readdata.cpp
%doc %{pref}/share/hdf5_examples/c++/run-c++-ex.sh
%doc %{pref}/share/hdf5_examples/c++/writedata.cpp
%doc %{pref}/share/hdf5_examples/c/h5_attribute.c
%doc %{pref}/share/hdf5_examples/c/h5_chunk_read.c
%doc %{pref}/share/hdf5_examples/c/h5_compound.c
%doc %{pref}/share/hdf5_examples/c/h5_drivers.c
%doc %{pref}/share/hdf5_examples/c/h5_elink_unix2win.c
%doc %{pref}/share/hdf5_examples/c/h5_extend_write.c
%doc %{pref}/share/hdf5_examples/c/h5_extlink.c
%doc %{pref}/share/hdf5_examples/c/h5_group.c
%doc %{pref}/share/hdf5_examples/c/h5_mount.c
%doc %{pref}/share/hdf5_examples/c/h5_read.c
%doc %{pref}/share/hdf5_examples/c/h5_ref2reg.c
%doc %{pref}/share/hdf5_examples/c/h5_reference.c
%doc %{pref}/share/hdf5_examples/c/h5_select.c
%doc %{pref}/share/hdf5_examples/c/h5_shared_mesg.c
%doc %{pref}/share/hdf5_examples/c/h5_write.c
%doc %{pref}/share/hdf5_examples/c/ph5example.c
%doc %{pref}/share/hdf5_examples/c/run-c-ex.sh
%doc %{pref}/share/hdf5_examples/fortran/attrexample.f90
%doc %{pref}/share/hdf5_examples/fortran/compound.f90
%doc %{pref}/share/hdf5_examples/fortran/dsetexample.f90
%doc %{pref}/share/hdf5_examples/fortran/fileexample.f90
%doc %{pref}/share/hdf5_examples/fortran/groupexample.f90
%doc %{pref}/share/hdf5_examples/fortran/grpdsetexample.f90
%doc %{pref}/share/hdf5_examples/fortran/grpit.f90
%doc %{pref}/share/hdf5_examples/fortran/grpsexample.f90
%doc %{pref}/share/hdf5_examples/fortran/hyperslab.f90
%doc %{pref}/share/hdf5_examples/fortran/mountexample.f90
%doc %{pref}/share/hdf5_examples/fortran/ph5example.f90
%doc %{pref}/share/hdf5_examples/fortran/refobjexample.f90
%doc %{pref}/share/hdf5_examples/fortran/refregexample.f90
%doc %{pref}/share/hdf5_examples/fortran/run-fortran-ex.sh
%doc %{pref}/share/hdf5_examples/fortran/rwdsetexample.f90
%doc %{pref}/share/hdf5_examples/fortran/selectele.f90
%doc %{pref}/share/hdf5_examples/hl/c++/ptExampleFL.cpp
%doc %{pref}/share/hdf5_examples/hl/c++/ptExampleVL.cpp
%doc %{pref}/share/hdf5_examples/hl/c++/run-hlc++-ex.sh
%doc %{pref}/share/hdf5_examples/hl/c/ex_ds1.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_image1.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_image2.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_lite1.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_lite2.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_lite3.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_table_01.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_table_02.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_table_03.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_table_04.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_table_05.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_table_06.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_table_07.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_table_08.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_table_09.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_table_10.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_table_11.c
%doc %{pref}/share/hdf5_examples/hl/c/ex_table_12.c
%doc %{pref}/share/hdf5_examples/hl/c/image24pixel.txt
%doc %{pref}/share/hdf5_examples/hl/c/image8.txt
%doc %{pref}/share/hdf5_examples/hl/c/pal_rgb.h
%doc %{pref}/share/hdf5_examples/hl/c/ptExampleFL.c
%doc %{pref}/share/hdf5_examples/hl/c/ptExampleVL.c
%doc %{pref}/share/hdf5_examples/hl/c/run-hlc-ex.sh
%doc %{pref}/share/hdf5_examples/hl/fortran/ex_ds1.f90
%doc %{pref}/share/hdf5_examples/hl/fortran/exlite.f90
%doc %{pref}/share/hdf5_examples/hl/fortran/run-hlfortran-ex.sh
%doc %{pref}/share/hdf5_examples/hl/run-hl-ex.sh
%doc %{pref}/share/hdf5_examples/run-all-ex.sh
