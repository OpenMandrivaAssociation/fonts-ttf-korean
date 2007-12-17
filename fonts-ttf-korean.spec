%define version	2.1
%define release %mkrel 8

%if %mdkversion < 20070
%define fccachefile fonts.cache-1
%endif

Summary:	Baekmuk korean fonts
Name:		fonts-ttf-korean
Version:	%{version}
Release:	%{release}

Source0:	ftp://ftp.mizi.com/pub/baekmuk/baekmuk-ttf-%{version}.tar.bz2
Source1:	ftp://ftp.mizi.com/pub/baekmuk/baekmuk-doc-%{version}.tar.bz2
Source2:	%name-fonts.alias.bz2
Source3:	cidinst.korean
Source4:	cidunin.korean

License:	GPL
Group:		System/Fonts/True type
BuildArch:	noarch
BuildRequires:	freetype-tools
Obsoletes: 	baekmuk hwan-fonts
Provides:	baekmuk hwan-fonts
Requires(post): fontconfig
Requires(postun): fontconfig

%description
Baekmuk Korean TTF Fonts.

%prep

%setup -q -T -c -a0 -a1
 
%build

%install
rm -fr %buildroot

install -d %buildroot/%{_datadir}/fonts/TTF/korean/
install -m 0644 *.ttf %buildroot/%{_datadir}/fonts/TTF/korean


(
cd %buildroot/%{_datadir}/fonts/TTF/korean
ttmkfdir -u > fonts.dir
ln -s fonts.dir fonts.scale
bzcat %SOURCE2 > fonts.alias
%if %mdkversion < 20070
touch %fccachefile
%endif
) 

mkdir -p %{buildroot}%_sysconfdir/X11/fontpath.d/
ln -s ../../..%_datadir/fonts/TTF/korean \
    %{buildroot}%_sysconfdir/X11/fontpath.d/ttf-korean:pri=50


%post
[ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 


%postun
if [ "$1" = "0" ]; then
  [ -x %{_bindir}/fc-cache ] && %{_bindir}/fc-cache 
fi

%clean
rm -fr %buildroot

%files
%defattr(-,root,root,0755)
%doc COPYRIGHT*
%dir %{_datadir}/fonts/TTF/korean/
%{_datadir}/fonts/TTF/korean/*.ttf
%config(noreplace) %{_datadir}/fonts/TTF/korean/fonts.alias
%config(noreplace) %{_datadir}/fonts/TTF/korean/fonts.dir
%{_datadir}/fonts/TTF/korean/fonts.scale
%if %mdkversion < 20070
%ghost %{_datadir}/fonts/TTF/korean/%fccachefile
%endif
%{_sysconfdir}/X11/fontpath.d/ttf-korean:pri=50

