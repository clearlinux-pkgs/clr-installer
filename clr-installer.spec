#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : clr-installer
Version  : 2.0.0
Release  : 26
URL      : https://github.com/clearlinux/clr-installer/archive/2.0.0.tar.gz
Source0  : https://github.com/clearlinux/clr-installer/archive/2.0.0.tar.gz
Summary  : No detailed summary available
Group    : Development/Tools
License  : Apache-2.0 BSD-2-Clause BSD-3-Clause GPL-3.0 MIT
Requires: clr-installer-bin = %{version}-%{release}
Requires: clr-installer-data = %{version}-%{release}
Requires: clr-installer-license = %{version}-%{release}
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


%prep
%setup -q -n clr-installer-2.0.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1557185077
export LDFLAGS="${LDFLAGS} -fno-lto"
make  %{?_smp_mflags}


%install
export SOURCE_DATE_EPOCH=1557185077
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/clr-installer
cp COPYING %{buildroot}/usr/share/package-licenses/clr-installer/COPYING
cp vendor/github.com/VladimirMarkelov/clui/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_VladimirMarkelov_clui_LICENSE
cp vendor/github.com/atotto/clipboard/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_atotto_clipboard_LICENSE
cp vendor/github.com/coreos/go-systemd/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_coreos_go-systemd_LICENSE
cp vendor/github.com/digitalocean/go-smbios/LICENSE.md %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_digitalocean_go-smbios_LICENSE.md
cp vendor/github.com/digitalocean/go-smbios/scripts/license.txt %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_digitalocean_go-smbios_scripts_license.txt
cp vendor/github.com/godbus/dbus/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_godbus_dbus_LICENSE
cp vendor/github.com/huandu/xstrings/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_huandu_xstrings_LICENSE
cp vendor/github.com/leonelquinteros/gotext/LICENSE %{buildroot}/usr/share/package-licenses/clr-installer/vendor_github.com_leonelquinteros_gotext_LICENSE
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
%exclude /usr/bin/clr-installer-gui
/usr/bin/clr-installer

%files data
%defattr(-,root,root,-)
%exclude /usr/share/applications/clr-installer-gui.desktop
%exclude /usr/share/clr-installer/themes/clr.png
%exclude /usr/share/polkit-1/actions/org.clearlinux.clr-installer-gui.policy
%exclude /usr/share/polkit-1/rules.d/org.clearlinux.clr-installer-gui.rules
/usr/share/clr-installer/iso_templates/initrd_init_template
/usr/share/clr-installer/iso_templates/isolinux.cfg.template
/usr/share/clr-installer/themes/clr-installer.theme
/usr/share/clr-installer/themes/style.css
/usr/share/defaults/clr-installer/bundles.json
/usr/share/defaults/clr-installer/chpasswd
/usr/share/defaults/clr-installer/clr-installer.yaml
/usr/share/defaults/clr-installer/kernels.json
/usr/share/locale/en_US/LC_MESSAGES/clr-installer.po
/usr/share/locale/es_MX/LC_MESSAGES/clr-installer.po
/usr/share/locale/zh_CN/LC_MESSAGES/clr-installer.po

%files extras
%defattr(-,root,root,-)
/usr/bin/clr-installer-gui
/usr/share/applications/clr-installer-gui.desktop
/usr/share/clr-installer/themes/clr.png
/usr/share/polkit-1/actions/org.clearlinux.clr-installer-gui.policy
/usr/share/polkit-1/rules.d/org.clearlinux.clr-installer-gui.rules

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/clr-installer/COPYING
/usr/share/package-licenses/clr-installer/vendor_github.com_VladimirMarkelov_clui_LICENSE
/usr/share/package-licenses/clr-installer/vendor_github.com_atotto_clipboard_LICENSE
/usr/share/package-licenses/clr-installer/vendor_github.com_coreos_go-systemd_LICENSE
/usr/share/package-licenses/clr-installer/vendor_github.com_digitalocean_go-smbios_LICENSE.md
/usr/share/package-licenses/clr-installer/vendor_github.com_digitalocean_go-smbios_scripts_license.txt
/usr/share/package-licenses/clr-installer/vendor_github.com_godbus_dbus_LICENSE
/usr/share/package-licenses/clr-installer/vendor_github.com_huandu_xstrings_LICENSE
/usr/share/package-licenses/clr-installer/vendor_github.com_leonelquinteros_gotext_LICENSE
/usr/share/package-licenses/clr-installer/vendor_github.com_mattn_go-runewidth_LICENSE
/usr/share/package-licenses/clr-installer/vendor_github.com_nsf_termbox-go_LICENSE
/usr/share/package-licenses/clr-installer/vendor_github.com_spf13_pflag_LICENSE
/usr/share/package-licenses/clr-installer/vendor_golang.org_x_crypto_LICENSE
/usr/share/package-licenses/clr-installer/vendor_golang.org_x_sys_LICENSE
/usr/share/package-licenses/clr-installer/vendor_golang.org_x_text_LICENSE
/usr/share/package-licenses/clr-installer/vendor_gopkg.in_yaml.v2_LICENSE
/usr/share/package-licenses/clr-installer/vendor_gopkg.in_yaml.v2_LICENSE.libyaml
/usr/share/package-licenses/clr-installer/vendor_gopkg.in_yaml.v2_NOTICE
