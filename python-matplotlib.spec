# TODO:
# - files section
%define		module	matplotlib
Summary:	Matlab(TM) style python plotting package
Name:		python-%{module}
Version:	0.82
Release:	0.1
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/matplotlib/%{module}-%{version}.tar.gz
# Source0-md5:	94da6c11af51d5872c498e59fd31c9a0
URL:		http://matplotlib.sourceforge.net/
BuildRequires:	python >= 2.2.1
%pyrequires_eq	python-modules
BuildRequires:	python-numpy
BuildRequires:	ncurses-devel
BuildRequires:	freetype-devel
BuildRequires:	python-devel
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
matplotlib strives to produce publication quality 2D graphics using
matlab plotting for inspiration. Although the main lib is object
oriented, there is a functional interface "pylab" for people coming
from Matlab.

%prep
%setup -q -n %{module}-%{version}

%build
python setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

find $RPM_BUILD_ROOT%{py_sitescriptdir}/ -name \*.py | xargs rm -f

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG KNOWN_BUGS NUMARRAY_ISSUES README TODO
%{py_libdir}/*/*
%{_datadir}/%{module}
