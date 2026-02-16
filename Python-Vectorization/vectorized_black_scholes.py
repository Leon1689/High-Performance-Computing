import numpy as np
from scipy.stats import norm
class BlackScholesEngine:

    def black_scholes_price(S, K, T, r, sigma, option_type='call'):
        """Basic Black-Scholes formula implementation."""
        # Handling near-expiry cases to avoid division by zero
        T = np.maximum(T, 1e-9)
        d1 = (np.log(S / K) + (r + 0.5 * sigma**2) * T) / (sigma * np.sqrt(T))
        d2 = d1 - sigma * np.sqrt(T)
        # Discount factor for the strike price payment
        discount = np.exp(-r * T)
        
        if option_type == 'call':
            return S * norm.cdf(d1) - K * np.exp(-r * T) * norm.cdf(d2)
        else:
            return K * np.exp(-r * T) * norm.cdf(-d2) - S * norm.cdf(-d1)
        else:
            raise ValueError("Invalid option_type. Must be 'call' or 'put'."
# --- Performance Benchmark ---
if __name__ == "__main__":
    # Test scenario: 1 million option contracts
    N = 1_000_000
    print(f"Starting benchmark with {N:,} options...")
    
    # Simulating random market data
    S_sim = np.random.uniform(90, 110, N)
    K_sim = np.random.uniform(90, 110, N)
    T_sim = np.random.uniform(0.1, 2.0, N)
    sigma_sim = np.random.uniform(0.1, 0.4, N)
    r_sim = 0.05
    
    # Measure execution time
    start = time.perf_counter()
    results = BlackScholesEngine.calculate_price(S_sim, K_sim, T_sim, r_sim, sigma_sim)
    end = time.perf_counter()
    
    # Output metrics
    duration = end - start
    print("-" * 30)
    print(f"Calculation completed in: {duration:.4f} seconds")
    print(f"Throughput: {int(N / duration):,} options/sec")
    print("-" * 30)
    print(f"Sample prices: {results[:5]}")
