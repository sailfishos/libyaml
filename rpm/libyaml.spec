Name:       libyaml
Summary:    YAML 1.1 parser and emitter written in C
Version:    0.2.5
Release:    1
Group:      System Environment/Libraries
License:    MIT
URL:        http://pyyaml.org/
Source0:    %{name}-%{version}.tar.gz
Requires(post): /sbin/ldconfig
Requires(postun): /sbin/ldconfig

%description
YAML is a data serialization format designed for human readability and
interaction with scripting languages.  LibYAML is a YAML parser and
emitter written in C.


%package devel
Summary:    Development files for LibYAML applications
Group:      Development/Libraries
Requires:   %{name} = %{version}-%{release}

%description devel
The %{name}-devel package contains libraries and header files for
developing applications that use LibYAML.


%prep
%setup -q -n %{name}-%{version}/upstream

%build
%reconfigure --disable-static
%make_build

%install
rm -rf %{buildroot}
%make_install

%check
make check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
%license License
%{_libdir}/%{name}*.so.*

%files devel
%defattr(-,root,root,-)
%{_libdir}/%{name}*.so
%doc ReadMe.md
%{_libdir}/pkgconfig/yaml-0.1.pc
%{_includedir}/yaml.h

