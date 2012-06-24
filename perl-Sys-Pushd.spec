%define		perl_sitelib	%(eval "`perl -V:installsitelib`"; echo $installsitelib)
Summary:	Sys-Pushd perl module
Summary(pl):	Modu� perla Sys-Pushd
Name:		perl-Sys-Pushd
Version:	0.001
Release:	3
Copyright:	GPL
Group:		Development/Languages/Perl
Group(pl):	Programowanie/J�zyki/Perl
Source:		ftp://ftp.perl.org/pub/CPAN/modules/by-module/Sys/Sys-Pushd-%{version}.tar.gz
BuildRequires:	perl >= 5.005_03-10
%requires_eq	perl
Requires:	%{perl_sitearch}
BuildRoot:	/tmp/%{name}-%{version}-root

%description
Sys-Pushd - changes directory temporarily. 

%description -l pl
Sys-Pushd - umo�liwia tymczasow� zmian� katalogu.

%prep
%setup -q -n Sys-Pushd-%{version}

%build
perl Makefile.PL
make

%install
rm -rf $RPM_BUILD_ROOT
make install DESTDIR=$RPM_BUILD_ROOT

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
