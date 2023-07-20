pkgname="openai-client-bin"
pkgdesc="OpenAI client made using PySide6 Qt"
pkgver="1.0.0"
pkgrel=1
arch=("x86_64")


license=('MIT')


# binaries in virtual environment will be removed
# if default behaviour makepkg is not overridden
options=(!strip)

# use pacman -Qs "package-name"
depends=("git>=2.0" "python>=3.5" "python-pip>=20.0" "tar>=1.0")

provides=("openai-client")

# backup=(etc/$pkgname/{config.ini,wsetup.sh,xsetup.sh})
# backup=(~/.config/openai-client)
# backup=(home/${USER}/.config/openai-client)

source=("git+https://github.com/awesomeDev12/openai-client.git"
        "https://github.com/awesomeDev12/openai-client-arch-bin/releases/download/v1.0.0/binaries.tar.gz"
        "launch_arch.sh")

# sha512sums=("SKIP")
sha512sums=("SKIP" "SKIP" "SKIP")

package() {

  # Make necessary directories

  mkdir -p "${pkgdir}/usr/bin"
  mkdir -p "${pkgdir}/usr/share"
  mkdir -p "${pkgdir}/usr/share/icons"
  mkdir -p "${pkgdir}/usr/share/applications"
  mkdir -p "${pkgdir}/opt"
  mkdir -p "${pkgdir}/opt/openai-client"

  cp "${srcdir}/launch_arch.sh" "${pkgdir}/usr/bin/openai-client"
  chmod +x "${pkgdir}/usr/bin/openai-client"

  cp "${srcdir}/openai-client/desktop/openai-client.jpg" "${pkgdir}/usr/share/icons/openai-client.jpg"  
  cp "${srcdir}/openai-client/desktop/openai-client.desktop" "${pkgdir}/usr/share/applications/openai-client.desktop"  

  # Extract the file using tar
  tar xzf "${srcdir}/binaries.tar.gz" -C "$srcdir"

  cp -r "${srcdir}/binaries" "${pkgdir}/opt/openai-client/binaries"





}


