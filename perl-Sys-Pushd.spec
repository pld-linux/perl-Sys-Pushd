%include	/usr/lib/rpm/macros.perl
Summary:	Sys-Pushd perl module
Summary(pl):	Modu³ perla Sys-Pushd
Name:		perl-Sys-Pushd
Version:	0.001
Release:	3
License:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/Jêzyki/Perl
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sys/Sys-Pushd-%{version}.tar.gz
BuildRequires:	rpm-perlprov >= 3.0.3-16
BuildRequires:	perl >= 5.005_03-14
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Sys-Pushd - changes directory temporarily.

%description -l pl
Sys-Pushd - umo¿liwia tymczasow± zmianê katalogu.

%prep
%setup -q -n Sys-Pushd-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

(
  cd $RPM_BUILD_ROOT%{perl_sitearch}/auto/Sys/Pushd
  sed -e "s#$RPM_BUILD_ROOT##" .packlist >.packlist.new
  mv .packlist.new .packlist
)

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man3/* \
        README TODO

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc {README,TODO}.gz

%{perl_sitelib}/Sys/Pushd.pm
%{perl_sitearch}/auto/Sys/Pushd

%{_mandir}/man3/*
