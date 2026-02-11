Python Vectorization & Performance Engineering
This directory documents high-performance Python programming exercises specifically designed for quantitative trading scenarios. The primary objective is to leverage the vectorized features of NumPy and Pandas to eliminate performance bottlenecks and achieve millisecond-level computational efficiency for financial logic.

🎯 Alignment with Optiver/IMC Requirements
In the evaluation process of top-tier market makers, Python proficiency is judged not just by logical correctness, but by an obsession with latency, numerical stability, and code scalability.

1. Vectorized Thinking (Vectorization vs. Iteration)

Focus: Absolute avoidance of explicit for loops when processing large-scale market data (L1/L2 Quotes) or complex option chains.

Demonstration: Refactoring complex mathematical models (e.g., Black-Scholes) into pure NumPy matrix operations to utilize SIMD (Single Instruction, Multiple Data) instructions.

2. Numerical Stability & Precision

Focus: Precision in calculating Greeks (Δ,Γ,V) is critical for risk management.

Demonstration: Handling edge cases (e.g., Days to Expiration (DTE) approaching zero or extreme volatility) to ensure models do not produce NaN or inf results in volatile markets.

3. High-Performance Toolkits

Focus: Utilizing Numba (@jit) or Cython for scenarios where pure vectorization is insufficient (e.g., path-dependent simulations).

Demonstration: Benchmarking execution times between vanilla Python, NumPy, and Numba-accelerated implementations.
