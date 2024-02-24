# Original spec from https://gitlab.com/tofik-rpms/sway/
%global forgeurl https://github.com/ErikReider/SwayNotificationCenter
%global alt_pkg_name SwayNotificationCenter

Name:           swaync
Version:        0.10.0
%forgemeta
Release:        1%{?dist}
Summary:        Notification daemon with GTK GUI
Provides:       desktop-notification-daemon
Provides:       sway-notification-center = %{version}-%{release}
Provides:       %{alt_pkg_name} = %{version}-%{release}
License:        GPLv3
URL:            %{forgeurl}
Source:         %{forgesource}

BuildRequires:  meson >= 0.51.0
BuildRequires:  vala
BuildRequires:  sassc
BuildRequires:  granite-devel
BuildRequires:  scdoc
BuildRequires:  pkgconfig(gtk+-3.0) >= 3.22
BuildRequires:  pkgconfig(gtk-layer-shell-0) >= 0.1
BuildRequires:  pkgconfig(json-glib-1.0) >= 1.0
BuildRequires:  pkgconfig(libhandy-1) >= 1.4.0
BuildRequires:  pkgconfig(glib-2.0) >= 2.50
BuildRequires:  pkgconfig(gobject-introspection-1.0) >= 1.68
BuildRequires:  pkgconfig(gee-0.8) >= 0.20
BuildRequires:  pkgconfig(bash-completion)
BuildRequires:  pkgconfig(fish)
BuildRequires:  pkgconfig(libpulse)
BuildRequires:  systemd-devel
BuildRequires:  systemd

Requires:       dbus
Requires:       gtk3
Requires:       gtk-layer-shell
%{?systemd_requires}

%description
A simple GTK based notification daemon for SwayWM

%package bash-completion
BuildArch:      noarch
Summary:        Bash completion files for %{name}
Provides:       %{alt_pkg_name}-bash-completion = %{version}-%{release}

Requires:       bash
Requires:       %{name} = %{version}-%{release}

%description bash-completion
This package installs Bash completion files for %{name}

%package zsh-completion
BuildArch:      noarch
Summary:        Zsh completion files for %{name}
Provides:       %{alt_pkg_name}-bash-completion = %{version}-%{release}

Requires:       zsh
Requires:       %{name} = %{version}-%{release}

%description zsh-completion
This package installs Zsh completion files for %{name}

%package fish-completion
BuildArch:      noarch
Summary:        Fish completion files for %{name}
Provides:       %{alt_pkg_name}-bash-completion = %{version}-%{release}

Requires:       fish
Requires:       %{name} = %{version}-%{release}

%description fish-completion
This package installs Fish completion files for %{name}


%prep
%forgeautosetup

%build
%meson
%meson_build

%install
%meson_install

%post
%systemd_user_post swaync.service

%preun
%systemd_user_preun swaync.service

%files
%doc README.md
%{_bindir}/swaync-client
%{_bindir}/swaync
%license COPYING
%config(noreplace) %{_sysconfdir}/xdg/swaync/configSchema.json
%config(noreplace) %{_sysconfdir}/xdg/swaync/config.json
%config(noreplace) %{_sysconfdir}/xdg/swaync/style.css
%{_userunitdir}/swaync.service
%{_datadir}/dbus-1/services/org.erikreider.swaync.service
%{_datadir}/glib-2.0/schemas/org.erikreider.swaync.gschema.xml
%{_mandir}/man1/swaync-client.1.gz
%{_mandir}/man1/swaync.1.gz
%{_mandir}/man5/swaync.5.gz

%files bash-completion
%{_datadir}/bash-completion/completions/swaync
%{_datadir}/bash-completion/completions/swaync-client

%files zsh-completion
%{_datadir}/zsh/site-functions/_swaync
%{_datadir}/zsh/site-functions/_swaync-client

%files fish-completion
%{_datadir}/fish/vendor_completions.d/swaync-client.fish
%{_datadir}/fish/vendor_completions.d/swaync.fish

%changelog
* Fri Feb 23 2024 Ruben Rivera <sneexy@disroot.org> - 0.10.0-2
- Make self modifications to start copr building

* Sat Feb 10 2024 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.10.0-1
- Update to 0.10.0

* Tue May 30 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.9.0-2
- Fixed linter complains
- Consistent Provides: versioning

* Mon May 29 2023 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.9.0-1
- Update to 0.9.0

* Sat Dec 31 2022 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.7.3-2
- Completion subpackages architecture set to: noarch

* Sat Dec 31 2022 Jerzy Drożdż <jerzy.drozdz@jdsieci.pl> - 0.7.3-1
- Initial build

