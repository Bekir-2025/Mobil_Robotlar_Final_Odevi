import numpy as np
import matplotlib.pyplot as plt

class ChannelRobot:
    def __init__(self, start_pos, sensor_range=3.0, step_size=0.2):
        self.pos = np.array(start_pos, dtype=float)
        self.path = [self.pos.copy()]
        self.sensor_range = sensor_range
        self.step_size = step_size
        self.heading = np.array([1.0, 0.0])

    def scan_environment(self, obstacles):
        """
        Sensör Füzyonu Simülasyonu (Kamera + Lazer):
        Robotun görüş menzili içindeki engelleri algılayıp yerel doluluk haritasını çıkarır.
        """
        local_grid = []
        for obs in obstacles:
            dist = np.linalg.norm(self.pos - obs)
            if 0 < dist <= self.sensor_range:
                local_grid.append(obs)
        return local_grid

    def modified_vfh_step(self, obstacles):
        """
        Modifiye Edilmiş VFH (Duvar Takibi) Algoritması:
        Hedef olmadığı için sadece itici kuvvet hesaplanır ve 90 derece normaline gidilir.
        """
        local_obs = self.scan_environment(obstacles)
        
        repulsive_force = np.array([0.0, 0.0])
        
        if not local_obs:
            self.pos += self.heading * self.step_size
            self.path.append(self.pos.copy())
            return

        for obs in local_obs:
            dist = np.linalg.norm(self.pos - obs)
            force_mag = 1.0 / (dist ** 2) 
            direction = (self.pos - obs) / dist
            repulsive_force += direction * force_mag
        

        normal_vector = np.array([repulsive_force[1], -repulsive_force[0]])
        
        norm = np.linalg.norm(normal_vector)
        if norm > 0:
            self.heading = normal_vector / norm
            
        self.pos += self.heading * self.step_size
        self.path.append(self.pos.copy())

def generate_u_channel():
    """
    Simülasyon için U şeklinde yerel minimum (local minima) tuzağı olan bir dar kanal oluşturur.
    """
    obstacles = []
    for x in np.arange(0, 10, 0.2):
        obstacles.append([x, 5])
    for x in np.arange(0, 8, 0.2):
        obstacles.append([x, 1])
    for y in np.arange(1, 5, 0.2):
        obstacles.append([8, y])
    return np.array(obstacles)

def main():
    print("Modifiye VFH Kanal Navigasyon Simülasyonu Başlıyor...")
    
    obstacles = generate_u_channel()
    robot = ChannelRobot(start_pos=[1.0, 2.5], sensor_range=2.5, step_size=0.15)
    
    for _ in range(250):
        robot.modified_vfh_step(obstacles)
        
    path = np.array(robot.path)
    
    plt.figure(figsize=(10, 6))
    plt.scatter(obstacles[:, 0], obstacles[:, 1], color='black', label='Kanal Duvarları (Engeller)', s=15)
    plt.plot(path[:, 0], path[:, 1], color='red', label='Robotun Otonom Rotası', linewidth=2)
    plt.scatter(path[0, 0], path[0, 1], color='green', label='Başlangıç', s=100, zorder=5)
    plt.scatter(path[-1, 0], path[-1, 1], color='blue', label='Bitiş', s=100, zorder=5)
    
    plt.title("Modifiye Edilmiş VFH ile Dar Kanal (U-Tuzağı) Navigasyonu")
    plt.xlabel("X Koordinatı")
    plt.ylabel("Y Koordinatı")
    plt.legend()
    plt.grid(True)
    plt.axis('equal')
    
    plt.show()

if __name__ == "__main__":
    main()