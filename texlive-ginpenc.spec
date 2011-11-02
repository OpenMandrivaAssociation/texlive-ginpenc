Name:		texlive-ginpenc
Version:	1.0
Release:	1
Summary:	Modification of inputenc for German
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/ginpenc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ginpenc.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ginpenc.doc.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ginpenc.source.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3
Conflicts:	texlive-source <= 20110705-3

%description
If the inputenc is used and German umlauts are input directly,
they are converted to the LICR representation \"a (etc.). This
breaks the sort algorithm of makeindex, for instance. Ginpenc
converts umlauts and the sharp-s to the short forms defined by
babel, e.g., "a instead, if the text is typeset in German.

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
%{_texmfdistdir}/tex/latex/ginpenc/ansinew.gie
%{_texmfdistdir}/tex/latex/ginpenc/applemac.gie
%{_texmfdistdir}/tex/latex/ginpenc/ascii.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp1250.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp1252.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp437.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp437de.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp850.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp852.gie
%{_texmfdistdir}/tex/latex/ginpenc/cp865.gie
%{_texmfdistdir}/tex/latex/ginpenc/decmulti.gie
%{_texmfdistdir}/tex/latex/ginpenc/ginpenc.sty
%{_texmfdistdir}/tex/latex/ginpenc/latin1.gie
%{_texmfdistdir}/tex/latex/ginpenc/latin2.gie
%{_texmfdistdir}/tex/latex/ginpenc/latin3.gie
%{_texmfdistdir}/tex/latex/ginpenc/latin5.gie
%{_texmfdistdir}/tex/latex/ginpenc/latin9.gie
%{_texmfdistdir}/tex/latex/ginpenc/next.gie
%doc %{_texmfdistdir}/doc/latex/ginpenc/README
%doc %{_texmfdistdir}/doc/latex/ginpenc/ginpenc.pdf
%doc %{_texmfdistdir}/doc/latex/ginpenc/news-message.txt
%doc %{_texmfdistdir}/doc/latex/ginpenc/testginpenc.tex
#- source
%doc %{_texmfdistdir}/source/latex/ginpenc/Makefile
%doc %{_texmfdistdir}/source/latex/ginpenc/ginpenc.dtx
%doc %{_texmfdistdir}/source/latex/ginpenc/ginpenc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1 -a2

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
