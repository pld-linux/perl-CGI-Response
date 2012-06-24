%define	pdir	CGI
%define	pnam	Response
%include	/usr/lib/rpm/macros.perl
Summary:	CGI-Response perl module
Summary(pl):	Modu� perla CGI-Response
Name:		perl-CGI-Response
Version:	0.03
Release:	8

License:	GPL
Group:		Development/Languages/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI-Response - Respond to CGI requests.

%description -l pl
Modu� perla CGI-Response.

%prep
%setup -q -n CGI-Response-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TO-DO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/CGI/Response.pm
%{_mandir}/man3/*
