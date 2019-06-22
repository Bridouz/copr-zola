Name: zola
Version: 0.8.0
Release: 1%{?dist}
Summary: Static site generator
License: MIT
URL: https://getzola.org
Source0: https://github.com/getzola/zola/archive/v%{version}.tar.gz
BuildRequires: pkgconfig(libcurl)
BuildRequires: cargo
BuildRequires: compat-openssl10-devel
BuildRequires: /usr/bin/g++

%description
Zola is a static site generator written in Rust.

%define debug_package %{nil}

%prep
%autosetup

%build
cargo build --release

%install
install -Dpm 755 target/release/zola %{buildroot}%{_bindir}/zola

%check
cargo test --release

%files
%license LICENSE
%{_bindir}/zola
