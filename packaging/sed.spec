#
# Please submit bugfixes or comments via http://bugs.tizen.org/
#

Name:           sed
Version:        4.1.5
Release:        1
License:        GPL-2.0+
Summary:        A GNU stream text editor
Url:            http://sed.sourceforge.net/
Group:          Applications/Text
Source0:        ftp://ftp.gnu.org/pub/gnu/sed/sed-%{version}.tar.gz

%description
The sed (Stream EDitor) editor is a stream or batch (non-interactive)
editor.  Sed takes text as input, performs an operation or set of
operations on the text and outputs the modified text.  The operations
that sed performs (substitutions, deletions, insertions, etc.) can be
specified in a script file or from the command line.

%prep
%setup -q


%build

%configure --disable-static \
    --without-included-regex \
    --bindir=%{_bindir} \
    --disable-nls

make %{?_smp_mflags}

%check
make check


%install
%make_install

%remove_docs


%files
%{_bindir}/sed


