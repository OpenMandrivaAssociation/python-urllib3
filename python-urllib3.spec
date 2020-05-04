%bcond_without python2
%define	module	urllib3

Summary:	Python HTTP library with thread-safe connection pooling, file post, and more
Name:		python-%{module}
# ***** WARNING *****
# Before updating, make sure python-requests supports the
# new version and is being updated at the same time.
Version:	1.25.9
Release:	1
Source0:	https://github.com/urllib3/urllib3/archive/%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://urllib3.readthedocs.org/
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python-setuptools
%if %{with python2}
BuildRequires:	pkgconfig(python2)
BuildRequires:	python2-setuptools
%endif

%description
There are two critical features missing from the Python standard
library: Connection re-using/pooling and file posting. It's not
terribly hard to implement these yourself, but it's much easier to use
a module that already did the work for you.

The Python standard libraries urllib and urllib2 have little to do
with each other. They were designed to be independent and standalone,
each solving a different scope of problems, and urllib3 follows in a
similar vein.

%package -n python2-urllib3
Summary:	Python 2.x HTTP library with thread-safe connection pooling and more
Group:		Development/Python

%description -n python2-urllib3
There are two critical features missing from the Python standard
library: Connection re-using/pooling and file posting. It's not
terribly hard to implement these yourself, but it's much easier to use
a module that already did the work for you.

The Python standard libraries urllib and urllib2 have little to do
with each other. They were designed to be independent and standalone,
each solving a different scope of problems, and urllib3 follows in a
similar vein.

%prep
%autosetup -n %{module}-%{version} -p1

%install
%if %{with python2}
PYTHONDONTWRITEBYTECODE=1 python2 setup.py install --root=%{buildroot}
%endif

PYTHONDONTWRITEBYTECODE=1 %__python setup.py install --root=%{buildroot}

%files
%doc *.txt
%{py_puresitedir}/urllib3*

%if %{with python2}
%files -n python2-urllib3
%{py2_puresitedir}/urllib3*
%endif
