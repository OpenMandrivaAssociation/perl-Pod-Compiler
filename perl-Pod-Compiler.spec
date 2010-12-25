%define upstream_name    Pod-Compiler
%define upstream_version 0.20

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

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
The following section describes the objects returned by Pod::Compiler and
their methods. These objects all inherit from Tree::DAG_Node, so all
methods described there are valid as well.

The set/retrieve methods all work in the following way: If no argument is
specified, the corresponding value is returned. Otherwise the object's
value is set to the given argument and returned.

Common methods
    The following methods are common for all the classes:

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
%{_mandir}/man3/*
%perl_vendorlib/*
/usr/bin/podlint
/usr/share/man/man1/podlint.1.lzma

