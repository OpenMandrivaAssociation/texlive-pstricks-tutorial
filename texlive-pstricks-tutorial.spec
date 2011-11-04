# revision 15878
# category Package
# catalog-ctan undef
# catalog-date undef
# catalog-license undef
# catalog-version undef
Name:		texlive-pstricks-tutorial
Version:	20111104
Release:	1
Summary:	TeXLive pstricks-tutorial package
Group:		Publishing
URL:		http://tug.org/texlive
License:	http://www.tug.org/texlive/LICENSE.TL
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks-tutorial.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/pstricks-tutorial.doc.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(post):	texlive-tlpkg
Conflicts:	texlive-texmf <= 20110705-3
Conflicts:	texlive-doc <= 20110705-3

%description
TeXLive pstricks-tutorial package.

#-----------------------------------------------------------------------
%files
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap1-figures.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap1-src.tar.gz
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap1.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap2-figures.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap2-src.tar.gz
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap2.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap3-figures.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap3-src.tar.gz
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap3.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap4-figures.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap4-src.tar.gz
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap4.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap5-figures.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap5-src.tar.gz
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap5.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap6-figures.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap6-src.tar.gz
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap6.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap7-figures.pdf
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap7-src.tar.gz
%doc %{_texmfdistdir}/doc/generic/pstricks-tutorial/chap7.pdf
%doc %{_tlpkgobjdir}/*.tlpobj

#-----------------------------------------------------------------------
%prep
%setup -c -a0 -a1

%build

%install
mkdir -p %{buildroot}%{_texmfdistdir}
cp -fpar doc %{buildroot}%{_texmfdistdir}
mkdir -p %{buildroot}%{_tlpkgobjdir}
cp -fpa tlpkg/tlpobj/*.tlpobj %{buildroot}%{_tlpkgobjdir}
