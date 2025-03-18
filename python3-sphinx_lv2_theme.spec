Summary:	A minimal static theme for Sphinx
Summary(pl.UTF-8):	Minimalny statyczny motyw dla Sphinksa
Name:		python3-sphinx_lv2_theme
Version:	1.4.2
Release:	1
License:	ISC
Group:		Libraries/Python
#Source0Download: https://pypi.org/simple/sphinx_lv2_theme/
Source0:	https://files.pythonhosted.org/packages/source/s/sphinx_lv2_theme/sphinx_lv2_theme-%{version}.tar.gz
# Source0-md5:	76a0a4be34713b93f8a04af4574df7ee
URL:		https://pypi.org/project/sphinx_lv2_theme/
BuildRequires:	python3-modules >= 1:3.6
BuildRequires:	python3-setuptools
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python3-modules >= 1:3.6
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a minimal pure-CSS theme for Sphinx that uses the
documentation style of the LV2 plugin specification and related
projects.

%description -l pl.UTF-8
Minimalny, składający się z czystego CSS, motyw dla Sphinksa,
używający stylu dokumentacji specyfikacji wtyczek LV2 i powiązanych
projektów.

%prep
%setup -q -n sphinx_lv2_theme-%{version}

%build
%py3_build

%install
rm -rf $RPM_BUILD_ROOT

%py3_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc LICENSE NEWS README.md
%{py3_sitescriptdir}/sphinx_lv2_theme
%{py3_sitescriptdir}/sphinx_lv2_theme-%{version}-py*.egg-info
