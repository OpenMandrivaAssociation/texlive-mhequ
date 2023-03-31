Name:		texlive-mhequ
Version:	64978
Release:	2
Summary:	Multicolumn equations, tags, labels, sub-numbering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mhequ
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mhequ.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mhequ.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
MHequ simplifies creating multi-column equation environments,
and tagging the equations therein. It supports sub-numbers of
blocks of equations (like (1.2a), (1.2b), etc) and references
to each equation individually (1.2a) or to the whole block
(1.2). The labels can be shown in draft mode. Comments in the
package itself describe usage.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mhequ
%doc %{_texmfdistdir}/doc/latex/mhequ

#-----------------------------------------------------------------------
%prep
%autosetup -p1 -c -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
