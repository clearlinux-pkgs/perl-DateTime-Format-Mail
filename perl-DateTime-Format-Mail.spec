#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-DateTime-Format-Mail
Version  : 0.403
Release  : 18
URL      : https://cpan.metacpan.org/authors/id/B/BO/BOOK/DateTime-Format-Mail-0.403.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/B/BO/BOOK/DateTime-Format-Mail-0.403.tar.gz
Source1  : http://http.debian.net/debian/pool/main/libx/libxml-feed-perl/libxml-feed-perl_0.53+dfsg-1.debian.tar.xz
Summary  : 'Convert between DateTime and RFC2822/822 formats'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-DateTime-Format-Mail-license = %{version}-%{release}
Requires: perl-DateTime-Format-Mail-perl = %{version}-%{release}
BuildRequires : buildreq-cpan
BuildRequires : perl(B::Hooks::EndOfScope)
BuildRequires : perl(Class::Data::Inheritable)
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(Class::Singleton)
BuildRequires : perl(DateTime)
BuildRequires : perl(DateTime::Locale)
BuildRequires : perl(DateTime::TimeZone)
BuildRequires : perl(Devel::StackTrace)
BuildRequires : perl(Eval::Closure)
BuildRequires : perl(Exception::Class)
BuildRequires : perl(File::ShareDir)
BuildRequires : perl(MRO::Compat)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Module::Runtime)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Validate)
BuildRequires : perl(Params::ValidationCompiler)
BuildRequires : perl(Role::Tiny)
BuildRequires : perl(Specio::Exporter)
BuildRequires : perl(Sub::Exporter::Progressive)
BuildRequires : perl(Sub::Identify)
BuildRequires : perl(Try::Tiny)
BuildRequires : perl(Variable::Magic)
BuildRequires : perl(namespace::autoclean)
BuildRequires : perl(namespace::clean)

%description
DateTime::Format::Mail
Convert between DateTime and RFC2822/822 formats
To install, run the following commands after untarring the
distribution:

%package dev
Summary: dev components for the perl-DateTime-Format-Mail package.
Group: Development
Provides: perl-DateTime-Format-Mail-devel = %{version}-%{release}
Requires: perl-DateTime-Format-Mail = %{version}-%{release}

%description dev
dev components for the perl-DateTime-Format-Mail package.


%package license
Summary: license components for the perl-DateTime-Format-Mail package.
Group: Default

%description license
license components for the perl-DateTime-Format-Mail package.


%package perl
Summary: perl components for the perl-DateTime-Format-Mail package.
Group: Default
Requires: perl-DateTime-Format-Mail = %{version}-%{release}

%description perl
perl components for the perl-DateTime-Format-Mail package.


%prep
%setup -q -n DateTime-Format-Mail-0.403
cd %{_builddir}
tar xf %{_sourcedir}/libxml-feed-perl_0.53+dfsg-1.debian.tar.xz
cd %{_builddir}/DateTime-Format-Mail-0.403
mkdir -p deblicense/
cp -r %{_builddir}/debian/* %{_builddir}/DateTime-Format-Mail-0.403/deblicense/

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test || :

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Mail
cp %{_builddir}/DateTime-Format-Mail-0.403/LICENSE %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Mail/ea436f0324de15ab475a4b13c31b892fe85fe2c9
cp %{_builddir}/debian/copyright %{buildroot}/usr/share/package-licenses/perl-DateTime-Format-Mail/808cdef4c992763637fe5a5a7551c6cd5186080b
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/DateTime::Format::Mail.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-DateTime-Format-Mail/808cdef4c992763637fe5a5a7551c6cd5186080b
/usr/share/package-licenses/perl-DateTime-Format-Mail/ea436f0324de15ab475a4b13c31b892fe85fe2c9

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/vendor_perl/5.32.1/DateTime/Format/Mail.pm
