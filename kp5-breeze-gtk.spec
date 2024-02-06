#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeplasmaver	5.93.0
%define		qtver		5.15.2
%define		kpname		breeze-gtk
Summary:	Artwork, styles and assets for the Breeze visual style for the Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.93.0
Release:	0.1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	https://download.kde.org/unstable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	70712a12cf4e293be298ae997ddce489
URL:		http://www.kde.org/
BuildRequires:	Qt6Core-devel >= %{qtver}
BuildRequires:	Qt6DBus-devel
BuildRequires:	Qt6Gui-devel
BuildRequires:	Qt6Widgets-devel
BuildRequires:	Qt6Xml-devel
BuildRequires:	cmake >= 3.16.0
BuildRequires:	gettext-devel
BuildRequires:	hardlink >= 1.0-3
BuildRequires:	kf6-attica-devel
BuildRequires:	kf6-extra-cmake-modules >= 1.4.0
BuildRequires:	kf6-frameworkintegration-devel
BuildRequires:	kf6-kauth-devel
BuildRequires:	kf6-kcmutils-devel
BuildRequires:	kf6-kcodecs-devel
BuildRequires:	kf6-kconfig-devel
BuildRequires:	kf6-kconfigwidgets-devel
BuildRequires:	kf6-kcoreaddons-devel
BuildRequires:	kf6-kguiaddons-devel
BuildRequires:	kf6-ki18n-devel
BuildRequires:	kf6-kiconthemes-devel
BuildRequires:	kf6-kservice-devel
BuildRequires:	kf6-kwidgetsaddons-devel
BuildRequires:	kf6-kwindowsystem-devel
BuildRequires:	kp5-breeze-devel
BuildRequires:	kp5-kdecoration-devel >= %{kdeplasmaver}
BuildRequires:	libstdc++-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python3-pycairo-devel
BuildRequires:	qt6-build >= %{qtver}
BuildRequires:	qt6-qmake
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	sassc
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_debugsource_packages	0

%description
Artwork, styles and assets for the Breeze visual style for the Plasma
Desktop.

%package -n %{kpname}-icon-theme
Summary:	Breeze icon theme
Summary(pl.UTF-8):	Breeze Motyw ikon
Group:		Themes
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
Conflicts:	kp5-breeze < 5.4.0-5
BuildArch:	noarch

%description -n %{kpname}-icon-theme
Breeze is an icon theme.

%description -n %{kpname}-icon-theme -l pl.UTF-8
Breeze to motyw ikon.

%package -n %{kpname}-cursor-theme
Summary:	Breeze cursor theme
Group:		Themes
Conflicts:	breeze-icon-theme < 5.4.0-7
Conflicts:	kp5-breeze < 5.4.0-5
BuildArch:	noarch

%description -n %{kpname}-cursor-theme
Breeze cursor theme.

%prep
%setup -q -n %{kpname}-%{version}

%build
%cmake -B build \
	 -G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest
%endif

%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%{_datadir}/themes/Breeze-Dark
%{_datadir}/themes/Breeze
