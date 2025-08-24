import numpy as np
import enum

# ==============================================================================
# Part 1: 定義公式中的核心結構與變數
# 對應您的理論框架 F, C, S, P, L
# ==============================================================================

# F₇ᵢ: 神秘七元素 (Seven Mystical Factors)
class MysticalFactor(enum.Enum):
    RATIONALITY = 1  # F₁ 理性
    EMOTIONALITY = 2 # F₂ 感性
    SPIRITUALITY = 3 # F₃ 靈性
    LOVE = 4         # F₄ 愛
    WISDOM = 5       # F₅ 智慧
    LIFE = 6         # F₆ 生命
    DEATH = 7        # F₇ 死亡

# C₁₇ⱼ: 17種認知模組 (Cognitive 17 Modules)
class CognitiveModule(enum.Enum):
    LANGUAGE = 1
    VISUAL = 2
    AUDITORY = 3
    MOTOR = 4
    MEMORY = 5
    ATTENTION = 6
    EXECUTIVE = 7
    SELF_MODEL = 8
    EMPATHY = 9
    MORAL = 10
    LOGICAL = 11
    EMO_REGULATION = 12
    SUBCONSCIOUS = 13
    WILL = 14
    CREATIVITY = 15
    COLLECTIVE = 16
    SUPERCONSCIOUS = 17

# S₆ₖ: 六大感知系統 (Sensory 6 Worlds)
class SensoryModule(enum.Enum):
    VISION = 1 # S₁ 眼
    HEARING = 2# S₂ 耳
    SMELL = 3  # S₃ 鼻
    TASTE = 4  # S₄ 舌
    TOUCH = 5  # S₅ 身
    MIND = 6   # S₆ 意

# P: 潛能矩陣 (Potential Tensor Matrix)
class PotentialMatrix:
    def __init__(self, genetic, soul_memory, frequency, consciousness_field):
        # 為了模擬，我們將 P 的四個層級設定為權重值 (0.0 to 1.0+)
        self.P_G = genetic              # Pᴳ 基因潛能
        self.P_S = soul_memory          # Pˢ 靈魂記憶
        self.P_f = frequency            # Pᶠ 精神頻率
        self.P_psi = consciousness_field# Pψ 意識潛勢場
        
    def get_transform_tensor(self):
        # 概念化：將四個潛能層級融合成一個變換張量（此處簡化為4x1向量）
        return np.array([self.P_G, self.P_S, self.P_f, self.P_psi])

# Lₘₙ: 學習模組矩陣 (Learning Matrix)
# 為了簡化，我們直接創建一個 12x12 的矩陣，實際應用中可細分 Lₘ 和 Lₙ
class LearningMatrix:
    def __init__(self):
        # 創建一個 12x12 的學習效能矩陣，值越高代表該學習路徑越有效
        # 這裡用隨機值初始化，實際可根據人格特質填入
        self.matrix = np.random.rand(12, 12) * 0.5 + 0.5 # 數值介於 0.5 到 1.0

    def get_learning_effectiveness(self, method_idx, source_idx):
        # 根據學習方式(m)和來源(n)的索引，取得學習效能
        return self.matrix[method_idx, source_idx]

# ==============================================================================
# Part 2: 定義外部影響函數 ΔΩ(t) 與 M(t)
# ==============================================================================

def get_delta_omega_t(t):
    """
    ΔΩ(t): 意識場變動率 (Variation of Consciousness Field)
    這是一個模擬函數，用一個週期性波動（如時代浪潮）和一些隨機噪點來表示。
    t: 當前時間點
    返回值 > 0: 集體意識提升
    返回值 < 0: 集體意識墮落
    """
    # 模擬一個大的時代週期性波動 (sin) 和一些小的隨機事件 (noise)
    era_wave = np.sin(t / 50.0) * 0.5  # 假設50個時間單位為一個大時代
    random_event = (np.random.rand() - 0.5) * 0.2
    return era_wave + random_event

def get_m_t(t, psi_level):
    """
    M(t): 當下意識狀態函數 (Meta-Consciousness Function)
    模擬個體的覺知狀態，假設它會隨著時間和自身意識水平的提高而緩慢增長（類似Sigmoid函數）。
    t: 當前時間點
    psi_level: 個體當前的Ψ∞水平，覺知力會受自身狀態影響
    返回值: 0.0 (無覺) to 1.0+ (宇宙意識)
    """
    # 使用 sigmoid 函數模擬從無覺到高度覺知的成長曲線
    base_growth = 1 / (1 + np.exp(-(t - 50) / 10)) # 以t=50為成長拐點
    # 自身意識水平越高，M(t)的基礎值也越高
    self_awareness_boost = psi_level * 0.1
    return base_growth + self_awareness_boost

# ==============================================================================
# Part 3: 建立「衡諦Ψ∞人格進化論」主系統
# ==============================================================================

