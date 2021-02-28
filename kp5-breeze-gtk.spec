%define		kdeplasmaver	5.15.3
%define		qtver		5.9.0
%define		kpname		breeze-gtk
Summary:	Artwork, styles and assets for the Breeze visual style for the Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.15.3
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	b369b343d6dd4ef3af6d18340a83f308
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5X11Extras-devel
BuildRequires:	Qt5Xml-devel
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	hardlink >= 1.0-3
BuildRequires:	kf5-attica-devel
BuildRequires:	kf5-extra-cmake-modules >= 1.4.0
BuildRequires:	kf5-frameworkintegration-devel
BuildRequires:	kf5-kauth-devel
BuildRequires:	kf5-kcmutils-devel
BuildRequires:	kf5-kcodecs-devel
BuildRequires:	kf5-kconfig-devel
BuildRequires:	kf5-kconfigwidgets-devel
BuildRequires:	kf5-kcoreaddons-devel
BuildRequires:	kf5-kguiaddons-devel
BuildRequires:	kf5-ki18n-devel
BuildRequires:	kf5-kiconthemes-devel
BuildRequires:	kf5-kservice-devel
BuildRequires:	kf5-kwidgetsaddons-devel
BuildRequires:	kf5-kwindowsystem-devel
BuildRequires:	kp5-breeze-devel
BuildRequires:	kp5-kdecoration-devel >= %{kdeplasmaver}
BuildRequires:	libstdc++-devel
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	python3-pycairo-devel
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	sassc
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	gtk-update-icon-cache
Requires:	hicolor-icon-theme
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

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
install -d build
cd build
%cmake -G Ninja \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

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
%attr(755,root,root) %{_libdir}/kconf_update_bin/gtkbreeze5.5
%{_datadir}/kconf_update/gtkbreeze5.5.upd
%{_datadir}/themes/Breeze-Dark
%{_datadir}/themes/Breeze
