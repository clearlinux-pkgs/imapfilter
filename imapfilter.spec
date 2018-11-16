#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : imapfilter
Version  : 2.6.12
Release  : 4
URL      : https://github.com/lefcha/imapfilter/archive/v2.6.12.tar.gz
Source0  : https://github.com/lefcha/imapfilter/archive/v2.6.12.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
Requires: imapfilter-bin
Requires: imapfilter-license
Requires: imapfilter-data
Requires: imapfilter-man
BuildRequires : lua-dev
BuildRequires : openssl-dev
BuildRequires : pcre-dev
Patch1: 0001-fix-path-and-compiler-flags.patch

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
Requires: imapfilter-man = %{version}-%{release}

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
%setup -q -n imapfilter-2.6.12
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1538588451
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1538588451
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/doc/imapfilter
cp LICENSE %{buildroot}/usr/share/doc/imapfilter/LICENSE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
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
/usr/share/doc/imapfilter/LICENSE

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/imapfilter.1
/usr/share/man/man5/imapfilter_config.5
