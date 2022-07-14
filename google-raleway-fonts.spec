Name:		google-raleway-fonts
Version:	1.0
Release:	1
Summary:	Google Raleway fonts

License:	OFL
Group:		System/Fonts/True type
Url:		https://fonts.google.com/specimen/Raleway
Source0: https://fonts.google.com/download?family=Raleway#/Raleway.zip
BuildArch:	noarch

%description
Raleway is an elegant sans-serif typeface family.

%prep
%autosetup -p1 -c %{name}

%install
mkdir -p %{buildroot}%{_datadir}/fonts/TTF/raleway
install -Dm 644 *.ttf  %{buildroot}%{_datadir}/fonts/TTF/raleway/

%files
%{_datadir}/fonts/TTF/raleway
