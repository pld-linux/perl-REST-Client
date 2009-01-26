#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%include	/usr/lib/rpm/macros.perl
%define	pdir	REST
%define	pnam	Client
Summary:	REST::Client - A simple client for interacting with RESTful http/https resources
Name:		perl-REST-Client
Version:	62
Release:	0.1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-authors/id/M/MC/MCRAWFOR/REST-Client-62.tar.gz
# Source0-md5:	335f37bdf834b69bb5b5474b5cd54fc8
URL:		http://search.cpan.org/dist/REST-Client/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
REST::Client provides a simple way to interact with HTTP RESTful resources.

%prep
%setup -q -n Rest%{pnam}

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
%{perl_vendorlib}/REST/*.pm
%{_mandir}/man3/*
