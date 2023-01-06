#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	22.12.1
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		ktp-desktop-applets
Summary:	ktp destop applets
Name:		ka5-%{kaname}
Version:	22.12.1
Release:	1
License:	GPL v2+/LGPL v2.1+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	6fc57b0a6521e6798ecaf6c6f786f050
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel >= %{qtver}
BuildRequires:	cmake >= 2.8.12
BuildRequires:	gettext-devel
BuildRequires:	ka5-ktp-common-internals-devel >= %{kdeappsver}
BuildRequires:	kf5-extra-cmake-modules >= %{kframever}
BuildRequires:	kf5-ki18n-devel >= %{kframever}
BuildRequires:	kf5-kwindowsystem-devel >= %{kframever}
BuildRequires:	kf5-plasma-framework-devel >= %{kframever}
BuildRequires:	ninja
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	tar >= 1:1.22
BuildRequires:	telepathy-qt5-devel >= 0.9.8
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Telepathy Desktop applets.

%description -l pl.UTF-8
Aplety Telepathy Desktop.

%prep
%setup -q -n %{kaname}-%{version}

%build
install -d build
cd build
%cmake \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON \
	..
%ninja_build

%if %{with tests}
ctest
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%dir %{_libdir}/qt5/qml/org/kde/ktpchat
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/ktpchat/libktpchatplugin.so
%{_libdir}/qt5/qml/org/kde/ktpchat/qmldir
%dir %{_libdir}/qt5/qml/org/kde/ktpcontactlist
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/ktpcontactlist/libktpcontactlistplugin.so
%{_libdir}/qt5/qml/org/kde/ktpcontactlist/qmldir
%{_datadir}/kservices5/plasma-applet-org.kde.ktp-chat.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.ktp-contactlist.desktop
%{_datadir}/kservices5/plasma-applet-org.kde.person.desktop
%dir %{_datadir}/plasma/plasmoids/org.kde.ktp-chat
%dir %{_datadir}/plasma/plasmoids/org.kde.ktp-chat/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.ktp-chat/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.ktp-chat/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.ktp-chat/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.ktp-chat/contents/ui/ActionDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.ktp-chat/contents/ui/ChatWidget.qml
%{_datadir}/plasma/plasmoids/org.kde.ktp-chat/contents/ui/ConversationDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.ktp-chat/contents/ui/ConversationDelegateButton.qml
%{_datadir}/plasma/plasmoids/org.kde.ktp-chat/contents/ui/FullChatList.qml
%{_datadir}/plasma/plasmoids/org.kde.ktp-chat/contents/ui/OutgoingDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.ktp-chat/contents/ui/TextDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.ktp-chat/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.ktp-chat/metadata.desktop
%dir %{_datadir}/plasma/plasmoids/org.kde.ktp-contactlist
%dir %{_datadir}/plasma/plasmoids/org.kde.ktp-contactlist/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.ktp-contactlist/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.ktp-contactlist/contents/ui/ContactList.qml
%{_datadir}/plasma/plasmoids/org.kde.ktp-contactlist/contents/ui/ListContactDelegate.qml
%{_datadir}/plasma/plasmoids/org.kde.ktp-contactlist/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.ktp-contactlist/metadata.desktop
%dir %{_datadir}/plasma/plasmoids/org.kde.person
%dir %{_datadir}/plasma/plasmoids/org.kde.person/contents
%dir %{_datadir}/plasma/plasmoids/org.kde.person/contents/config
%dir %{_datadir}/plasma/plasmoids/org.kde.person/contents/ui
%{_datadir}/plasma/plasmoids/org.kde.person/contents/config/config.qml
%{_datadir}/plasma/plasmoids/org.kde.person/contents/config/main.xml
%{_datadir}/plasma/plasmoids/org.kde.person/contents/ui/Person.qml
%{_datadir}/plasma/plasmoids/org.kde.person/contents/ui/main.qml
%{_datadir}/plasma/plasmoids/org.kde.person/contents/ui/settingsGeneral.qml
%{_datadir}/plasma/plasmoids/org.kde.person/metadata.desktop
