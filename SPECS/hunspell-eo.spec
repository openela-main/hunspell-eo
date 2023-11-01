Name: hunspell-eo
Summary: Esperanto hunspell dictionaries
Version: 1.0
Release: 0.15.dev%{?dist}
Source: https://netix.dl.sourceforge.net/project/aoo-extensions/3377/1/1.0-dev.oxt
URL: http://extensions.services.openoffice.org/project/literumilo
License: LGPLv3
BuildArch: noarch

Requires: hunspell
Supplements: (hunspell and langpacks-eo)

%description
Esperanto hunspell dictionaries.

%prep
%autosetup -c

%build
chmod -x *

%install
mkdir -p $RPM_BUILD_ROOT/%{_datadir}/myspell
cp -p literumilo.dic $RPM_BUILD_ROOT/%{_datadir}/myspell/eo.dic
cp -p literumilo.aff $RPM_BUILD_ROOT/%{_datadir}/myspell/eo.aff


%files
%{_datadir}/myspell/*

%changelog
* Sat Jul 07 2018 Parag Nemade <pnemade AT fedoraproject DOT org> - 1.0-0.15.dev
- Update Source tag

* Wed Feb 07 2018 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.14.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_28_Mass_Rebuild

* Wed Jul 26 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.13.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_27_Mass_Rebuild

* Fri Feb 10 2017 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.12.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_26_Mass_Rebuild

* Fri Feb 19 2016 Parag Nemade <pnemade AT redhat DOT com> - 1.0-0.11.dev
- Add Supplements: tag for langpacks naming guidelines
- Clean the specfile to follow current packaging guidelines

* Thu Feb 04 2016 Fedora Release Engineering <releng@fedoraproject.org> - 1.0-0.10.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_24_Mass_Rebuild

* Wed Jun 17 2015 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.9.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_23_Mass_Rebuild

* Sat Jun 07 2014 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.8.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_21_Mass_Rebuild

* Sat Aug 03 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.7.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_20_Mass_Rebuild

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.6.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Jul 19 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.5.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_18_Mass_Rebuild

* Fri Jan 13 2012 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.4.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Wed Feb 09 2011 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 1.0-0.3.dev
- Rebuilt for https://fedoraproject.org/wiki/Fedora_15_Mass_Rebuild

* Fri Jul 09 2010 Caolan McNamara <caolanm@redhat.com> - 1.0-0.2.dev
- drop buildrequire

* Thu Dec 03 2009 Caolan McNamara <caolanm@redhat.com> - 1.0-0.1.dev
- latest version

* Fri Jul 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20041129-3
- Rebuilt for https://fedoraproject.org/wiki/Fedora_12_Mass_Rebuild

* Tue Feb 24 2009 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.20041129-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_11_Mass_Rebuild

* Sun Nov 02 2008 Caolan McNamara <caolanm@redhat.com> - 0.20041129-1
- initial version
