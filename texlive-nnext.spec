Name:		texlive-nnext
Version:	56575
Release:	2
Summary:	Extension for the gb4e package
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/latex/contrib/nnext
License:	lppl1.3
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nnext.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nnext.doc.r%{version}.tar.xz
Source2:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/nnext.source.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
This is an add-on for the gb4e package used in linguistics. It
implements the \Next, \NNext, \Last, and \LLast commands from
the linguex package or the \nextx, \anextx, \lastx, \blastx,
and \bblastx commands from the expex package.

%prep
%setup -c -a1 -a2
%autopatch -p1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%doc %{_texmfdistdir}/source/latex/nnext
%{_texmfdistdir}/tex/latex/nnext
%doc %{_texmfdistdir}/doc/latex/nnext

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
