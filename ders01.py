# İlk önce Python'ı kurmalısınız.
# Python kurulumunu yaptıktan sonra, terminalden veya komut istemcisinden python veya python3 yazarak Python'u başlatabilirsiniz.   yada
# Visual Studio Code gibi bir IDE kullanarak Python dosyaları oluşturabilirsiniz.
# Python dosyaları genellikle .py uzantısıyla kaydedilir.
# Python dosyası oluşturmak için bir metin düzenleyici veya IDE kullanabilirsiniz.
# Örnek bir Python dosyası oluşturmak için aşağıdaki adımları izleyebilirsiniz: 
# 1. Bir metin düzenleyici veya IDE açın (örneğin, Visual Studio Code, PyCharm, Notepad++, vb.).
# 2. Yeni bir dosya oluşturun ve adını ders01.py olarak kaydedin.
# 3. Aşağıdaki kodu dosyaya yapıştırın:
print("Merhaba, Python!")
# 4. Dosyayı kaydedin.
# 5. Terminal veya komut istemcisini açın ve dosyanın bulunduğu dizine gidin.
# 6. Aşağıdaki komutu çalıştırarak Python dosyasını çalıştırın
# python ders01.py
# veya
# python3 ders01.py
# Python dosyası çalıştırıldığında "Merhaba, Python!" mesajını ekrana yazdıracaktır.
# Python'da yorum satırları # ile başlar. Yorum satırları, kodun çalışmasını etkilemez ve sadece açıklama amacıyla kullanılır.
# Python'da değişkenler, veri saklamak için kullanılır. Değişkenler, bir değeri temsil eden isimlendirilmiş alanlardır.
# Değişkenler, veri türlerine göre farklı şekillerde tanımlanabilir. Python'da değişken tanımlamak için aşağıdaki adımları izleyebilirsiniz:
# 1. Bir değişken adı seçin. Değişken adı, harf, rakam ve alt çizgi (_) karakterlerinden oluşabilir, ancak rakamla başlayamaz.
# 2. Değişken adını bir değere atayın. Değer, sayılar, metin, listeler, sözlükler vb. olabilir.
# 3. Değişkeni kullanmak için adını yazın.
# Örnek:
# Değişken tanımlama
x = 5
y = "Merhaba"
# Değişkenleri kullanma
print(x)  # 5
print(y)  # Merhaba
# Python'da veri türleri, verilerin nasıl saklandığını ve işlendiğini belirler. Python'da yaygın olarak kullanılan veri türleri şunlardır:  
# 1. int: Tam sayılar (örneğin, 5, -10, 0)
# 2. float: Ondalık sayılar (örneğin, 3.14, -0.5, 2.0)
# 3. str: Metin (örneğin, "Merhaba", "Python", "123")
# 4. list: Liste (örneğin, [1, 2, 3], ["a", "b", "c"])
# 5. tuple: Demet (örneğin, (1, 2, 3), ("a", "b", "c"))
# 6. dict: Sözlük (örneğin, {"anahtar": "değer"}, {"isim": "Ali", "yaş": 25})
# 7. bool: Mantıksal değerler (True veya False)
# Python'da veri türlerini kullanmak için aşağıdaki adımları izleyebilirsiniz:
# 1. Bir veri türü seçin (örneğin, int, float, str, list, tuple, dict, bool).
# 2. Veri türünü bir değişkene atayın.
# 3. Değişkeni kullanmak için adını yazın.
# Örnek:
# int veri türü

x = 5
y = -10     
z = 0
print(x)  # 5   
print(y)  # -10
print(z)  # 0
# float veri türü
x = 3.14

y = -0.5
z = 2.0
print(x)  # 3.14
print(y)  # -0.5

print(z)  # 2.0
# str veri türü
x = "Merhaba"

y = "Python"
z = "123"

print(x)  # Merhaba
print(y)  # Python
print(z)  # 123
# list veri türü
x = [1, 2, 3] # Liste İçinde Tam Sayılar
y = ["a", "b", "c"] # Liste İçinde Karakterler
z = [1, "a", 3.14] # Liste İçinde Farklı Veri Türleri
print(x)  # [1, 2, 3]
print(y)  # ['a', 'b', 'c']
print(z)  # [1, 'a', 3.14]
print(type(x))  # <class 'list'> tipini gösterir
print(type(y))  # <class 'list'> tipini gösterir
print(type(z))  # <class 'list'> tipini gösterir
# tuple veri türü
x = (1, 2, 3) # Demet İçinde Tam Sayılar
y = ("a", "b", "c") # Demet İçinde Karakterler
z = (1, "a", 3.14) # Demet İçinde Farklı Veri Türleri
print(x)  # (1, 2, 3)
print(y)  # ('a', 'b', 'c')
print(z)  # (1, 'a', 3.14)
print(type(x))  # <class 'tuple'> tipini gösterir
print(type(y))  # <class 'tuple'> tipini gösterir
print(type(z))  # <class 'tuple'> tipini gösterir
# Tuple'lar, listelere benzer, ancak değiştirilemezler. Yani bir tuple oluşturduktan sonra içeriğini değiştiremezsiniz.
# Tuple'lar, parantez () içinde tanımlanır ve virgülle ayrılmış değerlerden oluşur.
# Tuple'lar, listelere göre daha hafif ve hızlıdır, bu nedenle bazı durumlarda tercih edilebilirler.
