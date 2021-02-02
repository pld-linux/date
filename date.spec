Summary:	A date and time library based on the C++11/14/17 <chrono> header
Name:		date
Version:	3.0.0
Release:	1
License:	MIT
Group:		Development/Libraries
Source0:	https://github.com/HowardHinnant/date/archive/v%{version}/%{name}-%{version}.tar.gz
# Source0-md5:	c76681532f87644c59c19938961bc85c
Patch0:		%{name}-cmake.patch
URL:		https://howardhinnant.github.io/date/date.html
BuildRequires:	cmake >= 3.7
BuildRequires:	libstdc++-devel >= 6:5
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	tzdata
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A date and time library based on the C++11/14/17 <chrono> header.

%package devel
Summary:	Header files for date library
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Header files for date library.

%prep
%setup -q
%patch0 -p1

%build
install -d build
cd build
%cmake .. \
	-DUSE_SYSTEM_TZ_DB:BOOL=ON \
	-DBUILD_TZ_LIB:BOOL=ON
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
%doc README.md
%attr(755,root,root) %{_libdir}/libdate-tz.so.*.*.*
%ghost %{_libdir}/libdate-tz.so.3

%files devel
%defattr(644,root,root,755)
%dir %{_includedir}/date
%{_includedir}/date/date.h
%{_includedir}/date/tz.h
%{_libdir}/cmake/date
%{_libdir}/libdate-tz.so
