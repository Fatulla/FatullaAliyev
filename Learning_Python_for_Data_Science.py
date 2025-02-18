# Rəqəm və Mətn Dəyişənləri

# Tam ədəd (integer)
eded1 = 9
print(eded1)

# Kəsr ədəd (float)
eded2 = 9.2
print(eded2)

# Toplama əməliyyatı
print(eded1 + eded1)
print(eded2 + 1.3)

# Mətn ifadəsi (string)
metn = "Salam, Süni İntellekt dövrü!"
print(metn)

# Məlumat tipləri
print(type(eded1))  # int
print(type(eded2))  # float
print(type(metn))   # str
print(type("1"))    # str (rəqəm kimi görünsə də, mətndir)

# Mətn əməliyyatları
print("a" + "b")  # ab
print("a" " b")   # a b
print("a" + "-b") # a-b

# Mətnin təkrarlanması
print("a" * 3)  # aaa

# Mətn metodları

metn = "gələcəyi_yaradanlar"

# Mətnin uzunluğu
print(len(metn))

# Böyük-kiçik hərflərə çevirmək
print(metn.upper())  # Bütün hərfləri böyük edir
print(metn.lower())  # Bütün hərfləri kiçik edir

# Böyük və kiçik hərfləri yoxlamaq
print(metn.islower())  # True (bütün hərflər kiçikdir)
B = metn.upper()
print(B.islower())  # False (bütün hərflər böyükdür)
print(B.isupper())  # True (bütün hərflər böyükdür)

# Simvolları əvəz etmək (Replace)
print(metn.replace("ə", "a"))  # ə hərflərini a ilə əvəz edir
print(metn.replace("a", "i"))  # a hərflərini i ilə əvəz edir

# Boşluqları silmək (strip)
metn = " gələcəyi_yaradanlar "
print(metn.strip())  # Əvvəl və sonda boşluqları silir

metn = "*gələcəyi_yaradanlar*"
print(metn.strip("*"))  # Əvvəl və sonda olan * işarələrini silir

metn = "lgələcəyi_yaradanlarl"
print(metn.strip("l"))  # Əvvəl və sondakı 'l' hərfini silir

# Mətn dəyişəni
metn = "geleceyi yaradanlar"

# Mətndə istifadə oluna bilən funksiyalar (metodlar)
print(dir(metn))  # Mövcud metodları siyahı şəklində göstərir

# İlk hərfi böyük edir (capitalize)
print(metn.capitalize())  # "Geleceyi yaradanlar"

# Hər sözün ilk hərfini böyük edir (title)
print(metn.title())  # "Geleceyi Yaradanlar"

# Alt sətirlər (Substringlər)

metn = "geleceyi_yaradanlar"

# 1-ci indeksdəki simvol (ikinci simvol)
print(metn[1])  # "e"

# İlk 3 simvol (0-dan 3-cü indeksə qədər, 3 daxil deyil)
print(metn[0:3])  # "gel"

# Dəyişənlər (Variables)

a = 9
b = "aabb"
c = a * 2  # 9 * 2 = 18

# Riyazi əməliyyatlar
print(a / c)  # 9 / 18 = 0.5
print(a * c)  # 9 * 18 = 162
print(a * 5)  # 9 * 5 = 45

# Məlumat tipləri (Data types)
print(type(100))    # int (tam ədəd)
print(type(100.2))  # float (kəsr ədəd)
print(type(1 + 2j)) # complex (mürəkkəb ədəd)

# Float tipində dəyişən
a = 100.0
print(type(a))  # float

# Məlumat Tipi Dəyişdirmə (Type Conversion)

# İstifadəçidən giriş almaq
toplama_bir = input("Birinci ədədi daxil edin: ")
toplama_iki = input("İkinci ədədi daxil edin: ")

# Daxil edilən məlumatlar standart olaraq string tipində olur
print("Birinci dəyişənin tipi:", type(toplama_bir))

# String birləşdirmə (Yanlış toplama)
print("Səhv toplama:", toplama_bir + toplama_iki)  

# Düzgün toplama (Integer tipinə çevirməklə)
print("Düzgün toplama:", int(toplama_bir) + int(toplama_iki))

# Nümunə üçün digər tip çevirmələri
print(int(11.0))   # 11.0 → 11 (Tam ədədə çevrilir)
print(float(12))   # 12 → 12.0 (Kəsr ədədə çevrilir)
print(type(str(12)))  # 12 → "12" (Mətnə çevrilir)

# Çap funksiyası (print)
print("SALAM, SÜNİ İNTELLEKT DÖVRÜ!")

print("geleceyi","yaradanlar")  # Boşluq ilə ayırır
print("geleceyi", "yaradanlar", sep="_")  # Alt xətt ilə ayırır

# Boş sətir çap etmək
print()

# `type()` funksiyası arqumentsiz işlədilə bilməz, ona görə nümunə:
print(type(42))  # int

# `print()` funksiyası arqumentsiz işlədilir və boş sətir çap edir:
print()
type()

# Siyahılar (Listlər)

# Boş siyahı yaratmaq
bos_siyahi = []
bos_siyahi_2 = list()

# Rəqəmlərdən ibarət siyahı
qiymetler = [90, 80, 70, 50]
print("Siyahının tipi:", type(qiymetler))  # list

# Fərqli məlumat tipləri olan siyahı
qarisiq_siyahi = ["a", 19.3, 90]

# Siyahının içində başqa bir siyahı olan geniş siyahı
genis_siyahi = ["a", 19.3, 90, qiymetler]

# Siyahının uzunluğu (elementlərin sayı)
print("Geniş siyahının uzunluğu:", len(genis_siyahi))  # 4