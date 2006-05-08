# TODO:
# - files section
%define		module	matplotlib
Summary:	Matlab(TM) style Python plotting package
Summary(pl):	Pakiet do rysowania w Pythonie podobny do Matlaba(TM)
Name:		python-%{module}
Version:	0.87.2
Release:	0.2
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/matplotlib/%{module}-%{version}.tar.gz
# Source0-md5:	74dde3c3e33797f56ebd6ca578090f8e
URL:		http://matplotlib.sourceforge.net/
Requires:       python-numpy-MA
Requires:       python-numpy-FFT
BuildRequires:	freetype-devel
BuildRequires:	ncurses-devel
BuildRequires:	python >= 2.2.1
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	python-numarray-devel
BuildRequires:	python-numpy-devel
%pyrequires_eq	python-modules
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
matplotlib strives to produce publication quality 2D graphics using
matlab plotting for inspiration. Although the main lib is object
oriented, there is a functional interface "pylab" for people coming
from Matlab.

%description -l pl
matplotlib usi³uje tworzyæ grafikê 2D o jako¶ci publikacji przy u¿yciu
wykresów matlaba jako inspiracji. Chocia¿ g³ówna biblioteka jest
zorientowana obiektowo, jest interfejs funkcyjny "pylab" dla ludzi
przechodz±cych z Matlaba.

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
