%define pkgname cellprofiler-libtiff
%define version 3.9.4
%define release 1
%define tarname tiff
%define pref /usr/cellprofiler

Name:      %{pkgname}
Summary:   libtiff
Version:   %{version}
Release:   %{release}
Source0:   %{tarname}-%{version}.tar.gz
License:   libtiff
URL:       http://www.remotesensing.org/libtiff/
Packager:  Vebjorn Ljosa <ljosa@broad.mit.edu>
BuildRoot: %{_tmppath}/%{pkgname}-buildroot
Prefix:    %{pref}
Requires:  cellprofiler-zlib cellprofiler-libjpeg
BuildRequires: cellprofiler-zlib-devel cellprofiler-libjpeg-devel gcc gcc-c++

%description
libtiff installed under /usr/cellprofiler

%package -n %{pkgname}-devel
Summary:   libtiff development files installed under /usr/cellprofiler
Group: Development/Libraries
Requires: %{pkgname} = %{version}

%description -n %{pkgname}-devel
libtiff development files installed under /usr/cellprofiler


%prep

%setup -q -n tiff-%{version}


%build

./configure --prefix %{pref} \
--enable-cxx \
--with-zlib-include-dir="%{pref}/include" \
--with-zlib-lib-dir="%{pref}/lib" \
--with-jpeg-include-dir="%{pref}/include" \
--with-jpeg-lib-dir="%{pref}/lib" && \

make


%install

make prefix=$RPM_BUILD_ROOT%{pref} install

%clean

[ "$RPM_BUILD_ROOT" != "/" ] && rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root)
%{pref}/bin/fax2tiff
%{pref}/bin/bmp2tiff
%{pref}/bin/ppm2tiff
%{pref}/bin/tiffmedian
%{pref}/bin/pal2rgb
%{pref}/bin/tiffset
%{pref}/bin/tiffdump
%{pref}/bin/tiffdither
%{pref}/bin/tiffinfo
%{pref}/bin/fax2ps
%{pref}/bin/tiff2rgba
%{pref}/bin/tiff2ps
%{pref}/bin/tiff2bw
%{pref}/bin/tiffcrop
%{pref}/bin/ras2tiff
%{pref}/bin/tiff2pdf
%{pref}/bin/tiffcp
%{pref}/bin/gif2tiff
%{pref}/bin/thumbnail
%{pref}/bin/raw2tiff
%{pref}/bin/tiffsplit
%{pref}/bin/tiffcmp
%{pref}/bin/rgb2ycbcr
%{pref}/lib/libtiffxx.so.3.9.4
%{pref}/lib/libtiff.so.3.9.4
%{pref}/lib/libtiff.so
%{pref}/lib/libtiff.so.3
%{pref}/lib/libtiffxx.so
%{pref}/lib/libtiffxx.so.3

