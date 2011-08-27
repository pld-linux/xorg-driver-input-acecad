Summary:	X.org input driver for Acecad Flair devices
Summary(pl.UTF-8):	Sterownik wejściowy X.org dla urządzeń Acecad Flair
Name:		xorg-driver-input-acecad
Version:	1.5.0
Release:	2
License:	MIT
Group:		X11/Applications
Source0:	http://xorg.freedesktop.org/releases/individual/driver/xf86-input-acecad-%{version}.tar.bz2
# Source0-md5:	a03721cae66c475e5f6513fa51142869
URL:		http://xorg.freedesktop.org/
BuildRequires:	autoconf >= 2.60
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	pkgconfig >= 1:0.19
BuildRequires:	sysfsutils-devel >= 2.0
BuildRequires:	xorg-proto-inputproto-devel
BuildRequires:	xorg-proto-randrproto-devel
BuildRequires:	xorg-util-util-macros >= 1.8
BuildRequires:	xorg-xserver-server-devel >= 1.0.99.901
BuildRequires:	rpmbuild(macros) >= 1.389
%{?requires_xorg_xserver_xinput}
Requires:	xorg-xserver-server >= 1.0.99.901
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
X.org input driver for Acecad Flair devices.

%description -l pl.UTF-8
Sterownik wejściowy X.org dla urządzeń Acecad Flair.

%prep
%setup -q -n xf86-input-acecad-%{version}

%build
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__autoheader}
%{__automake}
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/xorg/modules/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc COPYING ChangeLog README
%attr(755,root,root) %{_libdir}/xorg/modules/input/acecad_drv.so
%{_mandir}/man4/acecad.4*
