%define	module	urllib3

Summary:	Python HTTP library with thread-safe connection pooling, file post, and more
Name:		python-%{module}
# ***** WARNING *****
# Before updating, make sure python-requests supports the
# new version and is being updated at the same time.
Version:	2.5.0
Release:	1
Source0:	https://files.pythonhosted.org/packages/source/u/urllib3/urllib3-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		https://urllib3.readthedocs.org/
# Also: https://github.com/urllib3/urllib3
BuildArch:	noarch
BuildRequires:	pkgconfig(python3)
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)

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
%autosetup -n %{module}-%{version} -p1
%py_build

%install
%py_install

%files
%doc *.txt
%{py_puresitedir}/urllib3*
