%define		kdeplasmaver	5.11.0
%define		qtver		5.3.2
%define		kpname		breeze-gtk
Summary:	Artwork, styles and assets for the Breeze visual style for the Plasma Desktop
Name:		kp5-%{kpname}
Version:	5.11.0
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Libraries
Source0:	http://download.kde.org/stable/plasma/%{kdeplasmaver}/%{kpname}-%{version}.tar.xz
# Source0-md5:	f31f75aea26eed544c8a33db77de2f5c
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
BuildRequires:	kp5-kdecoration-devel
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	qt5-qmake
BuildRequires:	rpmbuild(macros) >= 1.596
BuildRequires:	tar >= 1:1.22
BuildRequires:	xz
Requires:	%{kpname}-cursor-theme = %{version}-%{release}
Requires:	%{kpname}-icon-theme = %{version}-%{release}
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
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n %{kpname}-icon-theme
Breeze is an icon theme.

%description -n %{kpname}-icon-theme -l pl.UTF-8
Breeze to motyw ikon.

%package -n %{kpname}-cursor-theme
Summary:	Breeze cursor theme
Group:		Themes
Conflicts:	breeze-icon-theme < 5.4.0-7
Conflicts:	kp5-breeze < 5.4.0-5
%if "%{_rpmversion}" >= "5"
BuildArch:	noarch
%endif

%description -n %{kpname}-cursor-theme
Breeze cursor theme.

%prep
%setup -q -n %{kpname}-%{version}

%build
install -d build
cd build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post
%update_icon_cache hicolor

%postun
%update_icon_cache hicolor

