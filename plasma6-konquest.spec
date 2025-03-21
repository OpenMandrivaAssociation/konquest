#define git 20240218
%define gitbranch release/24.02
%define gitbranchd %(echo %{gitbranch} |sed -e "s,/,-,g")
%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		plasma6-konquest
Version:	24.12.3
Release:	%{?git:0.%{git}.}2
Summary:	Conquer the planets of your enemy
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		https://www.kde.org/applications/games/konquest/
%if 0%{?git:1}
Source0:	https://invent.kde.org/games/konquest/-/archive/%{gitbranch}/konquest-%{gitbranchd}.tar.bz2#/konquest-%{git}.tar.bz2
%else
Source0:	https://download.kde.org/%{stable}/release-service/%{version}/src/konquest-%{version}.tar.xz
%endif
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF6Config) cmake(KF6ConfigWidgets) cmake(KF6CoreAddons) cmake(KF6Crash) cmake(KF6DBusAddons) cmake(KF6GuiAddons) cmake(KF6I18n) cmake(KDEGames6) cmake(KF6WidgetsAddons) cmake(KF6XmlGui) cmake(Qt6Core) cmake(Qt6Gui) cmake(Qt6Svg) cmake(Qt6Widgets) cmake(KF6DocTools)
BuildRequires:	cmake(Qt6StateMachine)
BuildRequires:  cmake(Qt6Qml)
BuildRequires:  cmake(Qt6QmlCore)
BuildRequires:  cmake(Qt6QmlNetwork)

%description
Konquest is the KDE version of Gnu-Lactic Konquest. Players conquer other
planets by sending ships to them. The goal is to build an interstellar
empire and ultimately conquer all other player's planets.

%files -f %{name}.lang
%{_bindir}/konquest
%{_datadir}/applications/org.kde.konquest.desktop
%{_datadir}/konquest
%{_iconsdir}/hicolor/*/apps/konquest.png
%{_datadir}/metainfo/org.kde.konquest.appdata.xml

#------------------------------------------------------------------------------

%prep
%autosetup -p1 -n konquest-%{?git:%{gitbranchd}}%{!?git:%{version}}

%build
%cmake \
	-DKDE_INSTALL_USE_QT_SYS_PATHS:BOOL=ON \
	-G Ninja
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
