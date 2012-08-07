%define	module	urllib3
%define name	python-%{module}
%define version 1.5
%define release 1

Summary:	Python HTTP library with thread-safe connection pooling, file post, and more
Name:		%{name}
Version:	%{version}
Release:	%{release}
Source0:	http://pypi.python.org/packages/source/u/%{module}/%{module}-%{version}.tar.gz
License:	MIT
Group:		Development/Python
Url:		http://urllib3.readthedocs.org/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
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
%__rm -rf %{buildroot}
PYTHONDONTWRITEBYTECODE= %__python setup.py install --root=%{buildroot}

%clean
%__rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc *.txt
%py_sitedir/urllib3*
%py_sitedir/dummyserver*
