%define upstream_name    Pod-Compiler
%define upstream_version 0.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 3

Summary:    Compile POD into an object tree
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Pod/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Pod::Parser)
BuildRequires: perl(Storable)
BuildRequires: perl(Test::Simple)
BuildRequires: perl(Tree::DAG_Node)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}

%description
This package, based on Pod::Parser, compiles a given POD document into an
object tree (based on Tree::DAG_Node). It prints errors and warnings about the
POD it reads. The result can be used to conveniently convert the POD into any
other format.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor

%{make}

%check
%{make} test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_bindir}/podlint
%{_mandir}/man1/*
%{_mandir}/man3/*
%perl_vendorlib/*

