%define stable %([ "`echo %{version} |cut -d. -f3`" -ge 70 ] && echo -n un; echo -n stable)
Name:		konquest
Version:	 18.12.3
Release:	1
Epoch:		1
Summary:	Conquer the planets of your enemy
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/konquest/
Source0:	http://download.kde.org/%{stable}/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	cmake
BuildRequires:	ninja
BuildRequires:	cmake(ECM)
BuildRequires:	cmake(KF5Config) cmake(KF5ConfigWidgets) cmake(KF5CoreAddons) cmake(KF5Crash) cmake(KF5DBusAddons) cmake(KF5GuiAddons) cmake(KF5I18n) cmake(KF5KDEGames) cmake(KF5WidgetsAddons) cmake(KF5XmlGui) cmake(Qt5Core) cmake(Qt5Gui) cmake(Qt5Svg) cmake(Qt5Widgets) cmake(KF5DocTools)

%description
Konquest is the KDE version of Gnu-Lactic Konquest. Players conquer other
planets by sending ships to them. The goal is to build an interstellar
empire and ultimately conquer all other player's planets.

%files -f %{name}.lang
%{_bindir}/konquest
%{_datadir}/applications/org.kde.konquest.desktop
%{_datadir}/konquest
%{_iconsdir}/hicolor/*/apps/konquest.png
%{_datadir}/kxmlgui5/konquest/konquestui.rc
%{_datadir}/metainfo/org.kde.konquest.appdata.xml

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde5
%ninja

%install
%ninja_install -C build
%find_lang %{name} --all-name --with-html
