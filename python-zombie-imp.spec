Name:           python-zombie-imp
Version:        0.0.4
Release:        2
Summary:        A copy of the `imp` module that was removed in Python 3.12
Group:          Development/Python
License:        Python-2.0.1
URL:            https://github.com/encukou/zombie-imp
Source0:         https://files.pythonhosted.org/packages/source/z/zombie_imp/zombie_imp-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  pkgconfig(python)
BuildRequires:  python%{pyver}dist(setuptools)
#BuildRequires:  python3-testsuite
Provides:       python%{pyver}dist(zombie-imp) = %{version}-%{release}
BuildSystem:    python

%description
A copy of the imp module that was removed in Python 3.12.
This is a compat package to ease transition to Python 3.12.
It shouldn't be used and packages using `imp` module
should use `importlib.metadata` instead.


%files
%doc README.*
%{python_sitelib}/__pycache__/imp.cpython-*.pyc
%{python_sitelib}/imp.py
%{python_sitelib}/zombie_imp-%{version}.dist-info
%{python_sitelib}/zombie_imp/
