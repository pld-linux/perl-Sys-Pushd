%define		pdir	Sys
%define		pnam	Pushd
Summary:	Sys::Pushd perl module
Summary(pl.UTF-8):	Moduł perla Sys::Pushd
Name:		perl-Sys-Pushd
Version:	0.001
Release:	11
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/%{pdir}/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	5bb67fb42c03ef9527d61674db59689e
URL:		http://search.cpan.org/dist/Sys-Pushd/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys::Pushd - changes directory temporarily.

%description -l pl.UTF-8
Sys::Pushd - umożliwia tymczasową zmianę katalogu.

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
