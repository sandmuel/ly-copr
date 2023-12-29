Name:           ly
Summary:        Display manager with console UI

Version:        0.5.0
Release:        1%{?dist}

License:        WTFPL
URL:            https://github.com/cylgom/ly
Source0:        %{url}/archive/v%{version}/%{name}-%{version}.tar.gz

BuildRequires:  make
BuildRequires:  automake
BuildRequires:  gcc
BuildRequires:  gcc-c++
BuildRequires:  kernel-devel
BuildRequires:  pam-devel
BuildRequires:  libxcb-devel


%description
Ly is a lightweight TUI (ncurses-like) display manager for Linux and BSD.


%prep
git clone --recurse-submodules https://github.com/fairyglade/ly
cd ly


%build
make


%install
make run
make install installsystemd


%post
systemctl enable ly.service


%preun


%postun


%files


%changelog
