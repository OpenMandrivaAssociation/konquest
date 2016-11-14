Name:		konquest
Version:	16.08.3
Release:	1
Epoch:		1
Summary:	Conquer the planets of your enemy
Group:		Graphical desktop/KDE
License:	GPLv2 and LGPLv2 and GFDL
URL:		http://www.kde.org/applications/games/konquest/
Source:		http://download.kde.org/stable/applications/%{version}/src/%{name}-%{version}.tar.xz
BuildRequires:	libkdegames-devel
BuildRequires:	cmake(KDEGames)
BuildRequires:	kdelibs-devel

%description
Konquest is the KDE version of Gnu-Lactic Konquest. Players conquer other
planets by sending ships to them. The goal is to build an interstellar
empire and ultimately conquer all other player's planets.

%files                                                                                                 
%{_bindir}/konquest                                                                                    
%{_datadir}/applications/kde4/konquest.desktop                                                         
%{_datadir}/apps/konquest                                                                              
%doc %{_docdir}/*/*/konquest                                                                           
%{_iconsdir}/hicolor/*/apps/konquest.png

#------------------------------------------------------------------------------

%prep
%setup -q

%build
%cmake_kde4 \
	-DCMAKE_MINIMUM_REQUIRED_VERSION=3.1
%make

%install
%makeinstall_std -C build

