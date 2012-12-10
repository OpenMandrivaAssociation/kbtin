%define name    kbtin
%define version 1.0.13
%define release %mkrel 2

Name:           %{name}
Summary:        A very heavily extended clone the TinTin++ MUD client
Version:        %{version}
Release:        %{release}
URL:            http://kbtin.sourceforge.net/ 
Source0:        http://prdownloads.sourceforge.net/%name/%name-%version.tar.gz
License:        GPLv2+
Group:          Games/Other
BuildRequires:  zlib-devel gnutls-devel
BuildRoot:      %{_tmppath}/%{name}-buildroot

%description
KBtin is a console-based MUD client, which means it is meant to be used as a
client to play MUDs (multiplayer text-based games : MUD stands for Multi-User
Dungeon).
It is highly configurable and features everything a MUD client must have,
maybe more.
It improves on the well known TinTin++ MUD client.

%prep
%setup -q -n %{name}-%{version}

%build
%configure
%make

%install
rm -rf %{buildroot}
%makeinstall

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,0755)
%doc AUTHORS BUGS COPYING ChangeLog FAQ KEYPAD NEWS OLDNEWS README
%{_mandir}/*/*
%{_bindir}/*
%{_datadir}/%name/*


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 1.0.13-2mdv2011.0
+ Revision: 619896
- the mass rebuild of 2010.0 packages

* Sat Oct 24 2009 Samuel Verschelde <stormi@mandriva.org> 1.0.13-1mdv2010.0
+ Revision: 459175
- import kbtin

