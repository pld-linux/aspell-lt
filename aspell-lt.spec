Summary:	Lithuanian dictionary for aspell
Summary(pl):	S³ownik litewski dla aspella
Name:		aspell-lt
Version:	1.0
%define	subv	1
Release:	1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/lt/aspell6-lt-%{version}-%{subv}.tar.bz2
# Source0-md5:	2b1bb1c749c0513df18ee3ad826d3011
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lithuanian dictionary (i.e. word list) for aspell.

%description -l pl
S³ownik litewski (lista s³ów) dla aspella.

%prep
%setup -q -n aspell6-lt-%{version}-%{subv}

%build
# note: configure is not autoconf-generated
./configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Copyright README
%{_libdir}/aspell/*
%{_datadir}/aspell/*
