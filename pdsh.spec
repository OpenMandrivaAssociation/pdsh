%define _disable_ld_no_undefined 1

Name:		pdsh
Version:	2.35
Release:	1
Source0:	https://github.com/chaos/pdsh/releases/download/pdsh-%{version}/pdsh-%{version}.tar.gz
Summary:	Parallel remote shell utility
URL:		https://github.com/chaos/pdsh
License:	GPL-2.0
Group:		System
BuildRequires:	autoconf automake slibtool
BuildSystem:	autotools
BuildOption:	--with-ssh
BuildOption:	--with-xcpu

%description
Pdsh is a multithreaded remote shell client which executes commands on
multiple remote hosts in parallel.  Pdsh can use several different
remote shell services, including standard "rsh", Kerberos IV, and ssh.

See the man page in the doc directory for usage information.

%files
%{_bindir}/dshbak
%{_bindir}/pdcp
%{_bindir}/pdsh
%{_bindir}/rpdcp
%dir %{_libdir}/pdsh
%{_libdir}/pdsh/execcmd.so
%{_libdir}/pdsh/sshcmd.so
%{_libdir}/pdsh/xcpucmd.so
%{_libdir}/pdsh/xrcmd.so
%{_mandir}/man1/dshbak.1*
%{_mandir}/man1/pdcp.1*
%{_mandir}/man1/pdsh.1*
%{_mandir}/man1/rpdcp.1*
