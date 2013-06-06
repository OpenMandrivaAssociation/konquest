Name:		konquest
Version:	4.10.4
Release:	1
Epoch:		1
Summary:	Conquer the planets of your enemy
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/konquest/
Source:		ftp://ftp.kde.org/pub/kde/stable/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel

%description
Konquest is the KDE version of Gnu-Lactic Konquest. Players conquer other
planets by sending ships to them. The goal is to build an interstellar
empire and ultimately conquer all other player's planets.

%files
%{_kde_bindir}/konquest
%{_kde_applicationsdir}/konquest.desktop
%{_kde_appsdir}/konquest
%{_kde_docdir}/*/*/konquest
%{_kde_iconsdir}/hicolor/*/apps/konquest.png

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4
%make

%install
%makeinstall_std -C build

%changelog
* Wed Jun 05 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.4-1
- New version 4.10.4

* Tue May 07 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.3-1
- New version 4.10.3

* Wed Apr 03 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.2-1
- New version 4.10.2

* Sat Mar 09 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.1-1
- New version 4.10.1

* Wed Feb 13 2013 Andrey Bondrov <andrey.bondrov@rosalab.ru> 1:4.10.0-1
- Split from kdegames4 package

