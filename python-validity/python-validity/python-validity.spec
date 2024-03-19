%global selinuxtype targeted
%global selinux_policyver 3.14.3-22
%global modulename python3-validity

%global pypi_name validity
%define _unitdir %{_exec_prefix}/lib/systemd/system

Name:           python-%{pypi_name}
Version:        0.14
Release:        4%{?dist}
Summary:        Validity fingerprint sensor driver

License:        MIT
URL:            https://github.com/uunicorn/%{name}
Source0:        https://github.com/uunicorn/%{name}/archive/refs/heads/master.tar.gz#/%{name}-%{version}.tar.gz
# restart python3-validity after resume
Source1:        python3-validity-restart-after-resume.service
Patch0:         python-validity-0.12-restart-always.patch
BuildArch:      noarch

Requires:       selinux-policy >= %{selinux_policyver}
BuildRequires:  selinux-policy
BuildRequires:  selinux-policy-devel
BuildRequires:  selinux-policy-%{selinuxtype}
# must be in copr builds
BuildRequires:  systemd-rpm-macros
Requires(post): selinux-policy-base >= %{selinux_policyver}


%description
Validity fingerprint sensor driver. Git version.


%package -n python3-%{pypi_name}
Summary:        %{summary}

BuildRequires:  python3-devel
BuildRequires:  python3-setuptools
BuildRequires:  policycoreutils
BuildRequires:  checkpolicy
BuildRequires:  bzip2
Requires:       policycoreutils
Requires:       innoextract
Requires:       open-fprintd
%{?python_provide:%python_provide python3-%{pypi_name}}


%description -n python3-%{pypi_name}
Validity fingerprint sensor driver.


%prep
%autosetup -n %{name}-%{version} -p1


%build
%py3_build

cd selinux
checkmodule -M -m -o python3-validity.mod python3-validity.te
semodule_package -o python3-validity.pp -m python3-validity.mod
bzip2 python3-validity.pp
cd ..

%pre
%selinux_relabel_pre -s %{selinuxtype}

%install
%py3_install

install -d -m 0700 %{buildroot}%{_sysconfdir}/python-validity
install -d -m 0755 %{buildroot}%{_unitdir}/
install -d -m 0755 %{buildroot}%{_prefix}/lib/udev/rules.d
install -d -m 0755 %{buildroot}%{_datadir}/selinux/packages

install -m 0600 etc/python-validity/dbus-service.yaml %{buildroot}%{_sysconfdir}/python-validity/
install -m 0644 debian/python3-validity.service %{buildroot}%{_unitdir}/
install -m 0644 %{SOURCE1} %{buildroot}%{_unitdir}/
install -m 0644 debian/python3-validity.udev %{buildroot}%{_prefix}/lib/udev/rules.d/40-python3-validity.udev
install -m 0644 selinux/python3-validity.pp.bz2 %{buildroot}%{_datadir}/selinux/packages/

%post -n python3-%{pypi_name}
%selinux_modules_install -s %{selinuxtype} %{_datadir}/selinux/packages/%{modulename}.pp.bz2
validity-sensors-firmware || true
systemctl daemon-reload
udevadm control --reload-rules 
udevadm trigger
%systemd_post python3-validity.service python3-validity-restart-after-resume.service


%preun -n python3-%{pypi_name}
%systemd_preun python3-validity.service python3-validity-restart-after-resume.service


%postun -n python3-%{pypi_name}
%systemd_postun_with_restart python3-validity.service python3-validity-restart-after-resume.service
if [ $1 -eq 0 ]; then
    %selinux_modules_uninstall -s %{selinuxtype} %{modulename}
fi

%posttrans
%selinux_relabel_post -s %{selinuxtype}

%files -n python3-%{pypi_name}
%doc README.md
%license LICENSE
%config(noreplace) %{_sysconfdir}/python-validity/dbus-service.yaml
%{_prefix}/lib/systemd/system/python3-validity.service
%{_prefix}/lib/systemd/system/python3-validity-restart-after-resume.service
%{_prefix}/lib/udev/rules.d/40-python3-validity.udev
%{python3_sitelib}/validitysensor/
%{python3_sitelib}/python_%{pypi_name}-%{version}-py*.egg-info/
%{_bindir}/validity-led-dance
%{_bindir}/validity-sensors-firmware
%{_exec_prefix}/lib/%{name}/dbus-service
%{_datadir}/dbus-1/system.d/io.github.uunicorn.Fprint.conf
%{_datadir}/%{name}/
%{_datadir}/selinux/packages/python3-validity.pp.bz2


%changelog
* Mon Mar 18 2024 Ruben R. <sneexy@amogus.cloud> - 0.14.4
- Edit specs to grab sources remotely

* Wed Jan 31 2024 Ruben R. <sneexy@amogus.cloud> - 0.14-3
- hopefully build from git

* Mon Apr  3 2023 Arkady L. Shane <ashejn@gmail.com> - 0.14-2
- rebuilt for fedora 38

* Sun Jun 19 2022 Arkady L. Shane <ashejn@gmail.com> - 0.14-1
- update to 0.14
- apply all upstream patches

* Tue Apr 26 2022 Arkady L. Shane <ashejn@gmail.com> - 0.13-2
- add service to restart python3-validy after resume

* Sun Apr  3 2022 Arkady L. Shane <ashejn@gmail.com> - 0.13-1
- update to 0.13

* Tue Aug  3 2021 Arkady L. Shane <ashejn@gmail.com> - 0.12-6
- Unsafe load() call disabled by Gentoo. See bug #65934

* Mon Jul  5 2021 Arkady L. Shane <ashejn@gmail.com> - 0.12-5
- add systemd-rpm-macros package to expand macros

* Mon Jul  5 2021 Arkady L. Shane <ashejn@gmail.com> - 0.12-4
- apply some new selinux hooks
- drop some true exits

* Tue Jun 22 2021 Arkady L. Shane <ashejn@gmail.com> - 0.12-3
- always restart service

* Wed Jun 16 2021 Arkady L. Shane <ashejn@gmail.com> - 0.12-2
- skip possible transaction errors

* Tue Nov 03 2020 Veit Wahlich <cru@zodia.de> - 0.12-1
- Initial build.
