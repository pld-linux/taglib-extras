Summary:	A tag library extra support for MP4 and WMA files
Summary(pl.UTF-8):	Dodatek do biblioteka tag dla plików MP4 i WMA
Name:		taglib-extras
Version:	0.1
Release:	1
License:	GPL
Group:		X11/Libraries
Source0:	http://www.jefferai.com/taglib-extras/%{name}-%{version}.tar.gz
# Source0-md5:	c6d32e4f203768a2e4b5a83c5285f0a7
URL:		http://ktown.kde.org/~wheeler/taglib.html
BuildRequires:	autoconf >= 2.52
BuildRequires:	automake >= 1.6
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A tag library extras

%description -l pl.UTF-8
Dodatek dla biblioteki tag

%package devel
Summary:	libtag-extras - header files
Summary(pl.UTF-8):	libtag-extras - pliki nagłówkowe
Group:		X11/Development/Libraries
Requires:	%{name} = %{version}-%{release}
Requires:	libstdc++-devel

%description devel
Extras header files for tag library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dodatków biblioteki tag.

%prep
%setup -q -n %{name}

%build
%cmake \
	-DCMAKE_INSTALL_PREFIX=%{_prefix} \
	-DLIB_INSTALL_DIR=%{_libdir} \
	-DCMAKE_BUILD_TYPE=%{!?debug:Release}%{?debug:Debug} \
%if "%{_lib}" == "lib64"
	-DLIB_SUFFIX=64 \
%endif
	.

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/libtag-extras.so.*.*.*
%attr(755,root,root) %ghost %{_libdir}/libtag-extras.so.?

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/taglib-extras-config
%{_libdir}/libtag-extras.so
%{_pkgconfigdir}/taglib-extras.pc
%{_includedir}/taglib-extras
