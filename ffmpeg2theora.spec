Name:           ffmpeg2theora
Version:        0.26
Release:        1%{?dist}
Summary:        Convert any file that ffmpeg can decode to theora

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://v2v.cc/~j/ffmpeg2theora/
Source0:        http://v2v.cc/~j/ffmpeg2theora/ffmpeg2theora-%{version}.tar.bz2
BuildRoot:      %{_tmppath}/%{name}-%{version}-%{release}-root-%(%{__id_u} -n)

BuildRequires:  scons
BuildRequires:  ffmpeg-devel
BuildRequires:  libkate-devel
BuildRequires:  libogg-devel >= 1.1
BuildRequires:  libtheora-devel >= 1.1.0
BuildRequires:  libvorbis-devel


%description
With ffmpeg2theora you can convert any file that ffmpeg can
decode to theora. right now the settings are hardcoded into
the binary. the idea is to provide ffmpeg2theora as a binary
along sites like v2v.cc to enable as many people as possible
to encode video clips with the same settings.

%prep
%setup -q


%build
scons APPEND_CCFLAGS="$RPM_OPT_FLAGS"


%install
rm -rf $RPM_BUILD_ROOT
scons install destdir=$RPM_BUILD_ROOT prefix=%{_prefix}
mkdir -p $RPM_BUILD_ROOT%{_mandir}/man1
mv $RPM_BUILD_ROOT%{_prefix}/man/man1/ffmpeg2theora.1 $RPM_BUILD_ROOT%{_mandir}/man1
rm -rf $RPM_BUILD_ROOT%{_prefix}/man

%clean
rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
%doc ChangeLog README TODO AUTHORS COPYING
%{_bindir}/ffmpeg2theora
%{_mandir}/man1/ffmpeg2theora.1.gz


%changelog
* Sun Feb 28 2010 Nicolas Chauvet <kwizart@fedoraproject.org> - 0.26-1
- Update to 0.26

* Fri Oct 16 2009 kwizart <kwizart at gmail.com> - 0.25-1
- Update to 0.25

* Fri Mar 27 2009 kwizart <kwizart at gmail.com> - 0.24-1
- Update to 0.24

* Fri Dec 19 2008 kwizart <kwizart at gmail.com> - 0.23-2
- Fix URL - Fix back description

* Fri Dec 19 2008 kwizart <kwizart at gmail.com> - 0.23-1
- Update to 0.23
- Change to build system to Scons

* Sat Aug 09 2008 Thorsten Leemhuis <fedora [AT] leemhuis [DOT] info - 0.21-2
- rebuild

* Fri May 30 2008 kwizart <kwizart at gmail.com> - 0.21-1
- Update to 0.21

* Thu Mar  7 2008 kwizart <kwizart at gmail.com> - 0.20-3
- Patch for new_ffmpeg

* Thu Feb 19 2008 kwizart <kwizart at gmail.com> - 0.20-2
- Rebuild for ffmpeg and gcc43

* Wed Dec 19 2007 kwizart <kwizart at gmail.com> - 0.20-1
- Update to 0.20 (stable)
- Fix License is GPLv2+

* Mon Nov 12 2007 kwizart <kwizart at gmail.com> - 0.19-1.1
- Rebuild for faad2

* Wed Aug 29 2007 kwizart <kwizart at gmail.com> 0.19-1
- Update to 0.19
- Update license field

* Fri Jun 15 2007 kwizart <kwizart at gmail.com> 0.18-2
- Submit to rpm.livna.org

* Fri Jun 15 2007 J. S. <users at livna.org> 0.18-1
- Initial Build
