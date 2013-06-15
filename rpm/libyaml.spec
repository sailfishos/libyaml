# 
# Do NOT Edit the Auto-generated Part!
# Generated by: spectacle version 0.26
# 

Name:       libyaml

# >> macros
# << macros

Summary:    YAML 1.1 parser and emitter written in C
Version:    0.1.4
Release:    1
Group:      System Environment/Libraries
License:    MIT
URL:        http://pyyaml.org/
Source0:    %{name}-%{version}.tar.gz
Source100:  libyaml.yaml
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
%setup -q -n %{name}-%{version}/%{name}

# >> setup
# << setup

%build
# >> build pre
# << build pre

%configure --disable-static
make %{?jobs:-j%jobs}

# >> build post
# << build post

%install
rm -rf %{buildroot}
# >> install pre
# << install pre
%make_install

# >> install post
#make DESTDIR=%{buildroot} INSTALL="install -p" install
#rm -f %{buildroot}%{_libdir}/*.{la,a}
# << install post

%check
# >> check
make check
# << check

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%defattr(-,root,root,-)
# >> files
%doc LICENSE README
%{_libdir}/%{name}*.so.*
# << files

%files devel
%defattr(-,root,root,-)
# >> files devel
%doc doc/html
%{_libdir}/%{name}*.so
%{_libdir}/pkgconfig/yaml-0.1.pc
%{_includedir}/yaml.h
# << files devel