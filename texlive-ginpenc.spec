Name:		texlive-ginpenc
Version:	24980
Release:	2
Summary:	Modification of inputenc for German
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ginpenc
License:	LPPL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ginpenc.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ginpenc.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/ginpenc.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
If the inputenc is used and German umlauts are input directly,
they are converted to the LICR representation \"a (etc.). This
breaks the sort algorithm of makeindex, for instance. Ginpenc
converts umlauts and the sharp-s to the short forms defined by
babel, e.g., "a instead, if the text is typeset in German.

%post
%{_sbindir}/texlive.post

%postun
if [ $1 -eq 0 ]; then
	%{_sbindir}/texlive.post
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
%doc %{_texmfdistdir}/doc/latex/ginpenc/ChangeLog
%doc %{_texmfdistdir}/doc/latex/ginpenc/Makefile
%doc %{_texmfdistdir}/doc/latex/ginpenc/README
%doc %{_texmfdistdir}/doc/latex/ginpenc/ginpenc.pdf
%doc %{_texmfdistdir}/doc/latex/ginpenc/news-message.txt
%doc %{_texmfdistdir}/doc/latex/ginpenc/testginpenc.tex
#- source
%doc %{_texmfdistdir}/source/latex/ginpenc/ginpenc.dtx
%doc %{_texmfdistdir}/source/latex/ginpenc/ginpenc.ins

#-----------------------------------------------------------------------
%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar tex doc source %{buildroot}%{_texmfdistdir}
