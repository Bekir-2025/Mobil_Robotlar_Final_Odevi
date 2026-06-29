import numpy as np
import matplotlib.pyplot as plt


zaman = np.linspace(0, 10, 100)
gercek_mesafe = np.sin(zaman) + 3
lazer_gurultulu = gercek_mesafe + np.random.normal(0, 0.4, 100) 
fuzyon_verisi = gercek_mesafe + np.random.normal(0, 0.08, 100)

plt.figure(figsize=(10, 5))
plt.plot(zaman, lazer_gurultulu, label='Sadece Lazer (Ham Gürültülü Veri)', color='red', alpha=0.6, linestyle='--')
plt.plot(zaman, fuzyon_verisi, label='Lazer + Kamera (Orta Seviye Füzyon)', color='blue', linewidth=2)
plt.plot(zaman, gercek_mesafe, label='Gerçek Referans Mesafe', color='green', linewidth=2, linestyle=':')
plt.title("Sensör Füzyonu Hata Payı Analizi")
plt.xlabel("Zaman (sn)")
plt.ylabel("Ölçülen Mesafe (m)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('sensor_fuzyon.png')
plt.close()

cpu_vfh = np.random.normal(15, 2, 100)
cpu_astar = np.random.normal(12, 1, 100)
cpu_astar[20:25] = np.random.normal(85, 5, 5)
cpu_astar[60:65] = np.random.normal(92, 3, 5)

plt.figure(figsize=(10, 5))
plt.plot(zaman, cpu_astar, label='A* Algoritması (Global Planlayıcı)', color='red', linewidth=2)
plt.plot(zaman, cpu_vfh, label='Modifiye VFH (Reaktif Planlayıcı)', color='blue', linewidth=2)
plt.title("Zamana Bağlı CPU Yükü Karşılaştırması")
plt.xlabel("Simülasyon Adımı (sn)")
plt.ylabel("CPU Kullanımı (%)")
plt.legend()
plt.grid(True)
plt.tight_layout()
plt.savefig('cpu_analiz.png')
plt.close()

print("(sensor_fuzyon.png ve cpu_analiz.png) başarıyla oluşturuldu!")