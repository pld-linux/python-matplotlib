# TODO:
# - use system fonts (cm*.ttf) and metrics in mpl-data dir?
%define		module	matplotlib
Summary:	Matlab(TM) style Python plotting package
Summary(pl.UTF-8):	Pakiet do rysowania w Pythonie podobny do Matlaba(TM)
Name:		python-%{module}
Version:	1.2.1
Release:	1
License:	GPL
Group:		Libraries/Python
Source0:	http://downloads.sourceforge.net/matplotlib/%{module}-%{version}.tar.gz
# Source0-md5:	326a959c4c3f85417a3daf805cfb54f9
URL:		http://matplotlib.sourceforge.net/
BuildRequires:	freetype-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
BuildRequires:	python >= 2.4
BuildRequires:	python-PyQt
BuildRequires:	python-PyQt4
BuildRequires:	python-dateutil
BuildRequires:	python-devel
BuildRequires:	python-numpy-devel >= 1:1.0.3
BuildRequires:	python-numpy-numarray-devel
BuildRequires:	python-pygtk-devel
BuildRequires:	python-pytz
# Need for import pyqtconfig needed by qt detection.
BuildRequires:	python-sip-devel
BuildRequires:	python-tkinter
BuildRequires:	python-wxPython
BuildRequires:	rpm-pythonprov
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

rm -f setup.cfg

%build
export CFLAGS="%{rpmcflags}"
%{__python} setup.py build

%install
rm -rf $RPM_BUILD_ROOT

python setup.py install \
	--root=$RPM_BUILD_ROOT \
	--optimize=2

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

# matplotlib can use system fonts, so drop these copies
rm -f $RPM_BUILD_ROOT%{py_sitedir}/matplotlib/mpl-data/Vera*.ttf

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/%{module}/tests

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc CHANGELOG README.txt TODO
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%dir %{py_sitedir}/%{module}/backends
%{py_sitedir}/%{module}/backends/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/backends/*.so
%dir %{py_sitedir}/%{module}/backends/qt4_editor
%{py_sitedir}/%{module}/backends/qt4_editor/*.py[co]
%dir %{py_sitedir}/%{module}/backends/Matplotlib.nib
%{py_sitedir}/%{module}/backends/Matplotlib.nib/*.nib
%{py_sitedir}/%{module}/delaunay
%{py_sitedir}/%{module}/mpl-data
%{py_sitedir}/%{module}/projections
%{py_sitedir}/%{module}/sphinxext
%{py_sitedir}/%{module}/testing
%{py_sitedir}/%{module}/tri

%{py_sitedir}/mpl_toolkits
%{py_sitedir}/pylab.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-*.egg-info
%endif
