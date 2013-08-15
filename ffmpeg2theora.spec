#global posttag svn18165

Name:           ffmpeg2theora
Version:        0.29
Release:        5%{?posttag}%{?dist}
Summary:        Convert any file that ffmpeg can decode to theora

Group:          Applications/Multimedia
License:        GPLv2+
URL:            http://v2v.cc/~j/ffmpeg2theora/
Source0:        http://v2v.cc/~j/ffmpeg2theora/downloads/ffmpeg2theora-%{version}.tar.bz2
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
%setup -q -n %{name}-%{version}


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
* Thu Aug 15 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.29-5
- Rebuilt for FFmpeg 2.0.x

* Sun May 26 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.29-4
- Rebuilt for x264/FFmpeg

* Mon Mar 04 2013 Nicolas Chauvet <kwizart@gmail.com> - 0.29-3
- Rebuilt for F-19 Features

* Sat Nov 24 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.29-2
- Rebuilt for ffmpeg

* Fri Oct 19 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.29-1
- Update to 0.29

* Tue Jun 26 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.28-6.svn18165
- Rebuilt for FFmpeg

* Sat May  5 2012 Michel Salim <salimma@fedoraproject.org> - 0.28-5.svn18165
- Update to latest upstream commit, for FFmpeg 0.10 compatibility

* Fri May 04 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.28-4
- Rebuilt for FFmpeg

* Tue Feb 28 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.28-3
- Rebuilt for x264/FFmpeg

* Wed Feb 08 2012 Nicolas Chauvet <kwizart@gmail.com> - 0.28-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_17_Mass_Rebuild

* Fri Sep 23 2011 Nicolas Chauvet <kwizart@gmail.com> - 0.28-1
- Update to 0.28

* Thu Oct 14 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.27-1
- Update to 0.27

* Mon May 31 2010 Nicolas Chauvet <kwizart@gmail.com> - 0.26-2
- Rebuilt for ldflags

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
