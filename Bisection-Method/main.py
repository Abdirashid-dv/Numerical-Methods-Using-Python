def bisection_method(f, a, b, tol=1e-6):
    """
    Bir fonksiyonun [a, b] aralığında kökünü ikiye bölme yöntemiyle bulur.

    :param f: Kökünü bulmaya çalıştığımız fonksiyon.
    :param a: Aralığın başlangıcı.
    :param b: Aralığın sonu.
    :param tol: Tolerans; işlem, aralık tol'dan küçük olduğunda durdurulur.
    :return: Fonksiyonun kökü (veya kökün bir yaklaşımı).
    :n_iter: İterasyon sayısı.
    """
    global n_iter

    n_iter = 0
    if f(a) * f(b) >= 0:
        print("ikiye bölme yöntemi başarısız oldu.")
        return None

    while (b - a) / 2.0 > tol:
        n_iter += 1
        midpoint = (a + b) / 2.0
        if f(midpoint) == 0:
            return midpoint  # Tam kök bulundu.
        elif f(a) * f(midpoint) < 0:  # Kök sol yarıda yer alıyor.
            b = midpoint
        else:  # Kök sağ yarıda yer alıyor.
            a = midpoint

    return (a + b) / 2.0


# Örnek kullanım
if __name__ == "__main__":
    # Köklerini bulacağımız bir fonksiyon tanımlayın.
    func = lambda x: x**3 - 2 * x - 5

    # Bir kökün olduğundan şüphelendiğimiz [a, b] aralığı ve tolerans
    a, b, tol = 2, 3, 1e-6

    # Kökü bul ve yazdır.
    root = bisection_method(func, a, b, tol)
    if root is not None:
        print(f"{n_iter}'inci iterasyon Kök yaklaşık olarak burada: {root}")
