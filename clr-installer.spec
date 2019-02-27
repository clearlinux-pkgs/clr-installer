#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-installer
Version  : 1.1.6
Release  : 16
URL      : https://github.com/clearlinux/clr-installer/archive/1.1.6.tar.gz
Source0  : https://github.com/clearlinux/clr-installer/archive/1.1.6.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-3-Clause GPL-3.0 MIT
Requires: clr-installer-bin = %{version}-%{release}
Requires: clr-installer-data = %{version}-%{release}
Requires: clr-installer-license = %{version}-%{release}
Requires: clr-installer-services = %{version}-%{release}
BuildRequires : buildreq-golang

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
%setup -q -n clr-installer-1.1.6

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1551297199
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1551297199
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-installer
cp COPYING %{buildroot}/usr/share/package-licenses/clr-installer/COPYING
cp vendor/github.com/VladimirMarkelov/clui/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_VladimirMarkelov_clui_LICENSE
cp vendor/github.com/atotto/clipboard/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_atotto_clipboard_LICENSE
cp vendor/github.com/digitalocean/go-smbios/LICENSE.md %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_digitalocean_go-smbios_LICENSE.md
cp vendor/github.com/digitalocean/go-smbios/scripts/license.txt %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_digitalocean_go-smbios_scripts_license.txt
cp vendor/github.com/huandu/xstrings/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_huandu_xstrings_LICENSE
cp vendor/github.com/mattn/go-runewidth/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_mattn_go-runewidth_LICENSE
cp vendor/github.com/nsf/termbox-go/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_nsf_termbox-go_LICENSE
cp vendor/github.com/spf13/pflag/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_spf13_pflag_LICENSE
cp vendor/golang.org/x/crypto/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_golang.org_x_crypto_LICENSE
cp vendor/golang.org/x/sys/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_golang.org_x_sys_LICENSE
cp vendor/golang.org/x/text/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_golang.org_x_text_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_gopkg.in_yaml.v2_LICENSE
cp vendor/gopkg.in/yaml.v2/LICENSE.libyaml %{buildroot}/usr/share/package-licenses/clr-installer/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
cp vendor/gopkg.in/yaml.v2/NOTICE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_gopkg.in_yaml.v2_NOTICE
%make_install

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/clr-installer
/usr/bin/clr-installer-desktop.sh

%files data
%defattr(-,root,root,-)
/usr/share/applications/clr-installer.desktop
/usr/share/clr-installer/themes/clr-installer.theme
/usr/share/defaults/clr-installer/bundles.json
/usr/share/defaults/clr-installer/chpasswd
/usr/share/defaults/clr-installer/clr-installer.yaml
/usr/share/defaults/clr-installer/kernels.json

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-installer/COPYING
/usr/share/package-licenses/clr-installer/vendor_github.com_VladimirMarkelov_clui_LICENSE
/usr/share/package-licenses/clr-installer/vendor_github.com_atotto_clipboard_LICENSE
/usr/share/package-licenses/clr-installer/vendor_github.com_digitalocean_go-smbios_LICENSE.md
/usr/share/package-licenses/clr-installer/vendor_github.com_digitalocean_go-smbios_scripts_license.txt
/usr/share/package-licenses/clr-installer/vendor_github.com_huandu_xstrings_LICENSE
/usr/share/package-licenses/clr-installer/vendor_github.com_mattn_go-runewidth_LICENSE
/usr/share/package-licenses/clr-installer/vendor_github.com_nsf_termbox-go_LICENSE
/usr/share/package-licenses/clr-installer/vendor_github.com_spf13_pflag_LICENSE
/usr/share/package-licenses/clr-installer/vendor_golang.org_x_crypto_LICENSE
/usr/share/package-licenses/clr-installer/vendor_golang.org_x_sys_LICENSE
/usr/share/package-licenses/clr-installer/vendor_golang.org_x_text_LICENSE
/usr/share/package-licenses/clr-installer/vendor_gopkg.in_yaml.v2_LICENSE
/usr/share/package-licenses/clr-installer/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
/usr/share/package-licenses/clr-installer/vendor_gopkg.in_yaml.v2_NOTICE

%files services
%defattr(-,root,root,-)
/usr/lib/systemd/system/clr-installer.service
