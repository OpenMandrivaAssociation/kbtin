Name:		kbtin
Version:	1.0.20
Release:	1
Summary:	A very heavily extended clone the TinTin++ MUD client
Group:		Games/Other
License:	GPLv2+
URL:		https://kbtin.sourceforge.net/
Source0:	http://prdownloads.sourceforge.net/%{name}/%{name}-%{version}.tar.xz
BuildRequires:	pkgconfig(gnutls)
BuildRequires:	pkgconfig(zlib)

%description
KBtin is a console-based MUD client, which means it is meant to be used as a
client to play MUDs (multiplayer text-based games : MUD stands for Multi-User
Dungeon). It is highly configurable and features everything a MUD client must
have, maybe more. It improves on the well known TinTin++ MUD client.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%doc AUTHORS BUGS COPYING ChangeLog FAQ KEYPAD NEWS OLDNEWS
%{_mandir}/*/*
%{_bindir}/*
%{_datadir}/%{name}

