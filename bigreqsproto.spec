#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : bigreqsproto
Version  : 1.1.2
Release  : 11
URL      : http://xorg.freedesktop.org/archive/individual/proto/bigreqsproto-1.1.2.tar.bz2
Source0  : http://xorg.freedesktop.org/archive/individual/proto/bigreqsproto-1.1.2.tar.bz2
Summary  : BigReqs extension headers
Group    : Development/Tools
License  : MIT-Opengroup
Requires: bigreqsproto-doc
BuildRequires : gcc-dev32
BuildRequires : gcc-libgcc32
BuildRequires : gcc-libstdc++32
BuildRequires : glibc-dev32
BuildRequires : glibc-libc32
BuildRequires : libxslt-bin
BuildRequires : pkgconfig(32xorg-macros)
BuildRequires : pkgconfig(xorg-macros)
BuildRequires : xmlto

%description
Big Requests Extension
This extension defines a protocol to enable the use of requests
that exceed 262140 bytes in length.

%package dev
Summary: dev components for the bigreqsproto package.
Group: Development
Provides: bigreqsproto-devel

%description dev
dev components for the bigreqsproto package.


%package dev32
Summary: dev32 components for the bigreqsproto package.
Group: Default

%description dev32
dev32 components for the bigreqsproto package.


%package doc
Summary: doc components for the bigreqsproto package.
Group: Documentation

%description doc
doc components for the bigreqsproto package.


%prep
%setup -q -n bigreqsproto-1.1.2
pushd ..
cp -a bigreqsproto-1.1.2 build32
popd

%build
export LANG=C
%configure --disable-static
make V=1  %{?_smp_mflags}

pushd ../build32
export CFLAGS="$CFLAGS -m32"
export CXXFLAGS="$CXXFLAGS -m32"
%configure --disable-static  --libdir=/usr/lib32
make V=1  %{?_smp_mflags}
popd
%check
export LANG=C
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
pushd ../build32
%make_install32
if [ -d  %{buildroot}/usr/lib32/pkgconfig ]
then
pushd %{buildroot}/usr/lib32/pkgconfig
for i in *.pc ; do mv $i 32$i ; done
popd
fi
popd
%make_install

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/include/X11/extensions/bigreqsproto.h
/usr/include/X11/extensions/bigreqstr.h
/usr/lib64/pkgconfig/bigreqsproto.pc

%files dev32
%defattr(-,root,root,-)
/usr/lib32/pkgconfig/32bigreqsproto.pc

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/bigreqsproto/*
