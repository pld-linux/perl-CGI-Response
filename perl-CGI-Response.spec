%include	/usr/lib/rpm/macros.perl
Summary:	CGI-Response perl module
Summary(pl):	Modu³ perla CGI-Response
Name:		perl-CGI-Response
Version:	0.03
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/CGI/CGI-Response-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-Response - Respond to CGI requests.

%description -l pl
Modu³ perla CGI-Response.

%prep
%setup -q -n CGI-Response-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/CGI/Response
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README TO-DO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TO-DO}.gz

%{perl_sitelib}/CGI/Response.pm
%{perl_sitearch}/auto/CGI/Response

%{_mandir}/man3/*
