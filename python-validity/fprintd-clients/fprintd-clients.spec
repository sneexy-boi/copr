%define orig_name fprintd

Name:		fprintd-clients
Version:	1.94.5
Release:	1%{?dist}
Epoch:		1
Summary:	Clients for D-Bus service for Fingerprint reader access

License:	GPLv2+
Source0:	https://gitlab.freedesktop.org/libfprint/fprintd/-/archive/v%{version}/fprintd-v%{version}.tar.gz
Url:		http://www.freedesktop.org/wiki/Software/fprint/fprintd
ExcludeArch:	s390 s390x

Obsoletes:	fprintd < %{epoch}:%{version}-%{release}
BuildRequires:	meson
BuildRequires:	gcc
BuildRequires:	gcc-c++
BuildRequires:	git
BuildRequires:	dbus-glib-devel
BuildRequires:	pam-devel
BuildRequires:	libfprint-devel >= 1.90.1
BuildRequires:	polkit-devel
BuildRequires:	gtk-doc
BuildRequires:	gettext
BuildRequires:	perl-podlators
%if 0%{?fedora} > 37
BuildRequires:	pkgconfig(libsystemd)
BuildRequires:	pkgconfig(systemd)
%else
BuildRequires:	systemd-devel
%endif
BuildRequires:	python3-dbusmock
BuildRequires:	python3-libpamtest

%description
D-Bus service to access fingerprint readers.

%package pam
Summary:	PAM module for fingerprint authentication
Requires:	%{name} = %{epoch}:%{version}-%{release}
# Note that we obsolete pam_fprint, but as the configuration
# is different, it will be mentioned in the release notes
Provides:	pam_fprint = %{version}-%{release}
Obsoletes:	pam_fprint < 0.2-3
Obsoletes:	fprintd-pam < %{epoch}:%{version}-%{release}
Requires(postun): authselect >= 0.3

License:	GPLv2+

%description pam
PAM module that uses the fprintd D-Bus service for fingerprint
authentication.

%package devel
Summary:	Development files for %{name}
Requires:	%{name} = %{epoch}:%{version}-%{release}
License:	GFDLv1.1+
BuildArch:	noarch

%description devel
Development documentation for fprintd, the D-Bus service for
fingerprint readers access.

%prep
%autosetup -S git -n %{orig_name}-v%{version}

%build
%meson -Dgtk_doc=true -Dpam=true
%meson_build

%install
%meson_install
mkdir -p $RPM_BUILD_ROOT/%{_localstatedir}/lib/fprint

rm -f $RPM_BUILD_ROOT/%{_libdir}/security/pam_fprintd.{a,la,so.*}

# Remove daemon files:
rm -f $RPM_BUILD_ROOT/%{_libexecdir}/fprintd
rm -f $RPM_BUILD_ROOT/%{_sysconfdir}/fprintd.conf
rm -f $RPM_BUILD_ROOT/%{_datadir}/dbus-1/system.d/net.reactivated.Fprint.conf
rm -f $RPM_BUILD_ROOT/%{_datadir}/dbus-1/system-services/net.reactivated.Fprint.service
rm -f $RPM_BUILD_ROOT//usr/lib/systemd/system/fprintd.service

%find_lang %{orig_name}

%postun pam
if [ $1 -eq 0 ]; then
  /bin/authselect disable-feature with-fingerprint || :
fi

%files -f %{orig_name}.lang
%doc README COPYING AUTHORS TODO
%{_bindir}/fprintd-*
%{_datadir}/polkit-1/actions/net.reactivated.fprint.device.policy
%{_localstatedir}/lib/fprint
%{_mandir}/man1/fprintd.1.gz

%files pam
%doc pam/README
%{_libdir}/security/pam_fprintd.so
%{_mandir}/man8/pam_fprintd.8.gz

%files devel
%{_datadir}/gtk-doc/
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Device.xml
%{_datadir}/dbus-1/interfaces/net.reactivated.Fprint.Manager.xml

%changelog
* Thu Jun 12 2025 Ruben R. <sneexy@amogus.cloud> - 1.94.5-1
- Bump to fprintd-clients v1.94.5

* Mon Mar 18 2024 Ruben R. <sneexy@amogus.cloud> - 1.94.2-3
- Edit specs to grab sources remotely

