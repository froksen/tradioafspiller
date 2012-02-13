#
# spec file for package 
#
# Copyright (c) 2010 SUSE LINUX Products GmbH, Nuernberg, Germany.
#
# All modifications and additions to the file contributed by third parties
# remain the property of their copyright owners, unless otherwise agreed
# upon. The license for this file, and modifications and additions to the
# file, is the same license as for the pristine package itself (unless the
# license for the pristine package is not an Open Source License, in which
# case the license is the MIT License). An "Open Source License" is a
# license that conforms to the Open Source Definition (Version 1.9)
# published by the Open Source Initiative.

# Please submit bugfixes or comments via http://bugs.opensuse.org/
#

# norootforbuild

Name:           radio
Version:	svnr17
Release:	1
License:	GNU GPLv2
Summary:	Et script der afspiller radio i terminalen
Url:		http://code.google.com/p/tradioafspiller/
Group:		Applications/Tools
Source:		radio-svnr16.tar.gz
Packager: 	Ole Holm Frandsen "Froksen"
#Patch:
#BuildRequires:
#PreReq:
#Provides:
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
Requires: 	vlc,mplayer,gstreamer-0_10,python-gstreamer-0_10,python-base,python-devel,gstreamer-0_10-fluendo-mp3, libmp3, libmp3lame0, libmpeg2-0
BuildArch:	noarch

%description
Programmet er et forsøg på at lave en simpel radioafspiller der kører i terminalen.

Dette kan være smart hvis man f.eks. bruger Yakuake til KDE eller Guake til f.eks. GNOME. Da kan man hurtigt trække konsollen "ned" og skrive en kort kommando hvorefter der er dejlig musik fra 
f.eks. Danmarks Radio's P3. 

%prep
%setup -q

%build
echo OK

%install
#%make_install
mkdir -p $RPM_BUILD_ROOT/%{_bindir}
install -p -m 755 radio $RPM_BUILD_ROOT/%{_bindir}

%clean
%{?buildroot:%__rm -rf "%{buildroot}"}

%post

%postun

%files
%defattr(-,root,root)
#%doc ChangeLog README COPYING
/usr/bin/radio*

#%changelog:
