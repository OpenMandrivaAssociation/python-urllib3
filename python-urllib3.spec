%define module urllib3

Name:		python-urllib3
Summary:	Python HTTP library with thread-safe connection pooling, file post, and more
# ***** WARNING *****
# Before updating, make sure python-requests supports the
# new version and is being updated at the same time.
Version:	2.7.0
Release:	1
License:	MIT
Group:		Development/Python
URL:		https://urllib3.readthedocs.org/
Source0:	https://files.pythonhosted.org/packages/source/u/%{module}/%{module}-%{version}.tar.gz#/%{name}-%{version}.tar.gz
# Also: https://github.com/urllib3/urllib3

BuildSystem:	python
BuildArch:	noarch
BuildRequires:	python%{pyver}dist(pip)
BuildRequires:	python%{pyver}dist(hatchling)
BuildRequires:	python%{pyver}dist(hatch-vcs)
BuildRequires:	python%{pyver}dist(setuptools-scm)
BuildRequires:	python%{pyver}dist(wheel)

%description
There are two critical features missing from the Python standard
library: Connection re-using/pooling and file posting. It's not
terribly hard to implement these yourself, but it's much easier to use
a module that already did the work for you.

The Python standard libraries urllib and urllib2 have little to do
with each other. They were designed to be independent and standalone,
each solving a different scope of problems, and urllib3 follows in a
similar vein.

%files
%{python_sitelib}/%{module}
%{python_sitelib}/%{module}-%{version}.dist-info

