%define snapdate 080608

Summary:	Un Fonts in Koream
Name:		fonts-ttf-korean
Epoch:		1
Version:	1.0.2
Release:	0.%{snapdate}.10
License:	GPLv2
Group:		System/Fonts/True type
Url:		https://kldp.net/projects/unfonts/
Source0:	http://kldp.net/frs/download.php/4695/un-fonts-core-%version-%{snapdate}.tar.gz
BuildArch:	noarch
BuildRequires:	fontconfig
BuildRequires:	mkfontdir
Provides:	baekmuk = %{EVRD}
Provides:	hwan-fonts = %{EVRD}

%description
Un-fonts is comes from the HLaTeX as type1 fonts in 1998 by Koaunghi Un,
he made type1 fonts to use with Korean TeX(HLaTeX [1]) in the late 1990's and
release it under the GNU GPL license.

%prep
%setup -qn un-fonts

%build

%install
install -d %{buildroot}%{_datadir}/fonts/TTF/korean/
install -m 0644 *.ttf %{buildroot}%{_datadir}/fonts/TTF/korean

(
cd %{buildroot}%{_datadir}/fonts/TTF/korean
mkfontdir > fonts.dir
ln -sf fonts.dir fonts.scale
) 

mkdir -p %{buildroot}%{_sysconfdir}/X11/fontpath.d/
ln -s ../../..%{_datadir}/fonts/TTF/korean \
    %{buildroot}%{_sysconfdir}/X11/fontpath.d/ttf-korean:pri=50

%files
%doc README COPYING
%dir %{_datadir}/fonts/TTF/korean/
%{_datadir}/fonts/TTF/korean/*.ttf
%config(noreplace) %{_datadir}/fonts/TTF/korean/fonts.dir
%{_datadir}/fonts/TTF/korean/fonts.scale
%{_sysconfdir}/X11/fontpath.d/ttf-korean:pri=50

