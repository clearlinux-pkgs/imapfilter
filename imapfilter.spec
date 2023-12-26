#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: make
# autospec version: v3
# autospec commit: c1050fe
#
Name     : imapfilter
Version  : 2.8.2
Release  : 19
URL      : https://github.com/lefcha/imapfilter/archive/v2.8.2/imapfilter-2.8.2.tar.gz
Source0  : https://github.com/lefcha/imapfilter/archive/v2.8.2/imapfilter-2.8.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: imapfilter-bin = %{version}-%{release}
Requires: imapfilter-data = %{version}-%{release}
Requires: imapfilter-license = %{version}-%{release}
Requires: imapfilter-man = %{version}-%{release}
BuildRequires : lua-dev
BuildRequires : openssl-dev
BuildRequires : pcre2-dev
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}

%description
IMAPFilter
Description
IMAPFilter is a mail filtering utility. It connects to remote mail servers
using the Internet Message Access Protocol (IMAP), sends searching queries to
the server and processes mailboxes based on the results. It can be used to
delete, copy, move, flag, etc. messages residing in mailboxes at the same or
different mail servers. The 4rev1 and 4 versions of the IMAP protocol are
supported.

%package bin
Summary: bin components for the imapfilter package.
Group: Binaries
Requires: imapfilter-data = %{version}-%{release}
Requires: imapfilter-license = %{version}-%{release}

%description bin
bin components for the imapfilter package.


%package data
Summary: data components for the imapfilter package.
Group: Data

%description data
data components for the imapfilter package.


%package license
Summary: license components for the imapfilter package.
Group: Default

%description license
license components for the imapfilter package.


%package man
Summary: man components for the imapfilter package.
Group: Default

%description man
man components for the imapfilter package.


%prep
%setup -q -n imapfilter-2.8.2
cd %{_builddir}/imapfilter-2.8.2
pushd ..
cp -a imapfilter-2.8.2 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1703625751
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
make  %{?_smp_mflags}  PREFIX=/usr MYCFLAGS="$CFLAGS"

pushd ../buildavx2
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -m64 -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -m64 -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -m64 -march=x86-64-v3 "
make  %{?_smp_mflags}  PREFIX=/usr MYCFLAGS="$CFLAGS"
popd

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1703625751
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/imapfilter
cp %{_builddir}/imapfilter-%{version}/LICENSE %{buildroot}/usr/share/package-licenses/imapfilter/07789d5e69a7f4ad31a3c083eb36236f0717fcfd || :
pushd ../buildavx2/
%make_install_v3 PREFIX=/usr MANDIR=/usr/share/man
popd
%make_install PREFIX=/usr MANDIR=/usr/share/man
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/imapfilter
/usr/bin/imapfilter

%files data
%defattr(-,root,root,-)
/usr/share/imapfilter/account.lua
/usr/share/imapfilter/auxiliary.lua
/usr/share/imapfilter/common.lua
/usr/share/imapfilter/mailbox.lua
/usr/share/imapfilter/message.lua
/usr/share/imapfilter/options.lua
/usr/share/imapfilter/regex.lua
/usr/share/imapfilter/set.lua

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/imapfilter/07789d5e69a7f4ad31a3c083eb36236f0717fcfd

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/imapfilter.1
/usr/share/man/man5/imapfilter_config.5
