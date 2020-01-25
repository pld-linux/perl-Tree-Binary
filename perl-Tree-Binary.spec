#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define	pdir	Tree
%define	pnam	Binary
Summary:	Tree::Binary - A Object Oriented Binary Tree for Perl
#Summary(pl.UTF-8):	
Name:		perl-Tree-Binary
Version:	0.07
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Tree/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	a5f9a000a7accc4550965892ba80952f
URL:		http://search.cpan.org/dist/Tree-Binary/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This module is a fully object oriented implementation of a binary
tree. Binary trees are a specialized type of tree which has only
two possible branches, a left branch and a right branch. While it
is possible to use an n-ary tree, like Tree::Simple, to fill most of
your binary tree needs, a true binary tree object is just easier to
mantain and use.

# %description -l pl.UTF-8
# TODO

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Tree/*.pm
%{perl_vendorlib}/Tree/Binary
%{_mandir}/man3/*