%files -n %{pkgname}-devel
%defattr(-,root,root)
%{pref}/lib/libtiffxx.la
%{pref}/lib/libtiff.la
%{pref}/lib/libtiff.a
%{pref}/lib/libtiffxx.a
%{pref}/include/tiffio.hxx
%{pref}/include/tiff.h
%{pref}/include/tiffio.h
%{pref}/include/tiffconf.h
%{pref}/include/tiffvers.h
%doc %{pref}/share/doc/tiff-3.9.4/README
%doc %{pref}/share/doc/tiff-3.9.4/html/support.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.8.2.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.7.0beta.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.4beta029.html
%doc %{pref}/share/doc/tiff-3.9.4/html/internals.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.4beta016.html
%doc %{pref}/share/doc/tiff-3.9.4/html/misc.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.5.7.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.5.2.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.7.0alpha.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.6.0.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.5.6-beta.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.4beta035.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.4beta024.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.4beta033.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.4beta031.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.5.3.html
%doc %{pref}/share/doc/tiff-3.9.4/html/bugs.html
%doc %{pref}/share/doc/tiff-3.9.4/html/contrib.html
%doc %{pref}/share/doc/tiff-3.9.4/html/document.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.4beta036.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.4beta018.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.6.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.7.2.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.8.0.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.7.0beta2.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.9.0beta.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.7.3.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.9.2.html
%doc %{pref}/share/doc/tiff-3.9.4/html/intro.html
%doc %{pref}/share/doc/tiff-3.9.4/html/images/cramps.gif
%doc %{pref}/share/doc/tiff-3.9.4/html/images/jim.gif
%doc %{pref}/share/doc/tiff-3.9.4/html/images/bali.jpg
%doc %{pref}/share/doc/tiff-3.9.4/html/images/jello.jpg
%doc %{pref}/share/doc/tiff-3.9.4/html/images/dave.gif
%doc %{pref}/share/doc/tiff-3.9.4/html/images/cover.jpg
%doc %{pref}/share/doc/tiff-3.9.4/html/images/oxford.gif
%doc %{pref}/share/doc/tiff-3.9.4/html/images/strike.gif
%doc %{pref}/share/doc/tiff-3.9.4/html/images/ring.gif
%doc %{pref}/share/doc/tiff-3.9.4/html/images/smallliz.jpg
%doc %{pref}/share/doc/tiff-3.9.4/html/images/cat.gif
%doc %{pref}/share/doc/tiff-3.9.4/html/images/quad.jpg
%doc %{pref}/share/doc/tiff-3.9.4/html/images/warning.gif
%doc %{pref}/share/doc/tiff-3.9.4/html/images/back.gif
%doc %{pref}/share/doc/tiff-3.9.4/html/images/info.gif
%doc %{pref}/share/doc/tiff-3.9.4/html/images/note.gif
%doc %{pref}/share/doc/tiff-3.9.4/html/libtiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFbuffer.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFDataWidth.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFOpen.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFWriteDirectory.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/sgi2tiff.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFReadEncodedStrip.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFReadRGBATile.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFReadRGBAImage.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFRGBAImage.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/gif2tiff.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/fax2tiff.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiffcrop.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/ras2tiff.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFSetDirectory.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/pal2rgb.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFError.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/libtiff.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiffmedian.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFWriteEncodedStrip.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFReadEncodedTile.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFWriteScanline.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFReadRawTile.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFsize.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiffdither.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFquery.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFFlush.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFReadDirectory.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiff2rgba.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/fax2ps.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFReadScanline.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiffgt.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFGetField.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiffcmp.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFWarning.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFmemory.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFswab.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/raw2tiff.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiffsplit.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/rgb2ycbcr.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFWriteEncodedTile.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiff2bw.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiffset.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFReadTile.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFcolor.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiffcp.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFtile.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiff2pdf.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFReadRGBAStrip.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFcodec.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFReadRawStrip.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFstrip.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFWriteRawStrip.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiffsv.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiff2ps.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/index.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFPrintDirectory.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/thumbnail.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiffdump.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFClose.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/tiffinfo.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFWriteRawTile.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFWriteTile.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/ppm2tiff.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/man/TIFFSetField.3tiff.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.5.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.7.0.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.4beta028.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.7.4.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.4beta034.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.5.5.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.4beta007.html
%doc %{pref}/share/doc/tiff-3.9.4/html/images.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.5.4.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.8.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/index.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.7.1.html
%doc %{pref}/share/doc/tiff-3.9.4/html/addingtags.html
%doc %{pref}/share/doc/tiff-3.9.4/html/TIFFTechNote2.html
%doc %{pref}/share/doc/tiff-3.9.4/html/build.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.4beta032.html
%doc %{pref}/share/doc/tiff-3.9.4/html/tools.html
%doc %{pref}/share/doc/tiff-3.9.4/html/v3.9.1.html
%doc %{pref}/share/doc/tiff-3.9.4/README.vms
%doc %{pref}/share/doc/tiff-3.9.4/RELEASE-DATE
%doc %{pref}/share/doc/tiff-3.9.4/COPYRIGHT
%doc %{pref}/share/doc/tiff-3.9.4/ChangeLog
%doc %{pref}/share/doc/tiff-3.9.4/VERSION
%doc %{pref}/share/doc/tiff-3.9.4/TODO
%doc %{pref}/share/man/man1/tiffcrop.1
%doc %{pref}/share/man/man1/tiff2pdf.1
%doc %{pref}/share/man/man1/sgi2tiff.1
%doc %{pref}/share/man/man1/bmp2tiff.1
%doc %{pref}/share/man/man1/ppm2tiff.1
%doc %{pref}/share/man/man1/rgb2ycbcr.1
%doc %{pref}/share/man/man1/tiffdither.1
%doc %{pref}/share/man/man1/gif2tiff.1
%doc %{pref}/share/man/man1/tiffset.1
%doc %{pref}/share/man/man1/tiffgt.1
%doc %{pref}/share/man/man1/tiff2bw.1
%doc %{pref}/share/man/man1/fax2tiff.1
%doc %{pref}/share/man/man1/tiffinfo.1
%doc %{pref}/share/man/man1/ras2tiff.1
%doc %{pref}/share/man/man1/pal2rgb.1
%doc %{pref}/share/man/man1/thumbnail.1
%doc %{pref}/share/man/man1/tiffsv.1
%doc %{pref}/share/man/man1/tiffcmp.1
%doc %{pref}/share/man/man1/tiff2rgba.1
%doc %{pref}/share/man/man1/tiffmedian.1
%doc %{pref}/share/man/man1/raw2tiff.1
%doc %{pref}/share/man/man1/tiffsplit.1
%doc %{pref}/share/man/man1/tiffdump.1
%doc %{pref}/share/man/man1/tiff2ps.1
%doc %{pref}/share/man/man1/fax2ps.1
%doc %{pref}/share/man/man1/tiffcp.1
%doc %{pref}/share/man/man3/TIFFsize.3tiff
%doc %{pref}/share/man/man3/TIFFGetField.3tiff
%doc %{pref}/share/man/man3/libtiff.3tiff
%doc %{pref}/share/man/man3/TIFFOpen.3tiff
%doc %{pref}/share/man/man3/TIFFReadRGBAStrip.3tiff
%doc %{pref}/share/man/man3/TIFFWriteDirectory.3tiff
%doc %{pref}/share/man/man3/TIFFquery.3tiff
%doc %{pref}/share/man/man3/TIFFstrip.3tiff
%doc %{pref}/share/man/man3/TIFFWriteRawTile.3tiff
%doc %{pref}/share/man/man3/TIFFReadEncodedStrip.3tiff
%doc %{pref}/share/man/man3/TIFFtile.3tiff
%doc %{pref}/share/man/man3/TIFFError.3tiff
%doc %{pref}/share/man/man3/TIFFReadEncodedTile.3tiff
%doc %{pref}/share/man/man3/TIFFReadScanline.3tiff
%doc %{pref}/share/man/man3/TIFFSetDirectory.3tiff
%doc %{pref}/share/man/man3/TIFFFlush.3tiff
%doc %{pref}/share/man/man3/TIFFReadRGBAImage.3tiff
%doc %{pref}/share/man/man3/TIFFRGBAImage.3tiff
%doc %{pref}/share/man/man3/TIFFPrintDirectory.3tiff
%doc %{pref}/share/man/man3/TIFFcolor.3tiff
%doc %{pref}/share/man/man3/TIFFSetField.3tiff
%doc %{pref}/share/man/man3/TIFFClose.3tiff
%doc %{pref}/share/man/man3/TIFFswab.3tiff
%doc %{pref}/share/man/man3/TIFFReadTile.3tiff
%doc %{pref}/share/man/man3/TIFFWriteEncodedTile.3tiff
%doc %{pref}/share/man/man3/TIFFWarning.3tiff
%doc %{pref}/share/man/man3/TIFFDataWidth.3tiff
%doc %{pref}/share/man/man3/TIFFmemory.3tiff
%doc %{pref}/share/man/man3/TIFFcodec.3tiff
%doc %{pref}/share/man/man3/TIFFWriteScanline.3tiff
%doc %{pref}/share/man/man3/TIFFReadDirectory.3tiff
%doc %{pref}/share/man/man3/TIFFWriteEncodedStrip.3tiff
%doc %{pref}/share/man/man3/TIFFReadRawStrip.3tiff
%doc %{pref}/share/man/man3/TIFFReadRawTile.3tiff
%doc %{pref}/share/man/man3/TIFFReadRGBATile.3tiff
%doc %{pref}/share/man/man3/TIFFWriteTile.3tiff
%doc %{pref}/share/man/man3/TIFFbuffer.3tiff
%doc %{pref}/share/man/man3/TIFFWriteRawStrip.3tiff
