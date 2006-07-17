# TODO:
# - use system fonts (cm*.ttf) and metrics in mpl-data dir?
%define		module	matplotlib
Summary:	Matlab(TM) style Python plotting package
Summary(pl):	Pakiet do rysowania w Pythonie podobny do Matlaba(TM)
Name:		python-%{module}
Version:	0.87.4
Release:	0.3
License:	GPL
Group:		Libraries/Python
Source0:	http://dl.sourceforge.net/matplotlib/%{module}-%{version}.tar.gz
# Source0-md5:	b8ef6ee4b4a7267d94980b4678f950ea
URL:		http://matplotlib.sourceforge.net/
BuildRequires:	freetype-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	python >= 2.2.1
BuildRequires:	python-Numeric-devel
BuildRequires:	python-dateutil
BuildRequires:	python-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	python-pytz
BuildRequires:	python-numarray-devel
BuildRequires:	python-numpy-devel >= 1:0.9
%pyrequires_eq	python-modules
Requires:	python-dateutil
Requires:	python-numpy-FFT >= 1:0.9
Requires:	python-pytz
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

find $RPM_BUILD_ROOT%{py_sitedir} -name \*.py | xargs rm -f

# matplotlib can use system fonts, so drop these copies
rm -f $RPM_BUILD_ROOT%{py_sitedir}/matplotlib/mpl-data/Vera*.ttf

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG KNOWN_BUGS NUMARRAY_ISSUES README TODO
%dir %{py_sitedir}/matplotlib
%{py_sitedir}/matplotlib/*.py[co]
%attr(755,root,root) %{py_sitedir}/matplotlib/*.so
%dir %{py_sitedir}/matplotlib/backends
%{py_sitedir}/matplotlib/backends/*.py[co]
%attr(755,root,root) %{py_sitedir}/matplotlib/backends/*.so
%dir %{py_sitedir}/matplotlib/enthought
%{py_sitedir}/matplotlib/enthought/*.py[co]
%{py_sitedir}/matplotlib/enthought/resource
%dir %{py_sitedir}/matplotlib/enthought/traits
%{py_sitedir}/matplotlib/enthought/traits/*.py[co]
%attr(755,root,root) %{py_sitedir}/matplotlib/enthought/traits/*.so
%{py_sitedir}/matplotlib/enthought/traits/ui
%{py_sitedir}/matplotlib/enthought/util
%{py_sitedir}/matplotlib/mpl-data
%{py_sitedir}/matplotlib/numerix
%{py_sitedir}/matplotlib/toolkits
%{py_sitedir}/pylab.py[co]
