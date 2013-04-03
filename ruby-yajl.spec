%define rbname yajl-ruby
Summary:	Ruby C bindings to the excellent Yajl JSON stream-based parser library
Name:		ruby-yajl
Version:	1.1.0
Release:	0.1
License:	MIT
Group:		Development/Languages
URL:		http://rdoc.info/github/brianmario/yajl-ruby
Source0:	%{rbname}-%{version}.gem
BuildRequires:	rpm-rubyprov
BuildRequires:	rpmbuild(macros) >= 1.656
Requires:	ruby-activesupport
Requires:	ruby-json
Requires:	ruby-rake-compiler >= 0.7.5
Requires:	ruby-rspec >= 2.0.0
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
C binding to the excellent YAJL JSON parsing and generation library.

%prep
%setup -q

%build

%install
rm -rf $RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG.md README.md MIT-LICENSE
