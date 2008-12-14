# TODO:
# - add perl dependencies
#
Summary:	LTP GCOV extension code coverage tool
Name:		lcov
Version:	1.6
Release:	0.1
License:	GPL
Group:		Applications
Source0:	http://dl.sourceforge.net/ltp/%{name}-%{version}.tar.gz
# Source0-md5:	dd3efb076efd812c32285815f12a2935
URL:		http://ltp.sourceforge.net/coverage/lcov.php
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
LCOV is an extension of GCOV, a GNU tool which provides information
about what parts of a program are actually executed (i.e. "covered")
while running a particular test case. The extension consists of a set
of PERL scripts which build on the textual GCOV output to implement
HTML output and support for large projects.

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
