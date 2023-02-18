# Maintainer: Your Name <your@email.com>

pkgname=your-app-name
pkgver=1.0
pkgrel=1
pkgdesc="A short description of your application."
arch=('any')
url="http://yourwebsite.com"
license=('MIT')
depends=('python')
source=("$pkgname-$pkgver.tar.gz::https://github.com/your-username/your-repo-name/archive/v$pkgver.tar.gz")

build() {
  cd "$srcdir/$pkgname-$pkgver"
  # Build instructions go here, if any
}

package() {
  cd "$srcdir/$pkgname-$pkgver"
  install -Dm644 country_code.data "$pkgdir/usr/share/$pkgname/country_code.data"
  install -Dm644 dependency.py "$pkgdir/usr/share/$pkgname/dependency.py"
  install -Dm644 launcher.py "$pkgdir/usr/share/$pkgname/launcher.py"
  install -Dm644 main.py "$pkgdir/usr/share/$pkgname/main.py"
  install -Dm644 MainWindow.ui "$pkgdir/usr/share/$pkgname/MainWindow.ui"
  install -Dm644 mirrorlist.py "$pkgdir/usr/share/$pkgname/mirrorlist.py"
  install -Dm644 resources.py "$pkgdir/usr/share/$pkgname/resources.py"
  install -Dm644 threads.py "$pkgdir/usr/share/$pkgname/threads.py"
  install -Dm644 icons/ "$pkgdir/usr/share/$pkgname/icons/"
}
