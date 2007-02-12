Summary:	Lithuanian dictionary for aspell
Summary(pl.UTF-8):	Słownik litewski dla aspella
Name:		aspell-lt
Version:	1.1
%define	subv	0
%define	addv	cvs20060103
Release:	1.%{addv}.1
Epoch:		1
License:	GPL v2+
Group:		Applications/Text
Source0:	ftp://ftp.gnu.org/gnu/aspell/dict/lt/aspell6-lt-%{version}+%{addv}-%{subv}.tar.bz2
# Source0-md5:	ee034ad7cefa51e8b6b531f5ade527a6
URL:		http://aspell.sourceforge.net/
BuildRequires:	aspell >= 3:0.60
Requires:	aspell >= 3:0.60
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Lithuanian dictionary (i.e. word list) for aspell.

%description -l pl.UTF-8
Słownik litewski (lista słów) dla aspella.

%prep
%setup -q -n aspell6-lt-%{version}+%{addv}-%{subv}

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
