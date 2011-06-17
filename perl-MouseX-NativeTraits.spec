%define upstream_name       MouseX-NativeTraits
%define upstream_version    1.04

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
License:    Artistic
Group:      Development/Perl
Summary:    Extend your attribute interfaces for Mouse
Url:        http://search.cpan.org/dist/%{upstream_name}
Source:     http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  perl(Any::Moose)
BuildRequires:  perl(Module::Build)
BuildRequires:  perl(Mouse)
BuildRequires:  perl(Test::Fatal)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
Extend your attribute interfaces for Mouse

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor destdir=${RPM_BUILD_ROOT}/
make

%check
make test

%install
rm -rf %buildroot
make install DESTDIR=${RPM_BUILD_ROOT}
find ${RPM_BUILD_ROOT} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find ${RPM_BUILD_ROOT} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc README Changes
%{perl_vendorlib}/Mouse/Meta/Attribute/Custom/Trait/*.pm
%{perl_vendorlib}/Mouse/Meta/Attribute/*.pm
%{perl_vendorlib}/MouseX/NativeTraits.pm
%{perl_vendorlib}/MouseX/NativeTraits/*.pm
%{perl_vendorlib}/MouseX/NativeTraits/MethodProvider/*.pm
%{_mandir}/man3/*
