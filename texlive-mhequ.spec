# revision 15878
# category Package
# catalog-ctan /macros/latex/contrib/mhequ
# catalog-date 2008-05-01 20:41:51 +0200
# catalog-license other-free
# catalog-version 1.61
Name:		texlive-mhequ
Version:	1.61
Release:	2
Summary:	Multicolumn equations, tags, labels, sub-numbering
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/mhequ
License:	OTHER-FREE
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mhequ.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/mhequ.doc.tar.xz
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


%changelog
* Wed Jan 04 2012 Paulo Andrade <pcpa@mandriva.com.br> 1.61-2
+ Revision: 753980
- Rebuild to reduce used resources

* Sat Nov 05 2011 Paulo Andrade <pcpa@mandriva.com.br> 1.61-1
+ Revision: 719017
- texlive-mhequ
- texlive-mhequ
- texlive-mhequ
- texlive-mhequ

