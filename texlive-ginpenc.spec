%global tl_name ginpenc
%global tl_revision 79618

Name:		texlive-%{tl_name}
Epoch:		1
Version:	1.0
Release:	%{tl_revision}.1
Summary:	Modification of inputenc for German
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/ginpenc
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ginpenc.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ginpenc.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/ginpenc.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
If the inputenc is used and German umlauts are input directly, they are
converted to the LICR representation \"a (etc.). This breaks the sort
algorithm of makeindex, for instance. Ginpenc converts umlauts and the
sharp-s to the short forms defined by babel, e.g., "a instead, if the
text is typeset in German.

