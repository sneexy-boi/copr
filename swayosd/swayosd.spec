%global   forgeurl https://github.com/ErikReider/SwayOSD/
%global   branch main

Name:           swayosd
Version:        main
%forgemeta
Release:        1%{?dist}
Summary:        A GTK based on screen display for keyboard shortcuts like caps-lock and volume

License:        GPLv3
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  sassc
BuildRequires:  gtk-layer-shell-devel
BuildRequires:  g++
BuildRequires:  cargo
BuildRequires:  ninja-build
BuildRequires:  rust-gdk0.17-devel
BuildRequires:  rust-libudev-sys-devel
BuildRequires:  rust-cascade-devel
BuildRequires:  rust-zbus-devel
BuildRequires:  rust-lazy_static-devel
BuildRequires:  rust-memmem-devel
BuildRequires:  rust-input-sys-devel
BuildRequires:  rust-libc-devel
BuildRequires:  rust-input-linux-devel
BuildRequires:  rust-async-std-devel
BuildRequires:  rust-nix-devel
BuildRequires:  rust-anyhow-devel
BuildRequires:  rust-thiserror-devel
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-client) >= 1.14.91
BuildRequires:  pkgconfig(libpulse)

Requires:       gtk3
Requires:       gtk-layer-shell

Suggests:       swaync

%description
A OSD window for common actions like volume and capslock.


%prep
%forgeautosetup -p1


%build
%meson
%meson_build

%install
%meson_install


%check


%files
%license LICENSE
%doc README.md
%{_bindir}/*


%changelog
* Fri Feb 23 2024 Ruben Rivera <sneexy@disroot.org> - main-1
- Inital Creation
