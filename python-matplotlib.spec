# TODO:
# - use system fonts (cm*.ttf) and metrics in mpl-data dir?
# - decide what to do with matplotlib/backends/Matplotlib.nib/*.nib files
%define		module	matplotlib
Summary:	Matlab(TM) style Python plotting package
Summary(pl.UTF-8):	Pakiet do rysowania w Pythonie podobny do Matlaba(TM)
Name:		python-%{module}
Version:	0.98.5.2
Release:	0.1
License:	GPL
Group:		Libraries/Python
# http://downloads.sourceforge.net/matplotlib/matplotlib-0.98.5.2.tar.gz?modtime=1229668616&big_mirror=0
Source0:	http://dl.sourceforge.net/matplotlib/%{module}-%{version}.tar.gz
# Source0-md5:	3e8210ec8bb71a18962ec8b43688509c
URL:		http://matplotlib.sourceforge.net/
BuildRequires:	freetype-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	python >= 2.4
BuildRequires:	python-dateutil
BuildRequires:	python-devel
BuildRequires:	python-numpy-devel >= 1:1.0.3
BuildRequires:	python-numpy-numarray-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	python-pytz
BuildRequires:	tk-devel
%pyrequires_eq	python-modules
Requires:	python-dateutil
Requires:	python-numpy >= 1:1.1
Requires:	python-numpy-oldnumeric
Requires:	python-pytz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
matplotlib strives to produce publication quality 2D graphics using
matlab plotting for inspiration. Although the main lib is object
oriented, there is a functional interface "pylab" for people coming
from Matlab.

%description -l pl.UTF-8
matplotlib usiłuje tworzyć grafikę 2D o jakości publikacji przy użyciu
wykresów matlaba jako inspiracji. Chociaż główna biblioteka jest
zorientowana obiektowo, jest interfejs funkcyjny "pylab" dla ludzi
przechodzących z Matlaba.

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
%doc CHANGELOG KNOWN_BUGS TODO
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%dir %{py_sitedir}/%{module}/backends
%{py_sitedir}/%{module}/backends/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/backends/*.so
# %dir %{py_sitedir}/%{module}/enthought
# %{py_sitedir}/%{module}/enthought/*.py[co]
# %{py_sitedir}/%{module}/enthought/resource
#%dir %{py_sitedir}/%{module}/enthought/traits
#%{py_sitedir}/%{module}/enthought/traits/*.py[co]
#%attr(755,root,root) %{py_sitedir}/%{module}/enthought/traits/*.so
#%{py_sitedir}/%{module}/enthought/traits/ui
#%{py_sitedir}/%{module}/enthought/util
%{py_sitedir}/%{module}/delaunay
%{py_sitedir}/%{module}/mpl-data
%{py_sitedir}/%{module}/numerix
%{py_sitedir}/%{module}/projections

%{py_sitedir}/mpl_toolkits
# %{py_sitedir}/%{module}/toolkits
%{py_sitedir}/pylab.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-*.egg-info
%endif
