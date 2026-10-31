Summary:	A tag library extra support for MP4 and WMA files
Summary(pl.UTF-8):	Dodatki do biblioteki tag dla plików MP4 i WMA
Name:		taglib-extras
Version:	1.0.1
Release:	4
# helpers LGPL v2.1+, audible LGPL v2.1+, rmff GPL v2+ - so GPL as a whole
License:	GPL v2+
Group:		Libraries
# originally from <http://www.kollide.net/~jefferai/>, no longer exists; now available on some distfiles
Source0:	https://mirrors.mit.edu/macports/distfiles/taglib-extras/%{name}-%{version}.tar.gz
# Source0-md5:	e973ca609b18e2c03c147ff9fd9e6eb8
Patch0:		taglib-2.0.patch
URL:		https://taglib.org/
BuildRequires:	cmake >= 2.6.2
BuildRequires:	libstdc++-devel
BuildRequires:	perl-base
BuildRequires:	pkgconfig
BuildRequires:	rpmbuild(macros) >= 1.605
BuildRequires:	taglib-devel >= 2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Unofficial TagLib file type plugins formerly maintained by the Amarok
project.

%description -l pl.UTF-8
Nieoficjalne wtyczki typów plików TagLib dawniej utrzymywane przez
projekt Amarok.

%package devel
Summary:	libtag-extras - header files
Summary(pl.UTF-8):	libtag-extras - pliki nagłówkowe
Group:		Development/Libraries
Requires:	%{name}%{?_isa} = %{version}-%{release}
Requires:	libstdc++-devel%{?_isa}
Requires:	taglib-devel%{?_isa} >= 2.0

%description devel
Extras header files for tag library.

%description devel -l pl.UTF-8
Pliki nagłówkowe dodatków biblioteki tag.

%prep
%setup -q
%patch -P0 -p1

%build
install -d build
cd build
%cmake .. \
	-DLIB_INSTALL_DIR=%{_libdir}

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post	-p /sbin/ldconfig
%postun	-p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%{_libdir}/libtag-extras.so.*.*.*
%ghost %{_libdir}/libtag-extras.so.1

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/taglib-extras-config
%{_libdir}/libtag-extras.so
%{_pkgconfigdir}/taglib-extras.pc
%{_includedir}/taglib-extras
