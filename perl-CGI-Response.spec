%include	/usr/lib/rpm/macros.perl
%define		pdir	CGI
%define		pnam	Response
Summary:	CGI::Response perl module
Summary(pl):	Modu³ perla CGI::Response
Name:		perl-CGI-Response
Version:	0.03
Release:	9
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
BuildRequires:	perl >= 5.6
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Response - Respond to CGI requests.

%description -l pl
Modu³ perla CGI::Response - odpowiadaj±cy na ¿±dania CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TO-DO
%{perl_sitelib}/CGI/Response.pm
%{_mandir}/man3/*
