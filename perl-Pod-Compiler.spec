%define upstream_name    Pod-Compiler
%define upstream_version 0.21

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	3

Summary:	Compile POD into an object tree
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Pod/Pod-Compiler-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildRequires:	perl(Pod::Parser)
BuildRequires:	perl(Storable)
BuildRequires:	perl(Test::Simple)
BuildRequires:	perl(Tree::DAG_Node)
BuildArch:	noarch

%description
This package, based on Pod::Parser, compiles a given POD document into an
object tree (based on Tree::DAG_Node). It prints errors and warnings about the
POD it reads. The result can be used to conveniently convert the POD into any
other format.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes README
%{_bindir}/podlint
%{_mandir}/man1/*
%{_mandir}/man3/*
%{perl_vendorlib}/*

%changelog
* Sat Apr 23 2011 Funda Wang <fwang@mandriva.org> 0.200.0-3mdv2011.0
+ Revision: 657825
- rebuild for updated spec-helper

* Sat Dec 25 2010 Shlomi Fish <shlomif@mandriva.org> 0.200.0-2mdv2011.0
+ Revision: 625015
- Update the file list and the description
- import perl-Pod-Compiler


