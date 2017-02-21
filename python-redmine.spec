%global         sum Python Redmine is a library for communicating with a Redmine project management application

Name:           python-redmine
Version:        1.5.1
Release:        1%{?dist}
Summary:        %{sum}

License:        ASL 2.0
URL:            https://github.com/maxtepkeev/python-redmine
Source0:        https://pypi.python.org/packages/0d/24/4a665080920b4bd51670f3b33ac96fd2027fac64233b1aba952a15b771a6/%{name}-%{version}.tar.gz

BuildArch:      noarch

Requires:       python-requests

Buildrequires:  python2-devel
Buildrequires:  python-setuptools

%description
Python Redmine is a library for communicating with a
Redmine project management application

%package -n python2-redmine
Summary:        %{sum}
Requires:       python-requests

Buildrequires:  python2-devel
Buildrequires:  python-setuptools

%description -n python2-redmine
Python Redmine is a library for communicating with a
Redmine project management application

%prep
%autosetup -n %{name}-%{version}

%build
%{__python2} setup.py build

%install
%{__python2} setup.py install --skip-build --root %{buildroot}

%check
#nosetests -v unittests.py

%files -n python2-redmine
%{python2_sitelib}/*

%changelog
* Tue Feb 21 2017 Fabien Boucher <fboucher@redhat.com> - 1.5.1-1
- Initial packaging
