%define openfprintdlibdir %{_exec_prefix}/lib/open-fprintd
%define _unitdir %{_exec_prefix}/lib/systemd/system

Name:           open-fprintd
Version:        0.7
Release:        1%{?dist}
Summary:        Replacement of package fprintd for standalone backend services

License:        GPLv2
URL:            https://github.com/uunicorn/%{name}
Source0:        https://github.com/uunicorn/%{name}/archive/refs/tags/0.7.tar.gz#/%{name}-%{version}.tar.gz
# restart open-fprint after resume
Source1:        open-fprintd-restart-after-resume.service

BuildArch:      noarch

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
# must be in copr builds
BuildRequires:	systemd-rpm-macros

Requires:       fprintd-clients
Provides:       fprintd

%description
Replacement of package fprintd which allows you to have your own backend as a
standalone service.

%prep
%autosetup -n %{name}-%{version}

%build
%py3_build

%install
%py3_install

install -d -m 0755 %{buildroot}/%{_unitdir}
install -m 0644 debian/open-fprintd.service %{buildroot}/%{_unitdir}/
install -m 0644 debian/open-fprintd-suspend.service %{buildroot}/%{_unitdir}/
install -m 0644 debian/open-fprintd-resume.service %{buildroot}/%{_unitdir}/
install -m 0644 %{SOURCE1} %{buildroot}/%{_unitdir}/

%post
%systemd_post open-fprintd.service open-fprintd-restart-after-resume.service

%preun
%systemd_preun open-fprintd.service open-fprintd-restart-after-resume.service

%postun
%systemd_postun_with_restart open-fprintd.service open-fprintd-restart-after-resume.service

%files
%doc README.md
%license COPYING
%{python3_sitelib}/openfprintd/
%{python3_sitelib}/open_fprintd-%{version}-py*.egg-info/
%{openfprintdlibdir}/open-fprintd
%{openfprintdlibdir}/suspend.py
%{openfprintdlibdir}/resume.py
%{_unitdir}/%{name}*.service
%{_datadir}/dbus-1/system-services/net.reactivated.Fprint.service
%{_datadir}/dbus-1/system.d/net.reactivated.Fprint.conf

%changelog
* Thur Jun 12 2025 Ruben R. <sneexy@amogus.cloud> - 0.7-1
- Bump to open-fprintd 0.7

* Mon Mar 18 2024 Ruben R. <sneexy@amogus.cloud> - 0.12-8
- Edit specs to grab sources remotely

* Mon Apr  3 2023 Arkady L. Shane <ashejn@gmail.com> - 0.12-7
- rebuilt for Fedora 38

* Tue Apr 26 2022 Arkady L. Shane <ashejn@gmail.com> - 0.12-6
- retsart open-fprint after resume

* Wed Jul 14 2021 Arkady L. Shane <ashejn@gmail.com> - 0.12-5
- add systemd-rpm-macros package to expand macros

* Wed Jul 14 2021 Arkady L. Shane <ashejn@gmail.com> - 0.12-4
- fix typo

* Wed Jul 14 2021 Arkady L. Shane <ashejn@gmail.com> - 0.12-3
- update systemd scripts

* Wed Jun 16 2021 Arkady L. Shane <ashejn@gmail.com> - 0.12-2
- skip possible transaction errors

* Tue Nov 03 2020 Veit Wahlich <cru@zodia.de> - 0.6-1
- Initial build.