* Mon Apr  3 2023 Arkady L. Shane <ashejn@gmail.com> - 1.94.2-2
- fix build for Fedora 38, thanks a lot Patryk Obara

* Mon Apr  4 2022 Arkady L. Shane <ashejn@gmail.com> - 1.94.2-1
- update to 1.94.2

* Thu Oct 21 2021 Arkady L. Shane <ashejn@gmail.com> - 1.94.0-1
- update to 1.94.0

* Fri May 14 2021 Arkady L. Shane <ashejn@gmail.com> - 1.90.9-1
- Repackaged fprintd 1.90.1-2 without the daemon to use clients with open-fprintd
  thnaks to Veit Wahlich <cru@zodia.de>

* Wed Jan 13 13:33:37 CET 2021 Benjamin Berg <bberg@redhat.com> - 1.90.9-1
- Update to 1.90.9 (#1915788)
  Resolves: #1909669
  Resolves: #1909559

* Fri Dec 18 2020 Adam Williamson <awilliam@redhat.com> - 1.90.8-2
- Rebuild for libnss dependency issue

* Fri Dec 11 2020 Benjamin Berg <bberg@redhat.com> - 1.90.8-1
- Update to 1.90.8 (#1902255)
  This fixes PAM not working when fprintd was just started

* Wed Dec 09 2020 Benjamin Berg <bberg@redhat.com> - 1.90.7-1
- Update to 1.90.7 (#1902255)
  Resolves: #1905667
  Resolves: #1905964

* Mon Dec 07 2020 Benjamin Berg <bberg@redhat.com> - 1.90.6-1
- Update to 1.90.6 (#1902255)
  Resolves: #1904370

* Tue Dec 01 2020 Benjamin Berg <bberg@redhat.com> - 1.90.5-1
- Update to 1.90.5 (#1902255)

* Wed Nov 04 2020 Veit Wahlich <cru@zodia.de> - 1.90.1-2
- Repackaged fprintd 1.90.1-2 without the daemon to use clients with open-fprintd.

* Mon Jul 27 2020 Fedora Release Engineering <releng@fedoraproject.org> - 1.90.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_33_Mass_Rebuild

* Mon Feb 10 2020 Bastien Nocera <bnocera@redhat.com> - 1.90.1-1
+ fprintd-1.90.1-1
- Update to 1.90.1

* Tue Jan 28 2020 Fedora Release Engineering <releng@fedoraproject.org> - 0.9.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_32_Mass_Rebuild

* Wed Aug 14 2019 Benjamin Berg <bberg@redhat.com> - 0.9.0-1
+ fprintd-0.9.0-1
- Update to 0.9.0
- Add patch to fix length check of rhost

* Thu Jul 25 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-5
- Rebuilt for https://fedoraproject.org/wiki/Fedora_31_Mass_Rebuild

* Thu Jan 31 2019 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_30_Mass_Rebuild

* Fri Jul 20 2018 Bastien Nocera <bnocera@redhat.com> - 0.8.1-3
+ fprintd-0.8.1-3
- Fix missing .service file in files by installing systemd

* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Fri Jun 15 2018 Bastien Nocera <bnocera@redhat.com> - 0.8.1-1
+ fprintd-0.8.1-1
- Update to 0.8.1
- Fixes a possible crash on exit (#1515720)

* Wed May 30 2018 Bastien Nocera <bnocera@redhat.com> - 0.8.0-4
+ fprintd-0.8.0-4
- Rebuild

* Tue Feb 20 2018 Pavel Březina <pbrezina@redhat.com> - 0.8.0-3
+ fprintd-0.8.0-3
- Switch from authconfig to authselect

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0.8.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Sep 13 2017 Bastien Nocera <bnocera@redhat.com> - 0.8.0-1
+ fprintd-0.8.0-1
- Update to 0.8.0

* Wed Aug 02 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Binutils_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 0.7.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Thu Feb 09 2017 Bastien Nocera <bnocera@redhat.com> - 0.7.0-2
+ fprintd-0.7.0-2
- Fix fprintd-pam being disabled after upgrade (#1398371)

* Wed Oct 12 2016 Bastien Nocera <bnocera@redhat.com> - 0.7.0-1
+ fprintd-0.7.0-1
- Update to 0.7.0

* Thu Sep 22 2016 Bastien Nocera <bnocera@redhat.com> - 0.6.0-5
- Fix warning when uninstalling fprintd-pam (#1203671)

* Wed Feb 03 2016 Fedora Release Engineering <releng@fedoraproject.org> - 0.6.0-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.6.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Feb 21 2015 Till Maas <opensource@till.name> - 0.6.0-2
- Rebuilt for Fedora 23 Change
  https://fedoraproject.org/wiki/Changes/Harden_all_packages_with_position-independent_code

* Tue Feb 03 2015 Bastien Nocera <bnocera@redhat.com> 0.6.0-1
- Update to 0.6.0

* Sat Aug 16 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_22_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sun Aug 11 2013 Bastien Nocera <bnocera@redhat.com> 0.5.1-1
- Update to 0.5.1

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.5.0-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Tue Mar 05 2013 Bastien Nocera <bnocera@redhat.com> 0.5.0-1
- Update to 0.5.0

* Tue Feb 19 2013 Bastien Nocera <bnocera@redhat.com> 0.4.1-5
- Co-own the gtk-doc directory (#604351)

* Wed Feb 13 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-4
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.4.1-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Thu Nov 10 2011 Bastien Nocera <bnocera@redhat.com> 0.4.1-1
- Update to 0.4.1

* Tue Feb 08 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2.0-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Tue Nov 09 2010 Ray Strode <rstrode@redhat.com> 0.2.0-2
- Don't allow pam module to ever get unmapped, since that causes
  crashes in dbus-glib, gobject, etc.

* Thu Aug 19 2010 Bastien Nocera <bnocera@redhat.com> 0.2.0-1
- Update to 0.2.0

* Wed Dec 09 2009 Bastien Nocera <bnocera@redhat.com> 0.1-16.git04fd09cfa
- Remove use of g_error(), or people think that it crashes when we actually
  abort() (#543194)

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-15.git04fd09cfa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Jul 21 2009 Bastien Nocera <bnocera@redhat.com> 0.1-14.git04fd09cfa
- Merge polkit patch and fix for polkit patch

* Tue Jul 21 2009 Bastien Nocera <bnocera@redhat.com> 0.1-13.git04fd09cfa
- Make the -devel package noarch (#507698)

* Thu Jul  9 2009 Matthias Clasen <mclasen@redhat.com> 0.1-12.git04fd09cfa
- Fix the pam module (#510152)

* Sat Jun 20 2009 Bastien Nocera <bnocera@redhat.com> 0.1-11.git04fd09cfa
- Remove obsolete patch

* Tue Jun 9 2009 Matthias Clasen <mclasen@redhat.com> 0.1-10.git04fd09cfa
- Port to PolicyKit 1

* Thu May 07 2009 Bastien Nocera <bnocera@redhat.com> 0.1-9.git04fd09cfa
- Add /var/lib/fprint to the RPM to avoid SELinux errors (#499513)

* Tue Apr 21 2009 Karsten Hopp <karsten@redhat.com> 0.1-8.git04fd09cfa.1
- Excludearch s390 s390x, as we don't have libusb1 on mainframe, we can't build
  the required libfprint package

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.1-8.git04fd09cfa
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Tue Jan 27 2009 - Bastien Nocera <bnocera@redhat.com> - 0.1-7.git04fd09cfa
- Add a patch to handle device disconnects

* Mon Jan 26 2009 - Bastien Nocera <bnocera@redhat.com> - 0.1-6.git04fd09cfa
- Update to latest git, fixes some run-time warnings

* Wed Dec 17 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1-5.git43fe72a2aa
- Add patch to stop leaking a D-Bus connection on failure

* Tue Dec 09 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1-4.git43fe72a2aa
- Update D-Bus config file for recent D-Bus changes

* Thu Dec 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1-3.git43fe72a2aa
- Update following comments in the review

* Sun Nov 23 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1-2.gitaf42ec70f3
- Update to current git master, and add documentation

* Tue Nov 04 2008 - Bastien Nocera <bnocera@redhat.com> - 0.1-1
- First package