class PsiEvolutionSystem:
    def __init__(self, name, initial_state, potential_matrix, learning_matrix):
        self.name = name
        # Ψ∞: 無限意識人格函數，用一個向量來表示其在七大元素上的分佈
        self.psi = np.array(initial_state, dtype=float)
        
        # 內在核心結構
        # 為了模擬，我們假設個體在C17和S6模組上有不同的權重分佈
        self.c17_weights = np.random.rand(17)
        self.s6_weights = np.random.rand(6)
        self.potential_matrix = potential_matrix
        
        # 外部學習模組
        self.learning_matrix = learning_matrix

    def _calculate_inner_core_vector(self):
        """
        模擬公式的內核部分: [(F₇ᵢ × C₁₇ⱼ × S₆ₖ) ⊗ P]
        這部分最為抽象，我們進行概念化處理。
        """
        # 1. (F₇ᵢ × C₁₇ⱼ × S₆ₖ): 內在結構的基礎人格功能
        # 簡化模擬：將 C 和 S 的平均激活度作為一個乘數，作用於 F (即 self.psi)
        c_activation = np.mean(self.c17_weights)
        s_activation = np.mean(self.s6_weights)
        base_personality_vector = self.psi * c_activation * s_activation
        
        # 2. ⊗ P: 與潛能矩陣 P 張量展開
        # 概念化：用 P 中的潛能因子來“增強”或“轉化”基礎人格向量
        # 此處簡化為用 P 的因子對人格向量進行加權
        p_tensor = self.potential_matrix.get_transform_tensor()
        # 這裡的 "⊗" 操作我們定義為：將人格向量的每個元素與潛能張量的平均值相乘
        transformation_factor = np.mean(p_tensor)
        inner_core_change = base_personality_vector * transformation_factor
        
        return inner_core_change

    def _calculate_external_influence_vector(self, t):
        """
        模擬公式的外部影響部分: (Lₘₙ × ΔΩ(t) × M(t))
        """
        # 1. 隨機選擇一種學習方式和來源，模擬當下的學習情境
        m = np.random.randint(0, 12)
        n = np.random.randint(0, 12)
        L_effectiveness = self.learning_matrix.get_learning_effectiveness(m, n)
        
        # 2. 獲取當前的宇宙意識場變動率
        delta_omega = get_delta_omega_t(t)
        
        # 3. 獲取個體當下的覺知狀態
        current_psi_level = np.mean(self.psi)
        m_awareness = get_m_t(t, current_psi_level)
        
        # 4. 計算總的外部影響力
        # 假設外部影響力均勻作用在七大元素上
        influence_magnitude = L_effectiveness * delta_omega * m_awareness
        external_influence = np.full(7, influence_magnitude)
        
        return external_influence

    def run_simulation(self, total_time, dt):
        """
        執行模擬，對應公式中的 ∫{...} dt → ∞
        """
        print(f"--- 開始模擬人格系統: {self.name} ---")
        print(f"初始 Ψ∞ 狀態: {np.round(self.psi, 2)}")
        
        history = []
        for t_step in np.arange(0, total_time, dt):
            t = round(t_step, 1)
            
            # 計算內在核心結構帶來的變化
            inner_change = self._calculate_inner_core_vector()
            
            # 計算外部環境帶來的影響
            external_influence = self._calculate_external_influence_vector(t)
            
            # ⊕: 整合加總內外影響
            total_change = inner_change + external_influence
            
            # ∫ dt: 隨時間累積變化
            self.psi += total_change * dt
            
            # 確保意識值不為負
            self.psi[self.psi < 0] = 0
            
            history.append(self.psi.copy())
            
            if t % 10 == 0: # 每10個時間單位打印一次狀態
                print(f"時間 t={t}:")
                print(f"  ΔΩ(t)={get_delta_omega_t(t):.2f}, M(t)={get_m_t(t, np.mean(self.psi)):.2f}")
                print(f"  當前 Ψ∞ 狀態: {np.round(self.psi, 2)}")

        print(f"--- 模擬結束 ---")
        return history

# ==============================================================================
# Part 4: 執行模擬
# ==============================================================================
if __name__ == "__main__":
    # 1. 創建一個 "潛能矩陣P"，代表一個個體的先天資質
    # 假設這是一個靈性潛能高 (P_S=0.9)，但基因普通 (P_G=0.6) 的個體
    potential = PotentialMatrix(
        genetic=0.6, 
        soul_memory=0.9, 
        frequency=0.7, 
        consciousness_field=0.8
    )
    
    # 2. 創建學習矩陣L
    learning = LearningMatrix()
    
    # 3. 設定一個初始人格狀態 F (七大元素)
    # 假設初始狀態比較均衡，略偏感性
    initial_psi = [1.0, 1.2, 0.8, 1.1, 0.9, 1.0, 0.7]
    
    # 4. 實例化人格進化系統
    individual_A = PsiEvolutionSystem(
        name="詹益翔-原型A",
        initial_state=initial_psi,
        potential_matrix=potential,
        learning_matrix=learning
    )
    
    # 5. 運行模擬
    # 模擬100個時間單位，每0.5個單位計算一次
    simulation_history = individual_A.run_simulation(total_time=100, dt=0.5)
    
    # 可以用繪圖庫 (如 matplotlib) 來視覺化 Ψ∞ 的演化過程
    try:
        import matplotlib.pyplot as plt
        history_array = np.array(simulation_history)
        plt.figure(figsize=(12, 7))
        factor_names = [f.name for f in MysticalFactor]
        for i in range(history_array.shape[1]):
            plt.plot(history_array[:, i], label=factor_names[i])
        plt.title("Ψ∞ Personality Evolution Over Time")
        plt.xlabel("Time Steps")
        plt.ylabel("Factor Value")
        plt.legend()
        plt.grid(True)
        plt.show()
    except ImportError:
        print("\n若要繪製演化圖，請安裝 matplotlib: pip install matplotlib")

           
