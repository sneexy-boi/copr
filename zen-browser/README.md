# Zen Browser

[![⚡️ Powered By: Copr](https://img.shields.io/badge/⚡️_Powered_by-COPR-blue?style=flat-square)](https://copr.fedorainfracloud.org/)
![📦 Architecture: x86_64](https://img.shields.io/badge/📦_Architecture-x86__64-blue?style=flat-square)
[![Latest Version](https://img.shields.io/badge/dynamic/json?color=blue&label=Version&query=builds.latest.source_package.version&url=https%3A%2F%2Fcopr.fedorainfracloud.org%2Fapi_3%2Fpackage%3Fownername%3Dsneexy%26projectname%3Dzen-browser%26packagename%3Dzen-browser%26with_latest_build%3DTrue&style=flat-square&logoColor=blue)](https://copr.fedorainfracloud.org/coprs/sneexy/zen-browser/package/zen-browser/)
[![Copr build status](https://copr.fedorainfracloud.org/coprs/sneexy/zen-browser/package/zen-browser/status_image/last_build.png)](https://copr.fedorainfracloud.org/coprs/sneexy/zen-browser/package/zen-browser/)

Automatically up-to-date spec files for the [Zen Browser](https://zen-browser.app/) packaged for Fedora. Forked from my [Floorp](https://copr.fedorainfracloud.org/coprs/sneexy/floorp) package, based on the works from [the4runner](https://github.com/the4runner/firefox-dev) and [LovecraftianGodsKiller](https://github.com/LovecraftianGodsKiller/floorp). The Copr repo for this package [can be located here](https://copr.fedorainfracloud.org/coprs/sneexy/zen-browser).

If you have any issues with the package itself, feel free to report but I may not be able to fix it as this is my first time managing a package such as this. Feel free to contribute if you'd like if you can fix any issues yourself!

## ⚠️ Special Note
This is just an RPM packaging for the said software and does not include any licenses of its own. The only additional file included is the `.desktop` file written based on the original executable from the Firefox Release Channel (default).

## About the Application
This is a package of the Zen web browser. Zen Browser is a fork of Firefox
that aims to improve the browsing experience by focusing on a simple,
performant, private and beautifully designed browser.

Bugs related to Zen should be reported directly to the Zen Browser GitHub repo: 
<https://github.com/zen-browser/desktop/issues>

Bugs related to this package should be reported at this Git project:
<https://github.com/sneexy-boi/copr>

## Installation Instructions
1. Enable `sneexy/zen-browser` [Copr](https://copr.fedorainfracloud.org/) repository according to your package manager.

```Shell
# If you are using dnf... (you need to have 'dnf-plugins-core' installed)
sudo dnf copr enable sneexy/zen-browser

# If you are using yum... (you need to have 'yum-plugins-copr' installed)
sudo yum copr enable sneexy/zen-browser
```

2. (Optional) Update your package list.

```Shell
sudo dnf check-update
```

3. Execute the following command to install the package.

```Shell
sudo dnf install zen-browser
```

4. Launch the application from the Application Menu or execute following command in terminal.

```Shell
zen-browser
```
