%include	/usr/lib/rpm/macros.perl
%define	pdir	Sys
%define	pnam	Pushd
Summary:	Sys::Pushd perl module
Summary(pl):	Modu³ perla Sys::Pushd
Name:		perl-Sys-Pushd
Version:	0.001
Release:	9
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5bb67fb42c03ef9527d61674db59689e
BuildRequires:	rpm-perlprov >= 4.1-13
BuildRequires:	perl-devel >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys::Pushd - changes directory temporarily.

%description -l pl
Sys::Pushd - umo¿liwia tymczasow± zmianê katalogu.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README TODO
%{perl_vendorlib}/Sys/Pushd.pm
%{_mandir}/man3/*
