def false_position_method(func, a, b, max_iter=1000, tolerance=1e-6):  # 1e-6 = 0.000001
    """
    Fonksiyonun kökünü bulmak için Doğrusal İnterpolasyon Metodunu uygular.

    Parametreler:
    func (fonksiyon): Kökünü bulacağımız fonksiyon.
    a (float): Aralığın başlangıç noktası.
    b (float): Aralığın bitiş noktası.
    max_iter (int): Yapılacak maksimum iterasyon sayısı.
    tolerance (float): Kök yaklaşımı için tolerans.

    Döndürür:
    float: Fonksiyonun yaklaşık kökü.
    """
    global n  # İterasyon sayısını tutmak için global değişken
    n = 0  # İterasyon sayısı

    for iteration in range(max_iter):
        # Doğrusal interpolasyon ile kökü hesapla
        try:
            c = b - (func(b) * (b - a)) / (func(b) - func(a))
        except ZeroDivisionError:
            print("Sıfıra bölme hatası!")
            return None

        # Yaklaşımın tolerans içinde olup olmadığını kontrol et
        if abs(func(c)) < tolerance:
            return c

        # a ve b noktalarını güncelle
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c

        n += 1  # İterasyon sayısını güncelle

    return c  # Son hesaplanan değeri döndür


if __name__ == "__main__":
    # örneği kullanımı
    func = lambda x: x**3 - (7 * x**2) + (14 * x) - 6

    # Başlangıç noktaları a ve b (f(a) ve f(b)'nin zıt işaretlerde olduğundan emin olun)
    a = 0
    b = 1

    # Kök yaklaşımı için maksimum iterasyon sayısı ve tolerans
    max_iter, tol = 2, 0.001

    # Doğrusal İnterpolasyon Metodu kullanarak kökü bul
    root = false_position_method(func, a, b, max_iter, tol)
    if root is not None:
        print(f"{n} Yaklaşık kök: {root}")
