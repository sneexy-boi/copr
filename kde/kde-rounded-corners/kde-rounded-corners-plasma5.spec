%global oname kde-rounded-corners

Name:           kde-rounded-corners-plasma5
Version:        0.6.1
Release:        4%{?dist}
Summary:        Rounds the corners of your windows in KDE Plasma

License:        GPL-3.0-only
URL:            https://github.com/matinlotfali/KDE-Rounded-Corners
Source:         %{url}/archive/v%{version}/%{oname}-%{version}.tar.gz

BuildRequires:  cmake
BuildRequires:  extra-cmake-modules
BuildRequires:  gcc-c++
BuildRequires:  kf5-rpm-macros

BuildRequires:  cmake(KF5Config)
BuildRequires:  cmake(KF5ConfigWidgets)
BuildRequires:  cmake(KF5CoreAddons)
BuildRequires:  cmake(KF5GlobalAccel)
BuildRequires:  cmake(KF5KCMUtils)
BuildRequires:  cmake(KF5WindowSystem)

BuildRequires:  cmake(Qt5Core)
BuildRequires:  cmake(Qt5DBus)
BuildRequires:  cmake(Qt5Gui)
BuildRequires:  cmake(Qt5Network)
BuildRequires:  cmake(Qt5OpenGL)
BuildRequires:  cmake(Qt5Widgets)
BuildRequires:  cmake(Qt5Xml)
BuildRequires:  qt5-qtbase-private-devel

BuildRequires:  cmake(KWin)
BuildRequires:  cmake(KWinDBusInterface)
BuildRequires:  pkgconfig(epoxy)
BuildRequires:  pkgconfig(xcb)

Conflicts:      kde-rounded-corners
Provides:       kde-rounded-corners = %{version}

%description
%{summary}.

%prep
%autosetup -n KDE-Rounded-Corners-%{version} -p1

%build
%cmake_kf5 -DQT_MAJOR_VERSION=5
%cmake_build

%install
%cmake_install

%files
%license LICENSE
%doc README.md
%{_kf5_datadir}/kwin/shaders/shapecorners*.frag
%{_qt5_plugindir}/kwin/effects/configs/kwin_shapecorners_config.so
%{_qt5_plugindir}/kwin/effects/plugins/kwin4_effect_shapecorners.so

%changelog
* Tue Mar 19 2024 Ruben R. <sneexy@amogus.cloud>
- Backport for KDE Plasma 5

* Fri Jan 12 2024 Pavel Solovev <daron439@gmail.com>
- Initial build
