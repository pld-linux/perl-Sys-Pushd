%include	/usr/lib/rpm/macros.perl
Summary:	Sys-Pushd perl module
Summary(pl):	Modu³ perla Sys-Pushd
Name:		perl-Sys-Pushd
Version:	0.001
Release:	6
License:	GPL
Group:		Development/Languages/Perl
Group(de):	Entwicklung/Sprachen/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sys/Sys-Pushd-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys-Pushd - changes directory temporarily.

%description -l pl
Sys-Pushd - umo¿liwia tymczasow± zmianê katalogu.

%prep
%setup -q -n Sys-Pushd-%{version}

%build
perl Makefile.PL
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc *.gz
%{perl_sitelib}/Sys/Pushd.pm
%{_mandir}/man3/*
