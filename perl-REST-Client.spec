#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	REST
%define	pnam	Client
Summary:	REST::Client - A simple client for interacting with RESTful http/https resources
Summary(pl.UTF-8):	REST::Client - prosty klient do interakcji z zasobami RESTful http/https
Name:		perl-REST-Client
Version:	134
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MC/MCRAWFOR/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	8fc01b3bd1b0c05a1f4e3eb92568c244
URL:		http://search.cpan.org/dist/REST-Client/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
REST::Client provides a simple way to interact with HTTP RESTful
resources.

%description(pl.UTF-8)
REST::Client dostarcza prosty sposów na interakcję z zasobami HTTP
RESTful.
%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGES
%dir %{perl_vendorlib}/REST
%{perl_vendorlib}/REST/*.pm
%{_mandir}/man3/*
