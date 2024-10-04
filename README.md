# Radiometric Data Analysis Report

## 1. Introduction

This report provides a detailed analysis of the radiometric data collected from Ruirihills and Gembe hills. The data includes measurements of Alpha (KBq), Beta (Kcps), and Gamma (nGy/h) radiation, as well as geographical information such as latitude and elevation. The goal is to compare the ionization levels between the two locations and identify any significant relationships between the variables.

## 2. Descriptive Statistics
![EDA analysis](https://github.com/user-attachments/assets/c4dbf518-07d7-4d13-bdc0-abdf7ed13383)

### 2.1 Ruirihills

The descriptive statistics for Ruirihills are as follows:

- **Elevation (m):**
  - Count: 34
  - Mean: 1359.865294
  - Std: 3.797683
  - Min: 1344.520000
  - Max: 1378.540000

- **Alpha (KBq):**
  - Count: 34
  - Mean: 0.046500
  - Std: 0.121169
  - Min: 0.000000
  - Max: 0.528000

- **Gamma (nGy/h):**
  - Count: 34
  - Mean: 147.408824
  - Std: 68.461853
  - Min: 25.680000
  - Max: 296.000000

### 2.2 Gembe Hills

The descriptive statistics for Gembe hills are as follows:

- **Elevation (m):**
  - Count: 25
  - Mean: 1376.800000
  - Std: 21.167979
  - Min: 1349.000000
  - Max: 1405.000000

- **Alpha (KBq):**
  - Count: 25
  - Mean: 6.282076
  - Std: 8.124291
  - Min: 0.021200
  - Max: 24.600000

- **Gamma (nGy/h):**
  - Count: 25
  - Mean: 77.967600
  - Std: 30.186305
  - Min: 9.500000
  - Max: 153.600000

## 3. ANOVA Results

The ANOVA results for Ruirihills and Gembe hills are as follows:

- **Ruirihills:**
  - F-value: 23.8006060947207
  - p-value: 5.445250263308975e-07

- **Gembe Hills:**
  - F-value: 2.65153937652741
  - p-value: 0.0929654672412674

## 4. Correlation Matrices

### 4.1 Ruirihills
![CORRELATION MATRIX RUIRI](https://github.com/user-attachments/assets/70b81bba-2589-40b5-9626-fa5151fbd6f8)

The correlation matrix for Ruirihills is as follows:

|             | Latitude | Elevation (m) | Alpha (KBq) | Beta (Kcps) | Gamma (nGy/h) |
|-------------|----------|---------------|-------------|-------------|---------------|
| Latitude    | 1.000000 | 0.977047      | -0.057040   | 0.831078    | 0.831078      |
| Elevation   | 0.977047 | 1.000000      | -0.061236   | 0.813912    | 0.813912      |
| Alpha       | -0.057040| -0.061236     | 1.000000    | -0.070646   | -0.070646     |
| Beta        | 0.831078 | 0.813912      | -0.070646   | 1.000000    | 1.000000      |
| Gamma       | 0.831078 | 0.813912      | -0.070646   | 1.000000    | 1.000000      |

### 4.2 Gembe Hills
![CORRELATION MATRIX GEMBE](https://github.com/user-attachments/assets/d3a55c12-e476-4998-98f5-9c9d569f0e82)

The correlation matrix for Gembe hills is as follows:

|             | Latitude | Elevation (m) | Alpha (KBq) | Beta (Kcps) | Gamma (nGy/h) |
|-------------|----------|---------------|-------------|-------------|---------------|
| Latitude    | 1.000000 | -0.415207     | -0.057610   | 0.352921    | 0.319966      |
| Elevation   | -0.415207| 1.000000      | 0.102661    | -0.327370   | -0.109412     |
| Alpha       | -0.057610| 0.102661      | 1.000000    | 0.320832    | -0.168452     |
| Beta        | 0.352921 | -0.327370     | 0.320832    | 1.000000    | -0.109412     |
| Gamma       | 0.319966 | -0.109412     | -0.168452   | -0.109412   | 1.000000      |

## 5. Discussion

- The mean elevation of Ruirihills is slightly lower than that of Gembe hills.
- The mean Alpha radiation in Gembe hills is significantly higher than in Ruirihills.
- The Gamma radiation levels are higher in Ruirihills compared to Gembe hills.
- The ANOVA results indicate a significant difference in the radiometric measurements within Ruirihills, while the difference is not significant within Gembe hills.
- The correlation matrices show strong correlations between Latitude, Elevation, and Gamma radiation in Ruirihills. In Gembe hills, there are moderate correlations between the variables.

## 6. Conclusion

This analysis provides insights into the radiometric data collected from Ruirihills and Gembe hills. The differences in radiation levels and the relationships between variables have been identified. Further analysis could include spatial mapping to visualize these differences geographically.
