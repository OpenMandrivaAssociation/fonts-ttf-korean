%define snapdate 080608
%define rel 6

Summary:	Un Fonts in Koream
Name:		fonts-ttf-korean
Epoch:		1
Version:	1.0.2
Release:	%mkrel -c %snapdate %rel
URL:		http://kldp.net/projects/unfonts/
Source0:	http://kldp.net/frs/download.php/4695/un-fonts-core-%version-%snapdate.tar.gz
License:	GPLv2
Group:		System/Fonts/True type
BuildArch:	noarch
BuildRequires: fontconfig
BuildRoot:	%{_tmppath}/%name-%version-%release-root
BuildRequires:	mkfontdir
Obsoletes: 	baekmuk hwan-fonts
Provides:	baekmuk hwan-fonts

%description
Un-fonts is comes from the HLaTeX as type1 fonts in 1998 by Koaunghi Un,
he made type1 fonts to use with Korean TeX(HLaTeX [1]) in the late 1990's and
release it under the GNU GPL license.

%prep
%setup -q -n un-fonts
 
%build

%install
rm -fr %buildroot

install -d %buildroot/%{_datadir}/fonts/TTF/korean/
install -m 0644 *.ttf %buildroot/%{_datadir}/fonts/TTF/korean


(
cd %buildroot/%{_datadir}/fonts/TTF/korean
mkfontdir > fonts.dir
ln -sf fonts.dir fonts.scale
) 

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/korean \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-korean:pri=50


%clean
rm -fr %buildroot

%files
%defattr(-,root,root,0755)
%doc README COPYING
%dir %{_datadir}/fonts/TTF/korean/
%{_datadir}/fonts/TTF/korean/*.ttf
%config(noreplace) %{_datadir}/fonts/TTF/korean/fonts.dir
%{_datadir}/fonts/TTF/korean/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-korean:pri=50
