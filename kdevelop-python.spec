Name: kdevelop-python
Version: 1.6.0
Release: 1%{?dist}
License: GPLv2
Source0: http://download.kde.org/stable/kdevelop/4.6.0/src/kdev-python-1.6.0.tar.bz2

Summary: Python Plugin for KDevelop
URL: http://kdevelop.org

BuildRequires: kdevplatform-devel
BuildRequires: kdevelop-devel
BuildRequires: kdevelop-pg-qt-devel
BuildRequires: python2-devel

%description
Python language support for KDevelop Integrated Development
Environment.

%prep
%setup -qn kdev-python-%{version}

%build
mkdir -p %{_target_platform}
pushd %{_target_platform}
%{cmake_kde4} ../
popd
make %{?_smp_mflags} -C %{_target_platform}

%install
make install/fast DESTDIR=%{buildroot} -C %{_target_platform}
chmod +x %{buildroot}%{_kde4_libdir}/libpython%{python_version}-kdevelop.so.1.0
ln -s libpython%{python_version}-kdevelop.so.1.0 %{buildroot}%{_kde4_libdir}/libpython%{python_version}-kdevelop.so

%find_lang %{name} --all-name --with-kde

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig


%files -f %{name}.lang
%doc DESIGN TODO README
%{_kde4_appsdir}/kdevappwizard/templates/*
%{_kde4_appsdir}/kdevpythonsupport
%{_kde4_datadir}/kde4/services/kdevpdb.desktop
%{_kde4_datadir}/kde4/services/kdevpythonsupport.desktop
%{_kde4_datadir}/kde4/services/kcm_kdevpythonpep8.desktop
%{_kde4_datadir}/kde4/services/kcm_kdevpythondocfiles.desktop
%{_kde4_configdir}/kdev_python_docfiles.knsrc
%{_kde4_libdir}/kde4/kdevpythonlanguagesupport.so
%{_kde4_libdir}/kde4/kcm_pep8.so
%{_kde4_libdir}/kde4/kcm_docfiles.so
%{_kde4_libdir}/kde4/kdevpdb.so
%{_kde4_libdir}/libkdev4pythonduchain.so
%{_kde4_libdir}/libpython%{python_version}-kdevelop.so
%{_kde4_libdir}/libpython%{python_version}-kdevelop.so.1.0
%{_kde4_libdir}/libkdev4pythonparser.so
%{_kde4_libdir}/libkdev4pythoncompletion.so

%changelog
* Sat Mar 08 2014 sKotenok <chernbiy.kot@gmail.com> 1.6.0-1
- 1.6.0
* Sun May 19 2013 Tobias Herbert <blubbme@gmx.com> 1.5.1-1
- 1.5.1
* Sat May 11 2013 Tobias Herbert <blubbme@gmx.com> 1.5.0-1
- version bump to 1.5.0
* Thu Feb 14 2013 Minh Ngo <minh@fedoraproject.org> 1.4.1-2
- have added _kde4_appsdir macro
- have dropped updata-mime-database scriptlets
- have omitted cmake requirement
- have removed desktop-file-install script
- removing python2.7 hardcode
* Sat Dec 01 2012 Minh Ngo <minh@fedoraproject.org> 1.4.1-1
- initial buildOB