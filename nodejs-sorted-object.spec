%define		pkg	sorted-object
Summary:	Returns a copy of an object with its keys sorted
Name:		nodejs-%{pkg}
Version:	1.0.0
Release:	1
License:	WTFPL
Group:		Development/Libraries
Source0:	http://registry.npmjs.org/sorted-object/-/%{pkg}-%{version}.tgz
# Source0-md5:	3df65fa1a0a28c71b4cb5e8c5f72742f
URL:		https://github.com/domenic/sorted-object
BuildRequires:	rpmbuild(macros) >= 1.634
Requires:	nodejs
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Although objects in JavaScript are theoretically unsorted, in practice
most engines use insertion order-at least, ignoring numeric keys. This
manifests itself most prominently when dealing with an object's JSON
serialization.

%prep
%setup -qc
mv package/* .

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}
cp -pr lib package.json $RPM_BUILD_ROOT%{nodejs_libdir}/%{pkg}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE.txt README.md
%{nodejs_libdir}/%{pkg}
