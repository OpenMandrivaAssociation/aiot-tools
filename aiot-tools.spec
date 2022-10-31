# Work around build system deficiencies
%undefine _debugsource_packages

%define date 20221025

Name: aiot-tools
Version: 1.2
Release: %{?date:0.%{date}.}1
Source0: https://gitlab.com/mediatek/aiot/bsp/aiot-tools/-/archive/main/aiot-tools-main.tar.bz2#/%{name}-%{date}.tar.bz2
Patch0: pygpiod-version-req.patch
Summary: Tools for flashing boards using MediaTek AIoT SoCs
URL: https://github.com/aiot-tools/aiot-tools
License: MIT
Group: Development/Tools
BuildRequires: python%{pyver}dist(setuptools)
BuildArch: noarch

%description
Tools for flashing boards using MediaTek AIoT SoCs

%prep
%autosetup -p1 -n %{name}-main

%build
%py_build

%install
%py_install

%files
%{_bindir}/*
%{py_puresitedir}/aiot
%{py_puresitedir}/aiot_tools-*.egg-info
