%include	/usr/lib/rpm/macros.perl
Summary:	LTP GCOV extension code coverage tool
Summary(pl.UTF-8):	Frontend do GCOV
Name:		lcov
Version:	1.10
Release:	1
License:	GPL
Group:		Applications
Source0:	http://downloads.sourceforge.net/ltp/%{name}-%{version}.tar.gz
# Source0-md5:	b9fe33b921016fc68852c8a6beb3a3b5
URL:		http://ltp.sourceforge.net/coverage/lcov.php
BuildRequires:	rpm-perlprov >= 4.1-13
# /usr/bin/gcov is provided by gcc package
Requires:	gcc
Requires:	perl-GD
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LCOV is an extension of GCOV, a GNU tool which provides information
about what parts of a program are actually executed (i.e. "covered")
while running a particular test case. The extension consists of a set
of PERL scripts which build on the textual GCOV output to implement
HTML output and support for large projects.

%description -l pl.UTF-8
LCOV jest frontendem do programu GCOV - narzędzie pozwalającego badać
które fragmenty kodu są wykonywane (pokryte) podczas przeprowadzania
zestawu testów. LCOV składa się z zestawu skryptów języka PERL, które
prezentują dane generowane przez GCOV w postaci stron HTML.

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	PREFIX=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES README example
%attr(640,root,root) %config(noreplace) %verify(not md5 mtime size) %{_sysconfdir}/lcovrc
%attr(755,root,root) %{_bindir}/gendesc
%attr(755,root,root) %{_bindir}/genhtml
%attr(755,root,root) %{_bindir}/geninfo
%attr(755,root,root) %{_bindir}/genpng
%attr(755,root,root) %{_bindir}/lcov
%{_mandir}/man1/gendesc.1*
%{_mandir}/man1/genhtml.1*
%{_mandir}/man1/geninfo.1*
%{_mandir}/man1/genpng.1*
%{_mandir}/man1/lcov.1*
%{_mandir}/man5/lcovrc.5*
