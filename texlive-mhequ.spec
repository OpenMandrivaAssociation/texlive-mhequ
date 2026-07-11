%global tl_name mhequ
%global tl_revision 64978

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.72
Release:	%{tl_revision}.1
Summary:	Multicolumn equations, tags, labels, sub-numbering
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/mhequ
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mhequ.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/mhequ.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The mhequ style file simplifies creating multi-column equation
environments and tagging equations therein. It supports sub-numbering of
blocks of equations (like (1.2a), (1.2b), etc) and references to each
equation individually (1.2a) or to the whole block (1.2). The labels can
be shown in draft mode. The default behaviour is to show an equation
number if and only if the equation actually has a label, which reduces
visual clutter. Comments in the package itself describe its usage, which
should also be self-evident from the provided example file.

