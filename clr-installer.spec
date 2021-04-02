#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-installer
Version  : 2.7.2
Release  : 68
URL      : https://github.com/clearlinux/clr-installer/archive/2.7.2.tar.gz
Source0  : https://github.com/clearlinux/clr-installer/archive/2.7.2.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause GPL-3.0 ISC MIT
Requires: clr-installer-bin = %{version}-%{release}
Requires: clr-installer-data = %{version}-%{release}
Requires: clr-installer-license = %{version}-%{release}
Requires: clr-installer-services = %{version}-%{release}
BuildRequires : buildreq-golang
BuildRequires : glib-dev
BuildRequires : gtk3-dev

%description
# Clear Linux Installer
## Clear Linux OS Security
As the installer is a part of the Clear Linux OS distribution, this program follows the [Clear Linux OS Security processes](https://clearlinux.org/documentation/clear-linux/concepts/security).

%package bin
Summary: bin components for the clr-installer package.
Group: Binaries
Requires: clr-installer-data = %{version}-%{release}
Requires: clr-installer-license = %{version}-%{release}
Requires: clr-installer-services = %{version}-%{release}

%description bin
bin components for the clr-installer package.


%package data
Summary: data components for the clr-installer package.
Group: Data

%description data
data components for the clr-installer package.


%package extras
Summary: extras components for the clr-installer package.
Group: Default

%description extras
extras components for the clr-installer package.


%package license
Summary: license components for the clr-installer package.
Group: Default

%description license
license components for the clr-installer package.


%package services
Summary: services components for the clr-installer package.
Group: Systemd services

%description services
services components for the clr-installer package.


%prep
%setup -q -n clr-installer-2.7.2
cd %{_builddir}/clr-installer-2.7.2

%build
## build_prepend content
export GOFLAGS='-buildmode=pie'
## build_prepend end
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1612402531
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$FFLAGS -fno-lto "
export FFLAGS="$FFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1612402531
rm -rf %{buildroot}
## install_prepend content
export GOFLAGS='-buildmode=pie'
## install_prepend end
mkdir -p %{buildroot}/usr/share/package-licenses/clr-installer
cp %{_builddir}/clr-installer-2.7.2/COPYING %{buildroot}/usr/share/package-licenses/clr-installer/22273f3aad3947215054b423975932fc74575723
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/GehirnInc/crypt/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/e0726e45bac3188bf1729c2a20287fcd7a70c519
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/VladimirMarkelov/clui/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/27872e16fa2fec2b104134e269ebe79055ccbfc7
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/VladimirMarkelov/clui/LICENSE.BSD-2-Clause %{buildroot}/usr/share/package-licenses/clr-installer/e63f2b80da76bde6a70d82e7cecbba5d6a76edd6
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/atotto/clipboard/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/5485efdb8b4f1167116feb7f4df9798329000329
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/coreos/go-systemd/v22/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/172ca3bbafe312a1cf09cfff26953db2f425c28e
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/digitalocean/go-smbios/LICENSE.md %{buildroot}/usr/share/package-licenses/clr-installer/fea2174f095f21c24ebd4c9866166ead2bbc25d0
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/godbus/dbus/v5/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/994658c265db5dbf456fa6163905cc9c0b3bda46
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/gotk3/gotk3/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/2ef5b754654f3a15a60406433ef1eb9cdf5c358e
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/huandu/xstrings/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/8758b52c623c08eff9cadbd0f0e1541085e9984d
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/leonelquinteros/gotext/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/f4c26c28c2455b6a57bc272711025451e88dcf7e
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/mattn/go-runewidth/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/5ca808f075931c5322193d4afd5a3370c824f810
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/nightlyone/lockfile/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/f1289fc146b47bf6df99ffbba66318dc951d7efb
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/nsf/termbox-go/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/c920b3ea022bef40a99a9cc0768985d691010fb0
cp %{_builddir}/clr-installer-2.7.2/vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/b3c86ae465b21f7323059db335158b48187731c7
cp %{_builddir}/clr-installer-2.7.2/vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/clr-installer-2.7.2/vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/clr-installer-2.7.2/vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/d6a5f1ecaedd723c325a2063375b3517e808a2b5
cp %{_builddir}/clr-installer-2.7.2/vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/92170cdc034b2ff819323ff670d3b7266c8bffcd
cp %{_builddir}/clr-installer-2.7.2/vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/clr-installer/ad00ce7340d89dc13ccc59920ef75cb55af5b164
cp %{_builddir}/clr-installer-2.7.2/vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/clr-installer/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-installer

%files data
%defattr(-,root,root,-)
/usr/share/bash-completion/completions/clr-installer
/usr/share/clr-installer/iso_templates/initrd_init_template
/usr/share/clr-installer/iso_templates/isolinux.cfg.template
/usr/share/clr-installer/themes/clr-installer.theme
/usr/share/clr-installer/themes/high-contrast.theme
/usr/share/clr-installer/themes/style.css
/usr/share/defaults/clr-installer/bundles.json
/usr/share/defaults/clr-installer/chpasswd
/usr/share/defaults/clr-installer/clr-installer.yaml
/usr/share/defaults/clr-installer/kernels.json
/usr/share/locale/en_US/LC_MESSAGES/clr-installer.po
/usr/share/locale/es_MX/LC_MESSAGES/clr-installer.po
/usr/share/locale/zh_CN/LC_MESSAGES/clr-installer.po
/usr/share/zsh/site-functions/_clr-installer

%files extras
%defattr(-,root,root,-)
/usr/bin/clr-installer-gui
/usr/share/applications/clr-installer-gui.desktop
/usr/share/clr-installer/themes/clr.png
/usr/share/polkit-1/actions/org.clearlinux.clr-installer-gui.policy
/usr/share/polkit-1/rules.d/org.clearlinux.clr-installer-gui.rules

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-installer/172ca3bbafe312a1cf09cfff26953db2f425c28e
/usr/share/package-licenses/clr-installer/22273f3aad3947215054b423975932fc74575723
/usr/share/package-licenses/clr-installer/27872e16fa2fec2b104134e269ebe79055ccbfc7
/usr/share/package-licenses/clr-installer/2ef5b754654f3a15a60406433ef1eb9cdf5c358e
/usr/share/package-licenses/clr-installer/5485efdb8b4f1167116feb7f4df9798329000329
/usr/share/package-licenses/clr-installer/5ca808f075931c5322193d4afd5a3370c824f810
/usr/share/package-licenses/clr-installer/8758b52c623c08eff9cadbd0f0e1541085e9984d
/usr/share/package-licenses/clr-installer/92170cdc034b2ff819323ff670d3b7266c8bffcd
/usr/share/package-licenses/clr-installer/9522d95b2b9b284285cc3fb6ecc445aa3ee5e785
/usr/share/package-licenses/clr-installer/994658c265db5dbf456fa6163905cc9c0b3bda46
/usr/share/package-licenses/clr-installer/ad00ce7340d89dc13ccc59920ef75cb55af5b164
/usr/share/package-licenses/clr-installer/b3c86ae465b21f7323059db335158b48187731c7
/usr/share/package-licenses/clr-installer/c920b3ea022bef40a99a9cc0768985d691010fb0
/usr/share/package-licenses/clr-installer/d6a5f1ecaedd723c325a2063375b3517e808a2b5
/usr/share/package-licenses/clr-installer/e0726e45bac3188bf1729c2a20287fcd7a70c519
/usr/share/package-licenses/clr-installer/e63f2b80da76bde6a70d82e7cecbba5d6a76edd6
/usr/share/package-licenses/clr-installer/f1289fc146b47bf6df99ffbba66318dc951d7efb
/usr/share/package-licenses/clr-installer/f4c26c28c2455b6a57bc272711025451e88dcf7e
/usr/share/package-licenses/clr-installer/fea2174f095f21c24ebd4c9866166ead2bbc25d0

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/clr-installer-provision.service
