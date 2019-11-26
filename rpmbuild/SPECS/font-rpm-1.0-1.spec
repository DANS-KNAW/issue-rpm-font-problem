Name: font-rpm
Release: 1
Summary: RPM to reproduce problem with malencoded font metadata
License: none
Version: 1.0
BuildArch: noarch

%description
RPM to reproduce problem with malencoded font metadata

%files
/var/www/html/index.html
/var/www/html/OpenSans-Bold.ttf

%clean
echo "no clean"