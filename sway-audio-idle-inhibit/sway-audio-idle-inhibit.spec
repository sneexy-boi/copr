%global   forgeurl https://github.com/ErikReider/SwayAudioIdleInhibit

Name:           sway-audio-idle-inhibit
Version:        0.1.1
%forgemeta
Release:        2%{?dist}
Summary:        Prevents swayidle from sleeping while any application is outputting or receiving audio.

License:        GPLv3
URL:            %{forgeurl}
Source0:        %{forgesource}

BuildRequires:  meson
BuildRequires:  vala
BuildRequires:  g++
BuildRequires:  pkgconfig(wayland-protocols)
BuildRequires:  pkgconfig(wayland-client) >= 1.14.91
BuildRequires:  pkgconfig(libpulse)

Recommends:     sway-settings
Suggests:       swaync

%description
Prevents swayidle from sleeping while any application
is outputting or receiving audio. Should work with all Wayland
desktops that support the zwp_idle_inhibit_manager_v1
protocol but only tested in Sway.

This only works for Pulseaudio / Pipewire Pulse


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
* Fri Feb 23 2024 Ruben Rivera <sneexy@disroot.org> - 0.1.1-2
- Minor changes

* Mon Jan 02 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.1.1-1
- Initial build
