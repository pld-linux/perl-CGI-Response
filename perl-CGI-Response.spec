#
# Conditional build:
%bcond_without	tests	# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	CGI
%define	pnam	Response
Summary:	CGI::Response - respond to CGI requests
Summary(pl):	CGI::Response - odpowiadanie na zapytania CGI
Name:		perl-CGI-Response
Version:	0.03
Release:	11
License:	GPL
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	ce725b4c67d409157881141dbaaeb067
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
CGI::Response is a Perl5 module for constructing responses to Common
Gateway Interface (CGI) requests.  It is designed to be light-weight
and efficient for the most common tasks, and also to provide access to
all HTTP response features for more advanced CGI applications.

%description -l pl
CGI::Response jest modu³em Perla do konstruowania odpowiedzi na zapytania
przez Common Gateway Interface (CGI).  Jest zaprojektowany tak, aby byæ
lekkim i efektywnym w wiêkszo¶ci popularnych zadañ, a tak¿e umo¿liwiæ
dostêp do wszystkicy cech odpowiedzi HTTP bardziej zaawansowanym
aplikacjom CGI.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TO-DO
%{perl_vendorlib}/CGI/Response.pm
%{_mandir}/man3/*
