# NOTE:
# - bundles modified yajl-1.0.12

# Conditional build:
%bcond_with	tests		# build without tests

%define rbname yajl-ruby
Summary:	Ruby C bindings to the excellent Yajl JSON stream-based parser library
Name:		ruby-yajl
Version:	1.2.1
Release:	2
License:	MIT
Group:		Development/Languages
Source0:	http://rubygems.org/downloads/%{rbname}-%{version}.gem
# Source0-md5:	61d4348658120c1e633417cdc3404390
URL:		http://rdoc.info/github/brianmario/yajl-ruby
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.665
BuildRequires:	ruby-devel
%if %{with tests}
BuildRequires:	ruby-activesupport
BuildRequires:	ruby-json
BuildRequires:	ruby-rake-compiler >= 0.7.5
BuildRequires:	ruby-rspec >= 2.0.0
%endif
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C binding to the excellent YAJL JSON parsing and generation library.

%prep
%setup -q

%build
%__gem_helper spec

cd ext/yajl
%{__ruby} extconf.rb
%{__make} V=1 \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{ruby_vendorlibdir},%{ruby_vendorarchdir}/yajl,%{ruby_specdir}}
cp -a lib/* $RPM_BUILD_ROOT%{ruby_vendorlibdir}
install -p ext/yajl/yajl.so $RPM_BUILD_ROOT%{ruby_vendorarchdir}/yajl/yajl.so

cp -p %{rbname}-%{version}.gemspec $RPM_BUILD_ROOT%{ruby_specdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md MIT-LICENSE
%dir %{ruby_vendorarchdir}/yajl
%attr(755,root,root) %{ruby_vendorarchdir}/yajl/yajl.so
%{ruby_vendorlibdir}/yajl.rb
%{ruby_vendorlibdir}/yajl
%{ruby_specdir}/%{rbname}-%{version}.gemspec
