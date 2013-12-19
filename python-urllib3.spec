%define	module	urllib3
%define name	python-%{module}
%define version 1.4
%define release 1

Summary:	Python HTTP library with thread-safe connection pooling, file post, and more
Name:		%{name}
Version:	1.7.1
Release:	1
Source0:	https://pypi.python.org/packages/source/u/urllib3/urllib3-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://urllib3.readthedocs.org/
BuildArch:	noarch
BuildRequires:	python-devel, python-setuptools

%description
There are two critical features missing from the Python standard
library: Connection re-using/pooling and file posting. It's not
terribly hard to implement these yourself, but it's much easier to use
a module that already did the work for you.

The Python standard libraries urllib and urllib2 have little to do
with each other. They were designed to be independent and standalone,
each solving a different scope of problems, and urllib3 follows in a
similar vein.

%prep
%setup -q -n %{module}-%{version}

%install
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean

%files
%doc *.txt
%py_puresitedir/urllib3*
%py_puresitedir/dummyserver*


%changelog
* Tue Jul 17 2012 Lev Givon <lev@mandriva.org> 1.4-1
+ Revision: 810074
- Update to 1.4.

* Wed Apr 25 2012 Lev Givon <lev@mandriva.org> 1.3-1
+ Revision: 793427
- imported package python-urllib3


