Name:           sed
Version:        4.2.1
Release:        0
Summary:        A Stream-Oriented Non-Interactive Text Editor
License:        GPL-3.0+
Group:          System/Base
Url:            http://www.gnu.org/directory/sed.html
Source:         %name-%version.tar.bz2
PreReq:         %install_info_prereq
Provides:       base:/bin/sed
BuildRequires:  automake

%description
Sed takes text input, performs one or more operations on it, and
outputs the modified text. Sed is typically used for extracting parts
of a file using pattern matching or  for substituting multiple
occurrences of a string within a file.

%prep
%setup -q

%build
%define warn_flags -Wall -Wstrict-prototypes -Wpointer-arith -Wformat-security
export CFLAGS="%{optflags} %warn_flags"
./configure	--prefix=/usr \
		--mandir=%{_mandir} \
		--infodir=%{_infodir} \
		--disable-nls \
		--without-included-regex \
		%{_target_cpu}-suse-linux
%if %do_profiling
  make %{?_smp_mflags} CFLAGS="$CFLAGS "%cflags_profile_generate
  make %{?_smp_mflags} check
  make clean
  make %{?_smp_mflags} CFLAGS="$CFLAGS "%cflags_profile_feedback
%else
  make %{?_smp_mflags}
%endif
make %{?_smp_mflags} check

%install
%make_install


%docs_package

%files 
%defattr(-, root, root)
%{_bindir}/sed
%doc COPYING*

