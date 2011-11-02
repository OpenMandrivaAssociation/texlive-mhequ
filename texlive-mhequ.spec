Name:		texlive-mhequ
Version:	1.61
Release:	1
Summary:	Multicolumn equations, tags, labels, sub-numbering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mhequ
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mhequ.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mhequ.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
MHequ simplifies creating multi-column equation environments,
and tagging the equations therein. It supports sub-numbers of
blocks of equations (like (1.2a), (1.2b), etc) and references
to each equation individually (1.2a) or to the whole block
(1.2). The labels can be shown in draft mode. Comments in the
package itself describe usage.

%pre
    %_texmf_mktexlsr_pre

%post
    %_texmf_mktexlsr_post

%preun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_pre
    fi

%postun
    if [ $1 -eq 0 ]; then
	%_texmf_mktexlsr_post
    fi

#-----------------------------------------------------------------------
%files
%{_texmfdistdir}/tex/latex/mhequ/mhequ.sty
%doc %{_texmfdistdir}/doc/latex/mhequ/example.pdf
%doc %{_texmfdistdir}/doc/latex/mhequ/example.tex

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc %{buildroot}%{_texmfdistdir}
