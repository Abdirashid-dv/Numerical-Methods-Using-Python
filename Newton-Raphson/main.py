def newton_raphson_method(f, df, x0, tol=1e-6, max_iter=1000):
    """
    Newton-Raphson yöntemi kullanarak f(x) fonksiyonunun kökünü bulun.

    Parametreler:
    f (fonksiyon): Kökünü bulmaya çalıştığımız fonksiyon.
    df (fonksiyon): f fonksiyonunun türevi.
    x0 (float): Kök için başlangıç tahmini.
    tol (float): Kök yaklaşımı için tolerans.
    max_iter (int): Maksimum iterasyon sayısı.

    Döndürür:
    float: Fonksiyonun yaklaşık kökü.
    """
    xn = x0
    for n in range(max_iter):
        fxn = f(xn)
        if abs(fxn) < tol:
            print(f"{n} iterasyon sonra çözüm bulundu.")
            return xn
        dfxn = df(xn)
        if dfxn == 0:
            print("Sıfır türev. Çözüm bulunamadı.")
            return None
        xn = xn - fxn / dfxn
    print("Maksimum iterasyon aşıldı. Çözüm bulunamadı.")
    return None


# Örnek kullanım:
# Fonksiyonu ve türevini tanımlayın
f = lambda x: 5 / x - 2
df = lambda x: -5 / x**2

# Başlangıç tahmini
x0 = 3

# Kökü bul
root = newton_raphson_method(f, df, x0)
print("Fonksiyonun kökü:", root)
