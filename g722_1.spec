Summary:    libg722_1 is a library for the ITU G.722.1 and Annex C wideband speech codecs.
Name:       g722_1
Version:    0.2.0
Release:    1%{?dist}
License:    Polycom
Group:      System Environment/Libraries
URL:        http://www.soft-switch.org/libg722_1
BuildRoot:  %{_tmppath}/%{name}-%{version}-root
Source:     http://www.soft-switch.org/downloads/codecs/g722_1-0.2.0.tar.gz
BuildRoot:  %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

Docdir:     %{_prefix}/doc

BuildRequires: audiofile-devel
BuildRequires: doxygen libtool

%description
libg722_1 is a library for the ITU G.722.1 and Annex C wideband speech codecs.

%package devel
Summary:    G.722.1 development files
Group:      Development/Libraries
Requires:   %{name} = %{version}

%description devel
libg722_1 development files.

%prep
%setup -q

%build
./autogen.sh
%configure --enable-doc --disable-static --disable-rpath
make

%install
rm -rf %{buildroot}
make install DESTDIR=%{buildroot}
rm %{buildroot}%{_libdir}/libg722_1.la

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
%doc ChangeLog AUTHORS COPYING NEWS README 

%{_libdir}/libg722_1.so.*

%files devel
%defattr(-,root,root,-)
%doc doc/api
%{_includedir}/g722_1.h
%{_includedir}/g722_1
%{_libdir}/libg722_1.so
%{_libdir}/pkgconfig/g722_1.pc

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%changelog
* Sat Sep 20 2008 Steve Underwood <steveu@coppice.org> 0.0.1
- First pass