%files
%defattr(644,root,root,755)
%{_libdir}/kconf_update_bin/gtkbreeze5.5
%{_datadir}/kconf_update/gtkbreeze5.5.upd
%{_datadir}/themes/Breeze-Dark/assets/arrow-down-active.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-down-hover.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-down-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-down.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-left-active.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-left-hover.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-left-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-left.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-right-active.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-right-hover.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-right-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-right.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-down-active.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-down-hover.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-down-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-down.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-left-active.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-left-hover.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-left-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-left.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-right-active.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-right-hover.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-right-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-right.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-up-active.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-up-hover.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-up-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-small-up.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-up-active.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-up-hover.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-up-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/arrow-up.png
%{_datadir}/themes/Breeze-Dark/assets/button-active.png
%{_datadir}/themes/Breeze-Dark/assets/button-hover.png
%{_datadir}/themes/Breeze-Dark/assets/button-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/button.png
%{_datadir}/themes/Breeze-Dark/assets/check-checked-active.png
%{_datadir}/themes/Breeze-Dark/assets/check-checked-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-checked-backdrop-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/check-checked-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-checked-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/check-checked-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-checked-hover.png
%{_datadir}/themes/Breeze-Dark/assets/check-checked-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-checked-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/check-checked-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-mixed-active.png
%{_datadir}/themes/Breeze-Dark/assets/check-mixed-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-mixed-backdrop-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/check-mixed-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-mixed-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/check-mixed-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-mixed-hover.png
%{_datadir}/themes/Breeze-Dark/assets/check-mixed-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-mixed-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/check-mixed-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-checked-active.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-checked-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-checked-backdrop-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-checked-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-checked-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-checked-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-checked-hover.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-checked-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-checked-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-checked-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-unchecked-active.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-unchecked-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-unchecked-backdrop-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-unchecked-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-unchecked-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-unchecked-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-unchecked-hover.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-unchecked-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-unchecked-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-unchecked-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-unchecked.png
%{_datadir}/themes/Breeze-Dark/assets/check-selectionmode-unchecked@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-unchecked-active.png
%{_datadir}/themes/Breeze-Dark/assets/check-unchecked-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-unchecked-backdrop-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/check-unchecked-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-unchecked-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/check-unchecked-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-unchecked-hover.png
%{_datadir}/themes/Breeze-Dark/assets/check-unchecked-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-unchecked-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/check-unchecked-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/check-unchecked.png
%{_datadir}/themes/Breeze-Dark/assets/check-unchecked@2.png
%{_datadir}/themes/Breeze-Dark/assets/combo-entry-active.png
%{_datadir}/themes/Breeze-Dark/assets/combo-entry-button-active.png
%{_datadir}/themes/Breeze-Dark/assets/combo-entry-button-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/combo-entry-button.png
%{_datadir}/themes/Breeze-Dark/assets/combo-entry-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/combo-entry.png
%{_datadir}/themes/Breeze-Dark/assets/entry-active.png
%{_datadir}/themes/Breeze-Dark/assets/entry-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/entry.png
%{_datadir}/themes/Breeze-Dark/assets/frame-gap-end.png
%{_datadir}/themes/Breeze-Dark/assets/frame-gap-start.png
%{_datadir}/themes/Breeze-Dark/assets/frame.png
%{_datadir}/themes/Breeze-Dark/assets/handle-h.png
%{_datadir}/themes/Breeze-Dark/assets/handle-v.png
%{_datadir}/themes/Breeze-Dark/assets/line-h.png
%{_datadir}/themes/Breeze-Dark/assets/line-v.png
%{_datadir}/themes/Breeze-Dark/assets/menu-arrow-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/menu-arrow-selected.png
%{_datadir}/themes/Breeze-Dark/assets/menu-arrow.png
%{_datadir}/themes/Breeze-Dark/assets/menubar-button.png
%{_datadir}/themes/Breeze-Dark/assets/notebook-frame-bottom.png
%{_datadir}/themes/Breeze-Dark/assets/notebook-frame-right.png
%{_datadir}/themes/Breeze-Dark/assets/notebook-frame-top.png
%{_datadir}/themes/Breeze-Dark/assets/notebook-gap-horizontal.png
%{_datadir}/themes/Breeze-Dark/assets/notebook-gap-vertical.png
%{_datadir}/themes/Breeze-Dark/assets/null.png
%{_datadir}/themes/Breeze-Dark/assets/progressbar-bar.png
%{_datadir}/themes/Breeze-Dark/assets/progressbar-trough.png
%{_datadir}/themes/Breeze-Dark/assets/radio-checked-active.png
%{_datadir}/themes/Breeze-Dark/assets/radio-checked-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-checked-backdrop-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/radio-checked-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-checked-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/radio-checked-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-checked-hover.png
%{_datadir}/themes/Breeze-Dark/assets/radio-checked-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-checked-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/radio-checked-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-mixed-active.png
%{_datadir}/themes/Breeze-Dark/assets/radio-mixed-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-mixed-backdrop-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/radio-mixed-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-mixed-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/radio-mixed-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-mixed-hover.png
%{_datadir}/themes/Breeze-Dark/assets/radio-mixed-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-mixed-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/radio-mixed-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-unchecked-active.png
%{_datadir}/themes/Breeze-Dark/assets/radio-unchecked-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-unchecked-backdrop-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/radio-unchecked-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-unchecked-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/radio-unchecked-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-unchecked-hover.png
%{_datadir}/themes/Breeze-Dark/assets/radio-unchecked-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-unchecked-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/radio-unchecked-insensitive@2.png
%{_datadir}/themes/Breeze-Dark/assets/radio-unchecked.png
%{_datadir}/themes/Breeze-Dark/assets/radio-unchecked@2.png
%{_datadir}/themes/Breeze-Dark/assets/scale-slider-active.png
%{_datadir}/themes/Breeze-Dark/assets/scale-slider-hover.png
%{_datadir}/themes/Breeze-Dark/assets/scale-slider-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/scale-slider.png
%{_datadir}/themes/Breeze-Dark/assets/scale-trough-horizontal.png
%{_datadir}/themes/Breeze-Dark/assets/scale-trough-vertical.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-slider-horizontal-active.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-slider-horizontal-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-slider-horizontal-hover.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-slider-horizontal-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-slider-horizontal.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-slider-horizontal@2.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-slider-vertical-active.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-slider-vertical-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-slider-vertical-hover.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-slider-vertical-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-slider-vertical.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-slider-vertical@2.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-trough-horizontal.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-trough-horizontal@2.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-trough-vertical.png
%{_datadir}/themes/Breeze-Dark/assets/scrollbar-trough-vertical@2.png
%{_datadir}/themes/Breeze-Dark/assets/spinbutton-down-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/spinbutton-down-rtl-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/spinbutton-down-rtl.png
%{_datadir}/themes/Breeze-Dark/assets/spinbutton-down.png
%{_datadir}/themes/Breeze-Dark/assets/spinbutton-up-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/spinbutton-up-rtl-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/spinbutton-up-rtl.png
%{_datadir}/themes/Breeze-Dark/assets/spinbutton-up.png
%{_datadir}/themes/Breeze-Dark/assets/tab-bottom-active.png
%{_datadir}/themes/Breeze-Dark/assets/tab-bottom-inactive.png
%{_datadir}/themes/Breeze-Dark/assets/tab-left-active.png
%{_datadir}/themes/Breeze-Dark/assets/tab-left-inactive.png
%{_datadir}/themes/Breeze-Dark/assets/tab-right-active.png
%{_datadir}/themes/Breeze-Dark/assets/tab-right-inactive.png
%{_datadir}/themes/Breeze-Dark/assets/tab-top-active.png
%{_datadir}/themes/Breeze-Dark/assets/tab-top-inactive.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-close-active-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-close-active-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-close-active.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-close-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-close-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-close-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-close-hover-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-close-hover-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-close-hover.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-close-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-close.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-close@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-active-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-active-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-active.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-hover-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-hover-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-hover.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-active-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-active-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-active.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-hover-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-hover-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-hover.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-maximized-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-maximized.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize-maximized@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-maximize@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-minimize-active-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-minimize-active-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-minimize-active.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-minimize-active@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-minimize-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-minimize-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-minimize-hover-backdrop.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-minimize-hover-backdrop@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-minimize-hover.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-minimize-hover@2.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-minimize.png
%{_datadir}/themes/Breeze-Dark/assets/titlebutton-minimize@2.png
%{_datadir}/themes/Breeze-Dark/assets/togglebutton-active.png
%{_datadir}/themes/Breeze-Dark/assets/togglebutton-hover.png
%{_datadir}/themes/Breeze-Dark/assets/togglebutton-insensitive.png
%{_datadir}/themes/Breeze-Dark/assets/togglebutton.png
%{_datadir}/themes/Breeze-Dark/assets/toolbar-background.png
%{_datadir}/themes/Breeze-Dark/assets/toolbutton-active.png
%{_datadir}/themes/Breeze-Dark/assets/toolbutton-hover.png
%{_datadir}/themes/Breeze-Dark/assets/toolbutton-toggled.png
%{_datadir}/themes/Breeze-Dark/assets/tree-header.png
%{_datadir}/themes/Breeze-Dark/gtk-2.0/gtkrc
%{_datadir}/themes/Breeze-Dark/gtk-2.0/widgets/buttons
%{_datadir}/themes/Breeze-Dark/gtk-2.0/widgets/default
%{_datadir}/themes/Breeze-Dark/gtk-2.0/widgets/entry
%{_datadir}/themes/Breeze-Dark/gtk-2.0/widgets/menu
%{_datadir}/themes/Breeze-Dark/gtk-2.0/widgets/misc
%{_datadir}/themes/Breeze-Dark/gtk-2.0/widgets/notebook
%{_datadir}/themes/Breeze-Dark/gtk-2.0/widgets/progressbar
%{_datadir}/themes/Breeze-Dark/gtk-2.0/widgets/range
%{_datadir}/themes/Breeze-Dark/gtk-2.0/widgets/scrollbar
%{_datadir}/themes/Breeze-Dark/gtk-2.0/widgets/styles
%{_datadir}/themes/Breeze-Dark/gtk-2.0/widgets/toolbar
%{_datadir}/themes/Breeze-Dark/gtk-3.0/gtk.css
%{_datadir}/themes/Breeze-Dark/gtk-3.18/gtk.css
%{_datadir}/themes/Breeze-Dark/gtk-3.20/gtk.css
%{_datadir}/themes/Breeze/assets/arrow-down-active.png
%{_datadir}/themes/Breeze/assets/arrow-down-hover.png
%{_datadir}/themes/Breeze/assets/arrow-down-insensitive.png
%{_datadir}/themes/Breeze/assets/arrow-down.png
%{_datadir}/themes/Breeze/assets/arrow-left-active.png
%{_datadir}/themes/Breeze/assets/arrow-left-hover.png
%{_datadir}/themes/Breeze/assets/arrow-left-insensitive.png
%{_datadir}/themes/Breeze/assets/arrow-left.png
%{_datadir}/themes/Breeze/assets/arrow-right-active.png
%{_datadir}/themes/Breeze/assets/arrow-right-hover.png
%{_datadir}/themes/Breeze/assets/arrow-right-insensitive.png
%{_datadir}/themes/Breeze/assets/arrow-right.png
%{_datadir}/themes/Breeze/assets/arrow-small-down-active.png
%{_datadir}/themes/Breeze/assets/arrow-small-down-hover.png
%{_datadir}/themes/Breeze/assets/arrow-small-down-insensitive.png
%{_datadir}/themes/Breeze/assets/arrow-small-down.png
%{_datadir}/themes/Breeze/assets/arrow-small-left-active.png
%{_datadir}/themes/Breeze/assets/arrow-small-left-hover.png
%{_datadir}/themes/Breeze/assets/arrow-small-left-insensitive.png
%{_datadir}/themes/Breeze/assets/arrow-small-left.png
%{_datadir}/themes/Breeze/assets/arrow-small-right-active.png
%{_datadir}/themes/Breeze/assets/arrow-small-right-hover.png
%{_datadir}/themes/Breeze/assets/arrow-small-right-insensitive.png
%{_datadir}/themes/Breeze/assets/arrow-small-right.png
%{_datadir}/themes/Breeze/assets/arrow-small-up-active.png
%{_datadir}/themes/Breeze/assets/arrow-small-up-hover.png
%{_datadir}/themes/Breeze/assets/arrow-small-up-insensitive.png
%{_datadir}/themes/Breeze/assets/arrow-small-up.png
%{_datadir}/themes/Breeze/assets/arrow-up-active.png
%{_datadir}/themes/Breeze/assets/arrow-up-hover.png
%{_datadir}/themes/Breeze/assets/arrow-up-insensitive.png
%{_datadir}/themes/Breeze/assets/arrow-up.png
%{_datadir}/themes/Breeze/assets/button-active.png
%{_datadir}/themes/Breeze/assets/button-hover.png
%{_datadir}/themes/Breeze/assets/button-insensitive.png
%{_datadir}/themes/Breeze/assets/button.png
%{_datadir}/themes/Breeze/assets/check-checked-active.png
%{_datadir}/themes/Breeze/assets/check-checked-active@2.png
%{_datadir}/themes/Breeze/assets/check-checked-backdrop-insensitive.png
%{_datadir}/themes/Breeze/assets/check-checked-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze/assets/check-checked-backdrop.png
%{_datadir}/themes/Breeze/assets/check-checked-backdrop@2.png
%{_datadir}/themes/Breeze/assets/check-checked-hover.png
%{_datadir}/themes/Breeze/assets/check-checked-hover@2.png
%{_datadir}/themes/Breeze/assets/check-checked-insensitive.png
%{_datadir}/themes/Breeze/assets/check-checked-insensitive@2.png
%{_datadir}/themes/Breeze/assets/check-mixed-active.png
%{_datadir}/themes/Breeze/assets/check-mixed-active@2.png
%{_datadir}/themes/Breeze/assets/check-mixed-backdrop-insensitive.png
%{_datadir}/themes/Breeze/assets/check-mixed-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze/assets/check-mixed-backdrop.png
%{_datadir}/themes/Breeze/assets/check-mixed-backdrop@2.png
%{_datadir}/themes/Breeze/assets/check-mixed-hover.png
%{_datadir}/themes/Breeze/assets/check-mixed-hover@2.png
%{_datadir}/themes/Breeze/assets/check-mixed-insensitive.png
%{_datadir}/themes/Breeze/assets/check-mixed-insensitive@2.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-checked-active.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-checked-active@2.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-checked-backdrop-insensitive.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-checked-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-checked-backdrop.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-checked-backdrop@2.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-checked-hover.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-checked-hover@2.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-checked-insensitive.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-checked-insensitive@2.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-unchecked-active.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-unchecked-active@2.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-unchecked-backdrop-insensitive.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-unchecked-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-unchecked-backdrop.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-unchecked-backdrop@2.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-unchecked-hover.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-unchecked-hover@2.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-unchecked-insensitive.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-unchecked-insensitive@2.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-unchecked.png
%{_datadir}/themes/Breeze/assets/check-selectionmode-unchecked@2.png
%{_datadir}/themes/Breeze/assets/check-unchecked-active.png
%{_datadir}/themes/Breeze/assets/check-unchecked-active@2.png
%{_datadir}/themes/Breeze/assets/check-unchecked-backdrop-insensitive.png
%{_datadir}/themes/Breeze/assets/check-unchecked-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze/assets/check-unchecked-backdrop.png
%{_datadir}/themes/Breeze/assets/check-unchecked-backdrop@2.png
%{_datadir}/themes/Breeze/assets/check-unchecked-hover.png
%{_datadir}/themes/Breeze/assets/check-unchecked-hover@2.png
%{_datadir}/themes/Breeze/assets/check-unchecked-insensitive.png
%{_datadir}/themes/Breeze/assets/check-unchecked-insensitive@2.png
%{_datadir}/themes/Breeze/assets/check-unchecked.png
%{_datadir}/themes/Breeze/assets/check-unchecked@2.png
%{_datadir}/themes/Breeze/assets/combo-entry-active.png
%{_datadir}/themes/Breeze/assets/combo-entry-button-active.png
%{_datadir}/themes/Breeze/assets/combo-entry-button-insensitive.png
%{_datadir}/themes/Breeze/assets/combo-entry-button.png
%{_datadir}/themes/Breeze/assets/combo-entry-insensitive.png
%{_datadir}/themes/Breeze/assets/combo-entry.png
%{_datadir}/themes/Breeze/assets/entry-active.png
%{_datadir}/themes/Breeze/assets/entry-insensitive.png
%{_datadir}/themes/Breeze/assets/entry.png
%{_datadir}/themes/Breeze/assets/frame-gap-end.png
%{_datadir}/themes/Breeze/assets/frame-gap-start.png
%{_datadir}/themes/Breeze/assets/frame.png
%{_datadir}/themes/Breeze/assets/handle-h.png
%{_datadir}/themes/Breeze/assets/handle-v.png
%{_datadir}/themes/Breeze/assets/line-h.png
%{_datadir}/themes/Breeze/assets/line-v.png
%{_datadir}/themes/Breeze/assets/menu-arrow-insensitive.png
%{_datadir}/themes/Breeze/assets/menu-arrow-selected.png
%{_datadir}/themes/Breeze/assets/menu-arrow.png
%{_datadir}/themes/Breeze/assets/menubar-button.png
%{_datadir}/themes/Breeze/assets/notebook-frame-bottom.png
%{_datadir}/themes/Breeze/assets/notebook-frame-right.png
%{_datadir}/themes/Breeze/assets/notebook-frame-top.png
%{_datadir}/themes/Breeze/assets/notebook-gap-horizontal.png
%{_datadir}/themes/Breeze/assets/notebook-gap-vertical.png
%{_datadir}/themes/Breeze/assets/null.png
%{_datadir}/themes/Breeze/assets/progressbar-bar.png
%{_datadir}/themes/Breeze/assets/progressbar-trough.png
%{_datadir}/themes/Breeze/assets/radio-checked-active.png
%{_datadir}/themes/Breeze/assets/radio-checked-active@2.png
%{_datadir}/themes/Breeze/assets/radio-checked-backdrop-insensitive.png
%{_datadir}/themes/Breeze/assets/radio-checked-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze/assets/radio-checked-backdrop.png
%{_datadir}/themes/Breeze/assets/radio-checked-backdrop@2.png
%{_datadir}/themes/Breeze/assets/radio-checked-hover.png
%{_datadir}/themes/Breeze/assets/radio-checked-hover@2.png
%{_datadir}/themes/Breeze/assets/radio-checked-insensitive.png
%{_datadir}/themes/Breeze/assets/radio-checked-insensitive@2.png
%{_datadir}/themes/Breeze/assets/radio-mixed-active.png
%{_datadir}/themes/Breeze/assets/radio-mixed-active@2.png
%{_datadir}/themes/Breeze/assets/radio-mixed-backdrop-insensitive.png
%{_datadir}/themes/Breeze/assets/radio-mixed-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze/assets/radio-mixed-backdrop.png
%{_datadir}/themes/Breeze/assets/radio-mixed-backdrop@2.png
%{_datadir}/themes/Breeze/assets/radio-mixed-hover.png
%{_datadir}/themes/Breeze/assets/radio-mixed-hover@2.png
%{_datadir}/themes/Breeze/assets/radio-mixed-insensitive.png
%{_datadir}/themes/Breeze/assets/radio-mixed-insensitive@2.png
%{_datadir}/themes/Breeze/assets/radio-unchecked-active.png
%{_datadir}/themes/Breeze/assets/radio-unchecked-active@2.png
%{_datadir}/themes/Breeze/assets/radio-unchecked-backdrop-insensitive.png
%{_datadir}/themes/Breeze/assets/radio-unchecked-backdrop-insensitive@2.png
%{_datadir}/themes/Breeze/assets/radio-unchecked-backdrop.png
%{_datadir}/themes/Breeze/assets/radio-unchecked-backdrop@2.png
%{_datadir}/themes/Breeze/assets/radio-unchecked-hover.png
%{_datadir}/themes/Breeze/assets/radio-unchecked-hover@2.png
%{_datadir}/themes/Breeze/assets/radio-unchecked-insensitive.png
%{_datadir}/themes/Breeze/assets/radio-unchecked-insensitive@2.png
%{_datadir}/themes/Breeze/assets/radio-unchecked.png
%{_datadir}/themes/Breeze/assets/radio-unchecked@2.png
%{_datadir}/themes/Breeze/assets/scale-slider-active.png
%{_datadir}/themes/Breeze/assets/scale-slider-hover.png
%{_datadir}/themes/Breeze/assets/scale-slider-insensitive.png
%{_datadir}/themes/Breeze/assets/scale-slider.png
%{_datadir}/themes/Breeze/assets/scale-trough-horizontal.png
%{_datadir}/themes/Breeze/assets/scale-trough-vertical.png
%{_datadir}/themes/Breeze/assets/scrollbar-slider-horizontal-active.png
%{_datadir}/themes/Breeze/assets/scrollbar-slider-horizontal-active@2.png
%{_datadir}/themes/Breeze/assets/scrollbar-slider-horizontal-hover.png
%{_datadir}/themes/Breeze/assets/scrollbar-slider-horizontal-hover@2.png
%{_datadir}/themes/Breeze/assets/scrollbar-slider-horizontal.png
%{_datadir}/themes/Breeze/assets/scrollbar-slider-horizontal@2.png
%{_datadir}/themes/Breeze/assets/scrollbar-slider-vertical-active.png
%{_datadir}/themes/Breeze/assets/scrollbar-slider-vertical-active@2.png
%{_datadir}/themes/Breeze/assets/scrollbar-slider-vertical-hover.png
%{_datadir}/themes/Breeze/assets/scrollbar-slider-vertical-hover@2.png
%{_datadir}/themes/Breeze/assets/scrollbar-slider-vertical.png
%{_datadir}/themes/Breeze/assets/scrollbar-slider-vertical@2.png
%{_datadir}/themes/Breeze/assets/scrollbar-trough-horizontal.png
%{_datadir}/themes/Breeze/assets/scrollbar-trough-horizontal@2.png
%{_datadir}/themes/Breeze/assets/scrollbar-trough-vertical.png
%{_datadir}/themes/Breeze/assets/scrollbar-trough-vertical@2.png
%{_datadir}/themes/Breeze/assets/spinbutton-down-insensitive.png
%{_datadir}/themes/Breeze/assets/spinbutton-down-rtl-insensitive.png
%{_datadir}/themes/Breeze/assets/spinbutton-down-rtl.png
%{_datadir}/themes/Breeze/assets/spinbutton-down.png
%{_datadir}/themes/Breeze/assets/spinbutton-up-insensitive.png
%{_datadir}/themes/Breeze/assets/spinbutton-up-rtl-insensitive.png
%{_datadir}/themes/Breeze/assets/spinbutton-up-rtl.png
%{_datadir}/themes/Breeze/assets/spinbutton-up.png
%{_datadir}/themes/Breeze/assets/tab-bottom-active.png
%{_datadir}/themes/Breeze/assets/tab-bottom-inactive.png
%{_datadir}/themes/Breeze/assets/tab-left-active.png
%{_datadir}/themes/Breeze/assets/tab-left-inactive.png
%{_datadir}/themes/Breeze/assets/tab-right-active.png
%{_datadir}/themes/Breeze/assets/tab-right-inactive.png
%{_datadir}/themes/Breeze/assets/tab-top-active.png
%{_datadir}/themes/Breeze/assets/tab-top-inactive.png
%{_datadir}/themes/Breeze/assets/titlebutton-close-active-backdrop.png
%{_datadir}/themes/Breeze/assets/titlebutton-close-active-backdrop@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-close-active.png
%{_datadir}/themes/Breeze/assets/titlebutton-close-active@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-close-backdrop.png
%{_datadir}/themes/Breeze/assets/titlebutton-close-backdrop@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-close-hover-backdrop.png
%{_datadir}/themes/Breeze/assets/titlebutton-close-hover-backdrop@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-close-hover.png
%{_datadir}/themes/Breeze/assets/titlebutton-close-hover@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-close.png
%{_datadir}/themes/Breeze/assets/titlebutton-close@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-active-backdrop.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-active-backdrop@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-active.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-active@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-backdrop.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-backdrop@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-hover-backdrop.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-hover-backdrop@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-hover.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-hover@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-maximized-active-backdrop.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-maximized-active-backdrop@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-maximized-active.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-maximized-active@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-maximized-backdrop.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-maximized-backdrop@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-maximized-hover-backdrop.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-maximized-hover-backdrop@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-maximized-hover.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-maximized-hover@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-maximized.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize-maximized@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize.png
%{_datadir}/themes/Breeze/assets/titlebutton-maximize@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-minimize-active-backdrop.png
%{_datadir}/themes/Breeze/assets/titlebutton-minimize-active-backdrop@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-minimize-active.png
%{_datadir}/themes/Breeze/assets/titlebutton-minimize-active@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-minimize-backdrop.png
%{_datadir}/themes/Breeze/assets/titlebutton-minimize-backdrop@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-minimize-hover-backdrop.png
%{_datadir}/themes/Breeze/assets/titlebutton-minimize-hover-backdrop@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-minimize-hover.png
%{_datadir}/themes/Breeze/assets/titlebutton-minimize-hover@2.png
%{_datadir}/themes/Breeze/assets/titlebutton-minimize.png
%{_datadir}/themes/Breeze/assets/titlebutton-minimize@2.png
%{_datadir}/themes/Breeze/assets/togglebutton-active.png
%{_datadir}/themes/Breeze/assets/togglebutton-hover.png
%{_datadir}/themes/Breeze/assets/togglebutton-insensitive.png
%{_datadir}/themes/Breeze/assets/togglebutton.png
%{_datadir}/themes/Breeze/assets/toolbar-background.png
%{_datadir}/themes/Breeze/assets/toolbutton-active.png
%{_datadir}/themes/Breeze/assets/toolbutton-hover.png
%{_datadir}/themes/Breeze/assets/toolbutton-toggled.png
%{_datadir}/themes/Breeze/assets/tree-header.png
%{_datadir}/themes/Breeze/gtk-2.0/gtkrc
%{_datadir}/themes/Breeze/gtk-2.0/widgets/buttons
%{_datadir}/themes/Breeze/gtk-2.0/widgets/default
%{_datadir}/themes/Breeze/gtk-2.0/widgets/entry
%{_datadir}/themes/Breeze/gtk-2.0/widgets/menu
%{_datadir}/themes/Breeze/gtk-2.0/widgets/misc
%{_datadir}/themes/Breeze/gtk-2.0/widgets/notebook
%{_datadir}/themes/Breeze/gtk-2.0/widgets/progressbar
%{_datadir}/themes/Breeze/gtk-2.0/widgets/range
%{_datadir}/themes/Breeze/gtk-2.0/widgets/scrollbar
%{_datadir}/themes/Breeze/gtk-2.0/widgets/styles
%{_datadir}/themes/Breeze/gtk-2.0/widgets/toolbar
%{_datadir}/themes/Breeze/gtk-3.0/gtk.css
%{_datadir}/themes/Breeze/gtk-3.18/gtk.css
%{_datadir}/themes/Breeze/gtk-3.20/gtk.css
