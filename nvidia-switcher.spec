Name:           nvidia-switcher
Version:        0.0.1
Release:        1%{?dist}
Summary:        Switch between Nvidia and Nouveau drivers on Fedora
BuildArch:      noarch

License:        MIT
Source0:        %{name}-%{version}.tar

Requires:       bash xorg-x11-drv-nvidia-libs xorg-x11-drv-nouveau

%description
Switch between Nvidia and Nouveau drivers on Fedora

%prep
%setup -q

%install
rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/nvidia-switcher/
cp %{name} $RPM_BUILD_ROOT/%{_bindir}
cp share/* $RPM_BUILD_ROOT/%{_datadir}/nvidia-switcher/

%clean
rm -rf $RPM_BUILD_ROOT

%files
%{_bindir}/%{name}
%{_datadir}/nvidia-switcher
%{_datadir}/nvidia-switcher/disable-nouveau.conf
%{_datadir}/nvidia-switcher/load-nvidia.sh
%{_datadir}/nvidia-switcher/nvidia-primary.conf
