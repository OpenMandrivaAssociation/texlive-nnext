%global tl_name nnext
%global tl_revision 56575

Name:		texlive-%{tl_name}
Epoch:		1
Version:	0.0
Release:	%{tl_revision}.1
Summary:	Extension for the gb4e package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nnext
License:	lppl1.3
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nnext.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nnext.doc.r%{tl_revision}.tar.xz
Source2:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/nnext.source.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
This is an add-on for the gb4e package used in linguistics. It
implements the \Next, \NNext, \Last, and \LLast commands from the
linguex package or the \nextx, \anextx, \lastx, \blastx, and \bblastx
commands from the expex package.

