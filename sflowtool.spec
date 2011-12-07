Name:		sflowtool
Summary:	sflowtool is a utility for collecting and processing sFlow data
Version:	3.22
Release:	1
License:	Other
Source:		%{name}-%{version}.tar.gz
Group:		System/Configuration/Networking
URL:		http://www.inmon.com/technology/sflowTools.php

%description
The sFlow toolkit provides command line utilities and scripts for analyzing sFlow data.

sflowtool interfaces to utilities such as tcpdump, ntop and Snort for detailed packet tracing and analysis, NetFlow compatible collectors for IP flow accounting, and provides text based output that can be used in scripts to provide customized analysis and reporting and for integrating with other tools such as MRTG or rrdtool.

%prep
%setup -q

%build
%configure2_5x
%make

%install
%makeinstall_std

%files
%{_bindir}/%{name}
%doc AUTHORS INSTALL NEWS ChangeLog README
