# Floorp

[![⚡️ Powered By: Copr](https://img.shields.io/badge/⚡️_Powered_by-COPR-blue?style=flat-square)](https://copr.fedorainfracloud.org/)
![📦 Architecture: x86_64](https://img.shields.io/badge/📦_Architecture-x86__64-blue?style=flat-square)
[![Latest Version](https://img.shields.io/badge/dynamic/json?color=blue&label=Version&query=builds.latest.source_package.version&url=https%3A%2F%2Fcopr.fedorainfracloud.org%2Fapi_3%2Fpackage%3Fownername%3Dsneexy%26projectname%3Dfloorp%26packagename%3Dfloorp%26with_latest_build%3DTrue&style=flat-square&logoColor=blue)](https://copr.fedorainfracloud.org/coprs/sneexy/floorp/package/floorp/)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/sneexy/floorp/package/floorp/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/sneexy/floorp/package/floorp/)

Automatically (hopefully) updated spec files for the [Floorp](https://floorp.app/) browser packaged for Fedora. Based on the works from [the4runner](https://github.com/the4runner/firefox-dev) and [LovecraftianGodsKiller](https://github.com/LovecraftianGodsKiller/floorp). The Copr repo for this package [can be located here](https://copr.fedorainfracloud.org/coprs/sneexy/floorp).

If you have any issues with the package itself, feel free to report but I may not be able to fix it as this is my first time managing a package such as this. Feel free to contribute if you'd like if you can fix any issues yourself!

This package *may or may not* be broken for users on Immutable/Atomic Fedora, although this issue may only be related to users using custom [Universal Blue](https://universal-blue.org/)/[BlueBuild](https://blue-build.org/) images. [You can see my fix here.](https://github.com/sernik-tech/member-images/blob/main/config/scripts/system-wuzetka.sh#L12-L16)

## ⚠️ Special Note
This is just an RPM packaging for the said software and does not include any licenses of its own. The only additional file included is the `.desktop` file written based on the original executable from the Firefox Release Channel (default).

## About the Application
This is a release of the Floorp web browser. Floorp is a fork of Firefox ESR
with additional features aimed to make the overall Firefox Browser experince
better than vanilla Firefox.

Bugs related to Floorp should be reported directly to the Floorp GitHub repo: 
https://https://github.com/Floorp-Projects/Floorp/issues/

Bugs related to this package should be reported at this GitHub project:
https://github.com/sneexy-boi/floorp/issues/

## Installation Instructions
1. Enable `sneexy/floorp` [Copr](https://copr.fedorainfracloud.org/) repository according to your package manager.

```Shell
# If you are using dnf... (you need to have 'dnf-plugins-core' installed)
sudo dnf copr enable sneexy/floorp

# If you are using yum... (you need to have 'yum-plugins-copr' installed)
sudo yum copr enable sneexy/floorp
```

2. (Optional) Update your package list.

```Shell
sudo dnf check-update
```

3. Execute the following command to install the package.

```Shell
sudo dnf install floorp
```

4. Launch the application from the Application Menu or execute following command in terminal.

```Shell
floorp
```
