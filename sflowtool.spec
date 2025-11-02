Name:		sflowtool
Summary:	Utility for collecting and processing sFlow data
Version:	6.09
Release:	1
License:	Other
Source0:	https://github.com/sflow/sflowtool/archive/v%{version}/%{name}-%{version}.tar.gz
Group:		System/Configuration/Networking
URL:		https://www.inmon.com/technology/sflowTools.php

%description
The sFlow toolkit provides command
line utilities and scripts for analyzing sFlow data.
sflowtool interfaces to utilities such as tcpdump,
ntop and Snort for detailed packet tracing and analysis,
NetFlow compatible collectors for IP flow accounting,
and provides text based output that can be used in scripts
to provide customized analysis and reporting and for 
integrating with other tools such as MRTG or rrdtool.

%prep
%setup -q

%build
%configure
%make_build

%install
%make_install

%files
%{_bindir}/%{name}
%doc AUTHORS NEWS ChangeLog README
