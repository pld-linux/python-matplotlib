# Conditional build:
%bcond_without  python2 # CPython 2.x module
%bcond_without  python3 # CPython 3.x module
# TODO:
# - use system fonts (cm*.ttf) and metrics in mpl-data dir?
# - make sure all dependencies that are available for Python3 are build for Python3
#   and included in BR when neccessary
%define		module	matplotlib
Summary:	Matlab(TM) style Python plotting package
Summary(pl.UTF-8):	Pakiet do rysowania w Pythonie podobny do Matlaba(TM)
Name:		python-%{module}
Version:	1.5.3
Release:	3
License:	GPL
Group:		Libraries/Python
Source0:	https://github.com/matplotlib/matplotlib/archive/v%{version}.tar.gz
# Source0-md5:	079d9d8cd9910e00ed1236fb44a518a7
URL:		http://matplotlib.sourceforge.net/
BuildRequires:	rpmbuild(macros) >= 1.710
BuildRequires:	freetype-devel
BuildRequires:	libstdc++-devel
BuildRequires:	ncurses-devel
%if %{with python2}
BuildRequires:	python >= 1:2.6
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
%pyrequires_eq	python-modules
%endif
%if %{with python3}
BuildRequires:	python3 >= 1:3.3
BuildRequires:	python3-2to3
BuildRequires:	python3-PyQt4
BuildRequires:	python3-dateutil
BuildRequires:	python3-devel
BuildRequires:	python3-numpy-devel >= 1:1.0.3
BuildRequires:	python3-numpy-numarray-devel
BuildRequires:	python3-pytz
# Need for import pyqtconfig needed by qt detection.
#BuildRequires:	python3-sip-devel
BuildRequires:	python3-six
BuildRequires:	python3-tkinter
#BuildRequires:	python3-wxPython
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	tk-devel
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

%package -n python3-%{module}
Summary:	Matlab(TM) style Python 3 plotting package
Summary(pl.UTF-8):	Pakiet do rysowania w Pythonie 3 podobny do Matlaba(TM)
Group:		Libraries/Python
Requires:	python3-six
Requires:	python3-dateutil
Requires:	python3-numpy
Requires:	python3-pytz

%description -n python3-%{module}
matplotlib strives to produce publication quality 2D graphics using
matlab plotting for inspiration. Although the main lib is object
oriented, there is a functional interface "pylab" for people coming
from Matlab.

%description -n python3-%{module} -l pl.UTF-8
matplotlib usiłuje tworzyć grafikę 2D o jakości publikacji przy użyciu
wykresów matlaba jako inspiracji. Chociaż główna biblioteka jest
zorientowana obiektowo, jest interfejs funkcyjny "pylab" dla ludzi
przechodzących z Matlaba.

%prep
%setup -q -n %{module}-%{version}

rm -f setup.cfg

%build
export CFLAGS="%{rpmcflags}"

%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install

%py_ocomp $RPM_BUILD_ROOT%{py_sitedir}
%py_comp $RPM_BUILD_ROOT%{py_sitedir}
%py_postclean

# matplotlib can use system fonts, so drop these copies
rm -f $RPM_BUILD_ROOT%{py_sitedir}/matplotlib/mpl-data/Vera*.ttf

rm -rf $RPM_BUILD_ROOT%{py_sitedir}/%{module}/tests
%endif

%if %{with python3}
%py3_install

%py3_ocomp $RPM_BUILD_ROOT%{py3_sitedir}
%py3_comp $RPM_BUILD_ROOT%{py3_sitedir}

# matplotlib can use system fonts, so drop these copies
rm -f $RPM_BUILD_ROOT%{py3_sitedir}/matplotlib/mpl-data/Vera*.ttf

rm -rf $RPM_BUILD_ROOT%{py3_sitedir}/%{module}/tests
%endif


%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc CHANGELOG README.rst
%dir %{py_sitedir}/%{module}
%{py_sitedir}/%{module}/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/*.so
%dir %{py_sitedir}/%{module}/axes
%{py_sitedir}/%{module}/axes/*.py[co]
%dir %{py_sitedir}/%{module}/backends
%{py_sitedir}/%{module}/backends/*.py[co]
%attr(755,root,root) %{py_sitedir}/%{module}/backends/*.so
%dir %{py_sitedir}/%{module}/backends/qt_editor
%{py_sitedir}/%{module}/backends/qt_editor/*.py[co]
%dir %{py_sitedir}/%{module}/backends/Matplotlib.nib
%{py_sitedir}/%{module}/backends/Matplotlib.nib/*.nib
%{py_sitedir}/%{module}/backends/web_backend
%{py_sitedir}/%{module}/compat
%{py_sitedir}/%{module}/delaunay
%{py_sitedir}/%{module}/externals
%{py_sitedir}/%{module}/mpl-data
%{py_sitedir}/%{module}/projections
%{py_sitedir}/%{module}/sphinxext
%{py_sitedir}/%{module}/style
%{py_sitedir}/%{module}/testing
%{py_sitedir}/%{module}/tri

%{py_sitedir}/mpl_toolkits
%{py_sitedir}/pylab.py[co]
%if "%{py_ver}" > "2.4"
%{py_sitedir}/%{module}-*.egg-info
%{py_sitedir}/%{module}-*.pth
%endif
%endif

%if %{with python3}
%files -n python3-%{module}
%defattr(644,root,root,755)
%doc CHANGELOG README.rst
%dir %{py3_sitedir}/%{module}
%{py3_sitedir}/%{module}/*.py
%{py3_sitedir}/%{module}/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/*.so
%dir %{py3_sitedir}/%{module}/axes
%{py3_sitedir}/%{module}/axes/*.py
%{py3_sitedir}/%{module}/axes/__pycache__
%dir %{py3_sitedir}/%{module}/backends
%{py3_sitedir}/%{module}/backends/*.py
%{py3_sitedir}/%{module}/backends/__pycache__
%attr(755,root,root) %{py3_sitedir}/%{module}/backends/*.so
%dir %{py3_sitedir}/%{module}/backends/qt_editor
%{py3_sitedir}/%{module}/backends/qt_editor/*.py
%{py3_sitedir}/%{module}/backends/qt_editor/__pycache__
%dir %{py3_sitedir}/%{module}/backends/Matplotlib.nib
%{py3_sitedir}/%{module}/backends/Matplotlib.nib/*.nib
%{py3_sitedir}/%{module}/backends/web_backend
%{py3_sitedir}/%{module}/compat
%{py3_sitedir}/%{module}/delaunay
%{py3_sitedir}/%{module}/externals
%{py3_sitedir}/%{module}/mpl-data
%{py3_sitedir}/%{module}/projections
%{py3_sitedir}/%{module}/sphinxext
%{py3_sitedir}/%{module}/style
%{py3_sitedir}/%{module}/testing
%{py3_sitedir}/%{module}/tri
%{py3_sitedir}/mpl_toolkits
%{py3_sitedir}/pylab.py
%{py3_sitedir}/__pycache__
%{py3_sitedir}/%{module}-*.egg-info
%{py3_sitedir}/%{module}-*.pth
%endif
