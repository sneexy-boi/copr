%global             full_name zen-twilight
%global             application_name zen-twilight
%global             debug_package %{nil}

Name:               zen-twilight
Version:            1.18t.20251026110620
Release:            1%{?dist}
Summary:            Zen Browser (Twilight)

License:            MPLv2.0
URL:                https://github.com/zen-browser/desktop

Source0:            https://github.com/zen-browser/desktop/releases/download/twilight/zen.linux-x86_64.tar.xz
Source1:            %{full_name}.desktop
Source2:            policies.json
Source3:            %{full_name}

ExclusiveArch:      x86_64

BuildRequires:      patchelf

Recommends:         (plasma-browser-integration if plasma-workspace)
Recommends:         (gnome-browser-connector if gnome-shell)

Requires(post):     gtk-update-icon-cache
Conflicts:          zen-twilight-avx2, zen-twilight-arm

Provides: zen-twilight-avx2 = %{version}-%{release}
Obsoletes: zen-twilight-avx2 < 188278485-3

%description
This is a package of the Zen web browser. Zen Browser is a fork of Firefox
that aims to improve the browsing experience by focusing on a simple,
performant, private and beautifully designed browser.

Bugs related to Zen should be reported directly to the Zen Browser GitHub repo: 
<https://github.com/zen-browser/desktop/issues>

Bugs related to this package should be reported at this Git project:
<https://github.com/sneexy-boi/copr>

%prep
%setup -q -n zen
mv zen %{application_name}

%install
%__rm -rf %{buildroot}

%__install -d %{buildroot}{/opt/%{application_name},%{_bindir},%{_datadir}/applications,%{_datadir}/icons/hicolor/128x128/apps,%{_datadir}/icons/hicolor/64x64/apps,%{_datadir}/icons/hicolor/48x48/apps,%{_datadir}/icons/hicolor/32x32/apps,%{_datadir}/icons/hicolor/16x16/apps}

%__cp -r * %{buildroot}/opt/%{application_name}

%__install -D -m 0644 %{SOURCE1} -t %{buildroot}%{_datadir}/applications

%__install -D -m 0444 %{SOURCE2} -t %{buildroot}/opt/%{application_name}/distribution

%__install -D -m 0755 %{SOURCE3} -t %{buildroot}%{_bindir}

patchelf --set-rpath '$ORIGIN' %{buildroot}/opt/%{application_name}/libonnxruntime.so

%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default128.png %{buildroot}%{_datadir}/icons/hicolor/128x128/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default64.png %{buildroot}%{_datadir}/icons/hicolor/64x64/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default48.png %{buildroot}%{_datadir}/icons/hicolor/48x48/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default32.png %{buildroot}%{_datadir}/icons/hicolor/32x32/apps/%{full_name}.png
%__ln_s ../../../../../../opt/%{application_name}/browser/chrome/icons/default/default16.png %{buildroot}%{_datadir}/icons/hicolor/16x16/apps/%{full_name}.png

%post
gtk-update-icon-cache -f -t %{_datadir}/icons/hicolor

%files
%{_datadir}/applications/%{full_name}.desktop
%{_datadir}/icons/hicolor/128x128/apps/%{full_name}.png
%{_datadir}/icons/hicolor/64x64/apps/%{full_name}.png
%{_datadir}/icons/hicolor/48x48/apps/%{full_name}.png
%{_datadir}/icons/hicolor/32x32/apps/%{full_name}.png
%{_datadir}/icons/hicolor/16x16/apps/%{full_name}.png
%{_bindir}/%{full_name}
/opt/%{application_name}

%changelog
* Sat Sep 23 2023 Namelesswonder <Namelesswonder@users.noreply.github.com> - 118.0b9-3
- firefox-developer-edition.spec: Add weak dependency for each DE browser integration

* Tue Sep 12 2023 Namelesswonder <Namelesswonder@users.noreply.github.com> - 118.0b7-2
- firefox-developer-edition.spec: Trim changelog to resolve date warnings and bump release
