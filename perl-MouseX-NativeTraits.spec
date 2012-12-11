%define upstream_name       MouseX-NativeTraits
%define upstream_version    1.04

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	2
License:	Artistic
Group:		Development/Perl
Summary:	Extend your attribute interfaces for Mouse
Url:		http://search.cpan.org/dist/%{upstream_name}
Source:		http://www.cpan.org/modules/by-module/Config/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(Any::Moose)
BuildRequires:	perl(Module::Build)
BuildRequires:	perl(Mouse)
BuildRequires:	perl(Test::Fatal)
BuildArch:	noarch

%description
Extend your attribute interfaces for Mouse.

%prep
%setup -q -n %{upstream_name}-%{upstream_version} 

%build
perl Makefile.PL INSTALLDIRS=vendor destdir=%{buildroot}
make

%check
make test

%install
%makeinstall_std
find %{buildroot} -type f -name perllocal.pod -o -name .packlist -o -name '*.bs' -a -size 0 | xargs rm -f
find %{buildroot} -type d -depth | xargs rmdir --ignore-fail-on-non-empty

%files
%doc README Changes
%{perl_vendorlib}/Mouse/Meta/Attribute/Custom/Trait/*.pm
%{perl_vendorlib}/Mouse/Meta/Attribute/*.pm
%{perl_vendorlib}/MouseX/NativeTraits.pm
%{perl_vendorlib}/MouseX/NativeTraits/*.pm
%{perl_vendorlib}/MouseX/NativeTraits/MethodProvider/*.pm
%{_mandir}/man3/*


%changelog
* Fri Jun 17 2011 Bruno Cornec <bcornec@mandriva.org> 1.40.0-1mdv2011.0
+ Revision: 685830
- First import of perl-MouseX-NativeTraits-1.04
- create perl-MouseX-NativeTraits

