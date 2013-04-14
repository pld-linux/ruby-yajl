%define rbname yajl-ruby
Summary:	Ruby C bindings to the excellent Yajl JSON stream-based parser library
Name:		ruby-yajl
Version:	1.1.0
Release:	0.4
License:	MIT
Group:		Development/Languages
URL:		http://rdoc.info/github/brianmario/yajl-ruby
Source0:	%{rbname}-%{version}.gem
# Source0-md5:	5f35141b89be7da3b279b65ea0f3c0c2
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
BuildRequires:	ruby-devel
BuildRequires:	setup.rb
Requires:	ruby-activesupport
Requires:	ruby-json
Requires:	ruby-rake-compiler >= 0.7.5
Requires:	ruby-rspec >= 2.0.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C binding to the excellent YAJL JSON parsing and generation library.

%prep
%setup -q

# ext build
cp -p %{_datadir}/setup.rb .

%build
ruby setup.rb config \
	--prefix=%{_prefix} \
	--siterubyver=%{ruby_vendorlibdir} \
	--siterubyverarch=%{ruby_vendorarchdir} \

cd ext/yajl
# binary pkgs:
%{__ruby} extconf.rb
%{__make} \
	CC="%{__cc}" \
	LDFLAGS="%{rpmldflags}" \
	CFLAGS="%{rpmcflags} -fPIC"

%install
rm -rf $RPM_BUILD_ROOT
%{__ruby} setup.rb install \
	--prefix=$RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{ruby_vendorarchdir}/yajl
mv $RPM_BUILD_ROOT%{ruby_vendorarchdir}/{,yajl/}yajl.so

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md MIT-LICENSE
%dir %{ruby_vendorarchdir}/yajl
%attr(755,root,root) %{ruby_vendorarchdir}/yajl/yajl.so
%{ruby_vendorlibdir}/yajl.rb
%{ruby_vendorlibdir}/yajl
